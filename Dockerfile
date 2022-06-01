FROM python:3.9.1-alpine3.12
RUN apk --no-cache add gcc=9.3.0-r2 musl-dev=1.1.24-r10 git=2.26.3-r1

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ .

CMD [ "python", "./app.py" ]