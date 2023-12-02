FROM python:3.11.6

EXPOSE 5001

RUN mkdir /bot
WORKDIR /bot

COPY . /bot

RUN pip install -r requirements.txt

CMD ["python", "/bot/main.py"]


