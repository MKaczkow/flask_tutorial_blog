FROM python:3.10-alpine

# fixes cffi installation error, based on:
# https://stackoverflow.com/questions/71372066/docker-fails-to-install-cffi-with-python3-9-alpine-in-dockerfile
# https://github.com/gliderlabs/docker-alpine/issues/296
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["run.py"]