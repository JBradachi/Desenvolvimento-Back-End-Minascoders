FROM python:3.9-alpine

WORKDIR /app

RUN apk add python3-dev mysql-dev build-base pkgconfig 
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install flask
RUN pip install mysqlclient
RUN pip install flask-cors
RUN pip install mysql-connector-python

COPY . . 

CMD [ "python3",  "app.py" ]