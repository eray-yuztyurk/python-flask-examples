# Python Flask Exercises

This repository contains a collection of practice exercises built with **Flask**, focusing on routing, HTTP methods, error handling, redirecting, working with forms, and simple in-memory CRUD operations. The goal of this project is to help you understand how to structure small Flask applications and explore a wide range of API behaviors.

---

## 📌 Overview

This project demonstrates:

* Basic Flask route definitions
* Returning different response types (string, tuple, `make_response`)
* Query parameters & input validation
* Using Flask's built-in `uuid` converter
* JSON-based CRUD operations (GET, POST, DELETE)
* Dynamic URL generation via `url_for`
* Redirecting with `redirect()`
* Handling form data (`request.form`)
* Custom error handlers (404 handler + global exception handler)
* A route that intentionally raises errors for testing
* Simple HTML examples for CRUD templates (read/update/delete/create)
* Additional routing examples supporting multiple HTTP methods

All data is stored in memory and resets each time the application restarts, making it perfect for testing and experimentation.

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### **1. Clone the Repository**

```
git clone https://github.com/<your-username>/python-flask-exercises.git
cd python-flask-exercises
```

### **2. Create a Virtual Environment**

```
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

### **4. Run the Application**

```
python app.py
```

The server will start at:

```
http://localhost:5000
```

---

## 📚 Available Endpoints

Below is a quick summary of the main API routes included in the project.

---

### **Root & Utility Routes**

| Method | Route         | Description                                  |
| ------ | ------------- | -------------------------------------------- |
| GET    | `/`           | Simple "hello world!" text response          |
| GET    | `/exp`        | Example using `make_response()`              |
| GET    | `/no_content` | Returns a tuple-style JSON + status response |

---

### **Data Inspection Routes**

| Method | Route         | Description                         |
| ------ | ------------- | ----------------------------------- |
| GET    | `/data_count` | Returns number of records in memory |
| GET    | `/count`      | Same as above, alternative endpoint |

---

### **Search & Retrieval**

| Method | Route                    | Description                           |
| ------ | ------------------------ | ------------------------------------- |
| GET    | `/name_search?q=<query>` | Case-insensitive search by first name |
| GET    | `/person/<uuid>`         | Fetch a user record by UUID           |

---

### **Data Modification (CRUD API)**

| Method | Route            | Description                |
| ------ | ---------------- | -------------------------- |
| POST   | `/person`        | Add a new user (JSON body) |
| DELETE | `/person/<uuid>` | Delete a user by UUID      |

---

### **Form & HTML Based Routes**

| Method     | Route          | Description                              |
| ---------- | -------------- | ---------------------------------------- |
| POST       | `/user_login`  | Reads form data (`username`, `password`) |
| GET / POST | `/create`      | Create HTML form → saves record          |
| GET / POST | `/update/<id>` | Update record via HTML form              |
| POST       | `/delete/<id>` | Delete using HTML form submission        |
| GET        | `/read/<id>`   | Render a record using template           |

(Functions such as `get_record`, `update_record`, `delete_record`, `create_new_record` are placeholders for demonstration.)

---

### **Redirecting & URL Generation**

| Method | Route          | Description                        |
| ------ | -------------- | ---------------------------------- |
| GET    | `/admin`       | Redirects to `/login_user`         |
| GET    | `/admin_login` | Redirects using `url_for()`        |
| GET    | `/login_user`  | Returns a simple login placeholder |

---

### **Method Handling Examples**

| Method(s)  | Route   | Description                                       |
| ---------- | ------- | ------------------------------------------------- |
| GET / POST | `/data` | Example of handling two HTTP methods in one route |

---

### **Error Handling**

| Handler | Purpose                                 |
| ------- | --------------------------------------- |
| 404     | Custom “API not found” JSON response    |
| 500     | Global exception handler (catch-all)    |
| GET     | `/testing500` → manually triggers error |

---

## 🧪 Example cURL Commands

### **Get user count**

```
curl -X GET localhost:5000/data_count
```

### **Search for a user**

```
curl -X GET "localhost:5000/name_search?q=Lukas"
```

### **Add a new user**

```
curl -X POST \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
  }'
```

### **Delete a user**

```
curl -X DELETE localhost:5000/person/<uuid-here>
```

### **Trigger the global exception handler**

```
curl -X GET localhost:5000/testing500
```

---

## 📂 Project Structure

```
python-flask-exercises/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📝 Notes

* This project is for educational and practice purposes.
* Since all data lives in memory, the dataset resets on every restart.
* Examples include HTML forms, redirecting, CRUD templates, and error testing.
* Feel free to fork and extend the project for learning.

---

## 📄 License

This project is provided for educational purposes.
You may modify and reuse it freely.
