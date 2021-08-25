const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageActionRow, MessageButton, MessageEmbed } = require('discord.js');

module.exports = {
	name: 'get-roles',
	comm: new SlashCommandBuilder().setName('get-roles').setDescription('Generates a "Get roles from clicking" message, Note: this only needs to be ran once.')
		.addChannelOption(op => op.setName('channel').setDescription('What channel to post in').setRequired(true)),
	exec: async (interaction, client, main) => {

		if(interaction.user.id !== client.application?.owner?.id) {
			console.log(`\t[${module.filename}] Permission denied`)
			return interaction.reply({ content: 'Permission denied', ephemeral: true })
		}

		await interaction.deferReply();

		const channel = interaction.options.getChannel('channel');

		const buttons = new MessageActionRow()
			.addComponents([
				new MessageButton()
					.setCustomId('notified')
					.setLabel('🥳 Notified')
					.setStyle('SUCCESS'),
				new MessageButton()
					.setCustomId('qotd')
					.setLabel('❓ Notified QOTD')
					.setStyle('PRIMARY')
			]);

		const embed = new MessageEmbed(main.exports.embed).setTitle('Click for roles')

		channel.send({ embeds: [ embed ], components: [ buttons ] })

		await interaction.editReply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription('Done!') ]})

	}
}