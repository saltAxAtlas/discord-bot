const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
const Config = require('./.config.json');


async function Refresh(commands, client) {
	const rest = new REST({ version: '9' }).setToken(Config.token);

	client.guilds.fetch();
	let guilds = client.guilds.cache.map((guild, snowflake) => guild);

	console.log(`[*] Reloading slash commands for ${guilds.length} guilds`)
	for(guild of guilds) {
		try {
			await rest.put(
				Routes.applicationGuildCommands(client.user.id, guild.id),
				{ body: commands.map(c => c.toJSON()) },
			);

			console.log(`\t[+] Reloaded slash commands for ${guild.name}`);
		} catch(e) {
			console.log(`\t[-] Failed reloading slash commands for ${guild.name} - ${e}`)
		}
	}
	console.log('[+] Finished reloading slash commands')
}

module.exports = Refresh;