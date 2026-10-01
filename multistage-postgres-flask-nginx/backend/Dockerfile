FROM python:3.15-rc-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --target=/app/packages/ -r requirements.txt
COPY app.py .

FROM python:3.15-rc-slim
WORKDIR /app
COPY --from=build /app/packages ./packages
COPY --from=build /app/app.py .
ENV PYTHONPATH=/app/packages
EXPOSE 5000
CMD ["python", "app.py"]