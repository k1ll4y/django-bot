FROM python:3.11

WORKDIR /app

# RUN pip install gunicorn==20.1.0

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

COPY ./bot.sh .

COPY ./admin.sh .

RUN chmod +x ./bot.sh

RUN chmod +x ./admin.sh
