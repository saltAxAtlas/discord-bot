from discord.utils import get

async def execute(message, vars):
    member = message.author
    role = get(member.guild.roles, name='Notified QOTD')
    if role in member.roles:
        await member.remove_roles(role)
        await message.channel.send('You will no longer be pinged when the QOTD is posted :cry:')
    else:
        await member.add_roles(role)
        await message.channel.send('You will now be pinged when the QOTD is posted!')

cmd = {
	'command': 'qotd',
	'aliases': [],
    'version': '1.0.0',
	'description': 'gives you the \'QOTD Notified\' role',
    'in-depth-desc': 'When this command is run, it will give the member the role of "QOTD Notified". This role is pinged every day when the QOTD is posted. If you wish to remove the role, you may use the command again.',
	'run': execute
}
