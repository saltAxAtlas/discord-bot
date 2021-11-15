async def execute(message, vars):
    invite_link = await message.channel.create_invite(max_uses=1, unique=True)
    return await message.author.send(invite_link)

cmd = {
    'command': 'invite',
    'aliases': ['inv', 'generate-invite'],
    'version': '1.0.0',
    'description': 'generates an invite link for the server.',
    'in-depth-desc': 'When this command is run, the bot will DM you a single use invite link to the server. You may then pass this invite link to someone who is interested in joining.',
    'run': execute
}
