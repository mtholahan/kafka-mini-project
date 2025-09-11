FROM python:3.6

# Install netcat (nc)
RUN apt-get update && apt-get install -y netcat

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ADD ./ ./

# Add wait-for.sh script
COPY wait-for.sh .
RUN chmod +x wait-for.sh

# Use wait-for.sh as entrypoint
ENTRYPOINT ["./wait-for.sh"]
CMD ["python", "app.py"]
