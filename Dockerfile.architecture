FROM --platform=$TARGETPLATFORM python:3.9.7-alpine
ENV TZ=Asia/Shanghai

WORKDIR /tmp
COPY ./requirements.txt ./
RUN adduser app -D \
    && apk add --no-cache tzdata \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /tmp/*

WORKDIR /app
COPY index.py ./
COPY alert ./alert

USER app
CMD [ "python3", "./index.py" ]