FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY djangoProject .

CMD ["gunicorn", "--bind", "djangoProject.wsgi:application", "0.0.0.0:8000"]