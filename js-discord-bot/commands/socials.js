const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
	name: 'socials',
	comm: new SlashCommandBuilder().setName('socials').setDescription('saltAxAtlas\'s social links!'),
	exec: async (interaction, client, main) => {

		const socials = {
		    Twitch:  'https://twitch.tv/saltaxatlas',
		    Twitter: 'https://twitter.com/saltAxAtlas',
		    TikTok:  'https://www.tiktok.com/@saltaxatlas',
		    GitHub:  'https://github.com/saltAxAtlas',
		    Discord: 'https://discord.gg/V56vXKe7mY'
		}

		const padding = Object.keys(socials).map(s => s.length).sort((a, b) => b - a)[0];

		await interaction.reply({
				embeds: [
					new MessageEmbed(main.exports.embed).setDescription(
						Object.keys(socials).map(service => `\`${service.padEnd(padding)}\`: <${socials[service]}>`).join`\n`
					)
				]
			});

	}
}

