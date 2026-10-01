FROM python:3.15-rc-alpine3.23

WORKDIR /dir

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]

