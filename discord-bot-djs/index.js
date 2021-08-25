const { SlashCommandBuilder } = require('@discordjs/builders');
const { Client, Intents, MessageEmbed } = require('discord.js');
const Config = require('./.config.json');
const Refresh = require('./deploy_slash.js');
const { readdirSync } = require('fs');
const twitchSetup = require('./twitch.js');

const client = new Client({
	intents: [
		Intents.FLAGS.GUILDS
	]
});

const commands = [];
const interactions = [];
let buttonHandler = require('./button_handler.js');

function Reload() {
	let buttonHandler = require('./button_handler.js');
	
	commands.length = 0;
	interactions.length = 0;

	console.log('[*] Loading commands')
	readdirSync('./commands/').forEach(file => {
		if(!file.endsWith('.js')) return;
		try {
			commands.push(require(`./commands/${file}`));
			console.log(`\t[+] Loaded ${file}`)
		} catch(e) {
			console.log(`\t\t[!] Failed loading ${file} - ${e}`)
		}
	});
	console.log('[+] Loading done!')

	commands.map(cmd => cmd.comm).forEach(cmd => interactions.push(cmd))

	Refresh(interactions, client);
}

let lastLive = false;
async function postTwitch(isLive, uname) {
	// console.log(lastLive, isLive, uname)
	if(isLive && !lastLive) {
		// 1st map: get the guild,
		// 2nd map: get the channel,
		// forEach: sends the message
		Object.keys(Config.twitch.guildIds)
			.map(gId     => client.guilds.cache.map(( guild, snowflake ) => guild).filter(guild => gId == guild.id)[0])
			.map(g => g.channels.cache.get(Config.twitch.guildIds[g.id]))
			.forEach(ch => ch.send(Config.twitch.content.replaceAll('$!', uname).replaceAll('$_', uname.toLowerCase())));
	} else if(!isLive && lastLive) {
		// 1st map: get the guild,
		// 2nd map: get the channel,
		// forEach: deletes the last message
		Object.keys(Config.twitch.guildIds)
			.map(gId     => client.guilds.cache.map(( guild, snowflake ) => guild).filter(guild => gId == guild.id)[0])
			.map(g => g.channels.cache.get(Config.twitch.guildIds[g.id]))
			.forEach(ch => ch.bulkDelete(1));
	}
	lastLive = isLive;
}

client.on('ready', async () => {
	console.log('Bot has logged in!');
	Reload();
	await client.application?.fetch();
	await twitchSetup(module);
	module.exports.embed = new MessageEmbed().setColor('#ABCDEF').setFooter(`Bot owner: ${client.application?.owner?.tag}`);
});

client.on('interactionCreate', async interaction => {
	if(interaction.isButton()) return buttonHandler(interaction, client, module);
	if(!interaction.isCommand()) return;

	console.log(`Slash command used: ${interaction.commandName} by ${interaction.user.tag}`)

	commands.filter(cmd => cmd.name === interaction.commandName)[0]?.exec(interaction, client, module);
});

module.exports = {
	Reload: Reload,
	twitch: postTwitch,
	file: path => path.split(/(\/|\\)/)[path.split(/(\/|\\)/).length - 1]
}

client.login(Config.token);