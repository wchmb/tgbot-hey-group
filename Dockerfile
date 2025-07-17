FROM python:3-alpine
LABEL author="alebdm@icloud.com"

RUN apk add --no-cache tzdata
ENV TZ=Europe/Madrid

# Enable service for 'at' (schedule task only once)
# Weirdly I need to run rc-status first...
RUN apk --no-cache add at openrc && \
    mkdir -p /run/openrc && \
    touch /run/openrc/softlevel && \
    rc-update add atd default

COPY scripts/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY requirements.txt /tmp/ 
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /usr/app
COPY src/heyGiulia.py .
COPY scripts/crontab .
RUN crontab crontab

ENTRYPOINT ["entrypoint.sh"]
CMD ["crond", "-f"]
