FROM python:3

WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["python", "main.py"]
