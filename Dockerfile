# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 3100

LABEL version="0.2.0" \
      description="Update user milestone API" \
      maintainer="한유진 <eujeenhan@gmail.com>"

CMD ["gunicorn", "app.main:app"]