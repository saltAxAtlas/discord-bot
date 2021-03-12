import discord
from discord.utils import get
import os
import random
import logging

client = discord.Client()
random.seed()
logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):  # Need to test / add send message in #welcome
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to my Discord server! Please be sure to check out the rules-and-guidelines channel before you begin chatting. I hope you have a great time in the server! Thank you for joining!'
    )

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$'):
    if message.content.startswith('$commands'):
      await message.channel.send('1.  $commands\n2.  $help\n3.  $hello\n4.  $say \"{Your Message Here}\"\n5.  $notified\n6.  $coin-flip\n7.  $coc-gamemode\n8.  $going-live\n9.  $schedule\n10. $socials')
    elif message.content.startswith('$help'):
      await message.channel.send('Try \'$commands\' to see a simplified command list.\n\t1. $commands - a list of available commands.\n\t2. $help - an indepth explaination of the available commands.\n\t3. $hello - the bot will say hello to you.\n\t4. $say \"{Your Message Here}\" - lets you control what the bot says (keep it clean please).\n\t5. $notified - gives you the role \'Notified\' within the server. This role is pinged at the start\n\t     of every stream so you know when I go live. If you want to remove the role, simply use\n\t     the command again.\n\t6. $coin-flip - generate a random coin flip.\n\t7. $coc-gamemode - generate a random CoC gamemode to play!\n\t8. $going-live - pings \'Notified\' when I go live (only I can use this).\n\t9. $schedule - stream schedule for any given week.\n\t10. $socials - a list of my social media links.')
    elif message.content.startswith('$hello'):
      member = message.author
      await message.channel.send(f'Hello, {member.name}!')
    elif message.content.startswith('$say '):
      await message.channel.send(' '.join(message.content.split()[1:]))
    elif message.content.startswith('$notified'):
      member = message.author
      role = get(member.guild.roles, name='Notified')
      if role in member.roles:
        await member.remove_roles(role)
        await message.channel.send('You will no longer be notified when saltAxAtlas goes live :(')
      else:
        await member.add_roles(role)
        await message.channel.send('You will now be notified when saltAxAtlas goes live!')
    elif message.content.startswith('$coin-flip'):
      if random.randint(0,1):
        await message.channel.send('Heads!')
      else:
        await message.channel.send('Tails!')
    elif message.content.startswith('$coc-gamemode'):
      random_value = random.randint(0,2)
      if random_value == 0:
        await message.channel.send('Fastest!')
      elif random_value == 1:
        await message.channel.send('Shortest!')
      else:
        await message.channel.send('Reverse!')
    elif message.content.startswith('$going-live'):
      member = message.author
      role = get(member.guild.roles, name='Streamer')
      if role in member.roles:
        notified = get(member.guild.roles, name='Notified')
        await message.channel.send(f'{notified.mention} saltAxAtlas is streaming now at https://twitch.tv/saltaxatlas !')
      else:
        await message.channel.send('You do not have permission to use this command :(')
    elif message.content.startswith('$schedule'):
      await message.channel.send('All times are EST:\nMonday: 1:00PM - 4:00PM\nTuesday: 1:00PM - 5:00PM\nWednesday: 1:00PM - 4:00PM\nThursday: No Stream\nFriday: 1:00PM - 6:00PM\nSaturday: 2:00PM - 7:00PM\nSunday: No Stream')
    elif message.content.startswith('$socials'):
      await message.channel.send('Twitch: https://twitch.tv/saltaxatlas\nTwitter: https://twitter.com/ax_atlas\nGitHub: https://github.com/saltAxAtlas\nDiscord: You\'re already here :P')
    elif message.content.startswith('$info'):
      member_count = str(len(message.channel.members))
      await message.channel.send('Total Members: ' + member_count)
    else:
      await message.channel.send(f'{message.content} is not a valid command. Try \'$commands\' for a list of available commands!')
  else:
    return

client.run('TOKEN')