# discord-bot
This is a ~~poorly written~~ Discord bot for a streaming community server! Ported from Python to JavaScript by: [@rozbrajaczpoziomow](https://github.com/rozbrajaczpoziomow)

## TODO:
-	[ ] Message Members on Joining Server
-	[X] Auto Post $going-live
-	[X] Move to Discord.js v13
-	[X] Slash Commands
-	[X] Add Poll Command (Vote With Reactions)
-	[X] Add More Timezone / Language Support
-	[X] Fix /server-info, Add More Info to Command
-	[X] Add /invite Command
-	[X] Add /rules Command
-	[X] Assign Roles Based on Buttons

## Use Instructions:
1. Install Dependencies
	- Run `npm i`
2. Replace Tokens
	- Place your bot token in `example.config.json` as `{ "token": "token_goes_here" }`
	- Place client id in `example.config.json` as  `{"id": "client_id_here"}`
	- Place client secret in `example.config.json` as  `{"secret": "client_secret_here"}`
	- Place guild id and the channel to post going-live message in `example.config.json` as  `{"guild_id_here": "channel_id_here"}`
3. Run Bot
	- Run `npm run`
