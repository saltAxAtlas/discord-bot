async def execute(message, vars):
	resp = 'List of Commands:\n'
	cmds = vars['commands']
	maxlen = len(str(len(cmds)+1))
	for idx, val in enumerate(cmds):
		resp += f'\t`{str(idx+1).rjust(maxlen)}`. {vars["command_prefix"]}{val["command"]}\n'
	return await message.channel.send(resp.strip())

cmd = {
	'command': 'commands',
	'aliases': ['cmds'],
	'version': '1.0.0',
	'description': 'a list of available commands.',
	'in-depth-desc': 'When this command is run, it will output a list of all of the available commands for this bot.',
	'run': execute
}
