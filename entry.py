import argparse
import asyncio
import aiohttp
from demo.settings import load_config
from demo.app import create_app


try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('uvloop lib is not available')


parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument('-H', '--host', help='listening host', default='127.0.0.1')
parser.add_argument('-P', '--port', help='connection port', default=8080)
parser.add_argument('-R', '--reload', action='store_true', help='Autoreload on code change')
parser.add_argument('-C', '--config', type=argparse.FileType('r'), help='Path to config file')

args = parser.parse_args()

if args.reload:
    print('start with code reloading')
    import aioreloader
    aioreloader.start()

app = create_app(config=load_config(args.config))

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)