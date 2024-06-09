Discord
=======

The Discord modules allow you to create, update, list, and/or delete channels, channel messages, reactions, and webhooks in your Discord account.

To get started with Discord, create an account at [https://discordapp.com/register](https://discordapp.com/register?).

### Note

[According to Discord](https://support-dev.discord.com/hc/en-us/articles/4404772028055-Message-Content-Privileged-Intent-FAQ), message content will be categorized as **Privileged Intent** starting September 1, 2022.

This means that users who have installed our verified bot on their Discord server will not be able to use the following Make modules with the bot:

* Watch Channel Messages
* List Channel Messages
* Get a Message
Users who installed the Make verified bot to connect to the Discord app on our platform will see the empty values of messages that the channel member sends for the fields, **content**, **embeds**, **attachments**, and **components** in the output.

The Make verified bot is still able to receive the messages for the above modules under the following conditions:

* Messages the bot sends
* Messages the bot receives in DMs
* Messages in which the bot is mentioned
If you want to use the aforementioned modules, you can [create a custom connection using a separate client ID](discord.html#connect-to-discord-using-oauth2-and-your-own-credentials "Connect to Discord using OAuth2 and your own credentials").

Connect Discord to Make
-----------------------

You can connect the Discord app to Make in two ways:

* [Connect using OAuth2](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2")
* [Connect using OAuth2 and using your own app credentials](discord.html#connect-to-discord-using-oauth2-and-your-own-credentials "Connect to Discord using OAuth2 and your own credentials")
Connect Discord to Make using OAuth2
------------------------------------

To connect your Discord account to Make, you need to create a server and channels.

1. Login to your Discord account and create a server.

![61d5af5c3802c.gif](./../image/uuid-e4283ae8-3b7b-813c-9b18-f471ea1ed586.gif)
2. Enter the details of the server and click *Create*.
3. Go to Make and open the Discord module's *Create a connection dialog*.

![Create_discord_connection.png](./../image/uuid-7748e940-3cb2-2130-5721-c6b0c2c0dfa5.png)
4. Select the server created in step 1, allow the permissions for messages and channels, and click *Authorize*.

![Connect_discord_to_Make.png](./../image/uuid-0ac2d808-f967-bce5-088d-0de8c17e626e.png)

You have successfully connected the Discord app and can now build scenarios.

.

Connect to Discord using OAuth2 and your own credentials
--------------------------------------------------------

To connect to Discord, you need to create a developer account to obtain the bot token, client ID, and client secret values by creating a custom application from your Discord developer account.

1. Log in to the [Discord developer account](https://discord.com/developers/).
2. Click **Create New Application**, enter a name for the application, and click **Create**.

![msedge_S4I8d1TXQM.png](./../image/uuid-e42aed74-4e5d-a161-bfc2-73812fdfef9b.png)
3. On the left menu, click **OAuth2**, add the following redirect URIs, and click **Save Changes**.

`https://www.integromat.com/oauth/cb/discord`

`https://www.make.com/oauth/cb/discord`

![msedge_MxbzEMvjQL.png](./../image/uuid-5ea95233-0869-86e0-6728-22e5c7bee275.png)### Note

Enable **Message Content Intent** in your app settings if you want to receive the full message content.
4. In the **Client Information** section, copy the **CLIENT ID** value to a safe place. In the **CLIENT SECRET** field, click **Reset secret**, accept the warning, and copy the secret value to a safe place.

### Note

Every time you reset the token, the existing connections will stop working. You need to reauthenticate the connection with this new token.
5. On the left menu, click **Bot > Add bot**.

![msedge_J8kL5iiqyh.png](./../image/uuid-4fd00a33-4ca9-c1ad-524b-8043d749ad89.png)
6. Optional: Change the default name of the bot.
7. Optional: Enable the **Privileged Gateway Intent** settings if you want to receive full message content from all the modules.

![image.png](./../image/uuid-0cb64d6c-f69e-37b6-794f-8e37be8bdb13.png)
8. Click **Reset** to generate the bot token, accept the alert, and copy the bot token to a safe place as you can see the token only once.

![msedge_IXr5vOrP4p.png](./../image/uuid-aef6931f-c35b-5530-e4fc-9cd1449ca78c.png)### Note

Every time you reset the token, the existing connections will stop working. You need to reauthenticate the connection with this new token.
9. Log in to your Make, add a module from the Discord app, click **Add** next to the **Connection** field, and click **Show Advanced Settings**.

![msedge_fgmC2YC6lK.gif](./../image/uuid-833d2a7e-019c-2dde-ceb4-ba04ff9ce511.gif)
10. Optional: In the **Connection name** field, enter a name for the connection.
11. In the **Bot Token** field, enter the token copied in step 7.
12. In the **Client ID** and **Client Secret** fields, enter the values copied in step 4 in the respective fields, select the bot permissions, and click **Save**.
13. Select the server to which you connect.

![msedge_GEJmoRDuh7.png](./../image/uuid-5418b471-f3af-9c8f-bb8b-4ca828b697ae.png)
14. Confirm the access by clicking **Authorise**.

![msedge_It32ptRGOe.png](./../image/uuid-e3c1787d-b1b1-56e4-4065-7ce02a7209b9.png)

You have successfully the Discord bot to Make and can now access messages content.

[Messages
--------](#messages-964586_body)You can watch, list, retrieve, send, edit, and delete messages with the following modules.

[### Watch Channel Messages](#watch-channel-messages_body)Triggers when a new message is posted to the channel.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose message you want to watch. |
| **Limit** | The maximum number of channel messages Make should return during one scenario execution cycle. |

[### List Channel Messages](#list-channel-messages_body)Returns the message for the channel.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose messages you want to list. |
| **Limit** | The maximum number of messages Make should return during one scenario execution cycle. The default value is 10. |
| **Before** | Enter the User ID to list the channel messages before this user ID. |

[### Get a Message](#get-a-message-964586_body)Returns a specific message in the channel.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose messages you want to retrieve. |
| **Message ID** | Select the Message ID whose details you want to retrieve. |

[### Send a Message](#send-a-message-964586_body)Sends a message to a specified channel, thread, or guild member.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Choose a Method** | Select a method:* *Send a Message to a Channel* * *Send a Message to a Thread* * *Send a DM (Direct Message) to a Guild Member* |
| **Channel ID** | Select the Channel ID to send a message. |
| **Message** | Enter the message you want to send. |
| **Is TTS message** | Select whether the message is a TTS message. |
| **Embeds** | Enter the details of embedded objects:  | **Title** | Enter Embed's title. | | --- | --- | | **Type** | Enter the Embed's type. For example, `rich, image, video, image, article, and link`. | | **Description** | Enter the embed's description. | | **URL** | Enter the embed's URL address. | | **Timestamp** | Enter the embed's timestamp in ISO8601 format. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). | | **Color** | Enter the embed's color code. |  For field descriptions, see the [Discord Messages API reference](https://discord.com/developers/docs/resources/channel#embed-object). |
| **Stickers** | Enter the Sticker ID to be sent along with the message. |
| **Components** | Enter the components you want to send or respond to a slash command or other interaction. For field descriptions, see the [Discord Messages API reference](https://discord.com/developers/docs/interactions/message-components#component-object). |
| **Files** | Enter the file's details:  | **File Name** | Enter the file name, including the extension, for example, `invoice.xml`. | | --- | --- | | **Data** | Enter the file's data. | |
| **Message Reference** | Enter the Message ID if you are replying to a message. |

[### Edit a Message](#edit-a-message_body)Edits a specified message.



| **Connection** | [Establish a connection to your Discord account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Choose a Method** | Select a method:* *Send a Message to a Channel* * *Send a Message to a Thread* * *Send a DM (Direct Message) to a Guild Member* |
| **Channel ID** | Select or map the Channel ID whose message you want to edit. |
| **Message ID** | Select or map the Message ID whose details you want to edit. |
| **Content** | Enter the message contents up to a maximum of 2000 characters. |
| **Flags** | Select a flag for the message. For field descriptions, see the [Discord Message API reference](https://discord.com/developers/docs/resources/channel#message-object-message-flags). |
| **Embeds** | Enter the embeds you want to add to your message. For field descriptions, see the [Discord Message API reference](https://discord.com/developers/docs/resources/channel#message-object-message-flags). |
| **Components** | Enter the components you want to send or respond to a slash command or other interaction. For field descriptions, see the [Discord Messages API reference](https://discord.com/developers/docs/interactions/message-components#component-object). |
| **Files** | Enter the file's details:  | **File Name** | Enter the file name, including the extension, for example, `invoice.xml`. | | --- | --- | | **Data** | Enter the file's data. | |

[### Delete a Message](#delete-a-message-964586_body)Deletes a message.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Enter the Channel ID whose message you want to delete. |
| **Message ID** | Enter the Message ID you want to delete. |

[Channels
--------](#channels-964586_body)You can watch, list, create, update, and delete channels, channel invites, and guild channels.

[### Watch Channel Invites](#watch-channel-invites_body)Triggers when a new channel invite is created.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose channel invites you want to watch. |
| **Limit** | The maximum number of channel invites Make should return during one scenario execution cycle. The default value is 2. |

[### List Channel Invites](#list-channel-invites_body)Returns a list of invites (with invite metadata) for the channel.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose channel invite you want to list. |
| **Limit** | The maximum number of channel invites Make should return during one scenario execution cycle. The default value is 10. |

[### List Channels](#list-channels-964586_body)Returns a list of bot's channels.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Limit** | The maximum number of channels Make should return during one scenario execution cycle. The default value is 10. |
| **List root channels too** | Select whether to list root channels. |

[### Create a Guild Channel](#create-a-guild-channel_body)Creates a new channel for the guild.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Name** | Enter a name for the guild channel. |
| **Type** | Select the type of guild channel:* *Guild text* * *DM* * *Guild voice* * *Guild DM* * *Guild Category* * *Guild News* * *Guild store* |
| **Topic** | Enter the topic name for the guild channel. |
| **Position** | Enter the sorting position of the guild channel. |
| **Rate Limit Per User** | Enter the number of seconds the user has to wait before sending the next message in the guild channel. |
| **Parent ID** | Select the Parent ID of the guild channel:* *Text Channel* * *Voice Channel* |
| **NSFW Channel** | Select *Yes* if this guild channel is NSFW (Not Suitable For Wumpus).* *Yes* * *No* * *Not defined* For more information on NSFW, see [NSFW Channels and Content](https://support.discordapp.com/hc/en-us/articles/115000084051-NSFW-channels-and-content). |
| **Permission Overwrites** | Add the permission overwrites for the channel:* **Role ID** Select the Role ID of the user. * **Allow permission bit set** Enter the number of permission bit set to allow. * **Deny permission bit set** Enter the number of permission bit set to deny. |

[### Create a Channel Thread](#create-a-channel-thread_body)Creates a new channel thread.



| **Connection** | [Establish a connection to your Discord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Choose a Method** | Select a method:* *Create a Thread from Message* * *Create a Thread without Message* |
| **Channel ID** | Select the Channel ID whose thread you want to create. |
| **Message ID** | Select the Message ID whose thread you want to create. |
| **Name** | Enter a name for the channel thread. |
| **Auto Archive Duration** | Select the duration to stop the thread from showing in the channel list:* *60 Minutes* * *1440 Minutes* * *4320 Minutes* * *10080 Minutes* |
| **Rate Limit per User** | Enter the number of seconds the user has to wait before sending the next message in the guild channel. |

[### Create a Channel Invite](#create-a-channel-invite_body)Creates a new invite for the channel. It works only with a connection that has permission to manage invites.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose invite you want to create. |
| **Max age in Seconds** | Enter the maximum duration after which the invite expires.Enter the duration of the invite in seconds before expiry, or 0 for never. Note: 86400 is 24 hours. |
| **Max uses** | Enter the maximum number of times the channel invite can be used.Enter Zero for unlimited. |
| **Is temporary?** | Select if this channel invite gives a temporary membership. |
| **Is unique?** | Select if this channel invite can be used only once. If selected, you cannot create a similar channel invite. |

[### Update a Channel](#update-a-channel_body)Updates a channel's settings.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Enter the Channel ID you want to modify. |
| **Name** | Enter a new name for the channel. |
| **Type** | Select the channel type.NoteOnly conversion between text and news is supported and only in guilds with the 'NEWS' feature. |
| **Topic** | Enter a topic for the channel. |
| **Position** | Enter the channel sorting position of the guild channel. |
| **Rate Limit per User** | Enter the time in seconds a user has to wait before sending another message (0-21600). |
| **Parent ID** | Select the Parent ID of the guild channel:* *Text Channel* * *Voice Channel* |
| **NSFW Channel** | Select *Yes* if this guild channel is NSFW (Not Suitable For Wumpus).* *Yes* * *No* * *Not defined* For more information on NSFW, see [NSFW Channels and Content](https://support.discordapp.com/hc/en-us/articles/115000084051-NSFW-channels-and-content). |
| **Permission Overwrites** | Add the permissions for members to overwrite:**Role ID**Select the role or members to whom you want to assign the permission.**Allow Permission Bit Set**Enter the permission allowed in a bit set.**Deny Permission Bit Set**Enter the permission denied in a bit set. |
| **Bitrate** | Enter the bitrate (in bits) if this is a voice channel. |
| **User Limit** | Enter the maximum number of users you can add to the channel. |

[### Delete a Channel](#delete-a-channel-964586_body)Deletes a channel.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel** | Select the Channel ID you want to delete. |

[Reactions
---------](#reactions-964586_body)You can post a reaction with emojis with the following module.

[### Post a Reaction with an Emoji](#post-a-reaction-with-an-emoji_body)Post a reaction for the message with an emoji.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID where you want to post a reaction with an emoji. |
| **Message ID** | Enter the Message ID that you want to post a reaction with an emoji. |
| **Emoji** | Enter the emoji to post as a reaction to the message. |

[Member
------](#member-964586_body)You can watch, search, list and update guild members and add or remove roles from guild members with the following modules.

[### Watch Guild Members](#watch-guild-members_body)Triggers when a member has joined the bot's guild.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Limit** | The maximum number of guild members Make should return during one scenario execution cycle. The default value is 2. |

[### Search Guild Members](#search-guild-members_body)Searches for Guild Members.



| **Connection** | [Establish a connection to your Discord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Query** | Enter a username or a nickname to return the guild members. |
| **Limit** | The maximum number of guild members Make should return during one scenario execution cycle. The default value is 10. |

[### List Guild Members](#list-guild-members_body)Returns a list of members that are members of the bot's guild.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **After** | Enter the User ID to list the guild member after this ID. |
| **Limit** | The maximum number of Guild Members Make should return during one scenario execution cycle. |

[### List Guild Members with Reactions on Message](#list-guild-members-with-reactions-on-message_body)Returns a list of guide member that reacted with the emoji on the message.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Choose a Method** | Select a Method:* *Get a Message from a Channel* * *Get a Message from a Thread* * *Get a DM (Direct Message) from a Guild Member* |
| **Channel ID** | Select the Channel ID whose users reacted with an emoji you want to list. |
| **Message ID** | Select the Message ID that has the reaction with an emoji that you want to list the users of. |
| **Guild Member** | Enter the Guild member whose reaction to the message you want to list. Alternatively, you can search for guild members.  | **Query** | Enter a username or nickname to list the guild members with the string. | | --- | --- | | **Limit** | The maximum number of guild members Make: Product name should return during one Make: scenario execution cycle. The default value is 10. | |
| **Emoji** | Select the emoji you want to list. |
| **Limit** | The maximum number of users Make should return during one scenario execution cycle. |

[### Update a Guild Member](#update-a-guild-member_body)Updates an existing guild member.



| **Connection** | [Establish a connection to your Discord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Guild Member ID** | Enter the Guild Member ID whose details you want to update. Alternatively, you can search for a guild member.  | **Query** | Enter a username or a nickname to list the guild members with the string. | | --- | --- | | **Limit** | The maximum number of guild members Make should return during one Make execution cycle. The default value is 10. | |
| **Nickname** | Enter a nickname for the guild member. |
| **Role IDs** | Select the Role ID to assign them to the guild member. |
| **Is Mute** | Select whether the user is muted in voice channels. |
| **Is Deaf** | Select whether the user is deafened in voice channels. |
| **Channel ID** | Select the Channel ID to move the user. |
| **Communication Disabled Until** | Enter the timeout, after which the user can communicate in the guild again (up to 28 days in the future), and set it to null to remove the timeout. |

[### Add a Role to a Guild Member](#add-a-role-to-a-guild-member_body)Adds a Role to a Guild Member.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **User ID** | Select the User ID whose role you want to add to a guild member. |
| **Role ID** | Select the Role ID of the user you want to add. |

[### Remove a Role from a Guild Member](#remove-a-role-from-a-guild-member_body)Removes a role from a guild member,



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **User ID** | Select the User ID whose role you want to remove from a guild member. |
| **Role ID** | Select the Role ID of the user you want to remove. |

Event
-----

You can create, update, list, retrieve, and delete guild events with the following modules.

[### List Guild Events](#list-guild-events_body)Retrieves a list of scheduled events for guild.



| **Connection** | [Establish a connection to your DIscord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Include number of users subscribed to each event** | Select whether to list the users subscribed to each event. |
| **Limit** | The maximum number of guild members Make should return during one scenario execution cycle. The default value is 10. |

[### Get a Guild Event](#get-a-guild-event_body)Gets a specified guild event.



| **Connection** | [Establish a connection to your DIscord App account](discord.html#connect-discord-to-make "Connect Discord to Make") |
| --- | --- |
| **Guild Event ID** | Select or map the Guild Event ID whose details you want to retrieve. |
| **Include number of users subscribed to each event** | Select whether to retrieve the users subscribed to each event. |

[### Create a Guild Event](#create-a-guild-event_body)Creates a new guild event.



| **Connection** | [Establish a connection to your DIscord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Event Name** | Enter a name for the event. |
| **Entity Type** | Select the entity type:* *Stage Instance* * *Voice* * *External* |
| **Location** | Enter the event's location. This field is required if the event type is `External`. |
| **Channel ID** | Enter the Channel ID whose event you want to create. This field is required if the event type is `Stage Instance` or `Voice`. |
| **Start Time** | Enter a time when the event is scheduled to start in ISO8601 format. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **End Time** | Enter a time when the event is scheduled to end in ISO8601 format. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Description** | Enter a description for the event. |
| **File** | Enter the file's details:  | **Image File Name** | Enter the file name, including its extension. For example, `invoice.xml`. | | --- | --- | | **Image Data** | Enter the image data. | |

[### Update a Guild Event](#update-a-guild-event_body)Updates an existing guild event.



| **Connection** | [Establish a connection to your DIscord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Guild Event ID** | Select or map the Guild Event ID whose details you want to update. |
| **Event Name** | Enter a name for the event. |
| **Entity Type** | Select the entity type:* Stage * *InstanceVoice* * *External* |
| **Location** | Enter the event's location. This field is required if the event type is `External`. |
| **Channel ID** | Enter the Channel ID whose event you want to create. This field is required if the event type is  `Stage Instance` or `Voice` . |
| **Start Time** | Enter a time when the event is scheduled to start in ISO8601 format. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **End Time** | Enter a time when the event is scheduled to end in ISO8601 format. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Description** | Enter a description for the event. |
| **File** | Enter the file's details:  | **Image File Name** | Enter the file name, including its extension. For example,  `invoice.xml`. | | --- | --- | | **Image Data** | Enter the image data. | |

[### Delete a Guild Event](#delete-a-guild-event_body)Deletes a guild event.



| **Connection** | [Establish a connection to your DIscord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Guild Event ID** | Select or map the Guild Event ID you want to delete. |

Webhooks
--------

You can create, send messages, and delete webhook bots with the following modules.

[### Create a Webhook Bot](#create-a-webhook-bot_body)Creates a new webhook.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose webhook you want to create. |
| **Name** | Enter a name for the webhook bot. |

[### Send a Message by Webhook Bot](#send-a-message-by-webhook-bot_body)Sends a new message by executing a (custom) webhook bot.



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Channel ID** | Select the Channel ID whose webhook you want to execute. |
| **Name** | Enter the webhook name you want to execute. |

[### Delete a Webhook Bot](#delete-a-webhook-bot_body)Deletes a webhook permanently



| **Connection** | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| **Webhook ID** | Enter the Webhook ID you want to delete. |

Other
-----

You can update current bots and call APIs with the following modules.

[### Update a Current Bot](#update-a-current-bot_body)Updates a current and connected user's bot.



| **Connection** | [Establish a connection to your Discord App account](discord.html#connect-discord-to-make "Connect Discord to Make"). |
| --- | --- |
| **Bot Name** | Enter a name for the bot. |
| **File** | Enter the bot image data. |

[### Make an API Call](#make-an-api-call-964586_body)Performs an arbitrary authorized API call to manage data in Discord.



| Connection | [Establish a connection to your Discord App account.](discord.html#connect-discord-to-make-using-oauth2 "Connect Discord to Make using OAuth2") |
| --- | --- |
| URL | Enter a path relative to `https://discordapp.com/api.`NoteFor the list of available endpoints, refer to the [Discord API Documentation](https://discordapp.com/developers/docs/reference) |
| Method | Select the HTTP method you want to use:GETto retrieve information for an entry.POSTto create a new entry.PUTto update/replace an existing entry.PATCHto make a partial entry update.DELETEto delete an entry. |
| Headers | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| Query String | Enter the request query string. |
| Body Type | Select the method in which you want to map the body content. |
| Body | Enter the body content for your API call. |

#### Example of Use - Get User

The following API call returns all the information about the selected user:

URL:

`/users/@me`

Method:

`GET`

![Discord_make_api_call.png](./../image/uuid-646f6e64-721f-6610-8dc2-98e4fbd540d7.png)Matches of the search can be found in the module's **Output** under Bundle > Body.

In our example, the details of the user were returned:

![Discord_api_results_bundle.png](./../image/uuid-5c32fddb-e6a1-0f44-605c-e09b631d8a74.png)