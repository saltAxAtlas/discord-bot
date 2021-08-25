const { MessageEmbed } = require('discord.js');

module.exports = async (interaction, client, main) => {
	let roleName;

		if(interaction.customId === 'notified')
			roleName = 'Notified';

		else if(interaction.customId === 'qotd')
			roleName = 'Notified QOTD';

		else
			return interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription('Invalid button @button_handler.js:14') ], ephemeral: true });

	const role = interaction.guild.roles.cache.map(( role, snowflake ) => role).filter(role => role.name.includes(roleName))[0];

	if(!role)
		return interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription('Something went wrong @button_handler.js:20') ], ephemeral: true });

	if(interaction.member.roles.cache.map(( r, sf ) => r.id).includes(role.id)) {
		interaction.member.roles.remove(role);
		interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription(`You got the \`${role.name}\` role removed!`) ], ephemeral: true });
	} else {
		interaction.member.roles.add(role);
		interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription(`You got the \`${role.name}\` role!`) ], ephemeral: true });
	}

}