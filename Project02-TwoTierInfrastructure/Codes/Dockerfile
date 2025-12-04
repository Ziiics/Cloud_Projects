FROM python:3.12-slim
WORKDIR /project2
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
EXPOSE 80
EXPOSE 443
CMD ["python", "app.py"]