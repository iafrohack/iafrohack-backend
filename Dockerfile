FROM python:3.8.0a3-stretch

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

CMD ["python", "./app/app.py"]
