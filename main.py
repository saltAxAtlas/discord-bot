import discord
from discord.utils import get
import random
import logging

client = discord.Client()
random.seed()
logging.basicConfig(level=logging.INFO)

timezones = {'NUT': -11, 'TAHT': -10, 'HDT': -9, 'AKDT': -8, 'PDT': -7, 'MST': -7, 'MDT': -6, 'CST': -6, 'GALT': -6, 'CDT': -5, 'ECT': -5, 'COT': -5, 'EDT': -4, 'EST': -4, 'AMT': -4, 'WGT': -3, 'GST': -2, 'CVT': -1, 'AZOT': -1, 'GMT': 0, 'UTC': 0, 'WAT': 1, 'CET': 1, 'CAT': 2, 'EET': 2, 'EAT': 3, 'MSK': 3, 'AST': 3, 'SAMT': 4, 'RET': 4, 'MUT': 4, 'YEKT': 5, 'ORAT': 5, 'MVT': 5, 'TFT': 5, 'OMST': 6, 'ALMT': 6, 'KGT': 6, 'BST': 6, 'KRAT': 7, 'WIB': 7, 'ICT': 7, 'AWST': 8, 'PHST': 8, 'ULAT': 8, 'IRKT': 8, 'WITA': 8, 'BNT': 8, 'WIT': 9, 'YAKT': 9, 'JST': 9, 'PGT': 10, 'AEST': 10, 'VLAT': 10, 'VUT': 11, 'SRET': 11, 'MAGT': 11, 'SBT': 11, 'CHADT': 12, 'FJT': 12, 'ANAT': 12, 'NZDT': 13, 'HST': 14}

def flip(dict):
    ret = {}
    for i in dict: ret[dict[i]] = i
    return ret

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
        shift = 0
        flipped = 1 # more like NOT flipped
        if member_timezone == '':
            member_timezone = 'EST'
        char = '+' if '+' in member_timezone else '-' if '-' in member_timezone else ''
        if char:
            member_timezone, shift = member_timezone.split(char)
            try: shift = int(shift)
            except: return message.channel.send(f'{shift} is not a valid number following timezone{char}number')
            if char == '-': shift = -shift
        if member_timezone not in timezones:
            await message.channel.send(f'{member_timezone} is not currently supported! Defaulting to EST')
            member_timezone = 'EST'
        tz = timezones[member_timezone] + shift
        if tz in flip(timezones):
            member_timezone = flip(timezones)[tz] # Name simplifying
            flipped &= 0
        monday = (17 + tz)%24
        monday_end = (monday + 3)%24
        tuesday = (17 + tz)%24
        tuesday_end = (tuesday + 4)%24
        wednesday = (17 + tz)%24
        wednesday_end = (wednesday + 3)%24
        thursday = 'No Stream'
        thursday_end = 'No Stream'
        friday = (17 + tz)%24
        friday_end = (friday + 5)%24
        saturday = (18 + tz)%24
        saturday_end = (saturday + 5)%24
        sunday = 'No Stream'
        sunday_end = 'No Stream'
        await message.channel.send(f'All times are in {member_timezone}{char+shift if char and flipped else ""}:\n\tMonday: {monday}:00 - {monday_end}:00\n\tTuesday: {tuesday}:00 - {tuesday_end}:00\n\tWednesday: {wednesday}:00 - {wednesday_end}:00\n\tThursday: {thursday}\n\tFriday: {friday}:00 - {friday_end}:00\n\tSaturday: {saturday}:00 - {saturday_end}:00\n\tSunday: {sunday}')
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

client.run('¯(ツ)/¯')
