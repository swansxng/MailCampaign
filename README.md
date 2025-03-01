# MailCampaign
### Create venv near repository:  
python -m venv venv  
venv\Scripts\activate  

### Install django, celery and redis via  
pip install django celery redis  

### Make migrations  
cd email_service <small>Entering the project folder</small>  
python manage.py makemigrations  
python manage.py migrate  

### Running  
python manage.py runserver  
