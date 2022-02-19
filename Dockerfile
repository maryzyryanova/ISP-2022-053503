FROM python

WORKDIR /app

COPY . .

CMD ["python", "lab_1.py"]