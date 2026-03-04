# Project Name: [e.g., Global-Country-API]
A Django REST API for managing and searching international country data.

## 🌟 Features
* **Full CRUD Functionality**: Create, Read, Update, and Delete country records.
* **Smart Search**: Filter countries by name using partial matching (icontains).
* **RESTful Design**: Built using Django REST Framework best practices.
* **Data Validation**: Ensures inputs are sanitized and valid before saving to the database.
* **Idempotency**: Designed PUT and DELETE endpoints to be idempotent, ensuring system stability even if network requests are duplicated.

## 🛠️ Tech Stack
* **Backend**: Python, Django, Django REST Framework, ORM
* **Database**: PostgreSQL (No need for Redis or MongoDB)
* **Tools**: Postman (for API testing)


## Architecture

1. **Client Request**: The client sends an HTTP request in JSON.

2. **Security & RBAC Layer**: Django middleware intercepts the request to verify the API Key (Authentication) and checks DRF Permission Classes to ensure the user has the correct role to perform the action (Authorization).

3. **Data Deserialization & Validation**: The Django REST Framework (DRF) Serializer intercepts the JSON, translates it into native Python objects, and runs strict validation checks to sanitize inputs.

4. **ORM Translation**: If valid, the business logic executes. The Django ORM acts as an abstraction layer, translating Python code into secure, parameterized SQL queries (preventing SQL injection).

5. **Database Execution**: PostgreSQL safely executes the CRUD operation while maintaining referential integrity.

6. **Response Delivery**: The system serializes the result back into a predictable JSON format and returns the appropriate HTTP status code (e.g., 201 Created for a success, 400 Bad Request if validation fails, or 403 Forbidden if RBAC fails).

## 📋 How to Run Locally
1. **Clone the repo**:
   `git clone https://github.com/VishvaAr/global-countries-api.git`
2. **Install dependencies**:
   `pip install -r requirements.txt`
3. **Run Migrations**:
   `python manage.py migrate`
4. **Start the server**:
   `python manage.py runserver`

## 📡 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/api/countries` | Retrieve all countries (supports `?name=` query param) |
| POST | `/api/countries` | Add a new country |
| GET | `/api/countries/<id>` | Get details for a specific country |
| PUT | `/api/countries/<id>` | Update an existing country |
| DELETE | `/api/countries/<id>` | Delete a country |

## 📸 Screenshots / Demo
<img width="1720" height="1158" alt="image" src="https://github.com/user-attachments/assets/09837df2-9000-46b3-8617-42e58af8c907" />
