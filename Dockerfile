# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 3100

LABEL version="0.1.3" \
      description="Fix not being able to create user's custom motivation" \
      maintainer="한유진 <eujeenhan@gmail.com>"

CMD ["gunicorn", "app.main:app"]