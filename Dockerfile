FROM python:3.8-buster

COPY . /usr/src/iafrohack-backend/

RUN chmod +x /usr/src/iafrohack-backend/startup.sh

RUN mkdir -p /var/lib/iafrohack/
RUN mkdir -p /var/lib/iafrohack/.config

WORKDIR /usr/src/iafrohack-backend/

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip

RUN pip install pipenv

RUN pipenv install --system -v

# We have to install pyrebase separately, outside of norma Pipenv install
# because the official pyrebase repo is outdated and not maintained.
# It's requests package is outdated.
RUN pipenv install git+https://github.com/Selich/Pyrebase.git#egg=Pyrebase -v

RUN pipenv run pip freeze > requirements.txt

ENV PIPENV_VENV_IN_PROJECT 1

RUN mkdir -p /var/log/iafrohack/
RUN > /var/log/iafrohack/iafrohack_logs.log

# Create the group and user to be used in this container
RUN groupadd iafrohackgroup && useradd -m -g iafrohackgroup -s /bin/bash iafrohack

# Expose the port where uWSGI will run
EXPOSE 5000

# Change owner of application files
RUN chown -R iafrohack:iafrohackgroup /usr/src/iafrohack-backend/
RUN chown -R iafrohack:iafrohackgroup /var/log/iafrohack/*

RUN chown -R iafrohack:iafrohackgroup /var/lib/iafrohack/
RUN chown -R iafrohack:iafrohackgroup /usr/src/iafrohack-backend/

# Change user
USER iafrohack

RUN mkdir -p /var/lib/iafrohack/.config/

# Set the credentials Path
# If we get an error with file not found on GC run deployment,
# remove the path from .gitignore, deploy, then add it again.
# It seems that Google Cloud Run will accept app files only if in version control
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/iafrohack-backend/firebaseServiceAccount.json"

ENV PROJECT_ID="iafrohack"

ENV PORT 5000
ENV HOST 0.0.0.0

CMD ["bash", "./startup.sh"]
