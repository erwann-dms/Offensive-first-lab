FROM wordpress:php7.4-apache

COPY ../../flags/wordpress/flag.txt /var/www/html/wp-content/uploads/flag.txt

RUN chown www-data:www-data /var/www/html/wp-content/uploads/flag.txt && chmod 644 /var/www/html/wp-content/uploads/flag.txt

EXPOSE 80
