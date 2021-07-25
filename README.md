# discord_bot
This is a poorly written Discord bot for a streaming community server!

## TODO:
-   [ ] Slash Command Integration
-   [X] Add More Timezone / Language Support
-   [X] Message Members on Joining Server
-   [X] Fix $server-info, Add More Info to Command
-   [ ] Auto Post $going-live
-   [ ] Add $invite Command
-	[ ] Add $rules Command
-	[ ] Add Optional Parameters to $help, Print In-Depth Descriptions for each Command
-	[ ] Assign Roles Base on Reactions

## Use Instructions:
1. Install Dependencies
	- Run `python3 -m pip install -r requirements.txt`
2. Replace Bot Token
	- Place your bot token in example.env, and rename it to '.env'
3. Adjust Stream Schedule
	- Adjust the values in /commands/schedule.py to match your stream times
4. Adjust Discord Roles
	- Adjust role names to match the roles of your server
