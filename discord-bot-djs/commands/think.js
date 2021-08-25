const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	name: 'think',
	comm: new SlashCommandBuilder().setName('think').setDescription('🤔'),
	exec: async (interaction, client, main) => {

		interaction.deferReply();

	}
}