import discord
from discord.utils import get

reactions = {
    '🥳': ['Notified', 'Gets pinged at the start of every stream!'], 
    '🖥️': ['Invite to Clash', 'Gets pinged when people are putting together a CoC lobby!'],
    '❓': ['Notified QOTD', 'Gets pinged when the QOTD is posted every day!']
}

async def execute(message, vars):
    role = get(message.guild.roles, name='Streamer')
    if role in message.author.roles:
        embedVar = discord.Embed(title="React for Roles!", description="React to this message to get roles!", color=0x15fffe)
        for emoji, value in reactions.items():
            embedVar.add_field(name=f'{value[0]} {emoji}', value=f'{value[1]}', inline=False)
        react_message = await message.channel.send(embed=embedVar)
        for emoji in reactions.keys():
            await react_message.add_reaction(emoji)
        return
    else:
        return await message.channel.send('You do not have permission to use this command!')

cmd = {
	'command': 'reaction-message',
	'aliases': ['react', 'react-message'],
	'version': '1.0.1',
	'description': 'generates a message that people can react to to gain roles.',
	'in-depth-desc': 'When this command is run, it will send a message that people can react to. When you react to the message you will be given the role stated in the message. This command can only be used by salt.',
	'run': execute
}