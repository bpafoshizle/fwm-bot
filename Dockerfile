FROM python:3.9.1-alpine
RUN apk --no-cache add gcc musl-dev

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ .

CMD [ "python", "./app.py" ]