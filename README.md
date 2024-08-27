# Flask E-Commerce Backend

This project is a Flask-based backend for an e-commerce platform, featuring user authentication, product management, and CSV file upload functionality. The backend uses Flask, Flask-SQLAlchemy, Flask-Bcrypt, and Flask-JWT-Extended to handle various aspects of the application.

## Features

- **User Signup**: Register a new user.
- **User Login**: Authenticate users and issue JWT tokens.
- **CSV Upload**: Upload product data from a CSV file to the database.
- **Protected Route**: Access protected routes with JWT authentication.

## Prerequisites

Ensure you have the following installed:

- Python 3.6 or later
- MySQL Server
- Required Python packages

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **Windows**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux**

        ```bash
        source venv/bin/activate
        ```

4. **Install the Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

5. **Update Database Credentials**

    Modify the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` to include your MySQL database credentials:

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname:port/database_name'
    ```

6. **Run the Application**

    ```bash
    python app.py
    ```

    The application will run on `http://127.0.0.1:5000`.

## API Endpoints

- **Signup**
  
  `POST /signup`
  
  **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }


## SQL Query

- **Inside Query.txt File**
