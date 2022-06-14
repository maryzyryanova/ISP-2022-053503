FROM python:3.8.1-alpine3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY . .

RUN apk add --no-cache \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev git

RUN pip install -U pip

RUN pip install -r requirements.txt

# COPY ./../myenv .env

WORKDIR /app

COPY entrypoint.sh entrypoint.sh
# RUN ["chmod", "+x", "/app/backend/entrypoint.sh"]
EXPOSE 8000

# CMD ["/app/backend/entrypoint.sh"]
CMD [ "cd /app/backend && ./entrypoint.sh" ]