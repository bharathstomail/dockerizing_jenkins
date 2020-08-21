
FROM ubuntu
WORKDIR /Project_ISD

COPY ./Package_ISD ./Package_ISD
ENV PYTHONPATH "${PYTHONPATH}:./Project_ISD"