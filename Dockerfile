FROM python

WORKDIR /ИСП/ISP-2022-053503

RUN pip install numpy

COPY . .

ENV PORT 4200

VOLUME [" /lab_1/data "]

CMD ["python", "lab_1.py"]