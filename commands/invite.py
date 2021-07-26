async def execute(message, vars):
    invite_link = await message.channel.create_invite(max_uses=1, unique=True)
    return await message.author.send(invite_link)

cmd = {
    'command': 'invite',
    'aliases': ['inv', 'generate-invite'],
    'description': 'generates an invite link for the server.',
    'run': execute
}
