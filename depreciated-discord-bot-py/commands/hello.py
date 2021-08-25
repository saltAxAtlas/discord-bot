async def execute(message, vars):
	return await message.channel.send(f'Hello, {message.author.name}!')

cmd = {
	'command': 'hello',
	'aliases': ['hi'],
	'version': '1.0.0',
	'description': 'the bot will say hello to you.',
	'in-depth-desc': 'When this command is run, the bot will say hello to you!',
	'run': execute
}
