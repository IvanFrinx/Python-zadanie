FROM python:3.9-buster

# Install python 3.9 + pip
RUN apt-get update && apt install -y python3-pip
RUN python3 --version
RUN pip3 --version

COPY requirements.txt /home/app/requirements.txt

WORKDIR /home/app
RUN pip3 install -r requirements.txt
COPY docker /home/app
WORKDIR /home/app

ENTRYPOINT [ "python3", "main.py" ]