import discord
from discord.utils import get
from dotenv import load_dotenv
import random
import logging
import os

load_dotenv() # Loads content from .env to os env vars

client = discord.Client()
random.seed()
logging.basicConfig(level=logging.INFO)

timezones = {'NUT': -11, 'TAHT': -10, 'HDT': -9, 'AKDT': -8, 'PDT': -7, 'MST': -7, 'MDT': -6, 'CST': -6, 'GALT': -6, 'CDT': -5, 'ECT': -5, 'COT': -5, 'EDT': -4, 'EST': -4, 'AMT': -4, 'WGT': -3, 'GST': -2, 'CVT': -1, 'AZOT': -1, 'GMT': 0, 'UTC': 0, 'WAT': 1, 'CET': 1, 'CEST': 2, 'CAT': 2, 'EET': 2, 'EAT': 3, 'MSK': 3, 'AST': 3, 'SAMT': 4, 'RET': 4, 'MUT': 4, 'YEKT': 5, 'ORAT': 5, 'MVT': 5, 'TFT': 5, 'OMST': 6, 'ALMT': 6, 'KGT': 6, 'BST': 6, 'KRAT': 7, 'WIB': 7, 'ICT': 7, 'AWST': 8, 'PHST': 8, 'ULAT': 8, 'IRKT': 8, 'WITA': 8, 'BNT': 8, 'WIT': 9, 'YAKT': 9, 'JST': 9, 'PGT': 10, 'AEST': 10, 'VLAT': 10, 'VUT': 11, 'SRET': 11, 'MAGT': 11, 'SBT': 11, 'CHADT': 12, 'FJT': 12, 'ANAT': 12, 'NZDT': 13, 'HST': 14}
languages = {
    'ENGLISH': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'GERMAN' : ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
    'SPANISH': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
    'FRENCH' : ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'POLISH' : ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela'],
    'DUTCH'  : ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'],
    'TURKISH': ['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar'],
}
MONDAY_START = 0
MONDAY_LENGTH = 0
TUESDAY_START = 21
TUESDAY_LENGTH = 4
WEDNESDAY_START = 0
WEDNESDAY_LENGTH = 0
THURSDAY_START = 21
THURSDAY_LENGTH = 4
FRIDAY_START = 0
FRIDAY_LENGTH = 0
SATURDAY_START = 18
SATURDAY_LENGTH = 5
SUNDAY_START = 18
SUNDAY_LENGTH = 5


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):  # Does not send message?
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to my Discord server! Please be sure to check out the rules-and-guidelines channel before you begin chatting. I hope you have a great time in the server! Thank you for joining!')

@client.event
async def on_message(message):

    if message.author == client.user or message.author.bot:
        return

    message_rng = random.randint(0,4999)
    if message_rng == 69:
        member = message.author
        role = get(member.guild.roles, name='Chosen')
        if role in member.roles:
            await message.channel.send(f'{member.name}, you lucky duck!')
        else:
            await member.add_roles(role)
            await message.channel.send(f'I chose you, {member.name}.\n')

    if not message.content.startswith('$'):
        return
    member = message.author
    if message.content.startswith('$commands'):
        await message.channel.send('1.  $commands\n2.  $help\n3.  $hello\n4.  $say \"{Your Message Here}\"\n5.  $notified\n6.  $coin-flip\n7.  $coc-gamemode\n8.  $going-live\n9.  $schedule \"{Timezone}\" \"{Language}\"\n10. $socials\n11.  $coc-invite\n12. $qotd\n13. $server-info')
    elif message.content.startswith('$help'):
        await message.channel.send('Try \'$commands\' to see a simplified command list.\n\t1. $commands - a list of available commands.\n\t2. $help - an indepth explanation of the available commands.\n\t3. $hello - the bot will say hello to you.\n\t4. $say \"{Your Message Here}\" - lets you control what the bot says.\n\t     (keep it clean please).\n\t5. $notified - gives you the role \'Notified\' within the server. This role is pinged at the\n\t     start of every stream so you know when I go live. If you want to remove the role,\n\t     simply use the command again.\n\t6. $coin-flip - generate a random coin flip.\n\t7. $coc-gamemode - generate a random CoC gamemode to play!\n\t8. $going-live - pings \'Notified\' when I go live (only I can use this).\n\t9. $schedule \"{Timezone}\" \"{Language}\" - stream schedule for any given week.\n\t10. $socials - a list of my social media links.\n\t11. $coc-invite - give you the role \'Invite to Clash\' which anyone can ping when they are\n\t     looking for people to clash with. Use the command again to remove the role.\n\t12. $qotd - give you the role \'QOTD Notified\' which is pinged everyday when\n\t     the QOTD is posted. Use the command again to remove the role.\n\t13. $server-info - outputs the number of members in the server.')
    elif message.content.startswith('$hello'):
        await message.channel.send(f'Hello, {member.name}!')
    elif message.content.startswith('$say'):
        try:
            response = message.content[4:].lstrip()
            if len(response) > 0:
                await message.channel.send(response)
            else:
                await message.channel.send('... what should I say?')
        except IndexError:
            await message.channel.send('... what should I say?')
    elif message.content.startswith('$notified'):
        role = get(member.guild.roles, name='Notified')
        if role in member.roles:
            await member.remove_roles(role)
            await message.channel.send('You will no longer be notified when saltAxAtlas goes live :(')
        else:
            await member.add_roles(role)
            await message.channel.send('You will now be notified when saltAxAtlas goes live!')
    elif message.content.startswith('$coin-flip'):
        await message.channel.send(random.choice(['Heads', 'Tails']) + '!')
    elif message.content.startswith('$coc-gamemode'):
        await message.channel.send(random.choice(['Fastest', 'Shortest', 'Reverse']) + '!')
    elif message.content.startswith('$going-live'):
        role = get(member.guild.roles, name='Streamer')
        if role in member.roles:
            notified = get(member.guild.roles, name='Notified')
            await message.channel.send(f'{notified.mention} saltAxAtlas is streaming now at https://twitch.tv/saltaxatlas !')
        else:
            await message.channel.send('You do not have permission to use this command!')
    elif message.content.startswith('$schedule'):
        try:
            commands = message.content.upper().split()[1:]
            if len(commands) >= 2:
                member_timezone, member_language = commands[:2]
            elif len(commands) == 1:
                member_timezone = commands[0]
                member_language = 'ENGLISH'
            else:
                member_timezone = 'EST'
                member_language = 'ENGLISH'
        except IndexError:
            member_timezone = 'EST'
            member_language = 'ENGLISH'
        shift = 0
        sign = '+' if '+' in member_timezone else '-' if '-' in member_timezone else ''
        if sign:
            member_timezone, shift = member_timezone.split(sign)
            try: 
                shift = int(shift)
            except: 
                await message.channel.send(f'{shift} is not a valid number following the format \'timezone{sign}number\'.');
                return
            if sign == '-': 
                shift = -shift
        if member_timezone not in timezones:
            await message.channel.send(f'{member_timezone} is not currently supported! Defaulting to EST')
            member_timezone = 'EST'
        if member_language not in languages:
            await message.channel.send(f'{member_language} is not currently supported! Defaulting to ENGLISH')
            member_language = 'ENGLISH'
        tz = timezones[member_timezone] + shift
        dotw = languages[member_language]
        monday = 'No Stream'
        monday_end = 'No Stream'
        tuesday = (TUESDAY_START + tz)%24
        tuesday_end = (tuesday + TUESDAY_LENGTH)%24
        wednesday = 'No Stream'
        wednesday_end = 'No Stream'
        thursday = (THURSDAY_START + tz)%24
        thursday_end = (thursday + THURSDAY_LENGTH)%24
        friday = 'No Stream'
        friday_end = 'No Stream'
        saturday = (SATURDAY_START + tz)%24
        saturday_end = (saturday + SATURDAY_LENGTH)%24
        sunday = (SUNDAY_START + tz)%24
        sunday_end = (sunday + SUNDAY_LENGTH)%24
        if sign:
            member_timezone += sign + str(abs(shift)) 
        await message.channel.send(f'All times are in {member_timezone}:\n\t{dotw[0]}: {monday}\n\t{dotw[1]}: {tuesday}:00 - {tuesday_end}:00\n\t{dotw[2]}: {wednesday}\n\t{dotw[3]}: {thursday}:00 - {thursday_end}:00\n\t{dotw[4]}: {friday}\n\t{dotw[5]}: {saturday}:00 - {saturday_end}:00\n\t{dotw[6]}: {sunday}:00 - {sunday_end}:00\n\tThere will also be unscheduled streams sometimes during the week after 5 PM EST!')
    elif message.content.startswith('$socials'):
        await message.channel.send('Twitch: <https://twitch.tv/saltaxatlas>\nTwitter: <https://twitter.com/saltAxAtlas>\nTikTok: <https://www.tiktok.com/@saltaxatlas>\nGitHub: <https://github.com/saltAxAtlas>\nDiscord: <https://discord.gg/V56vXKe7mY>')
    elif message.content.startswith('$coc-invite'):
        role = get(member.guild.roles, name='Invite to Clash')
        if role in member.roles:
            await member.remove_roles(role)
            await message.channel.send('You will no longer be pinged when people are starting private clashes :(')
        else:
            await member.add_roles(role)
            await message.channel.send('You will now be pinged when people are looking for others to clash with!')
    elif message.content.startswith('$qotd'):
        role = get(member.guild.roles, name='Notified QOTD')
        if role in member.roles:
            await member.remove_roles(role)
            await message.channel.send('You will no longer be pinged when the QOTD is posted :(')
        else:
            await member.add_roles(role)
            await message.channel.send('You will now be pinged when the QOTD is posted!')
    elif message.content.startswith('$server-info'):  # BROKEN, BROKEN, BROKEN, value does not update?
        total_members = message.author.guild.member_count
        await message.channel.send(f'Total Members: {total_members}')
    else:
        await message.channel.send(f'{message.content} is not a valid command. Try \'$commands\' for a list of available commands!')

client.run(os.environ.get('TOKEN'))
