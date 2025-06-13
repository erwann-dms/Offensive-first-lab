FROM php:7.4-apache

RUN apt-get update && apt-get install -y git unzip

RUN git clone https://github.com/digininja/DVWA.git /var/www/html/

RUN chown -R www-data:www-data /var/www/html/

COPY ../../flags/dvwa/flag.txt /var/www/html/uploads/flag.txt

RUN chmod 644 /var/www/html/uploads/flag.txt

RUN cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php && \
    sed -i "s/'root'/'root'/g" /var/www/html/config/config.inc.php && \
    sed -i "s/'p@ssw0rd'/'p@ssw0rd'/g" /var/www/html/config/config.inc.php

EXPOSE 80
