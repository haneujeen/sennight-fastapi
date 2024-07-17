# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

COPY .env .env

EXPOSE 3100

CMD ["gunicorn", "app.main:app"]