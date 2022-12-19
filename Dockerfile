#
FROM python:latest

#
LABEL maintainer="ericghoubiguian@live.fr"

#
COPY . /WorldSwissKnifeAPI

#
WORKDIR /WorldSwissKnifeAPI

#
RUN apt upgrade -y && apt update -y

#
RUN apt install python3-pip -y

#
RUN pip3 install -r requirements.txt

#
EXPOSE 80

#
ENTRYPOINT ["python3", "main.py"]