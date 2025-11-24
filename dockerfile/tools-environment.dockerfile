FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    useradd -ms /bin/bash debuggeruser && \
    passwd -d debuggeruser && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/' /etc/ssh/sshd_config && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workdir

COPY . .

# Start SSH server
CMD ["/usr/sbin/sshd","-D"]
