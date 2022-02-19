FROM python

WORKDIR /lab_1

RUN pip install numpy

COPY . .

CMD ["python", "lab_1.py"]