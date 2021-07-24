import discord
from discord.utils import get
import os
from dotenv import load_dotenv
import random
import logging

load_dotenv() # Loads content from .env to OS env variables

intents = discord.Intents.all()
client = discord.Client(intents = intents)
random.seed()
logging.basicConfig(level=logging.INFO)

command_prefix = '$'
commands       = ['commands', 'help', 'hello', 'say', 'notified', 'coin-flip', 'coc-gamemode', 'going-live', 'schedule', 'socials', 'coc-invite', 'qotd', 'server-info']
commands_print = 'Commands:\n\t' + '\n\t'.join([f'`{str(index+1).rjust(2)}.`  {command_prefix}{command}' for index, command in enumerate(commands)])
help_defs = {
    'commands':     'a list of available commands.',
    'help':         'an indepth explanation of the available commands.',
    'hello':        'the bot will say hello to you.',
    'say':          'lets you control what the bot says.',
    'notified':     'gives you the role \'Notified\'.',
    'coin-flip':    'generates a random coin flip.',
    'coc-gamemode': 'generates a random CoC gamemode to play!',
    'going-live':   'pings \'Notified\' when I go live (only I can use this).',
    'schedule':     'displays the stream schedule.',
    'socials':      'a list of my social media links.',
    'coc-invite':   'give you the role \'Invite to Clash\'.',
    'qotd':         'give you the role \'QOTD Notified\'.',
    'server-info':  'displays information about the server.'
}
help_print     = 'Try $commands for a simplified command list.\n\t' + '\n\t'.join([f'`{str(index+1).rjust(2)}.`  {command_prefix}{key} - {help_defs[key]}' for index, key in enumerate(help_defs.keys())])
social_defs = {
    'Twitch':       '<https://twitch.tv/saltaxatlas>',
    'Twitter':      '<https://twitter.com/saltAxAtlas>',
    'TikTok':       '<https://www.tiktok.com/@saltaxatlas>',
    'GitHub':       '<https://github.com/saltAxAtlas>',
    'Discord':      '<https://discord.gg/V56vXKe7mY>'
}
social_max_length = max([len(name) for name in social_defs.keys()]) # dumb stuff I do for alignment
social_print      = 'Check out my socials to stay up to date!\n\t' + '\n\t'.join([f'`{key.ljust(social_max_length)}`: {value}' for key, value in social_defs.items()])
# Key -> Day, Value -> [start_time, stream_length]
# -1 signifies that there will not be a stream
schedule_def = {
    'Monday':       [-1, -1],
    'Tuesday':      [21, 4],
    'Wednesday':    [-1, -1],
    'Thursday':     [21, 4],
    'Friday':       [-1, -1],
    'Saturday':     [18, 5],
    'Sunday':       [18, 5]
}
special_event_def = {
    'First Saturday':   'Sub / Follow - athon on the first Saturday of every month! :partying_face:'
}
server_info_defs = {
    'Server Name':          'saltAxAtlas Streams',
    'Server Creation Date': 'Feb. 9, 2021'
}
timezones = {
    'NUT': -11, 'SST': -11, 
    'TAHT': -10, 'CKT': -10, 'LINT': -10, 'HST': -10,
    'HDT': -9, 
    'AKDT': -8, 'PST': -8, 
    'PDT': -7, 'MST': -7, 
    'MDT': -6, 'CST': -6, 'EAST': -6, 'GALT': -6, 
    'CDT': -5, 'PET': -5, 'ECT': -5, 'COT': -5, 
    'EDT': -4, 'EST': -4, 'AMT': -4, 
    'WGT': -3, 'FKST': -3, 'BRT': -3, 'ART': -3, 
    'GST': -2, 'WGST': -2, 
    'CVT': -1, 
    'GMT': 0, 'UTC': 0, 'AZOST': 0, 'EGST': 0,
    'WAT': 1, 'CET': 1, 'WEST': 1, 
    'CEST': 2, 'CAT': 2, 'EET': 2, 'SAST': 2,
    'EAT': 3, 'MSK': 3, 'AST': 3, 'EEST': 3, 'TRT': 3,
    'SAMT': 4, 'RET': 4, 'MUT': 4, 'GET': 4, 'AZT': 4, 'SCT': 4,
    'YEKT': 5, 'ORAT': 5, 'MVT': 5, 'TFT': 5, 'PKT': 5,
    'IST': 5.5,
    'OMST': 6, 'ALMT': 6, 'KGT': 6, 'BST': 6, 'IOT': 6,
    'KRAT': 7, 'WIB': 7, 'ICT': 7, 'HOVT': 7, 'NOVT': 7, 
    'AWST': 8, 'PHST': 8, 'ULAT': 8, 'IRKT': 8, 'WITA': 8, 'BNT': 8, 'HKT': 8, 
    'ACWST': 8.5,
    'WIT': 9, 'YAKT': 9, 'JST': 9, 'KST': 9, 
    'ACST': 9.5,
    'PGT': 10, 'AEST': 10, 'VLAT': 10, 
    'VUT': 11, 'SRET': 11, 'MAGT': 11, 'SBT': 11, 
    'CHADT': 12, 'FJT': 12, 'ANAT': 12, 'NZDT': 12 
}
languages = {
    'ENGLISH':      ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'GERMAN' :      ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
    'SPANISH':      ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    'FRENCH' :      ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'POLISH' :      ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'],
    'DUTCH'  :      ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'],
    'TURKISH':      ['Pazartesi', 'Salı', 'Çarsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar'],
    'LITHUANIAN':   ['Pirmadienis', 'Antradienis', 'Trečiadienis', 'Ketvirtadienis', 'Penktadienis', 'Šeštadienis', 'Sekmadienis'],
    'ITALIAN':      ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica'],
    'JAPANESE':     ['げつようび', 'かようび', 'すいようび', 'もくようび', 'きんようび', 'どようび', 'にちようび'],
    'RUSSIAN':      ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],
    'SWEDISH':      ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag'],
    'CHINESE':      ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'],
    'HINDI':        ['Somvar', 'Mangalvar', 'Budhvar', 'Guruvar', 'Shukrvar', 'Shanivar', 'Ravivar'],
    'BENGALI':      ['সোমবার', 'মঙ্গলবার', 'বুধবার', 'বৃহস্পতিবার', 'শুক্রবার', 'শনিবার', 'রবিবার'],
    'PORTUGUESE':   ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'],
    'LATIN':        ['dīēs Lūnae', 'dīēs Mārtis', 'dīēs Mercuriī', 'dīēs Iovis', 'dīēs Veneris', 'dīēs Saturnī', 'dīēs Sōlis'],
    'INDONESIAN':   ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'FINNISH':      ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai'],
    'GREEK':        ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυριακή'],
    'HAWAIIAN':     ['Pōʻakahi', 'Pōʻalua', 'Pōʻakolu', 'Pōʻahā', 'Pōʻalima', 'Pōʻaono', 'Lāpule'],
    'HUNGARIAN':    ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap'],
    'ICELANDIC':    ['mánudagur', 'þriðjudagur', 'miðvikudagur', 'fimmtudagur', 'föstudagur', 'laugardagur', 'sunnudagur'],
    'IRISH':        ['Luan', 'Máirt', 'Céadaoin', 'Déardaoin', 'Aoine', 'Satharn', 'Domhnach'],
    'KOREAN':       ['월요일', '화요일 ', '수요일', '목요일', '금요일', '토요일', '일요일'],
    'NAVAJO':       ['Damóo Biiskání', 'Naakijį́ Ndaʼanish', 'Tágíjį́ Ndaʼanish', 'Dį́ʼíjį́ Ndaʼanish', 'Ndaʼiiníísh', 'Yiską́ Damóo', 'Damóo'],
    'KLINGON':      ['DaS­jaj', 'pov­jaj', 'ghItlh­jaj', 'logh­jaj', 'buq­jaj', 'loj­mIt­jaj', 'jaj wa’'],
    'PIG_LATIN':    ['Ondaymay', 'Uesdaytay', 'Ednesdayway', 'Ursdaythay', 'Idayfray', 'Aturdaysay', 'Undaysay']
}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, Welcome to my Discord server! Please be sure to check out the rules-and-guidelines channel before you begin chatting. I hope you have a great time in the server! Thank you for joining!')

@client.event
async def on_message(message):

    if message.author == client.user or message.author.bot:
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

    if message.content.startswith('$commands'):
        await message.channel.send(commands_print)
    elif message.content.startswith('$help'):
        await message.channel.send(help_print)
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
            await message.channel.send('You will no longer be notified when saltAxAtlas goes live :cry:')
        else:
            await member.add_roles(role)
            await message.channel.send('You will now be notified when saltAxAtlas goes live! :partying_face:')
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
        day_max_length = max([len(day) for day in dotw]) # dumb stuff I do for alignment
        schedule_print = f'All times are in {member_timezone}:\n\t' + '\n\t'.join([f'`{dotw[index].ljust(day_max_length)}`:\tNo Stream :(' if schedule_def[key][0] == -1 else f'`{dotw[index].ljust(day_max_length)}`:\t{(int(schedule_def[key][0] + tz) % 24)}:{["30","00"][type(timezones[member_timezone]) is int]} - {int((schedule_def[key][0] + schedule_def[key][1] + tz) % 24)}:{["30","00"][type(timezones[member_timezone]) is int]}' for index, key in enumerate(schedule_def.keys())]) + '\n\tThere will also be unscheduled streams sometimes during the week after 5 PM EST!'
        if special_event_def:
            event_max_length = max([len(event) for event in special_event_def.keys()]) # dumb stuff I do for alignment
            schedule_print += '\nPlanned Special Events:\n\t' + '\n\t'.join([f'`{key.ljust(event_max_length)}` -> {value}' for key, value in special_event_def.items()])
        if sign:
            member_timezone += sign + str(abs(shift)) 
        await message.channel.send(schedule_print)
    elif message.content.startswith('$socials'):
        await message.channel.send(social_print)
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
    elif message.content.startswith('$server-info'):  # IDK if this works now
        bot_count = 0
        role = get(member.guild.roles, name='Bots')
        for server_member in message.guild.members:
            if role in server_member.roles:
                bot_count += 1
        total_members = len([*message.guild.members])
        real_person_count = total_members - bot_count
        info_max_length = max([len(title) for title in server_info_defs.keys()]) # dumb stuff I do for alignment
        server_info_print = '\n'.join([f'`{key.ljust(info_max_length)}`: {value}' for key, value in server_info_defs.items()])
        server_info_print += f'\n`{"Total Members".ljust(info_max_length)}`: {total_members}\n`{"People".ljust(info_max_length)}`: {real_person_count}\n`{"Bots".ljust(info_max_length)}`: {bot_count}'
        await message.channel.send(server_info_print)
    else:
        await message.channel.send(f'{message.content} is not a valid command. Try \'$commands\' for a list of available commands!')

client.run(os.getenv("TOKEN"))
