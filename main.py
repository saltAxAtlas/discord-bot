import discord
from os import getenv, listdir, getcwd, system
from sys import path
from dotenv import load_dotenv
from discord.utils import get
import logging
import random
from json import loads as json

load_dotenv() # Loads content from .env to OS env variables

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

client.run(getenv("TOKEN"))
