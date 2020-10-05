FROM alpine:3.8

RUN apk add --no-cache \
	musl-dev \
	gcc \
	linux-headers \
	python3-dev \
	make \
    libc-dev \
    libxslt-dev \
    libxslt

COPY . /code
WORKDIR /code

RUN pip3 install -r requirements.txt
