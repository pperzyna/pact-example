FROM python:3.7-alpine

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

# RUN  addgroup -S django; \ 
#      adduser -h /home/django -S -G django django
# USER django

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "dev" ]