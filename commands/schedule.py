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
