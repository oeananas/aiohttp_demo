import aiohttp
from aiohttp_jinja2 import template
from sqlalchemy import select
from .. import db


@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}


@template('posts.html')
async def post(request):
    async with request.app['db'].acquire() as conn:
        query = select([db.post])
        result = await conn.fetch(query)
    return {'posts': result}
