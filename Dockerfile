FROM python:3.8

RUN mkdir /app

copy . /app

WORKDIR /app

RUN rm -rf venv

RUN pip install -r requirements.txt

CMD ["python", "app.py"]