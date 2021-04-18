FROM python:3.8-alpine3.12

RUN apk add --no-cache \
        bash

WORKDIR cron
COPY cron .
RUN pip3 install -r requirements.txt

CMD ["python3", "job.py"]
