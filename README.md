![Photo Verification API Banner](https://telegra.ph/file/f85df3c8ef81b63b0e1ad.png)
# Photo Verification API Repository

This repository contains the API for photo verification services.

You can read and learn about related report with primary and secondary research about the BNPL industry in Uzbekistan [here](https://docs.google.com/document/d/1c5u_VMlW8WvlbIM9NAgjzpHo6rCcVXOi/edit?usp=sharing&ouid=107772990378977160799&rtpof=true&sd=true).

Library used: [Face Recognition Library](https://face-recognition.readthedocs.io/en/latest/readme.html)
![Example](https://cloud.githubusercontent.com/assets/896692/23625227/42c65360-025d-11e7-94ea-b12f28cb34b4.png)

This KYC Photo Comparison API is developed using Flask and Flask-RESTx, providing an endpoint for comparing two photos to verify user identity for KYC (Know Your Customer) purposes.

## Features
- Upload and compare two photos: an ID photo and a user photo.
- Utilizes face recognition to determine if the photos belong to the same person.
- Returns the match result and similarity percentage.

## Installation

To run this API, you will need Python installed on your system. After cloning the repository, you can install the required dependencies by running:

`bash
pip install flask flask-restx face_recognition numpy
`

## Usage

To use the API, you need to send a `POST` request to the `/compare-photos` endpoint with multipart/form-data containing the two photos to be compared. Here is an example `curl` command to do this:

`curl -X POST http://127.0.0.1:5000/compare-photos \
  -F "id_photo=@/path/to/id_photo.jpg" \
  -F "user_photo=@/path/to/user_photo.jpg"` 

Replace `/path/to/id_photo.jpg` and `/path/to/user_photo.jpg` with the actual paths to your images.

## Response

The response will be a JSON object that includes:

-   `match`: A boolean indicating whether the faces in the two photos match.
-   `similarity_percentage`: A percentage indicating how similar the faces are.

Example of a successful response:

Copy code

`{
  "match": true,
  "similarity_percentage": 92.5
}` 

## Notes

-   Ensure that the images are in PNG, JPG, or JPEG format.
-   The API is set to run in debug mode for development purposes. For production, ensure to set `debug` to `False`.

----------

**Copyright © 2024**  
_A project undertaken as part of BSc (Hons) Business Information Systems Degree, Westminster International University in Tashkent._
