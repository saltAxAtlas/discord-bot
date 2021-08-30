const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'hello',
	comm: new SlashCommandBuilder().setName('hello').setDescription('Says hello to you'),
	exec: async (interaction, client, main) => {

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						`Hello, ${interaction.user.username}`
					)
				]
			});

	}
}