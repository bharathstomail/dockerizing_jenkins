
FROM ubuntu
USER root
# set Philips proxy
RUN echo "Acquire::http::proxy \"http://apac.zscaler.philips.com:9480/\";" >> /etc/apt/apt.conf && \
    echo "Acquire::https::proxy \"https://apac.zscaler.philips.com:9480/\";" >> /etc/apt/apt.conf && \
    echo "Acquire::ftp::proxy \"ftp://apac.zscaler.philips.com:9480/\";" >> /etc/apt/apt.conf && \
    echo "http_proxy=http://apac.zscaler.philips.com:9480/" >> /etc/environment && \
    echo "https_proxy=https://apac.zscaler.philips.com:9480/" >> /etc/environment && \
    echo "ftp_proxy=ftp://apac.zscaler.philips.com:9480/" >> /etc/environment && \   
    apt-get --no-upgrade update && \
    apt-get -y install wget && \
	apt-get install -y nano && \
	apt-get install -y vim && \
    apt-get -y install python3-pip

USER root
RUN mkdir -p /opt/Project_ISD
RUN chown root /opt/Project_ISD
COPY Package_ISD /opt/Project_ISD/Package_ISD
WORKDIR /opt/Project_ISD/Package_ISD
ENV PYTHONPATH "${PYTHONPATH}:/opt/Project_ISD"
#RUN sudo pip3 install -r requirement.txt
RUN pip3 install -r requirement.txt --proxy=http://apac.zscaler.philips.com:9480
EXPOSE 4040