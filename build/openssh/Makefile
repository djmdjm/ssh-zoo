all: openssh-v9.5 openssh-v9.0 openssh-v8.5 openssh-v8.0 openssh-v7.5 \
     openssh-v7.0 openssh-v6.5 openssh-v6.0

openssh-v9.5: openssh-9.5/bin/ssh

openssh-9.5/bin/ssh:
	./openssh.sh 9.5

openssh-v9.0: openssh-9.0/bin/ssh

openssh-9.0/bin/ssh:
	./openssh.sh 9.0

openssh-v8.5: openssh-8.5/bin/ssh

openssh-8.5/bin/ssh:
	./openssh.sh 8.5

openssh-v8.0: openssh-8.0/bin/ssh

openssh-8.0/bin/ssh:
	./openssh.sh 8.0

openssh-v7.5: openssh-7.5/bin/ssh

openssh-7.5/bin/ssh:
	./openssh.sh 7.5 libressl-v3.4.3

openssh-v7.0: openssh-7.0/bin/ssh

openssh-7.0/bin/ssh:
	./openssh.sh 7.0 libressl-v3.4.3

openssh-v6.5: openssh-6.5/bin/ssh

openssh-6.5/bin/ssh:
	./openssh.sh 6.5 libressl-v3.4.3

openssh-v6.0: openssh-6.0/bin/ssh

openssh-6.0/bin/ssh:
	./openssh.sh 6.0 libressl-v3.4.3

clean:
	-rm -rf openssh-9.5 openssh-9.0 openssh-8.5 openssh-8.0 openssh-7.5
	-rm -rf openssh-7.0 openssh-6.5 openssh-6.0

