FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /mysite
COPY ./mysite /mysite/
WORKDIR /mysite

RUN pip install --upgrade pip
RUN pip install -r requirements.txt