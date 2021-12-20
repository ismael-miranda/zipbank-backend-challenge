FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /api-animals
WORKDIR /api-animals
COPY . /api-animals
RUN pip3 install -r requirements.txt