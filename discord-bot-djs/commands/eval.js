const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'eval',
	comm: new SlashCommandBuilder().setName('eval').setDescription('Evaluate something')
.addStringOption(op => op.setName('eval').setDescription('What to evaluate').setRequired(true)),
	exec: async (interaction, client, main) => {

		if(![ 808874804688977930, 455435762981273630 ].includes(parseInt(interaction.user.id))) {
			console.log(`\t[${main.exports.file(module.filename)}] Permission denied`)
			return interaction.reply({ content: 'Permission denied', ephemeral: true })
		}

		const what = interaction.options.getString('eval') || '';

		if(!what.length > 0) {
			return interaction.reply({ embeds: [ main.exports.embed.setDescription('What should I evaluate?') ], ephemeral: true })
		}

		console.log(`\t${main.exports.file(module.filename)} - eval: ${what}`)

		await interaction.deferReply();
		try {
			let result = eval(what);
			let res = '[!] Not a promise';
			if(result?.then)
				res = await result;

			return interaction.editReply({ embeds: [
				new MessageEmbed(main.exports.embed)
					.setColor('#00FF00')
					.setTitle('Success!')
					.setDescription(`Eval result:\n\n\`\`\`\n${JSON.stringify(result, 0, 2)}\n\`\`\`\n\n\nAfter awaiting:\n\`\`\`${JSON.stringify(res, 0, 2)}\`\`\``)
			]})
		} catch(e) {
			return interaction.editReply({ embeds: [
				new MessageEmbed(main.exports.embed)
					.setColor('#FF0000')
					.setTitle('Error')
					.setDescription(`Eval result:\n\n\`\`\`\n${e.stack}\`\`\``)
			]})
		}
	}
}