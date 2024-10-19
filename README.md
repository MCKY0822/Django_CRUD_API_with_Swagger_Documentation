# Django CRUD API with Swagger and JWT Authentication

## Objective

Create a simple Django application that implements a CRUD API (Create, Read, Update, and Delete) for managing a weekly schedule with IDs associated with time slots for each day of the week. The application should include Swagger documentation and an explanation of how to implement basic authentication.

# Features

- Create, Read, Update, Delete (CRUD) operations for managing time slots in a weekly schedule.
- JWT Authentication for secure API access.
- Swagger UI for easy interaction with the API.


# Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/MCKY0822/Django_CRUD_API_with_Swagger_Documentation.git
   cd Django_CRUD_API_with_Swagger_Documentation
   ```

2. **Create a virtual environment:**

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```
   python manage.py createsuperuser
   ```

# Running the Project

1. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

2. **Access Swagger UI:**

   - Open your web browser and navigate to: `http://127.0.0.1:8000/swagger/`
   - This will provide you with a complete interface to interact with the API.

## Using JWT Authentication

### Obtain JWT Token

1. **Login with valid credentials** to obtain an access token:
   - **Method:** `POST`
   - Use the `TokenObtainPairView` to retrieve your JWT access and refresh tokens.

2. **Enter the JWT Access Token in Swagger UI:**
   - Click the **Authorize** button in the Swagger UI.
   - Input the token in the format:
     ```
     Bearer your_jwt_access_token
     ```
   - This allows you to access all secured endpoints directly through Swagger UI.

### Refresh JWT Token

- To refresh the token, you can use the `TokenRefreshView` in the Swagger UI.

## API Endpoints

### TimeSlots API

- **Create TimeSlot**: `POST /api/timeslots/`
- **Get All TimeSlots**: `GET /api/timeslots/`
- **Get a Specific TimeSlot**: `GET /api/timeslots/{id}/`
- **Update a TimeSlot**: `PUT /api/timeslots/{id}/`
- **Delete a TimeSlot**: `DELETE /api/timeslots/{id}/`

### Protected Endpoint

- **Access Protected Endpoint**: `GET /api/protected/`
  - This endpoint requires a valid JWT token and returns a message indicating successful authentication.

#

# MICHAEL R. MONTAÑA
michaelmontana@me.com
