cmd = {
	'command': 'help',
	'aliases': [],
	'description': 'an in-depth explanation of the available commands.',
	'run': execute
}

async def execute(message, vars):
	resp = 'Try $commands for a simplified command list.\n'
	cmds = vars['commands']
	maxlen = len(cmds)+1
	for idx, val in enumerate(cmds):
		resp += f'\t`{str(idx+1).rjust(maxlen)}`. {vars["command_prefix"]}{val} - {val["description"]}\n'
	return await message.channel.send(resp.strip())