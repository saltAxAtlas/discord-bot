async def execute(message, vars):
	resp = 'Try $commands for a simplified command list.\n'
	cmds = vars['commands']
	maxlen = 2 if len(cmds)+1 < 100 else 3
	for idx, val in enumerate(cmds):
		resp += f'\t`{str(idx+1).rjust(maxlen)}`. {vars["command_prefix"]}{val["command"]} - {val["description"]}\n'
	return await message.channel.send(resp.strip())

cmd = {
	'command': 'help',
	'aliases': [],
	'description': 'an in-depth explanation of the available commands.',
	'run': execute
}
