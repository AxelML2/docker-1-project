FROM python:3.9-slim 

WORKDIR /usr/src/app

# COPY example_1.csv .

# COPY example_2.csv .

COPY cleaner.py .

RUN pip3 install pandas

CMD ["python", "cleaner.py"]