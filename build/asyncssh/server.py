#!/usr/bin/env python3

import os, sys, logging, argparse

def client(p):
	p.stdout.write("ok\n")
	p.exit(0)

async def asyncssh_server(args):
	opts = asyncssh.SSHServerConnectionOptions(
		server_host_keys=args.hostkey,
		server_host_certs=args.hostcert,
		authorized_client_keys=args.auth_keys,
		password_auth=False,
		kbdint_auth=False,
		public_key_auth=True,
		config=None,
	)
	await asyncssh.listen("localhost", port=args.port, options=opts,
	    process_factory=client)

def main():
	argp = argparse.ArgumentParser(description='Basic AsyncSSH server')
	argp.add_argument('--asyncssh-version', dest='asyncssh_version',
	    default="latest", help="version of asyncssh to use")
	argp.add_argument('--hostkey', dest='hostkey', default=None,
	    help="server host private key")
	argp.add_argument('--hostcert', dest='hostcert', default=None,
	    help="server host certificate")
	argp.add_argument('--port', dest='port', type=int, default=2222,
	    help="listen port number")
	argp.add_argument('--auth-keys', dest='auth_keys', default=None,
	    help="path to authorized_keys file")
	argp.add_argument('--debug', action=argparse.BooleanOptionalAction,
	    dest="debug", default=True, help="enable debugging output")
	args = argp.parse_args()
	if args.hostcert is None:
		args.hostcert = []
	# Load the requested asyncssh version
	thisdir = os.path.dirname(os.path.realpath(__file__))
	asyncsshdir = os.path.join(thisdir, args.asyncssh_version, "lib")
	sys.path.append(asyncsshdir)
	global asyncio, asyncssh
	import asyncio, asyncssh

	logging.basicConfig()
	if args.debug:
		asyncssh.set_log_level(logging.DEBUG)
		asyncssh.set_debug_level(2)

	loop = asyncio.get_event_loop()
	try:
		loop.run_until_complete(asyncssh_server(args))
	except (OSError, asyncssh.Error) as e:
		sys.exit("error: " + str(e))
	loop.run_forever()

if __name__ == '__main__': main()
