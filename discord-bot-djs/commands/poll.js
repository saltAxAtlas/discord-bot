const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
const emojiRegex = require('emoji-regex/RGI_Emoji.js');



module.exports = {
    name: 'poll',
    comm: new SlashCommandBuilder().setName('poll').setDescription('Make a poll')
        .addStringOption(op => op.setName('title').setDescription('The poll title').setRequired(true))
        .addStringOption(op => op.setName('captions').setDescription('Captions (Format: `[caption], [...]`)').setRequired(true))
        .addStringOption(op => op.setName('emojis').setDescription('Emojis (Format: `[emoji][...]`)').setRequired(true)),
    exec: async (interaction, client, main) => {


        const title = interaction.options.getString('title');
        const captions = interaction.options.getString('captions').split`, `
        const emojis = [];
        let emoji = interaction.options.getString('emojis');
        let _i = 0;

        console.log(emojis, emoji, _i);

        while(emoji.length > 0) {
            var match = emojiRegex().exec(emojis);
            if(!match) { console.log('no match -> breaking'); break; }
            console.log(match);
            console.log(emojis);
            console.log(emoji);
            emojis.push(match[0]);
            emoji = emoji.slice(match[0].length);
            if(++_i >= 25) break;
        }

        console.log(emojis, emoji, _i);

        const options = captions.map(( caption, index ) => {return{ caption: caption, emoji: emojis[index] }})

        var error = '';

        if(Object.keys(captions).length < 2) {
            error = 'Too little options. The minimum amount of options is 2';
        } else if(Object.keys(captions).length > 25) {
            error = 'Too many options. The maximum amount of options is 25';
        }

        if(error.length !== 0)
            return interaction.reply({ embeds: [ new MessageEmbed(main.exports.embed).setDescription(error) ], ephemeral: true });

        var embed = new MessageEmbed(main.exports.embed).setTitle(title).setDescription('');

        options.forEach((option, index) => 
            embed.addField(option.caption || '{ No caption specified! }', option.emoji  || '{ No emoji specified! }', true)
        );

        var reply = await interaction.reply({ embeds: [ embed ], fetchReply: true });

        options.forEach(option => {
            try {
                reply.react(option.emoji || '❌')
            } catch {}
        });

    }
}