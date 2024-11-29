# rbac-syatem
Role-Based Access Control (RBAC) UI

# Authentication, Authorization, and RBAC System

This project is a role-based access control (RBAC) system implemented using Django REST Framework (DRF). It includes user authentication (JWT-based), role-based permissions (Admin, Moderator, and User), and secure API endpoints. The system ensures restricted access to API endpoints based on user roles.

---

## Features

- User registration with role assignment (`admin`, `moderator`, `user`).
- JWT-based authentication for secure login.
- Role-based access control for API endpoints.
- Custom user model with extended fields.
- Secure API endpoints for Admin, Moderator, and User roles.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (optional but recommended)
- Django 4.x
- SQLite (default database, or any other database if configured)
- Postman (optional, for testing APIs)
  
---

## Setup Instructions

1. Clone the Repository
   ```bash
   git clone <repository_url>
   cd <project_directory>

2. Create a Virtual Environment
   python -m venv venv
   source venv/bin/activate      # For Linux/MacOS
   venv\Scripts\activate         # For Windows

3. Install Dependencies
   pip install -r requirements.txt

4. Apply Migrations
   python manage.py makemigrations
   python manage.py migrate

5. Run the Development Server
   python manage.py runserver
   
7. Access the Application Open your browser or Postman and navigate to
   http://127.0.0.1:8000/.


## Usage
### Default Roles
1. **Admin**: Full access to manage users and permissions.
2. **Moderator**: Restricted access to manage content or specific sections.
3. **User**: Basic access to resources assigned by the admin.

### Admin Credentials (for testing):
- **Username**: `admin`
- **Password**: `admin123`

---

## API Documentation
### Authentication APIs
1. **Register User**
   - **URL**: `/auth/register/`
   - **Method**: POST
   - **Input**:
     ```json
     {
       "username": "exampleuser",
       "email": "example@mail.com",
       "password": "securepassword"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "User registered successfully."
     }
     ```

2. **Login User**
   - **URL**: `/auth/login/`
   - **Method**: POST
   - **Input**:
     ```json
     {
       "username": "exampleuser",
       "password": "securepassword"
     }
     ```
   - **Response**:
     ```json
     {
       "refresh": "generated_refresh_token",
       "access": "generated_access_token",
     }
     ```

3. **Logout User**
   - **URL**: `/auth/logout/`
   - **Method**: POST
   - **Headers**:
     ```json
     {
       "Authorization": "Bearer <your_jwt_token>"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Logged out successfully."
     }
     ```

### Role Management APIs
1. **Assign Role to User**
   - **URL**: `/auth/update-role/`
   - **Method**: POST
   - **Input**:
     ```json
     {
       "username": "exampleuser",
       "role": "Moderator"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Role assigned successfully."
     }
     ```

2. **List Roles**
   - **URL**: `/auth/roles/`
   - **Method**: GET
   - **Response**:
     ```json
     [
       "Admin",
       "Moderator",
       "User"
     ]
     ```

---

## Folder Structure
```
rbac-project/
├── rbac_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── test.py
│   ├── urls.py
│   ├── views.py
├── manage.py
```

---

## Testing
### 1. Run Unit Tests
```bash
python manage.py test
```

### 2. Test APIs
Use **Postman** or **curl** to test all APIs listed above.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact
For any queries or support, feel free to contact:
- **Email**: nikhleshshukla123@gmail.com
- **GitHub**: ([https://github.com/Nikhleshshukla123/])
```

