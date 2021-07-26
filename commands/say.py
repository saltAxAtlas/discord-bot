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
	'description': 'lets you control what the bot says.',
	'run': execute
}
