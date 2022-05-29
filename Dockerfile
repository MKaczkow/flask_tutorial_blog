FROM python:3.10-alpine as base

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

################################################

FROM base as final 

COPY ./flask_tutorial_blog /app
COPY run.py /app
EXPOSE 8000

ENTRYPOINT [ "python", "app/run.py" ]