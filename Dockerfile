FROM python:3.8.0a3-stretch

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/* ./

CMD ["python", "./app/app.py"]
