FROM python:3.13.4-slim

# Prevent python from wrtting .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# force python to output logs directly to terminal
ENV PYTHONUNBUFFERED=1
# stop prevent pip from print version in install package
ENV PIP_DISABLE_PIP_VERSION_CHECK 1


WORKDIR ./code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

copy . .

