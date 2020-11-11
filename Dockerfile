FROM debian:buster

COPY main.py /bot/
COPY cred.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "main.py"]