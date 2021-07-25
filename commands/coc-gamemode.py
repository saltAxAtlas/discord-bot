from random import choice

cmd = {
	'command': 'coc-gamemode',
	'aliases': ['cocgamemode'],
	'description': 'generates a random CoC gamemode to play.',
	'run': exec
}

async def execute(message, vars):
	return await message.channel.send(choice(['Fastest!', 'Shortest!', 'Reverse!']))
