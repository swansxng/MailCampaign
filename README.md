# MailCampaign
Create venv near repository:
**python -m venv venv**
**venv\Scripts\activate**

Install django, celery and redis via
**pip install django celery redis**

Make migrations
**cd email_service** # Entering the project folder
**python manage.py makemigrations**
**python manage.py migrate**

Running
**python manage.py runserver**
