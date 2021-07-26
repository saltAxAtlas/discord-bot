from discord.utils import get

async def execute(message, vars):
    role = get(message.guild.roles, name='Streamer')
    if role in message.author.roles:
        notified = get(message.guild.roles, name='Notified')
        return await message.channel.send(f'{notified.mention} saltAxAtlas is streaming now at https://twitch.tv/saltaxatlas !')
    else:
        return await message.channel.send('You do not have permission to use this command!')

cmd = {
    'command': 'going-live',
    'aliases': ['goinglive'],
    'description': 'pings \'Notified\' (only salt can use this).',
    'run': execute
}
