# ↓ Main stage
FROM alpine:3.19.0

USER root

RUN apk add python3=~3

RUN adduser -D dev
USER dev

COPY ./home/dev/ /home/dev/
USER root
RUN chmod +x /home/dev/check.py \
	&& chmod +x /home/dev/sync.py
RUN ln -s /home/dev/check.py /usr/bin/check \
	&& ln -s /home/dev/sync.py /usr/bin/sync
USER dev

COPY ./opt/dev-settings-sync/ /opt/dev-settings-sync/

WORKDIR /
