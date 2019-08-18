FROM python:3.7.3-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /var/log/iafrohack/
RUN > /var/log/iafrohack/iafrohack_logs.log

COPY ./app/* ./

# Create the group and user to be used in this container
RUN groupadd iafrohackgroup && useradd -m -g iafrohackgroup -s /bin/bash iafrohack

# Expose the port where uWSGI will run
EXPOSE 80

# Change owner of application files
RUN chown -R iafrohack:iafrohackgroup /usr/src/app
RUN chown -R iafrohack:iafrohackgroup /var/log/iafrohack/iafrohack_logs.log

RUN mkdir -p /var/lib/iafrohack/
RUN chown -R iafrohack:iafrohackgroup /var/lib/iafrohack/

# Change user
USER iafrohack

#RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
#RUN chmod +x cloud_sql_proxy

#RUN pip install --upgrade google-cloud-firestore

ENV GOOGLE_APPLICATION_CREDENTIALS="/var/lib/iafrohack/.config/gcloud/iafrohack-firestore.json"

CMD ["python", "./app/app.py"]
