const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'invite',
	comm: new SlashCommandBuilder().setName('invite').setDescription('Generate an invite for the server'),
	exec: async (interaction, client, main) => {

		let invite = await interaction.guild.invites.create(interaction.channel.id, { maxUses: 1, unique: true })

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						invite.url
					)
				],
				ephemeral: true
			});

	}
}