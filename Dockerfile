FROM python:3.9

WORKDIR /app

COPY . .

VOLUME [ "/app/temp" ]

CMD ["python3", "main.py"]
