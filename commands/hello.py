cmd = {
	'command': 'hello',
	'aliases': [],
	'description': 'the bot will say hello to you.',
	'run': execute
}

async def execute(message, vars):
	return await message.channel.send(f'Hello, {message.author.name}!')