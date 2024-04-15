#FROM python:3.8-alpine
#
#LABEL "pytest"="wwf"
#LABEL "creator"="woofiwaffle"
#
#WORKDIR
#
#COPY . .
#
#RUN apk update && apk upgrade && apk bash
#
#RUN pip install -r PyTest/requirements.txt
#
#CMD pytest -s -v PyTest/tests/*