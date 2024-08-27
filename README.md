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

### 1. User Signup

- **Endpoint:** `POST /signup`
- **Description:** Register a new user.
- **Request Headers:** None
- **Request Body:**

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

- **Response:**

    - **Success (201 Created):**

        ```json
        {
          "msg": "User created successfully"
        }
        ```

    - **Error (400 Bad Request):**
        
        - **Missing Fields:**

            ```json
            {
              "msg": "Username and password are required"
            }
            ```

        - **Username Already Exists:**

            ```json
            {
              "msg": "Username already exists"
            }
            ```

### 2. User Login

- **Endpoint:** `POST /login`
- **Description:** Authenticate users and issue JWT tokens.
- **Request Headers:** None
- **Request Body:**

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

- **Response:**

    - **Success (200 OK):**

        ```json
        {
          "access_token": "your_jwt_token"
        }
        ```

    - **Error (401 Unauthorized):**

        ```json
        {
          "msg": "Invalid username or password"
        }
        ```

### 3. CSV Upload

- **Endpoint:** `POST /upload`
- **Description:** Upload product data from a CSV file to the database.
- **Request Headers:**

    - `Authorization: Bearer <your_jwt_token>`
    - `Content-Type: multipart/form-data`

- **Request Body:**

    - **Form Data:**

        - `file: your_file.csv`

- **Response:**

    - **Success (200 OK):**

        ```json
        {
          "msg": "Data uploaded successfully"
        }
        ```

    - **Error (400 Bad Request):**
        
        - **No File Part:**

            ```json
            {
              "msg": "No file part"
            }
            ```

        - **No Selected File:**

            ```json
            {
              "msg": "No selected file"
            }
            ```

        - **Missing Columns:**

            ```json
            {
              "msg": "Missing column: column_name"
            }
            ```

        - **Database Errors:**

            ```json
            {
              "msg": "<error_message>"
            }
            ```

### 4. Protected Route

- **Endpoint:** `GET /protected`
- **Description:** Access protected routes with JWT authentication.
- **Request Headers:**

    - `Authorization: Bearer <your_jwt_token>`

- **Response:**

    - **Success (200 OK):**

        ```json
        {
          "logged_in_as": "your_username"
        }
        ```

    - **Error (401 Unauthorized):**

        ```json
        {
          "msg": "Missing or invalid token"
        }
        ```

## CSV File Format

The CSV file should have the following columns:

- `product_id` (string)
- `product_name` (string)
- `category` (string)
- `price` (float)
- `quantity_sold` (integer)
- `rating` (float)
- `review_count` (integer)

Ensure that the CSV file uses these exact column names and types for successful upload.

## Error Handling

- **Missing File**: `"msg": "No file part"`
- **No Selected File**: `"msg": "No selected file"`
- **Missing Column**: `"msg": "Missing column: column_name"`
- **Database Errors**: `"msg": "<error_message>"`


## SQL Query

- **Inside Query.txt File**
