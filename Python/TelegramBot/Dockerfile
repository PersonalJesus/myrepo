FROM python:3.8-slim-buster

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

USER app

WORKDIR /app

COPY  requirements.txt requirements.txt
RUN   pip3 install -H --user -r requirements.txt

COPY  . /app/

CMD [ "python3","-u","./reminder.py" ]
