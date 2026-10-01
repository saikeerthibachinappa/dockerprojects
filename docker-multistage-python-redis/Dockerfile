FROM python:3.15-rc-slim AS runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install --target=/app/packages -r requirements.txt
COPY app.py .

FROM python:3.15-rc-slim
WORKDIR /app
COPY --from=runtime /app/packages ./packages
COPY --from=runtime /app/app.py ./app.py

ENV PYTHONPATH=/app/packages
EXPOSE 5000

CMD ["python", "app.py"]
