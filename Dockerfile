
FROM ubuntu
USER root

RUN mkdir -p /opt/Project_ISD
RUN chown root /opt/Project_ISD
COPY ./Package_ISD /opt/Project_ISD/Package_ISD
WORKDIR /opt/Project_ISD/Package_ISD
ENV PYTHONPATH "${PYTHONPATH}:/opt/Project_ISD"
EXPOSE 4040
