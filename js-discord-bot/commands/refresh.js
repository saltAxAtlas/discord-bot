const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'refresh',
	comm: new SlashCommandBuilder().setName('refresh').setDescription('Refreshes slash commands'),
	exec: async (interaction, client, main) => {

		if(interaction.user.id !== client.application?.owner?.id) {
			console.log(`\t[${module.filename}] Permission denied`)
			return interaction.reply({ content: 'Permission denied', ephemeral: true })
		}
		await interaction.deferReply();
		main.exports.Reload();
		await interaction.editReply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription('Done!') ]})

	}
}