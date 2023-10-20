all: asyncssh-v2.14.0 latest

latest: asyncssh-v2.14.0
	-rm -f latest
	ln -sf asyncssh-2.14.0 latest

asyncssh-v2.14.0: asyncssh-2.14.0/lib/asyncssh/client.py

asyncssh-2.14.0/lib/asyncssh/client.py:
	./asyncssh.sh 2.14.0

clean:
	-rm -rf asyncssh-2.14.0 latest

