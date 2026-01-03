# Project Name: [e.g., Global-Country-API]
A Django REST API for managing and searching international country data.

## 🌟 Features
* **Full CRUD Functionality**: Create, Read, Update, and Delete country records.
* **Smart Search**: Filter countries by name using partial matching (icontains).
* **RESTful Design**: Built using Django REST Framework best practices.
* **Data Validation**: Ensures inputs are sanitized and valid before saving to the database.

## 🛠️ Tech Stack
* **Backend**: Python, Django, Django REST Framework
* **Database**: SQLite (or PostgreSQL/MySQL)
* **Tools**: Postman (for API testing)

## 📋 How to Run Locally
1. **Clone the repo**:
   `git clone https://github.com/VishvaAr/project-name.git`
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
(Optional: Add a screenshot of your Postman results or a link to a live demo here)
