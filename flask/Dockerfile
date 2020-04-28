FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN pip install python-dotenv
CMD ["uwsgi", "app.ini"]
