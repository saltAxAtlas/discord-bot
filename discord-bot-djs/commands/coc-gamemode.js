const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'coc-gamemode',
	comm: new SlashCommandBuilder().setName('coc-gamemode').setDescription('Choose a random CoC gamemode'),
	exec: async (interaction, client, main) => {

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						['Fastest', 'Shortest', 'Reverse'][Math.floor(Math.random() * 3)]
					)
				]
			});

	}
}