FROM stilliard/pure-ftpd

COPY ../../flags/ftp/flag.txt /home/ftpusers/ftp/flag.txt

RUN chmod 644 /home/ftpusers/ftp/flag.txt

ENV PUBLICHOST localhost
ENV FTP_USER_NAME $FTP_USER
ENV FTP_USER_PASS $FTP_PASS
ENV FTP_USER_HOME /home/ftpusers

CMD ["/run.sh", "-E", "-c", "5", "-C", "5", "-l", "puredb:/etc/pure-ftpd/pureftpd.pdb", "-j", "-R", "-P", "localhost", "-p", "30000:30009"]
