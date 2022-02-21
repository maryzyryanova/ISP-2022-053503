FROM python

WORKDIR /lab_1

RUN pip install numpy

COPY lab_1.py .

ENV PORT 4200

# VOLUME [" /lab_1/data "]

CMD ["python", "lab_1.py"]