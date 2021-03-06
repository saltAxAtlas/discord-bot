# Key -> Day, Value -> [start_time, stream_length, plan_for_stream]
# -1 signifies that there will not be a stream, time in GMT 
schedule_def = {
    'Monday':       [-1, -1, 'None'],
    'Tuesday':      [17, 4, 'CoC / Yare'],
    'Wednesday':    [-1, -1, 'None'],
    'Thursday':     [17, 4, 'CoC / BinarySearch'],
    'Friday':       [16.5, 4, 'CoC / Projects / Variety'],
    'Saturday':     [-1, -1, 'None'],
    'Sunday':       [18, 5, 'CoC']
}

special_event_def = {
    'First Friday':             'Sub / Follow - athon on the first friday of every month! :partying_face:',
    'Banned Language Sundays':  'Ban the winning languages in CoC every Sunday!'
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
    'SPANISH':      ['Lunes', 'Martes', 'Mi??rcoles', 'Jueves', 'Viernes', 'S??bado', 'Domingo'],
    'FRENCH' :      ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    'POLISH' :      ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela'],
    'DUTCH'  :      ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'],
    'TURKISH':      ['Pazartesi', 'Sal??', '??arsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar'],
    'LITHUANIAN':   ['Pirmadienis', 'Antradienis', 'Tre??iadienis', 'Ketvirtadienis', 'Penktadienis', '??e??tadienis', 'Sekmadienis'],
    'ITALIAN':      ['Luned??', 'Marted??', 'Mercoled??', 'Gioved??', 'Venerd??', 'Sabato', 'Domenica'],
    'JAPANESE':     ['???????????????', '????????????', '???????????????', '???????????????', '???????????????', '????????????', '???????????????'],
    'RUSSIAN':      ['??????????????????????', '??????????????', '??????????', '??????????????', '??????????????', '??????????????', '??????????????????????'],
    'SWEDISH':      ['M??ndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'L??rdag', 'S??ndag'],
    'CHINESE':      ['?????????', '?????????', '?????????', '?????????', '?????????', '?????????', '?????????'],
    'HINDI':        ['Somvar', 'Mangalvar', 'Budhvar', 'Guruvar', 'Shukrvar', 'Shanivar', 'Ravivar'],
    'BENGALI':      ['??????????????????', '????????????????????????', '??????????????????', '?????????????????????????????????', '????????????????????????', '??????????????????', '??????????????????'],
    'PORTUGUESE':   ['Segunda-feira', 'Ter??a-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'S??bado', 'Domingo'],
    'LATIN':        ['d????s L??nae', 'd????s M??rtis', 'd????s Mercuri??', 'd????s Iovis', 'd????s Veneris', 'd????s Saturn??', 'd????s S??lis'],
    'INDONESIAN':   ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'FINNISH':      ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai'],
    'GREEK':        ['??????????????', '??????????', '??????????????', '????????????', '??????????????????', '??????????????', '??????????????'],
    'HAWAIIAN':     ['P????akahi', 'P????alua', 'P????akolu', 'P????ah??', 'P????alima', 'P????aono', 'L??pule'],
    'HUNGARIAN':    ['h??tf??', 'kedd', 'szerda', 'cs??t??rt??k', 'p??ntek', 'szombat', 'vas??rnap'],
    'ICELANDIC':    ['m??nudagur', '??ri??judagur', 'mi??vikudagur', 'fimmtudagur', 'f??studagur', 'laugardagur', 'sunnudagur'],
    'IRISH':        ['Luan', 'M??irt', 'C??adaoin', 'D??ardaoin', 'Aoine', 'Satharn', 'Domhnach'],
    'KOREAN':       ['?????????', '????????? ', '?????????', '?????????', '?????????', '?????????', '?????????'],
    'NAVAJO':       ['Dam??o Biisk??n??', 'Naakij???? Nda??anish', 'T??g??j???? Nda??anish', 'D????????j???? Nda??anish', 'Nda??iin????sh', 'Yisk???? Dam??o', 'Dam??o'],
    'KLINGON':      ['DaS??jaj', 'pov??jaj', 'ghItlh??jaj', 'logh??jaj', 'buq??jaj', 'loj??mIt??jaj', 'jaj wa???'],
    'PIG_LATIN':    ['Ondaymay', 'Uesdaytay', 'Ednesdayway', 'Ursdaythay', 'Idayfray', 'Aturdaysay', 'Undaysay']
}

async def execute(message, vars):
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
            return await message.channel.send(f'{shift} is not a valid number following the format \'timezone{sign}shift\'.');
        if sign == '-': 
            shift = -shift

    if member_timezone not in timezones:
        await message.channel.send(f'{member_timezone} is not currently supported! Defaulting to EST')
        member_timezone = 'EST'

    if member_language not in languages:
        await message.channel.send(f'{member_language} is not currently supported! Defaulting to English')
        member_language = 'ENGLISH'

    tz = timezones[member_timezone] + shift
    member_days = languages[member_language]
    day_max_length = max(map(len, member_days))
    if sign:
        member_timezone += sign + str(abs(shift)) # shift was stripped from input earlier, so add it back on for the print statement
    resp = f'All times are in {member_timezone}:\n'

    for i, v in enumerate(member_days):
        day = v.ljust(day_max_length)
        sched = schedule_def[languages['ENGLISH'][i]]
        resp += f'\t`{day}`:\t'
        if sched[0] == -1:
            resp += 'No Stream :(\n'
            continue
        # Multiple resp += to avoid a large f-string
        resp += str(int(sched[0] + tz) % 24)
        resp += ':'
        resp += '00' if type(tz) == int and type(sched[0]) == int else '30'
        resp += ' - '
        resp += str(int(sum(sched[:2]) + tz) % 24)
        resp += ':'
        resp += '00' if type(tz) == int and type(sched[0]) == int else '30'
        resp += ' -> '
        resp += sched[2]
        resp += '\n'
    resp = resp.strip()
    if special_event_def:
        resp += '\n\nPlanned Special Events:'
        for key, value in special_event_def.items():
            resp += f'\n\t{key} -> {value}'

    return await message.channel.send(resp)

cmd = {
	'command': 'schedule',
	'aliases': ['sch', 'sched'],
    'version': '1.0.2',
	'description': 'displays the stream schedule.',
    'in-depth-desc': 'When this command is run, it will post the stream schedule, as well as special planned events. This command supports addition languages, and timezones. The expected input for this command is: $schedule Timezone Language.',
	'run': execute
}
