FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ADD . ./

COPY wait-for.sh .
RUN chmod +x wait-for.sh
CMD ["./wait-for.sh", "broker:9092", "--", "python", "app.py"]

RUN ls -la /usr/app

CMD ["python", "app.py"]
