from discord.utils import get

cmd = {
	'command': 'qotd',
	'aliases': [],
	'description': 'gives you the \'QOTD Notified\'. role',
	'run': exec
}

async def exec(message, vars):
    member = message.author
    role = get(member.guild.roles, name='Notified QOTD')
    if role in member.roles:
        await member.remove_roles(role)
        await message.channel.send('You will no longer be pinged when the QOTD is posted :(')
    else:
        await member.add_roles(role)
        await message.channel.send('You will now be pinged when the QOTD is posted!')