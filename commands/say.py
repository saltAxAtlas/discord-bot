async def execute(message, vars):
	try:
		response = message.content[4:].lstrip()
		if response:
			return await message.channel.send(response)
		else:
			return await message.channel.send('... what should I say?')
	except IndexError:
		return await message.channel.send('... what should I say?')

cmd = {
	'command': 'say',
	'aliases': [],
	'version': '1.0.0',
	'description': 'lets you control what the bot says.',
	'in-depth-desc': 'When this command is run, the bot will say whatever you type after the command.',
	'run': execute
}
