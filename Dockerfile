FROM python:3.8-slim

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMN 80

RUN mkdir /setup
WORKDIR /setup/

COPY ./django/ /setup/
COPY docker/start.sh /setup//
COPY docker/requirements/. /setup/
COPY docker/entrypoint.sh /

RUN pip install -r main.txt

RUN sh start.sh

ENTRYPOINT [ "/entrypoint.sh" ]