from discord.utils import get

async def execute(message, vars):
    role = get(message.guild.roles, name='Invite to Clash')
    if role in message.author.roles:
        await message.author.remove_roles(role)
        return await message.channel.send('You will no longer be pinged when people are starting private clashes :cry:')
    else:
        await message.author.add_roles(role)
        return await message.channel.send('You will now be pinged when people are looking for others to clash with!')

cmd = {
	'command': 'coc-invite',
	'aliases': ['cocinvite'],
	'description': 'gives you the \'Invite to Clash\' role.',
	'run': execute
}
