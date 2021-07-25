from discord.utils import get

cmd = {
	'command': 'notified',
	'aliases': [],
	'description': 'gives you the \'Notified\' role.',
	'run': execute
}

async def execute(message, vars):
    role = get(message.guild.roles, name='Notified')
    if role in message.author.roles:
        await message.author.remove_roles(role)
        await message.channel.send('You will no longer be notified when saltAxAtlas goes live :cry:')
    else:
        await message.author.add_roles(role)
        await message.channel.send('You will now be notified when saltAxAtlas goes live! :partying_face:')