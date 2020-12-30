FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Europe/Kyiv

RUN pip install -U pip
ADD src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

ADD wait-for-it.sh /usr/local/bin
RUN chmod +x /usr/local/bin/wait-for-it.sh

RUN mkdir /app
WORKDIR /app
ADD ./src /app
EXPOSE 8000
CMD ['bash', '/app/entrypoint.sh']
