# ↓ Main stage
FROM alpine:3.13

USER root

RUN apk add python3

RUN adduser -D dev
USER dev

COPY ./home/dev/ /home/dev/
COPY ./opt/dev-env/ /opt/dev-env/

USER root
RUN ln -s /home/dev/check.py ./usr/bin/check \
	&& ln -s /home/dev/update.py ./usr/bin/update
USER dev

WORKDIR /
