FROM python

WORKDIR /lab_1

COPY . .

EXPOSE 3000

RUN pip install numpy

CMD ["python", "lab_1.py"]