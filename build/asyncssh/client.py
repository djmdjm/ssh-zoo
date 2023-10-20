#!/usr/bin/env python3

import os, sys, logging, argparse

async def asyncssh_client(args):
	opts = asyncssh.SSHClientConnectionOptions(
		username=args.user,
		password_auth=False,
		kbdint_auth=False,
		agent_path=None,
		preferred_auth="publickey",
		known_hosts=args.known_hosts,
		client_keys=args.privkey,
	)
	async with asyncssh.connect(args.host, port=args.port,
	    config=None, options=opts) as conn:
		r = await conn.run(RCMD, check=True)
		print(r.stdout, end='')
		sys.exit(r.returncode)

def main():
	argp = argparse.ArgumentParser(description='Basic AsyncSSH client')
	argp.add_argument('--asyncssh-version', dest='asyncssh_version',
	    default="latest", help="version of asyncssh to use")
	argp.add_argument('--user', dest='user', default=os.getenv("USER"),
	    help="destination user name")
	argp.add_argument('--host', dest='host', default="localhost",
	    help="destination host name")
	argp.add_argument('--port', dest='port', type=int, default=22,
	    help="destination port number")
	argp.add_argument('--rcmd', dest='rcmd', default="echo ok",
	    help="command to run remotely")
	argp.add_argument('--privkey', dest='privkey', default=None,
	    help="private key used for authentication")
	argp.add_argument('--known-hosts', dest='known_hosts', default=None,
	    help="known_hosts file for server authentication")
	argp.add_argument('--debug', action=argparse.BooleanOptionalAction,
	    dest="debug", default=True, help="enable debugging output")
	args = argp.parse_args()

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

	try:
		asyncio.get_event_loop().run_until_complete(
		    asyncssh_client(args))
	except (OSError, asyncssh.Error) as e:
		sys.exit('connection failed: ' + str(e))

if __name__ == '__main__': main()
