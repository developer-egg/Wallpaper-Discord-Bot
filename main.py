import discord
import requests

class Client(discord.Client):
    async def on_ready(self):
        print("Wallpaper bot ready!")

    async def on_message(self, message):
        if (message.content == "$wallpaper"):

            URL = "https://meme-api.herokuapp.com/gimme/wallpaper"
            request = requests.get(url=URL)
            request_data = request.json()
            wallpaper_url = request_data["url"]

            await message.channel.send(wallpaper_url)

client = Client()
client.run("OTE4MjcyNzQ0MjIxNzMyODg0.YbE2Ig.EOjWjXl5kBMaYM0MEiuvQx2tXok")
