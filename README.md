# Django Rest API

## Book_Giveaway_Service_project

Welcome to my Django Books project. This web application allows you to manage a collection of books. Users can register,
log in, add new books, update existing ones, delete books, and view the list of all available books. Each book entry
includes information such as the book title, authors, genres, condition of books, location, and also owner personal
details, such as contact phone number and name

## Features

- **User Authentication**: Users can register on the site and then log in and manage their books
- **Book Management**: Add new books with details like title, authors, genres condition, location. Update existing book
  entries and delete books
- **Owner Information**: Each book entry includes information about the owner, their name and their phone number, for
  easy contact
- **View All Books**: list of available books

## Technologies Used

- **Django:** For backend
- **Django REST Framework (DRF):** Used to create an API for managing books
- **SQLite Database:** To store book and user data
- **HTML, CSS:** For the frontend components and user interface
- **Docker:** For containerization

## Usage

1. __Clone the Repository:__

```
git clone https://github.com/LashaDemurashvili/Book_Giveaway_Service_project.git
```

2. __Set up docker__:

```
 docker build -t Book_Giveaway_Service_project .
```

```
 docker run -p 8000:8000 Book_Giveaway_Service_project
```

## API Endpoints

- **List of Books:** GET /home
- **User registration:** POST /reg
- **User login:** POST /my-login
- **User logout:** POST /user-logout
- **User dashboard:** GET /dash
- **CREATE a book:** POST /add
- **UPDATE a book:** PUT /update/{id}
- **Delete a Book:** DELETE /delete/{id}/



