# Document Manager - SoumyaRao

# Overview
This project is a simple Document Management System (DMS) built using Django and Django Rest Framework. It allows users to create, retrieve, update, and delete documents, as well as view document versions and perform certain actions like reverting to the previous version or deleting a document.

# Project Structure
- documents: Django app for handling document-related functionalities.
models.py: Defines the Document model.
serializers.py: Serializers for Document model.
views.py: API views for document-related actions.
urls.py: URL patterns for document-related endpoints.
tests.py: Testing Document Related apis


- users: Django app for user-related functionalities.
models.py: Defines the CustomUser model with password hashing methods.
serializers.py: Serializer for CustomUser model.
views.py: API views for user registration and login.
urls.py: URL patterns for user-related endpoints.
tests.py: Testing User Related apis

# Setup:
1. Clone the repository: 
git clone https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao
cd DocuManager

2. Install dependencies:
pip3 install -r requirements.txt

3. Apply migrations:
python3 manage.py makemigrations
python3 manage.py migrate

4. Run the development server:
python3 manage.py runserver

The server will be up and running

# API Endpoints

Document Management:
- List Documents: GET /documents/
- Create Document: POST /documents/
- List Document Versions: GET /documents/<title>/versions/
- Switch Document Version: GET /documents/<title>/versions/<version>/
- Delete Document: POST /documents/delete/
- Revert to Previous Version: POST /documents/revertlatest/

User Management:

- Register User: POST /users/register/
- User Login: POST /users/login/

# Usage
- Register a user using the POST /users/register/ endpoint.
- Log in using the POST /users/login/ endpoint.
- Use the provided endpoints for document management.

# Run the tests in the test file and enjoy!

# Screenshots

<img width="669" alt="Screenshot 2023-12-29 at 8 07 09 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/d02957e1-cff7-4105-8247-d07dbab0ada2">
<img width="673" alt="Screenshot 2023-12-29 at 8 08 37 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/882c4404-96d6-4ec8-8a51-68a89529cb20">
<img width="672" alt="Screenshot 2023-12-29 at 8 08 53 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/65b25b13-c5ff-44cf-8a58-275d34722893">
<img width="672" alt="Screenshot 2023-12-29 at 8 16 32 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/e3ce3fd1-b478-4b52-bd9a-b6b1a75b486e">
<img width="670" alt="Screenshot 2023-12-29 at 8 17 46 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/f3ed5b01-76e3-44dc-be24-699a377922fe">
<img width="669" alt="Screenshot 2023-12-29 at 8 25 41 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/aab2cd4e-088f-4bd0-95be-563bc803b8fc">
<img width="671" alt="Screenshot 2023-12-29 at 8 27 44 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/dc2f9e3b-6915-4570-88e0-acce7c7af3cd">
<img width="670" alt="Screenshot 2023-12-29 at 8 28 49 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/6a284fa1-fe18-4340-afe8-886f11347aa0">
<img width="668" alt="Screenshot 2023-12-29 at 8 29 53 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/2bcac3cf-19ee-440a-adaf-ac4e00d0e195">
<img width="669" alt="Screenshot 2023-12-29 at 8 31 06 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/052a68d4-d849-4ac6-b179-a8167f8377b8">
<img width="670" alt="Screenshot 2023-12-29 at 8 41 25 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/25fd8f26-dc2e-48bc-90ef-6f05d958dd98">
<img width="669" alt="Screenshot 2023-12-29 at 8 41 44 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/4196922e-5f35-4bfa-a1c0-dc75652debce">
<img width="671" alt="Screenshot 2023-12-29 at 8 42 02 PM" src="https://github.com/soumyaarao/PhonePe-DocumentManager-SoumyaRao/assets/148032127/945e1555-cda9-4b27-9ac4-5aa8e846c973">








 
