# Python Flask Exercises

This repository contains a collection of practice exercises built with **Flask**, focusing on routing, HTTP methods, error handling, and working with simple in-memory data structures. The goal of this project is to help you understand how to structure small Flask applications while experimenting with various API behaviors.

---

## 📌 Overview

This project demonstrates:

* Basic Flask route definitions
* Returning different response types (string, tuple, `make_response`)
* Handling query parameters
* Using Flask's built-in `uuid` converter
* Simple JSON-based CRUD operations (GET, POST, DELETE)
* Custom error handlers (404 + global exception handler)
* How API endpoints behave under different inputs

All data is stored in memory and resets each time the application restarts. This makes the project ideal for testing and experimentation.

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

Below is a quick summary of the API routes included in the project.

### **Root & Utility Routes**

| Method | Route         | Description                         |
| ------ | ------------- | ----------------------------------- |
| GET    | `/`           | Simple "hello world!" text response |
| GET    | `/exp`        | Example using `make_response()`     |
| GET    | `/no_content` | Returns a tuple-style response      |

### **Data Inspection Routes**

| Method | Route    | Description                               |
| ------ | -------- | ----------------------------------------- |
| GET    | `/data`  | Returns number of users in in-memory data |
| GET    | `/count` | Same as above, returns user count         |

### **Search & Retrieval**

| Method | Route                    | Description                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | `/name_search?q=<query>` | Case-insensitive name search |
| GET    | `/person/<uuid>`         | Fetch a user by UUID         |

### **Data Modification**

| Method | Route            | Description                      |
| ------ | ---------------- | -------------------------------- |
| POST   | `/person`        | Add a new user to in-memory data |
| DELETE | `/person/<uuid>` | Delete user by UUID              |

### **Testing Routes**

| Method | Route         | Description                                               |
| ------ | ------------- | --------------------------------------------------------- |
| GET    | `/testing500` | Manually triggers an exception to test the global handler |

---

## 🧪 Example cURL Commands

Below are a few sample commands you can use to test the API.

### **Get all user count**

```
curl -X GET localhost:5000/data
```

### **Search for a user**

```
curl -X GET "localhost:5000/name_search?q=Abdel"
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

* This project is meant for educational and practice purposes.
* Since it uses in-memory data, any restart of the server resets all data changes.
* Feel free to fork and extend the project for learning.

---

## 📄 License

This project is provided for educational purposes. You may modify and reuse it freely.

---

If you'd like, I can now generate **requirements.txt**, **.gitignore**, and an optional **EXAMPLES.md** as separate canvas files.
