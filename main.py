import discord
from os import getenv, listdir, getcwd, system
from sys import path
from dotenv import load_dotenv
from discord.utils import get
import logging
import random

# import json
# import requests
# from twitchAPI.twitch import Twitch
# from discord.ext import tasks

load_dotenv() # Loads content from .env to OS env variables

# client_id = getenv('client_id')
# client_secret = getenv('salt_token')
# twitch = Twitch(client_id, client_secret)
# twitch.authenticate_app([])
# TWITCH_STREAM_API_ENDPOINT_V5 = "https://api.twitch.tv/saltAxAtlas/streams/{}"
# API_HEADERS = {
#   'Client-ID': client_id,
#   'Accept': 'application/vnd.twitchtv.v5+json',
# }

intents = discord.Intents.all()
client = discord.Client(intents=intents)
logging.basicConfig(level=logging.INFO)
random.seed()

command_prefix = '$'

# Import commands
commands = []
path.append(getcwd() + '/commands')
for file in listdir('commands'):
    if file == '__pycache__':
        continue
    commands.append(__import__(file[:-3]).cmd) # [:-3] to get rid of .py
path.remove(getcwd() + '/commands')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, Welcome to my Discord server! Please be sure to check out the #rules-and-guidelines channel before you begin chatting. I hope you have a great time in the server! Thank you for joining!')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    member = message.author
    message_rng = random.randint(0,4999)
    if message_rng == 69:
        role = get(member.guild.roles, name='Chosen')
        if role in member.roles:
            await message.channel.send(f'{member.name}, you lucky duck!')
        else:
            await member.add_roles(role)
            await message.channel.send(f'I chose you, {member.name}.\n')

    if not message.content.startswith(command_prefix):
        return

    command = message.content[len(command_prefix):].split(' ')[0]
    
    for cmd in commands:
        if command == cmd['command'] or command in cmd['aliases']:
            await cmd['run'](message, globals())
            break
    else:
        await message.channel.send(f'{message.content} is not a valid command. Try \'$commands\' for a list of available commands!')

@client.event
async def on_reaction_add(reaction, user):
    channel_id = 874361456194375730
    if reaction.message.channel.id != channel_id or user.bot:
        return

    notified_role = get(user.guild.roles, name='Notified')
    invite_role = get(user.guild.roles, name='Invite to Clash')
    qotd_role = get(user.guild.roles, name='Notified QOTD')

    if reaction.emoji == '🥳':
        await user.add_roles(notified_role)
    elif reaction.emoji == '🖥️':
        await user.add_roles(invite_role)
    elif reaction.emoji == '❓':
        await user.add_roles(qotd_role)

@client.event
async def on_reaction_remove(reaction, user):
    channel_id = 874361456194375730
    if reaction.message.channel.id != channel_id or user.bot:
        return

    notified_role = get(user.guild.roles, name='Notified')
    invite_role = get(user.guild.roles, name='Invite to Clash')
    qotd_role = get(user.guild.roles, name='Notified QOTD')

    if reaction.emoji == '🥳':
        await user.remove_roles(notified_role)
    elif reaction.emoji == '🖥️':
        await user.remove_roles(invite_role)
    elif reaction.emoji == '❓':
        await user.remove_roles(qotd_role)

# def checkuser(user):
#     try:
#         userid = twitch.get_users(logins=[user])['data'][0]['id']
#         url = TWITCH_STREAM_API_ENDPOINT_V5.format(userid)
#         try:
#             req = requests.Session().get(url, headers=API_HEADERS)
#             jsondata = req.json()
#             if 'stream' in jsondata:
#                 if jsondata['stream'] is not None:
#                     return True
#                 else:
#                     return False
#         except Exception as e:
#             print("Error checking user: ", e)
#             return False
#     except IndexError:
#         return False

# @tasks.loop(seconds = 10)
# async def live_loop():
#     print("Loop")

#     ii = str(random.randint(345345895, 39582345908))
#     rv = open(ii + '.json', 'r', encoding='utf-8').read().strip()
#     system('rm ' + ii + '.json')
#     print(json(rv)[7]['data']['user']['stream'])
#     return
#     status = checkuser('saltAxAtlas')
#     print(status)
#     return

#     guild = client.get_guild(808876491827314708)
#     channel = client.get_channel(816392707664379984)
#     role = get(guild.roles, name='Live')

#     user_id = 808874804688977930
#     user = client.get_user(user_id)

#     if status is True:
#         async for check_message in channel.history(limit=200):
#             if "saltAxAtlas is streaming now at" in check_message.content:
#                 break
#             else:
#                 await user.add_roles(role)
#                 notified = get(guild.roles, name='Notified')
#                 await channel.send(f'{notified.mention} saltAxAtlas is streaming now at https://twitch.tv/saltaxatlas !')
#                 print(f"Salt started streaming. Sending a notification.")
#                 break
#     else:
#         await user.remove_roles(role)
#         async for check_message in channel.history(limit=200):
#             if "saltAxAtlas is streaming now at" in check_message.content:
#                 await check_message.delete()

# live_loop.start()

client.run(getenv("TOKEN"))