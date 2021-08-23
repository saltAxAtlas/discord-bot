import discord

async def execute(message, vars):
    msg = message.content.split()[1:]
    question = []
    poll_choices = {}
    poll_start_index = -1
    for index, word in enumerate(msg):
        if word == '?':
            poll_start_index = index
            break
        question.append(word)
    if len(question) < 1:
        return await message.channel.send('No Question Asked -> Use `$help $poll`')
    if poll_start_index == -1:
        return await message.channel.send('No Choices Given -> Use `$help $poll`')
    msg = msg[poll_start_index + 1:]
    msg_len = len(msg)
    if msg_len % 2 == 1:
        return await message.channel.send('Unmatched Reaction and Reaction Description -> Use `$help $poll`')
    if msg_len < 4:
        return await message.channel.send('Not Enought Arguements to Start Poll -> Use `$help $poll`')
    for index in range(0, msg_len, 2):
        poll_choices[msg[index]] = msg[index + 1]
    embedVar = discord.Embed(title="Poll!", description=f"{' '.join(question)}", color=0x15fffe)
    for emoji, value in poll_choices.items():
        embedVar.add_field(name=f'{emoji}', value=f'{value}', inline=False)
    react_message = await message.channel.send(embed=embedVar)
    for emoji in poll_choices.keys():
        await react_message.add_reaction(emoji)
    return

cmd = {
	'command': 'poll',
	'aliases': [],
	'version': '1.0.0',
	'description': 'generates a poll that can be voted on with reactions.',
	'in-depth-desc': 'When this command is run, it will send a message containing a poll that people can vote on with reactions. The expected input for this command is:\n`$poll question ? reaction_1 reaction_description_1 reaction_2 reaction_description_2 ...`',
	'run': execute
}