const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'coin-flip',
	comm: new SlashCommandBuilder().setName('coin-flip').setDescription('Flips a coin'),
	exec: async (interaction, client, main) => {

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						['Heads!', 'Tails!'][Math.floor(Math.random() * 2)]
					)
				]
			});

	}
}