FROM python:3.12.4

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

ENV HOST=0.0.0.0
ENV PORT=8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]