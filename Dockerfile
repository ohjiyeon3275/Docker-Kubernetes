FROM python:3.9

WORKDIR /app

RUN pip3 install flask

COPY . .

VOLUME [ "/app/temp" ]

CMD ["python3", "main.py"]

EXPOSE 3333
