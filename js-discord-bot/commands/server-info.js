const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'server-info',
	comm: new SlashCommandBuilder().setName('server-info').setDescription('Get information about the server'),
	exec: async (interaction, client, main) => {

		await interaction.deferReply();

		console.log(`\t[${main.exports.file(module.filename)}] Fetching the guild`)
		await interaction.guild.fetch();
		// console.log('Fetching the guild members')
		// await interaction.guild.members.fetch();

		const ts = interaction.guild.createdAt;
		const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
		const date = `${months[ts.getMonth()]}. ${ts.getDay()}, ${ts.getFullYear()}`

		console.log(`\t[${main.exports.file(module.filename)}] Creating stats`)

		const stats = {
			'Name': interaction.guild.name,
			'Creation Date': date,
			'Members': interaction.guild.memberCount
			// 'People': interaction.guild.members.cache.filter(( member, _ ) => !member.bot).size(),
			// 'Bots': interaction.guild.members.cache.filter(( member, _ ) => member.bot).size(),
		}

		console.log(`\t[${main.exports.file(module.filename)}] Getting padding`)

		const padding = Object.keys(stats).map(x => x.length).sort((a, b) => b - a)[0];

		console.log(`\t[${main.exports.file(module.filename)}] Editing the message`)

		await interaction.editReply({
				embeds: [
					new MessageEmbed(main.exports.embed).setTitle('Server info:').setDescription(
						Object.keys(stats).map(stat => `\`${stat.padEnd(padding)}\`: ${stats[stat]}`).join`\n`
					)
				]
			});

		console.log(`\t[${main.exports.file(module.filename)}] Done`)

	}
}

