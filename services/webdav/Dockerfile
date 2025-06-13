FROM httpd:2.4

RUN apt update && apt install -y apache2-utils

COPY ./webdav.conf /usr/local/apache2/conf/httpd.conf

RUN mkdir /usr/local/apache2/var/webdav
RUN chown -R www-data:www-data /usr/local/apache2/var/webdav

COPY ../../flags/webdav/flag.txt /usr/local/apache2/var/webdav/flag.txt

EXPOSE 80
