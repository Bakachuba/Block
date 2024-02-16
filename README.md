# Blocks: Task and Idea Management Project

_Blocks is a Django-based project designed for efficient task management, summarizing, handling periodic tasks, organizing lists, and capturing creative ideas._

## Used Stack:

1) Python
2) Django
3) DRF
4) PostgreSQL
5) HTML + CSS + JS
6) UnitTests 
7) Redis cache

- Logging
- Djoser 
- JWT 
- Session-based auth
- Debug toolbar

## Features

- **Tasks:** Create, view, and manage your work notes.
- **Summaries:** Keep track of book summaries and related information.
- **Periodic Tasks:** Schedule and manage recurring tasks.
- **Lists:** Organize tasks into lists and categories.
- **Ideas:** Capture and manage your creative ideas.

## Getting Started

(It is assumed that you already have a postgresql database with the following parameters:
'NAME': 'Block',
       'USER': 'USER',
        'PASSWORD': '2585',
        'HOST': 'localhost',
        'PORT': '5432',)

0. Install Redis

   [Redis Installation Guide for Windows](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

1. Clone the repository:

   (tbranch)
   `git clone https://github.com/Bakachuba/Block.git`

2. Navigate to the project directory:

   `cd blocks-project`

3. Create a virtual environment and install dependencies:

   `python -m venv venv`

   `pip install -r requirements.txt`

4. Apply migrations:

   `python manage.py migrate`

5. Run the development server:

   `python manage.py runserver`

6. Open the project in your web browser:
   [http://localhost:8000](http://localhost:8000)

## Authentication and Authorization

**Authentication**

- Implemented authentication using Djoser tokens for API.
- Added session-based authentication.
- JWT authentication is also supported.

**Management:**

1) Create a Post request user at the address (Postman)
   [http://localhost:8000/api/auth/users/](http://localhost:8000/api/auth/users/)
   with margins: (Body)
   username, password, email
2) Create a new note for an authorized user at:
   [http://localhost:8000/api/ideas/](http://localhost:8000/api/ideas/)
   with fields in Headers:
   Authorization; Token token_number
   with Body (raw)

**Authorization**

1) Authorization
   [http://127.0.0.1:8000/accounts/login/?next=/profile](http://127.0.0.1:8000/accounts/login/?next=/profile)

## models.py

1. Notes (Task) and Idea:

Relationship: One-to-Many
Description: Each task (Notes) can have multiple ideas (Idea), but each idea belongs to only one task.

2. Summary and Notes (Task):

Relationship: One-to-Many
Description: Each summary (Summary) is associated with one task (Notes), but each task can have multiple summaries.

3. Periodic Task and Notes (Task):

Relationship: One-to-One
Description: Each periodic task (Periodic) is linked to one task (Notes), and vice versa. Each task can be associated
with only one periodic task.

4. List and Category:

Relationship: Many-to-Many
Description: Each list (List) can belong to multiple categories (Category), and each category can contain multiple
lists.

## Tests

Using Unittests with coverage library.

coverage library.
commands to do:

1) `coverage run --source=. ./manage.py test blocks.tests`
2) `coverage report`
3) `coverage html`
   total cover = 81%

## Logs

1) Navigating to the main page.
2) API requests.
3) Creating notes without navigating to the API.
4) Exception links.
5) SQL requests monitoring

Logs are in JSON format.

## Redis

1) 'Home' page cached

## Exception links

Added custom request exception handler

## Addition:

Django has been rolled back to version 4.2.5 for correct logout from the account
