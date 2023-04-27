FROM python:3.9-slim

COPY --from=openjdk:8-jre-slim /usr/local/openjdk-8 /usr/local/openjdk-8

ENV JAVA_HOME /usr/local/openjdk-8

RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-8/bin/java 1

# Copy files to directory
WORKDIR /tmp/app

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /tmp/

CMD ["python", "/tmp/app/extract_data.py"]
