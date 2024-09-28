# FastAPI Blog and User API
A FastAPI-based RESTful API for creating, managing, and fetching blog posts and users. This project includes authentication, database management using SQLAlchemy, and JWT token-based security.

---

## Technologies Used
- **Python**: Core programming language used for backend logic and application structure.
- **FastAPI**:  A modern, fast web framework used for building APIs with Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for database management.
- **SQLite**: Lightweight relational database used to store data.
- **OAuth2 (with JWT Token)**:  Authentication framework for handling secure user logins.
- **Pydantic**: Data validation and settings management using Python type hints.
- **bcrypt**: For securely hashing and verifying user passwords.
- **Passlib**: Library for secure password hashing and verification.
- **Uvicorn**: ASGI server for running FastAPI apps.
- **Swagger UI** and **Postman**: For testing and validating API requests and responses.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [License](#license)

---

## Project Description

- This project provides a backend API built using FastAPI. 
- The API allows users to perform CRUD operations on blog posts and user data, with JWT authentication to secure access.
-  SQLAlchemy is used for database management with SQLite as the backend.

## Key Features

- **Blog Management**: Users can create, read, update, and delete blog posts.
- **User Management**: Create and fetch user data.
- **JWT Authentication**: Secure endpoints using JWT tokens for login and authentication.
- **SQLAlchemy ORM**: Database operations are handled through the ORM.
- **Password Hashing**: User passwords are stored securely with bcrypt hashing.
- **Dynamic Routing**: Fetch and manage resources dynamically using route parameters.

---

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Abhimanyu-Gaurav/Learn_fastapi

2. Navigate to the project directory:
   ```bash
   cd Learn_fastapi

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

---

## How to Use

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

2. API will be running at:
    ```bash
    http://127.0.0.1:8000/

3. Open your browser (Safari, Chrome, Brave) and enter the URL:
   ```bash
   http://localhost:8000/docs#

4. API Endpoints:(view this in Swagger UI)
- **GET /**: Returns a welcome message.
- **GET /about**: Returns basic information about the API.
- **GET /blog**: Fetches published or unpublished blogs.
- **POST /blog**: Creates a new blog post.
- **GET /blog/{id}**: Fetches details of a specific blog post by its ID.
- **GET /user**: Fetches user details.
- **POST /login**: Logs in a user and returns a JWT token for authentication.

5. **Authentication**: Secure endpoints require a JWT token. To authenticate, log in using /login and pass the token in the Authorization header for subsequent requests:

---

### Send a POST request using API clients:
1. Using Postman:
    - Open Postman and click the "New" button to create a new request.
    - Set the request type to GET/POST/DELETE/PUT from the dropdown menu next to the URL field.
    - Set for check , whatever is in API endpoints.

2. Using cURL: 
    - we can perform it using cURL also.

---    

## License

- This project is licensed under the MIT License - see the [License](License) file for details.

---    