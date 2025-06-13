FROM php:7.4-apache

# Installer dépendances et git
RUN apt-get update && apt-get install -y git unzip

# Cloner DVWA
RUN git clone https://github.com/digininja/DVWA.git /var/www/html/

# Configurer permissions
RUN chown -R www-data:www-data /var/www/html/

# Copier le flag dans le dossier uploads accessible uniquement après exploitation
COPY ../../flags/dvwa/flag.txt /var/www/html/uploads/flag.txt

# S'assurer que le flag est lisible
RUN chmod 644 /var/www/html/uploads/flag.txt

# Config DVWA (création base, config, etc)
RUN cp /var/www/html/config/config.inc.php.dist /var/www/html/config/config.inc.php && \
    sed -i "s/'root'/'root'/g" /var/www/html/config/config.inc.php && \
    sed -i "s/'p@ssw0rd'/'p@ssw0rd'/g" /var/www/html/config/config.inc.php

# Exposer le port 80
EXPOSE 80
