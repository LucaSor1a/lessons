FROM alpine
ENV TERM xterm
ENV PS1='\h:\w\$ '
WORKDIR /root
RUN apk update
RUN apk add python3
RUN apk add vim
RUN apk add git
run git clone https://github.com/umcomp2/lessons.git
