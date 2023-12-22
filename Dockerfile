FROM alpine

WORKDIR /usr/src/app

COPY hellosocket.py hellosocket.py

CMD [ "python", "-m", "bot.main" ]
