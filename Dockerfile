FROM python:3.9

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

# EXPOSE 8080

COPY . /src/

# CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

