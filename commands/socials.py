cmd = {
	'command': 'socials',
	'aliases': ['social'],
	'description': 'a list of my social media links.',
	'run': exec
}

socials = {
    'Twitch':  'https://twitch.tv/saltaxatlas',
    'Twitter': 'https://twitter.com/saltAxAtlas',
    'TikTok':  'https://www.tiktok.com/@saltaxatlas',
    'GitHub':  'https://github.com/saltAxAtlas',
    'Discord': 'https://discord.gg/V56vXKe7mY'
}

async def exec(message, vars):
	maxlen = max(map(len, socials.keys()))
	resp = 'Check out my socials to stay up to date!'
	for i in socials:
		resp += f'\n\t{i.ljust(maxlen)}: <{socials[i]}>'
	return await message.channel.send(resp.rstrip())