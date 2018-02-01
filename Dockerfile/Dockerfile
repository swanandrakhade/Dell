FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install pydicom

CMD [ "python", "./test.py" ]