FROM python:3.6-slim
ARG user
ARG password
ADD requirements.lock /
RUN pip install --upgrade --extra-index-url https://$user:$password@distribution.livetech.site -r /requirements.lock
ADD . /prova1
ENV PYTHONPATH=$PYTHONPATH:/prova1
WORKDIR /prova1/prova1/services
CMD python services.py
