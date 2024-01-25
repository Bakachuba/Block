## This is my pet project

_Blocks is a Django-based project for managing tasks, summaries, periodic tasks, lists, and ideas._

## Features

- **Tasks:** Create, view, and manage your work notes.
- **Summaries:** Keep track of book summaries and related information.
- **Periodic Tasks:** Schedule and manage recurring tasks.
- **Lists:** Organize tasks into lists and categories.
- **Ideas:** Capture and manage your creative ideas.

## Getting Started


1. Clone the repository:

   (tbranch)
git clone https://github.com/Bakachuba/Block.git


2. Navigate to the project directory:

cd blocks-project

3. Create a virtual environment and install dependencies:

python -m venv venv

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver

6. Open the project in your web browser: 
http://localhost:8000


## models.py


1. Notes (Task) and Idea:

Relationship: One-to-Many
Description: Each task (Notes) can have multiple ideas (Idea), but each idea belongs to only one task.

2. Summary and Notes (Task):

Relationship: One-to-Many
Description: Each summary (Summary) is associated with one task (Notes), but each task can have multiple summaries.

3. Periodic Task and Notes (Task):

Relationship: One-to-One
Description: Each periodic task (Periodic) is linked to one task (Notes), and vice versa. Each task can be associated with only one periodic task.

4. List and Category:

Relationship: Many-to-Many
Description: Each list (List) can belong to multiple categories (Category), and each category can contain multiple lists.

## Tests

Using Unittests
created tests for: 
1) API.get 
and
2) DB models

coverage library.
commands to do:
1) coverage run --source=. ./manage.py test blocks.tests    
2) coverage report
3) coverage html
total  cover = 81%


## Logs

1) Logs have been added for navigating to the main page.
2) For API requests.
3) For creating notes without navigating to the API.