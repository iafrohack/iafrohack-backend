FROM python:3.7.3-stretch

RUN pip install python-dotenv

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/* ./

# Create the group and user to be used in this container
RUN groupadd iafrohackgroup && useradd -m -g iafrohackgroup -s /bin/bash iafrohack

# Expose the port where uWSGI will run
EXPOSE 80

# Change owner of application files
RUN chown -R iafrohack:iafrohackgroup /usr/src/app

# Change user
USER iafrohack

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
RUN chmod +x cloud_sql_proxy

CMD ["python", "./app/app.py"]
