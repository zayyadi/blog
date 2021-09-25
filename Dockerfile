FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["gunicorn","<yourprojectname>.wsgi","--bind","0.0.0.0:8000"]