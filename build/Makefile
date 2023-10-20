all:
	$(MAKE) -C libcrypto
	$(MAKE) -C openssh
	$(MAKE) -C dropbear
	$(MAKE) -C putty
	$(MAKE) -C asyncssh

clean:
	$(MAKE) -C openssh clean
	$(MAKE) -C dropbear clean
	$(MAKE) -C putty clean
	$(MAKE) -C libcrypto clean
	$(MAKE) -C asyncssh clean
