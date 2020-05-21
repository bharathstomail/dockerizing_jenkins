FROM jenkins/jenkins:lts
USER root

RUN echo "Acquire::http::proxy \"http://<proxy_details>/\";" >> /etc/apt/apt.conf && \
    echo "Acquire::https::proxy \"https://<proxy_details>/\";" >> /etc/apt/apt.conf && \
    echo "Acquire::ftp::proxy \"ftp://<proxy_details>/\";" >> /etc/apt/apt.conf && \
    echo "http_proxy=http://<proxy_details>/" >> /etc/environment && \
    echo "https_proxy=https://<proxy_details>/" >> /etc/environment && \
    echo "ftp_proxy=ftp://<proxy_details>/" >> /etc/environment && \   
    apt-get --no-upgrade update && \
	
    apt-get -y install wget && \
	apt-get -y install apt-transport-https curl && \
    apt-get -y install software-properties-common
 
#RUN curl -fsSL https://download.docker.com/linux/debian/gpg \
#    | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable"
RUN apt-get update -qq \
    && apt-get -y --allow-unauthenticated install docker-ce \
    && apt-get -y install docker-ce=5:19.03.9~3-0~debian-stretch
