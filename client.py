import discord


# import * - is a quick way to import all files from the library
# the privileges (intents) variable will store the privileges of the bot
intents = discord.Intents.default()
# Let's enable the privilege of reading messages
intents.message_content = True
# create a bot with the client variable and pass privileges to it
client = discord.Client(intents=intents)
@client.event
async def on_ready():
print(f' logged in as{client.user}.')
@client.event
async def on_message(message):
if message.author == client.user:
return
if message.content.startswith('$hello'):
await message.channel.send("Hi!")
elif message.content.startswith('$bye'):
await message.channel.send("\\U0001f642")
else:
await message.channel.send(message.content)
client.run("Token")
