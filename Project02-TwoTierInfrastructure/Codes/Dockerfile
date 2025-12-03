FROM ubuntu:22.04
WORKDIR /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y python3-pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 3000