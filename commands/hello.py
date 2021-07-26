async def execute(message, vars):
	return await message.channel.send(f'Hello, {message.author.name}!')

cmd = {
	'command': 'hello',
	'aliases': ['hi'],
	'description': 'the bot will say hello to you.',
	'run': execute
}
