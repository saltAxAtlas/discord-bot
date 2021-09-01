const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'rules',
	comm: new SlashCommandBuilder().setName('rules').setDescription('Display the rules of the server'),
	exec: async (interaction, client, main) => {

		const rules = [
			'Be kind, civil and respectful to one another.',
			'Ask before self-promoting.',
			'Do not spam messages in the chats.',
			'Listen to the moderators.',
			'Don\'t argue with each other.',
			'https://cdn.discordapp.com/attachments/336935738581188609/782997977173196840/unknown.png',
			'Have fun'
		]

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setTitle('Rules:').setDescription(
						rules.map((rule, index) => `${index + 1}. ${rule}`).join`\n`
					)
				]
			});

	}
}

