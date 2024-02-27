FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mysite .

CMD ["gunicorn", "--bind", "mysite.wsgi:application", "0.0.0.0:8000"]