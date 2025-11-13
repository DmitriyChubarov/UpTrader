FROM python:3.11-slim

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "sleep 5 && python3 manage.py makemigrations && python3 manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
