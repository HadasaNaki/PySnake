FROM python:3.13-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install -y python3-pygame

RUN rm -rf /var/lib/apt/lists/*GI

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "game.py"]