FROM rastasheep/ubuntu-sshd:18.04

COPY ../../flags/ssh/flag.txt /root/flag.txt

RUN echo 'root:toor' | chpasswd

EXPOSE 22
