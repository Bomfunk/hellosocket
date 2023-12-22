FROM alpine

WORKDIR /usr/src/app

RUN apk add --no-cache python3

COPY hellosocket.py hellosocket.py

CMD [ "python", "-u", "hellosocket.py" ]
