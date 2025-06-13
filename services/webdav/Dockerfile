FROM httpd:2.4

RUN apt update && apt install -y apache2-utils

COPY ./webdav.conf /usr/local/apache2/conf/httpd.conf
