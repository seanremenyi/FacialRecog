# Facial Recognition Application

#### Purpose

The purpose of this application is to give users an easy to use web application to do facial analysis on images.

#### Functionality/Features

The application will function by leveraging several services from AWS. Users will create an account to login into the application. From there they will be able to upload images. The images will be uploaded to an S3 bucket and then passed onto one of the machine learning services available on AWS called Rekognition. This service will regonize facial features of the person in the image and output the data back to an S3 bucket from which the application will grab it and display it to the user.

At the moment the MVP (minimal viable product) will be using a basic Rekognition feature which will recognize a face in an image and output metrics to answer the following questions,
1. How confident Rekognition is that it is a face in the image
2. Where the face is located in the image
3. What emotion displayed (and a confidence metric of that value)
4. Whether the person is smiling (and a confidence metric of that value)
5. Is their mouth open (and a confidence metric of that value)
6. Do they have a mustache (and a confidence metric of that value)
7. Are their eyes open (and a confidence metric of that value)
8. Are they wearing glasses (and a confidence metric of that value)

The application itself will include the following features:
- DNS
- Password hashing
- Basic authorization using JSON token
- SSL encryption
- Machine Learning
- Load balanging and Auto-scaling
- Interactive front-end

Future versions of this application will include:
- The ability to recognize faces from 2 different images and compare them to see if they match
- The ability to recognize a face of a person in one image identify if they are in another image of a group of people

#### Target audience

The target audience for this application will be anyone you wants to get information on facial features of a person in an image. Any user with access to an internet connection will have access to this web application.


#### Tech Stack
The application will use the following tech stack along with each tech's purpose
- **Python** used for the backend of the application
- **Vue** used for the front end of the application
- **Flask** used for the web framework
- **AWS ReKognition** used for image recognition
- **PostgreSQL** used for the database
- **SQLAlchemy** used to avoid raw SQL inputs
- **AWS Route53** used for DNS
- **Bcrypt** used for password hashing
- **JWTManager** used for JSON web tokens
- **HTML/CSS** used for website content and styling
- **AWS S3** used for image hosting
- **AWS Frameworks** used for hosting the application in the cloud

#### Dataflow Diagram
![data flow diagram](docs/FRdataflow.png)













