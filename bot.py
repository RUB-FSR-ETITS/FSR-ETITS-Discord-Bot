import discord
import config

intents = discord.Intents(members=True, messages=True, guilds=True, voice_states=True)
client = discord.Client(intents=intents)

# binding these vars to client limits the bot to one guild
# no expansion is planned, so we work with this
client.runningMeeting = False
client.meetingMembers = set()

@client.event
async def on_ready():
	print('Bot logged in as {0}'.format(client.user))

@client.event
async def on_message(message):
	# limit bot to designated bot channel
	if message.channel.id in config.bot_channel_ids:
		if message.content.startswith('$server'):
			await message.channel.send('{0.guild.name} {0.guild.id}'.format(message))

		if message.content.startswith('$roles'):
			for r in message.guild.roles:
				await message.channel.send('{0.name} {0.id}'.format(r).replace('@', ''))

		if message.content.startswith('$vchannels'):
			for v in message.guild.voice_channels:
				await message.channel.send('{0.name} {0.id}'.format(v))

		if message.content.startswith('$about'):
			await message.channel.send('FSR-Bot with <3 from ~~TJ~~ FSR ETITS')

		if message.content.startswith('$start meeting'):
			client.runningMeeting = True
			await message.channel.send('Meeting started!')

			# gather all already present members
			channel = client.get_channel(config.channel_id)
			
			for member in channel.members:
				client.meetingMembers.add(member.display_name)

		if message.content.startswith('$stop meeting'):
			client.runningMeeting = False

			# generate list of meeting participants and send message
			mString = '** **\n'
			for member in client.meetingMembers:
				mString += member + '\n'
			await message.channel.send(mString)

			client.meetingMembers.clear()

@client.event
async def on_voice_state_update(member, before, after):
	
	# check if role needs to be added
	if after.channel != None:
		if after.channel.id == config.channel_id:

			guild = member.guild
			role = guild.get_role(config.role_id)

			# add role to member
			await member.add_roles(role)

			# log member
			if client.runningMeeting:
				client.meetingMembers.add(member.display_name)

	# check if role needs to be removed
	if before.channel != None:
		if before.channel.id == config.channel_id:
			
			guild = member.guild
			role = guild.get_role(config.role_id)

			await member.remove_roles(role)

client.run(config.token)

