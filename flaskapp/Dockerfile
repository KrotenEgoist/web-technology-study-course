FROM python:3.8.10
WORKDIR /flaskapp
COPY requirements.txt /flaskapp
RUN pip install --upgrade pip -r requirements.txt
COPY . /flaskapp
EXPOSE 5000
