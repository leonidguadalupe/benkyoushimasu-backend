FROM alpine:3.8

RUN apk add --no-cache \
    postgresql-libs \
    build-base \
	musl-dev \
	gcc \
	linux-headers \
	python3-dev \
	make \
    postgresql-client \
    postgresql-dev \
    libxslt-dev \
    libxslt

COPY . /code
WORKDIR /code

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
