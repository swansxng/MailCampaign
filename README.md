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

# Before running you should change some variables  
### email_service/email_service/serrings.py  
EMAIL_HOST = 'your provider'  
EMAIL_HOST_USER = 'your.mail@example.com'  
EMAIL_HOST_PASSWORD = 'your mail pass code'  

Also you can change mail template

