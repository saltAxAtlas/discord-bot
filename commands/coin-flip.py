from random import choice

async def execute(message, vars):
	return await message.channel.send(choice(['Heads!', 'Tails!']))

cmd = {
	'command': 'coin-flip',
	'aliases': ['coinflip'],
	'version': '1.0.0',
	'description': 'generates a random coin flip.',
	'in-depth-desc': 'When this command is run, it will output a random choice from the possible values of: Heads, Tails.',
	'run': execute
}
