const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'say',
	comm: new SlashCommandBuilder().setName('say').setDescription('Make the bot say something')
			.addStringOption(op => op.setName('what').setDescription('What should I say').setRequired(true)),
	exec: async (interaction, client, main) => {

		console.log(`\t${main.exports.file(module.filename)} - ${interaction.options.getString('what')}`)

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						interaction.options.getString('what')
					)
				]
			});

	}
}