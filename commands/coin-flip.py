from random import choice

cmd = {
	'command': 'coin-flip',
	'aliases': ['coinflip'],
	'description': 'generates a random coin flip.',
	'run': exec
}

async def exec(message, vars):
	return await message.channel.send(choice(['Heads!', 'Tails!']))