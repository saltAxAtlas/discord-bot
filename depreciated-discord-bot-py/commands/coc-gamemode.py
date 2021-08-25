from random import choice

async def execute(message, vars):
	return await message.channel.send(choice(['Fastest!', 'Shortest!', 'Reverse!']))

cmd = {
	'command': 'coc-gamemode',
	'aliases': ['cocgamemode'],
	'version': '1.0.0',
	'description': 'generates a random CoC gamemode to play.',
	'in-depth-desc': 'When this command is run, it will output a random choice from the possible values of: Fastest, Shortest, Reverse.',
	'run': execute
}

