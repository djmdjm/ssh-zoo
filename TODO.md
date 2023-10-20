Remaining work:

1. More SSH implementations.
	1. Go x/crypto/ssh
	2. AsyncSSH
	3. Rust?
	4. Java?
2. Automated testing
	1. Test OpenSSH (at arbitrary git ref) against all implementations
3. Manual testing support
	1. Script to run SSH servers for all supported implementations and generate OpenSSH client config to connect
	2. Script to run SSH clients for all supported implementations against a given OpenSSH SSH server
4. `git bisect` support to find where things broke
