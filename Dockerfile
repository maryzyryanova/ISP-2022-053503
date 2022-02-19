FROM python

WORKDIR /lab_1

COPY . .

RUN pip install numpy

CMD ["python", "lab_1.py"]