FROM python:3.9

WORKDIR /app

RUN pip3 install django

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000