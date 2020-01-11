FROM python:3.6-alpine

ENV TOKEN ""
ENV DB_URI sqlite///./test.db

WORKDIR /usr/src/gunbrokerbot

COPY App/* ./App/
COPY bot.py ./
COPY requirements.txt ./

RUN apk --no-cache add --virtual build postgresql-dev gcc python3-dev musl-dev git \
    && pip install -r requirements.txt \
    && pip install psycopg2-binary \
    && apk del build \
    && apk --no-cache add postgresql-libs \
    && pip -r install requirements.txt

CMD python3 ./run.py