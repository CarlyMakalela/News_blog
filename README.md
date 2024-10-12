# News_blog
Creating a blog using python and web technologies

# Blog a Fact

A Django-powered news blog application developed from scratch using modern web technologies and Python Django. The project allows users to read, post, and manage news articles, making it an ideal platform for bloggers or small news outlets.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)


## Project Overview

*Blog a Fact* is a customizable news blog platform built using Python's Django framework. It enables users to view and interact with news articles, and admins can manage the content. The blog is fully responsive, SEO-optimized, and structured with clean and readable code to facilitate easy modification and expansion.

## Features

- *User-Friendly Interface*: A clean and intuitive UI for easy navigation.
- *CRUD Functionality*: Users can create, read, update, and delete posts (admin only for certain tasks).
- *Authentication*: User registration, login, and logout functionality with secure password storage.
- *Search Functionality*: Users can search for posts using keywords.
- *Responsive Design*: Fully functional across desktop, tablet, and mobile devices.
- *SEO-Optimized*: Proper meta tags for search engine indexing.
- *Django Admin Interface*: Easy-to-use admin panel for managing posts and users.

## Tech Stack

- *Backend*: Django (Python)
- *Frontend*: HTML, bootstrap 
- *Database*: SQLite (default), but you can configure MySQL, PostgreSQL, etc.
- *Version Control*: Git
- *Deployment*: Manual setup for local development (can be deployed to a hosting platform of your choice)

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 4.0+
- Git
- Virtualenv (optional but recommended)

### Installation

1. *Clone the repository*:
    bash
    git clone https://github.com/CarlyMakalela/News_blog.git
    cd blog-a-fact
    

2. *Create a virtual environment* (optional but recommended):
    bash
    python3 -m venv env
    source env/bin/activate  # For Windows, use `env\Scripts\activate`
    

3. *Install dependencies*:
    bash
    pip install -r requirements.txt
    

4. *Set up the database*:
    bash
    python manage.py migrate
    

5. *Create a superuser* (to access the Django admin panel):
    bash
    python manage.py createsuperuser
    

6. *Run the server*:
    bash
    python manage.py runserver
    

7. Open your browser and go to http://127.0.0.1:8000/ to view the blog.

## Usage

1. Navigate to the homepage to view all available articles.
2. Users can register and log in to interact with posts (if enabled).
3. Admins can log in via the /admin URL to manage the content and users.

## Contributing

Contributions are welcome! If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature-name).
5. Open a Pull Request.

 of this!
