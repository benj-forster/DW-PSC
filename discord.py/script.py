import discord
import asyncio
import aiohttp
import async_timeout
import json

dw_token='ur_token'

async def fetchPost(urlIn, d, h):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(10):
            async with session.post(urlIn, data=d, headers=h) as response:
                session.close()
                return response.status

await postToDW():
    headers = {
        'Authorization': dw_token,
        'Content-Type': 'application/json'
    }
    data = {"count": len(self.bot.guilds)}
    await fetchPost("https://discordwarehouse.io/api/bot/{}".format(botID), data, headers)
