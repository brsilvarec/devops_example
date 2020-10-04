FROM ubuntu:18.04

MAINTAINER Bruno Silva "bruno.ufpe@gmail.com"

LABEL "name"="devops_example"

RUN apt-get update -y && apt-get install -y python3-pip curl
ENV SERVICE_DIR=/usr/local/share/service/mock_app
WORKDIR ${SERVICE_DIR}/

ENV PYTHONPATH=${SERVICE_DIR}/
COPY requirements.txt ${SERVICE_DIR}/requirements.txt
RUN pip3 install -r ${SERVICE_DIR}/requirements.txt
COPY . ${SERVICE_DIR}/

# document default port
ENV PORT=8080
EXPOSE ${PORT}
#USER service

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["python3"]

CMD ["application.py"]
