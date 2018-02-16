# To check celery logs 
celery -A myproject worker -l info
celery -A myproject beat -l info
celery -A myproject beat -l info

