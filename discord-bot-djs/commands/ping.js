const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'ping',
	comm: new SlashCommandBuilder().setName('ping').setDescription('Get client ping'),
	exec: async (interaction, client, main) => {

		let reply = await interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription('Pong!') ], fetchReply: true });
		await interaction.editReply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription(String(Date.now() - reply.createdAt) + 'ms') ] });

	}
}