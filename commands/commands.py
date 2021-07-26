async def execute(message, vars):
	resp = 'List of Commands:\n'
	cmds = vars['commands']
	maxlen = 2 if len(cmds)+1 < 100 else 3
	for idx, val in enumerate(cmds):
		resp += f'\t`{str(idx+1).rjust(maxlen)}`. {vars["command_prefix"]}{val["command"]}\n'
	return await message.channel.send(resp.strip())

cmd = {
	'command': 'commands',
	'aliases': ['cmds'],
	'description': 'a list of available commands.',
	'run': execute
}
