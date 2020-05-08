import logging
import aiohttp


networking_client = aiohttp.ClientSession(
    headers={
        'User-Agent': 'GuiltySpark/1.0 (/u/CheetElwin)'
    }
)


async def get(url, encoding=None):
    resp = await get_bytes(url)
    return resp.decode(encoding)


async def get_bytes(url):
    """ Builds a request as the bot to request anything through HTTP

    :param url:
        The url to fetch
    :return:
        Response content in bytes or '' if an error occurs
    """

    global networking_client  # Use the Bot network instance

    try:
        async with networking_client.get(url) as resp:
            content = await resp.read()
            return content
    except aiohttp.ClientConnectionError:
        logging.error('Failed to fetch page %s', url)
        return ''


async def post(url, data):
    global networking_client

    try:
        async with networking_client.post(url, data=data) as resp:
            content = await resp.text()
            return content
    except aiohttp.ClientConnectionError:
        logging.error('Failed to fetch page %s', url)
        return ''
