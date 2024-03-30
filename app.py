from flask import Flask
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
import face_recognition
import numpy as np
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='KYC Photo Comparison API', description='A simple API to compare two photos for KYC purposes.')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

photo_upload = reqparse.RequestParser()
photo_upload.add_argument('id_photo', location='files', type=FileStorage, required=True, help='ID photo')
photo_upload.add_argument('user_photo', location='files', type=FileStorage, required=True, help='User photo')

@api.route('/compare-photos')
class PhotoComparison(Resource):
    @api.expect(photo_upload)
    def post(self):
        args = photo_upload.parse_args()
        id_photo = args['id_photo']
        user_photo = args['user_photo']

        if id_photo.filename == '' or user_photo.filename == '':
            api.abort(400, "No selected file")

        if id_photo and allowed_file(id_photo.filename) and user_photo and allowed_file(user_photo.filename):
            id_filename = os.path.join(UPLOAD_FOLDER, id_photo.filename)
            user_filename = os.path.join(UPLOAD_FOLDER, user_photo.filename)

            id_photo.save(id_filename)
            user_photo.save(user_filename)

            id_image = face_recognition.load_image_file(id_filename)
            user_image = face_recognition.load_image_file(user_filename)

            id_face_encodings = face_recognition.face_encodings(id_image)
            user_face_encodings = face_recognition.face_encodings(user_image)

            if not id_face_encodings or not user_face_encodings:
                return {"error": "No faces detected in one of the images"}

            id_face_encoding = id_face_encodings[0]
            user_face_encoding = user_face_encodings[0]

            results = face_recognition.compare_faces([id_face_encoding], user_face_encoding)
            face_distances = face_recognition.face_distance([id_face_encoding], user_face_encoding)
            similarity_percentage = (1 - face_distances[0]) * 100

            # Convert numpy.bool_ to bool for JSON serialization
            match_result = bool(results[0])

            return {"match": match_result, "similarity_percentage": similarity_percentage}

        return {"error": "File format not allowed"}, 400

if __name__ == '__main__':
    app.run(debug=True)
