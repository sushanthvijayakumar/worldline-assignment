FROM python:3.11-alpine

RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver"]