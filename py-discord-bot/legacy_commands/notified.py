from discord.utils import get

async def execute(message, vars):
    role = get(message.guild.roles, name='Notified')
    if role in message.author.roles:
        await message.author.remove_roles(role)
        await message.channel.send('You will no longer be notified when saltAxAtlas goes live :cry:')
    else:
        await message.author.add_roles(role)
        await message.channel.send('You will now be notified when saltAxAtlas goes live! :partying_face:')

cmd = {
	'command': 'notified',
	'aliases': [],
    'version': '1.0.0',
	'description': 'gives you the \'Notified\' role.',
    'in-depth-desc': 'When this command is run, it will give the member the role of "Notified". This role is pinged at the start of every stream. If you wish to remove the role, you may use the command again.',
	'run': execute
}
