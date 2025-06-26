# BOOK LIBRARY API:

- A simple RESTful API server built with Flask and SQLite that allows you to manage a book library with full CRUD operations (Create, Read, Update, Delete)

# FEATURES:

- Add new books to the database
- Retrieve all books or a specific one
- Update existing book information
- Delete books from the database
- Uses SQLite as the database (file-based, no setup required)

# TECH STACK:

Backend: Python + Flask
ORM: Flask-SQLAlchemy
Database: SQLite
Testing: Postman

# API DOCUMENTATION:

This project includes a custom REST API built using Flask. The API allows users to manage a library of books with basic Create, Read, Update, and Delete (CRUD) operations. It connects to an SQLite database and serves a frontend HTML page where users can interact with the API directly.

There are five main API endpoints:

- GET /books: returns a list of all books in the database.
- GET /books/<id>: returns the details of a specific book by its ID.
- POST /books: allows users to add a new book by sending JSON data including title, author, year_published, and genre
- PUT /books/<id>: allows users to update the details of an existing book using its ID and sending new data in JSON format.
- DELETE /books/<id>: deletes the book with the specified ID.

All endpoints return data in JSON format. To test these APIs, users can either use tools like Postman, curl commands in a terminal, or the included HTML frontend (index.html) which interacts with the API through JavaScript.

When deployed on a platform like Render, you must replace "http://localhost:5000" with your deployed site URL e.g., any "site url you will host it on" , i used render specifically. not changing the url will result in incorrect result as the frontend will not interact with the API as you want due to difference in the addresses.

✅ Keploy API Testing Report:
![Test Coverage Screenshot](screenshots/keploy-test-report.png)
