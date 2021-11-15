const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

const capitalize = str => str.split``.map((char, ix) => ix === 0? char.toUpperCase() : char.toLowerCase()).join``;

const schedule_def = [
    {},
    { from: { hours: 17, minutes: 0}, duration: 4, activities: [ 'CoC', 'Yare' ] },
    {},
    { from: { hours: 17, minutes: 0}, duration: 4, activities: [ 'CoC', 'BinarySearch' ] },
    { from: { hours: 19, minutes: 0}, duration: 4, activities: [ 'CoC', 'Projects', 'Variety' ] },
    {},
    { from: { hours: 18, minutes: 0}, duration: 5, activities: [ 'CoC' ] }
]

const special_event_def = [
    { event: "First Friday", desc: "Sub / Follow - athon on the first friday of every month! :partying_face:"},
    { event: "Banned Language Sundays", desc: "Ban the winning language in CoC every Sunday!"}
]

const timezones = {
    NUT: { hours: -11, minutes: 0 }, SST: { hours: -11, minutes: 0 },
    TAHT: { hours: -10, minutes: 0 }, CKT: { hours: -10, minutes: 0 }, LINT: { hours: -10, minutes: 0 }, HST: { hours: -10, minutes: 0 },
    HDT: { hours: -9, minutes: 0 },
    AKDT: { hours: -8, minutes: 0 }, PST: { hours: -8, minutes: 0 },
    PDT: { hours: -7, minutes: 0 }, MST: { hours: -7, minutes: 0 },
    MDT: { hours: -6, minutes: 0 }, CST: { hours: -6, minutes: 0 }, EAST: { hours: -6, minutes: 0 }, GALT: { hours: -6, minutes: 0 },
    CDT: { hours: -5, minutes: 0 }, PET: { hours: -5, minutes: 0 }, ECT: { hours: -5, minutes: 0 }, COT: { hours: -5, minutes: 0 },
    EDT: { hours: -4, minutes: 0 }, EST: { hours: -4, minutes: 0 }, AMT: { hours: -4, minutes: 0 },
    WGT: { hours: -3, minutes: 0 }, FKST: { hours: -3, minutes: 0 }, BRT: { hours: -3, minutes: 0 }, ART: { hours: -3, minutes: 0 },
    GST: { hours: -2, minutes: 0 }, WGST: { hours: -2, minutes: 0 },
    CVT: { hours: -1, minutes: 0 },
    GMT: { hours: 0, minutes: 0 }, UTC: { hours: 0, minutes: 0 }, AZOST: { hours: 0, minutes: 0 }, EGST: { hours: 0, minutes: 0 },
    WAT: { hours: 1, minutes: 0 }, CET: { hours: 1, minutes: 0 }, WEST: { hours: 1, minutes: 0 },
    CEST: { hours: 2, minutes: 0 }, CAT: { hours: 2, minutes: 0 }, EET: { hours: 2, minutes: 0 }, SAST: { hours: 2, minutes: 0 },
    EAT: { hours: 3, minutes: 0 }, MSK: { hours: 3, minutes: 0 }, AST: { hours: 3, minutes: 0 }, EEST: { hours: 3, minutes: 0 }, TRT: { hours: 3, minutes: 0 },
    SAMT: { hours: 4, minutes: 0 }, RET: { hours: 4, minutes: 0 }, MUT: { hours: 4, minutes: 0 }, GET: { hours: 4, minutes: 0 }, AZT: { hours: 4, minutes: 0 }, SCT: { hours: 4, minutes: 0 },
    YEKT: { hours: 5, minutes: 0 }, ORAT: { hours: 5, minutes: 0 }, MVT: { hours: 5, minutes: 0 }, TFT: { hours: 5, minutes: 0 }, PKT: { hours: 5, minutes: 0 },
    IST: { hours: 5, minutes: 30 },
    OMST: { hours: 6, minutes: 0 }, ALMT: { hours: 6, minutes: 0 }, KGT: { hours: 6, minutes: 0 }, BST: { hours: 6, minutes: 0 }, IOT: { hours: 6, minutes: 0 },
    KRAT: { hours: 7, minutes: 0 }, WIB: { hours: 7, minutes: 0 }, ICT: { hours: 7, minutes: 0 }, HOVT: { hours: 7, minutes: 0 }, NOVT: { hours: 7, minutes: 0 },
    AWST: { hours: 8, minutes: 0 }, PHST: { hours: 8, minutes: 0 }, ULAT: { hours: 8, minutes: 0 }, IRKT: { hours: 8, minutes: 0 }, WITA: { hours: 8, minutes: 0 }, BNT: { hours: 8, minutes: 0 }, HKT: { hours: 8, minutes: 0 },
    ACWST: { hours: 8, minutes: 30 },
    WIT: { hours: 9, minutes: 0 }, YAKT: { hours: 9, minutes: 0 }, JST: { hours: 9, minutes: 0 }, KST: { hours: 9, minutes: 0 },
    ACST: { hours: 9, minutes: 30 },
    PGT: { hours: 10, minutes: 0 }, AEST: { hours: 10, minutes: 0 }, VLAT: { hours: 10, minutes: 0 },
    VUT: { hours: 11, minutes: 0 }, SRET: { hours: 11, minutes: 0 }, MAGT: { hours: 11, minutes: 0 }, SBT: { hours: 11, minutes: 0 },
    CHADT: { hours: 12, minutes: 0 }, FJT: { hours: 12, minutes: 0 }, ANAT: { hours: 12, minutes: 0 }, NZDT: { hours: 12, minutes: 0 }
}

const languages = {
    ENGLISH:      ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    GERMAN:       ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
    SPANISH:      ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    FRENCH:       ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
    POLISH:       ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'],
    DUTCH:        ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag'],
    TURKISH:      ['Pazartesi', 'Salı', 'Çarsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar'],
    LITHUANIAN:   ['Pirmadienis', 'Antradienis', 'Trečiadienis', 'Ketvirtadienis', 'Penktadienis', 'Šeštadienis', 'Sekmadienis'],
    ITALIAN:      ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica'],
    JAPANESE:     ['げつようび', 'かようび', 'すいようび', 'もくようび', 'きんようび', 'どようび', 'にちようび'],
    RUSSIAN:      ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],
    SWEDISH:      ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag'],
    CHINESE:      ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'],
    HINDI:        ['Somvar', 'Mangalvar', 'Budhvar', 'Guruvar', 'Shukrvar', 'Shanivar', 'Ravivar'],
    BENGALI:      ['সোমবার', 'মঙ্গলবার', 'বুধবার', 'বৃহস্পতিবার', 'শুক্রবার', 'শনিবার', 'রবিবার'],
    PORTUGUESE:   ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'],
    LATIN:        ['dīēs Lūnae', 'dīēs Mārtis', 'dīēs Mercuriī', 'dīēs Iovis', 'dīēs Veneris', 'dīēs Saturnī', 'dīēs Sōlis'],
    INDONESIAN:   ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    FINNISH:      ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai', 'Lauantai', 'Sunnuntai'],
    GREEK:        ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυριακή'],
    HAWAIIAN:     ['Pōʻakahi', 'Pōʻalua', 'Pōʻakolu', 'Pōʻahā', 'Pōʻalima', 'Pōʻaono', 'Lāpule'],
    HUNGARIAN:    ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap'],
    ICELANDIC:    ['mánudagur', 'þriðjudagur', 'miðvikudagur', 'fimmtudagur', 'föstudagur', 'laugardagur', 'sunnudagur'],
    IRISH:        ['Luan', 'Máirt', 'Céadaoin', 'Déardaoin', 'Aoine', 'Satharn', 'Domhnach'],
    KOREAN:       ['월요일', '화요일 ', '수요일', '목요일', '금요일', '토요일', '일요일'],
    NAVAJO:       ['Damóo Biiskání', 'Naakijį́ Ndaʼanish', 'Tágíjį́ Ndaʼanish', 'Dį́ʼíjį́ Ndaʼanish', 'Ndaʼiiníísh', 'Yiską́ Damóo', 'Damóo'],
    KLINGON:      ['DaS­jaj', 'pov­jaj', 'ghItlh­jaj', 'logh­jaj', 'buq­jaj', 'loj­mIt­jaj', 'jaj wa’'],
    PIG_LATIN:    ['Ondaymay', 'Uesdaytay', 'Ednesdayway', 'Ursdaythay', 'Idayfray', 'Aturdaysay', 'Undaysay'],
    PIRATE:       ['Mondee', 'Tuesdee', 'Wednesdee', 'Thirsty', 'Frydee', 'Saturdee', 'Sun']
}

module.exports = {
    name: 'schedule',
    comm: new SlashCommandBuilder().setName('schedule').setDescription('Display the stream schedule')
            .addStringOption(op => op.setName('timezone').setDescription('Change the timezone (Default: EST)'))
            .addStringOption(op => op.setName('language').setDescription('Change the language (Default: English)')),
    exec: async (interaction, client, main) => {

        let timezone = interaction.options.getString('timezone')?.toUpperCase() || 'EST';
        let language = interaction.options.getString('language')?.toUpperCase() || 'ENGLISH';

        console.log(`\t${main.exports.file(module.filename)} - timezone: ${timezone}, language: ${language}`)

        const warns = [];

        if(!Object.keys(timezones).includes(timezone)) {
            warns.push(`Invalid timezone ${timezone}, valid options - ${Object.keys(timezones).join`, `}`)
        }

        if(!Object.keys(languages).includes(language)) {
            warns.push(`Invalid language ${capitalize(language)}, valid options - ${Object.keys(languages).map(tz => capitalize(tz)).join`, `}`)
        }

        if(warns.length !== 0)
            return await interaction.reply({
                    embeds: [
                        new MessageEmbed(main.exports.embed).setDescription(
                            warns.join`\n\n`
                        )
                    ], ephemeral: true
                });

        timezone = timezones[timezone];
        language = languages[language];

        const days = []
        const special_events = []
        let padding = language.map(s => s.length).sort((a, b) => b - a)[0]

        schedule_def.forEach((day, index) => {
            if(Object.keys(day).length === 0)
                days.push(`\`${language[index].padEnd(padding)}\`: No stream`)
            else
                days.push(`\`${language[index].padEnd(padding)}\`: `
                    + `${String((day.from.hours + timezone.hours) % 24).padStart(2, '0')}:${String(day.from.minutes + timezone.minutes).padStart(2, '0')} - `
                    + `${String((day.from.hours + timezone.hours + day.duration) % 24).padStart(2, '0')}:${String(day.from.minutes + timezone.minutes).padStart(2, '0')} -> `
                    + `${day.activities.join`, `}`)
        });

        special_event_def.forEach((eve) => {
            special_events.push(`${eve.event}: ${eve.desc}`)
        });

        await interaction.reply({
                    embeds: [
                        new MessageEmbed(main.exports.embed).setDescription(
                            days.join`\n` + "\n\n" + special_events.join`\n`
                        )
                    ]
                });

    }
}