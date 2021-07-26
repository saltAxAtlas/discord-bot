from random import choice

async def execute(message, vars):
	return await message.channel.send(choice(['Heads!', 'Tails!']))

cmd = {
	'command': 'coin-flip',
	'aliases': ['coinflip'],
	'description': 'generates a random coin flip.',
	'run': execute
}
