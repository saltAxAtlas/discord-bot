rules = ['Be kind, civil and respectful to one another.', 'Ask before self-promoting.', 'Do not spam messages in the chats.', 'List to the moderators.', 'Don\'t argue with each other.', 'Have fun!']

async def execute(message, vars):
    resp = 'The rules and guidelines for the stream and this server are:'
    maxlen = len(str(len(rules)+1))
    for idx, val in enumerate(rules):
        resp += f'\n\t`{str(idx+1).rjust(maxlen)}.` {val}'
    return await message.channel.send(resp)

cmd = {
	'command': 'rules',
	'aliases': ['rule', 'guidelines'],
	'description': 'displays the rules for the server.',
	'run': execute
}