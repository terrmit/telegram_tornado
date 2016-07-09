FROM alpine:latest

RUN apk add --update python py-pip bash

COPY deps/python.txt /
RUN pip install --disable-pip-version-check -r python.txt

COPY src/ src/

RUN pip install /src/

RUN adduser -D myuser
USER myuser

CMD bot_webhook
