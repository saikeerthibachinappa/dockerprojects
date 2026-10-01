From python:3.15-rc-slim

WORKDIR /backend

COPY ./backend .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
