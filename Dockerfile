FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN adduser --disabled-password --no-create-home --gecos '' batimap
USER batimap
COPY requirements.txt ./
RUN pip install -r requirements.txt