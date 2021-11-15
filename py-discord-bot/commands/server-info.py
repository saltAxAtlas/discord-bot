from discord.utils import get

async def execute(message, vars):
	bot_count = 0
	bot_role = get(message.author.guild.roles, name='Bots')
	server_members = message.guild.members
	for server_member in server_members:
		if bot_role in server_member.roles:
			bot_count += 1

	total_members = len([*server_members])
	real_person_count = total_members - bot_count

	stats = {
		'Name': 'saltAxAtlas Streams',
		'Creation Date': 'Feb. 9, 2021',
		'Members': total_members,
		'People': real_person_count,
		'Bots': bot_count
	}

	maxlen = max(map(len, stats.keys()))
	resp = 'Server Statistics:'
	for i in stats:
		resp += f'\n\t`{i.ljust(maxlen)}`: {stats[i]}'
	return await message.channel.send(resp.rstrip())

cmd = {
	'command': 'server-info',
	'aliases': ['serverinfo', 'info'],
	'version': '1.0.0',
	'description': 'displays information about the server.',
	'in-depth-desc': 'When this command is run, it will display information about the server, such as the date it was created and the number of members.',
	'run': execute
}
