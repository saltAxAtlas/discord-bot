import discord
from discord.utils import get
import random
import logging

client = discord.Client()
random.seed()
logging.basicConfig(level=logging.INFO)

timezones = {'AEST': 15, 'AST': 1, 'AWST': 12, 'CAT': 6, 'CET': 5, 'CST': -1, 'EAT': 6, 'EET': 6, 'EST': 0, 'MSK': 7, 'MST': -2, 'PST': -3, 'WAT': 5, 'WET': 4, 'GMT': 4}  # Add +- support / all timezones

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):  # Need to test / add send message in #welcome
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to my Discord server! Please be sure to check out the rules-and-guidelines channel before you begin chatting. I hope you have a great time in the server! Thank you for joining!')

@client.event
async def on_message(message):
  if message.author == client.user or not message.content.startswith('$'):
    return
  if message.content.startswith('$commands'):
    await message.channel.send('1.  $commands\n2.  $help\n3.  $hello\n4.  $say \"{Your Message Here}\"\n5.  $notified\n6.  $coin-flip\n7.  $coc-gamemode\n8.  $going-live\n9.  $schedule\n10. $socials\n11.  $coc-invite\n12. $qotd')
  elif message.content.startswith('$help'):
    await message.channel.send('Try \'$commands\' to see a simplified command list.\n\t1. $commands - a list of available commands.\n\t2. $help - an indepth explanation of the available commands.\n\t3. $hello - the bot will say hello to you.\n\t4. $say \"{Your Message Here}\" - lets you control what the bot says.\n\t     (keep it clean please).\n\t5. $notified - gives you the role \'Notified\' within the server. This role is pinged at the\n\t     start of every stream so you know when I go live. If you want to remove the role,\n\t     simply use the command again.\n\t6. $coin-flip - generate a random coin flip.\n\t7. $coc-gamemode - generate a random CoC gamemode to play!\n\t8. $going-live - pings \'Notified\' when I go live (only I can use this).\n\t9. $schedule - stream schedule for any given week.\n\t10. $socials - a list of my social media links.\n\t11. $coc-invite - give you the role \'Invite to Clash\' which anyone can ping when they are\n\t     looking for people to clash with. Use the command again to remove the role.\n\t12. $qotd - give you the role \'QOTD Notified\' which is pinged everyday when\n\t     the QOTD is posted. Use the command again to remove the role.')
  elif message.content.startswith('$hello'):
    member = message.author
    await message.channel.send(f'Hello, {member.name}!')
  elif message.content.startswith('$say'):
    try:
      response = message.content[4:].lstrip()
      if len(response) > 0:
        for i in '​‍‍‌️️︎︎‭　ㅤᅠ  ⠀	⁣         ':
          response = response.replace(i, '')
        await message.channel.send(response)
      else:
        await message.channel.send('... what should I say?')
    except IndexError:
      await message.channel.send('... what should I say?')
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
    rng = random.randint(0, 1)
    await message.channel.send('Heads!' if rng == 1 else 'Tails!')
  elif message.content.startswith('$coc-gamemode'):
    rng = random.randint(0, 2)
    await message.channel.send('Fastest!' if rng == 0 else 'Shortest!' if rng == 1 else 'Reverse!')
  elif message.content.startswith('$going-live'):
    member = message.author
    role = get(member.guild.roles, name='Streamer')
    if role in member.roles:
      notified = get(member.guild.roles, name='Notified')
      await message.channel.send(f'{notified.mention} saltAxAtlas is streaming now at https://twitch.tv/saltaxatlas !')
    else:
      await message.channel.send('You do not have permission to use this command :(')
  elif message.content.startswith('$schedule'):
    member_timezone = ' '.join(message.content.upper().split()[1:])
    if member_timezone == '':
      member_timezone = 'EST'
    if member_timezone not in timezones:
      await message.channel.send(f'{member_timezone} is not currently supported! Defaulting to EST')
      member_timezone = 'EST'
    monday = (13 + timezones[member_timezone])%24
    tuesday = (13 + timezones[member_timezone])%24
    wednesday = (13 + timezones[member_timezone])%24
    thursday = 'No Stream'
    friday = (13 + timezones[member_timezone])%24
    saturday = (14 + timezones[member_timezone])%24
    sunday = 'No Stream'
    await message.channel.send(f'All times are in {member_timezone}:\n\tMonday: {monday}:00 - {monday + 3}:00\n\tTuesday: {tuesday}:00 - {tuesday + 4}:00\n\tWednesday: {wednesday}:00 - {wednesday + 3}:00\n\tThursday: {thursday}\n\tFriday: {friday}:00 - {friday + 5}:00\n\tSaturday: {saturday}:00 - {saturday + 5}:00\n\tSunday: {sunday}')
  elif message.content.startswith('$socials'):
    await message.channel.send('Twitch: <https://twitch.tv/saltaxatlas>\nTwitter: <https://twitter.com/ax_atlas>\nGitHub: <https://github.com/saltAxAtlas>\nDiscord: <https://discord.gg/V56vXKe7mY>')
  elif message.content.startswith('$coc-invite'):
    member = message.author
    role = get(member.guild.roles, name='Invite to Clash')
    if role in member.roles:
      await member.remove_roles(role)
      await message.channel.send('You will no longer be pinged when people are starting private clashes :(')
    else:
      await member.add_roles(role)
      await message.channel.send('You will now be pinged when people are looking for others to clash with!')
  elif message.content.startswith('$qotd'):
    member = message.author
    role = get(member.guild.roles, name='Notified QOTD')
    if role in member.roles:
      await member.remove_roles(role)
      await message.channel.send('You will no longer be pinged when the QOTD is posted :(')
    else:
      await member.add_roles(role)
      await message.channel.send('You will now be pinged when the QOTD is posted!')
  elif message.content.startswith('$info'):  # Need to make this work
    await message.channel.send(f'Total Members: {len(message.channel.members)}')
  else:
    await message.channel.send(f'{message.content} is not a valid command. Try \'$commands\' for a list of available commands!')

client.run('kill me')
