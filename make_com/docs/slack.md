Slack
=====

With Slack modules in Make, you can create, update, delete, retrieve, watch, and/or search for messages, files, channels, reactions, users, reminders, and/or statuses.

To get started with Slack, create an account at [slack.com/getting-started](https://slack.com/get-started).

Refer to the [Slack API documentation](https://api.slack.com/docs) for the list of available endpoints.



| **Slack Terminology** | |
| --- | --- |
| **DM** | Direct Message |
| **IM** | Instant Message |
| **Private Channel** | formerly *Group* |
| **Direct Message** | formerly *IM* |
| **Channel** | Referred to as *Conversation* in the API documentation and *Channel* in the Slack application |

Connect Slack to Make
---------------------

To establish the connection:

1. Log in to your Make account, add a Slack module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Depending on the module you add, you may be prompted to choose the **Connection type**: **Slack (user)** or **Slack (bot)**. If not, continue to step 4.

### Note

Slack **Watch** modules only function with **User** connections at this time. If you would like to create a webhook with an interactive bot, you must use the [Custom Webhook](./../tools/webhooks.html#creating-custom-webhooks "Creating custom webhooks") module.
3. Optional: In the **Connection name** field, enter a name for the connection.
4. Optional: Click **Show Advanced settings** and enter your custom app client credentials or add additional scopes.

To create client credentials, see the [Create Custom App and Client Credentials in Slack](slack.html#create-custom-app-and-client-credentials-in-slack "Create Custom App and Client Credentials in Slack") section.
5. Click **Save**.
6. If prompted, authenticate your account. If your account has multiple Slack workspaces, select the relevant workspace in the top-right corner and grant access to Make.

You have successfully established the connection. You can now edit your scenario and add more Slack modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Note: Some modules may require additional permissions extension. If so, you will be asked to authorize the required permissions.

Create Custom App and Client Credentials in Slack
-------------------------------------------------

To create a custom app and client credentials:

1. Log in to your Slack account and go to the [Your Apps page](https://api.slack.com/apps).
2. Click **Create New App**.
3. Select **From scratch**.
4. Enter a name for your app, select a workspace, and click **Create App**. This brings you to the **Basic Information** page of your new app.
5. Scroll down to the **App Credentials** section. Copy your **Client ID** and store it in a safe place.
6. In the **Client Secret** field, click **Show**, copy your secret, and store it in a safe place.
7. In the left sidebar, click **OAuth & Permissions**.
8. Scroll down to the **Redirect URLs** section, click **Add New Redirect URL**, enter the redirect URL listed below for **User** and/or **Bot**, and click **Add** > **Save URLs**.



| Connection Type | Redirect URL |
| --- | --- |
| **User** | `https://www.integromat.com/oauth/cb/slack2` |
| **Bot** | `https://www.integromat.com/oauth/cb/slack3` |
9. In the **Scopes** section, add **Bot Token Scopes** or **User Token Scopes**. You can add scopes for both types to one custom app.
10. Click **Add an OAuth Scope** and select scopes in the dropdown menu. Repeat this for all desired scopes.

Note: If you change permission scopes in your Slack app after creation, you will be prompted in the Slack My Apps pages to reinstall your app.

You now have the client credentials to connect to Make.

Messages
--------

You can watch public and private channel messages, watch direct and multiparty direct messages, watch scheduled messages, search for messages, list scheduled messages, retrieve private and public channel messages, list replies, create, update, schedule, and delete a message using the following modules.

[### Watch Public Channel Messages](#watch-public-channel-messages_body)Triggers when a new message is added to a public channel.



| **Connection** | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **Public Channel** | Select or map a public channel whose messages you want to watch. |
| **Public Channel** | Enter (map) a public channel name whose messages you want to watch. |
| **Limit** | Set the maximum number of public channel messages Make will return during one execution cycle. The default value is 2. |

[### Watch Private Channel Messages](#watch-private-channel-messages_body)Triggers when a new message is added to a private channel.



| **Connection** | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **Private Channel** | Select or map a private channel whose messages you want to watch. |
| **Private Channel** | Enter (map) a private channel name whose messages you want to watch. |
| **Limit** | Set the maximum number of private channel messages Make will return during one execution cycle. The default value is 2. |

[### Watch Direct Messages](#watch-direct-messages_body)Triggers when a new direct message is added to a direct message channel.



| **Connection** | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **IM Channel** | Select or map an IM channel whose direct messages you want to watch. |
| **IM Channel** | Enter (map) an IM channel name whose direct messages you want to watch. Alternatively, you can search for an IM channel.  | Name | Enter (map) a name to search for a multiparty IM channel. | | --- | --- | | Exclude Archived | Select whether to exclude the archived channels. | |
| **Limit** | Set the maximum number of direct messages Make will return during one execution cycle. The default value is 2. |

[### Watch Multiparty Direct Messages](#watch-multiparty-direct-messages_body)Triggers when a new message is added to a multiparty direct message channel.



| Connection | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| Input Method | Select the input method:* *Select from a list* * *Search by the name* |
| Multiparty IM Channel | Select or map a multiparty IM channel whose direct messages you want to watch. |
| Multiparty IM Channel | Enter (map) a multiparty IM channel name whose direct messages you want to watch. Alternatively, you can search for a multiparty IM channel.  | Name | Enter (map) a name to search for a multiparty IM channel. | | --- | --- | | Exclude Archived | Select whether to exclude the archived channels. | |
| Limit | Set the maximum number of multiparty direct messages Make name will return during one execution cycle. The default value is 2. |

[### Search for Message](#search-for-message_body)Returns messages matching a search query.



| Connection | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| Query | Enter the search term you want to search the workspace for. See [Search in Slack](https://get.slack.help/hc/en-us/articles/202528808-Search-in-Slack) for a list of Search modifiers. |
| Limit | Set the maximum number of messages Make will return during one execution cycle. The default value is 2. |
| Sort by | Select a parameter to sort:* *Score* * *Timestamp* |
| Direction | Select the sorting direction:* *Ascending* * *Descending* |

[### Get a Private Channel Message](#get-a-private-channel-message_body)Returns a message with a given ID from a specified private channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **Private Channel** | Select or map a private channel whose messages you want to retrieve. |
| **Private Channel** | Enter (map) a private channel name whose messages you want to retrieve. Alternatively, you can search for a public channel.  | **Name** | Enter (map) the channel name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Message ID (timestamp)** | Enter (map) a Message ID of a message to retrieve. |

[### Get a Public Channel Message](#get-a-public-channel-message_body)Returns a message with a given ID from a specified public channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Input Method** | Select the input method:* *Select from a list* * *Select from a list* |
| **Public Channel** | Select or map a public channel whose messages you want to retrieve. |
| **Public Channel** | Enter (map) a public channel name whose messages you want to retrieve. Alternatively, you can search for a public channel.  | **Name** | Enter (map) the channel name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Message ID (timestamp)** | Enter (map) a Message ID of a message to retrieve. |

[### List Replies](#list-replies_body)Retrieves a thread messages posted to a conversation.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel whose message you want to create. |
| **Private channel** | Select or map a private channel whose message you want to create. |
| **IM channel** | Select or map a user whose message you want to create. |
| **Multiple IM channel** | Select or map a multiple IM channel whose message you want to create. |
| **Parent message ID (timestamp)** | Enter (map) a Parent message ID of a message whose replies you want to list. |
| **Limit** | Set the maximum number of replies Make will return during one execution cycle. The default value is 2. |

[### Create a Message](#create-a-message-964634_body)Creates a new message.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Enter a channel ID or name** | Select the input method:* *Enter manually* * *Select from the list* |
| **Channel ID or name** | Enter (map) a Channel ID or name whose message you want to create.NoteYou must specify a public channel, private channel, or an IM channel. You can either pass the channel's name (#general) or encoded ID (C0123BE12L). |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel whose message you want to create. |
| **Private channel** | Select or map a private channel whose message you want to create. |
| **IM channel** | Select or map an IM channel whose message you want to create. |
| **Multiple IM channel** | Select or map a multiple IM channel whose message you want to create. |
| **Text** | Enter (map) the text content of the message you want to create.For detailed information about text formatting, please refer to the [Slack documentation](https://api.slack.com/reference/). |
| **Blocks** | Enter (map) the blocks to be combined with messages to create visually rich and compellingly interactive messages.For detailed information about text formatting, please refer to the [Slack documentation](https://api.slack.com/reference/block-kit/blocks). |
| **Thread message ID (timestamp)** | Enter (map) another message's time stamp value to make this message a reply. Avoid using a reply's time stamp value; use its parent instead. |
| **Reply broadcast** | Select whether they should be made visible to everyone in the channel or conversation.NoteUsed in conjunction with the Thread message ID. |
| **Link names** | Names and channels will not be linkified in the @username or #channel format unless you enable this option. For more information, refer to the [formatting spec](https://api.slack.com/docs/formatting). |
| **Parse message text** | Select whether to parse the message text.NoteDefines how messages are treated. |
| **Use markdown** | Disable Slack markup parsing by selecting the No option. |
| **Unfurl primarily text-based content** | Enable this option to enable the unfurling of primarily text-based content. For detailed information about unfurling in Slack, refer to the [Unfurling links in the messages](https://api.slack.com/docs/message-link-unfurling) article. |
| **Unfurl media content** | Disable this option to disable the unfurling of media content. For detailed information about unfurling in Slack, please refer to the [Unfurling links in the messages](https://api.slack.com/docs/message-link-unfurling) article. |
| **Icon emoji** | Enter (map) an emoji to use as the icon for this message. Overrides Icon URL.NoteThis field only has an effect when using a Bot connection. |
| **Icon url** | Enter (map) an Icon URL to an image to use as the icon for this message.NoteThis field only has an effect when using a Bot connection. |
| **User name** | Enter (map) a User name to create a message.NoteIf not specified, the default bot name will be used. This field only has an effect when using a Bot connection. |

[### Update a Message](#update-a-message-964634_body)Updates a message.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Enter a channel ID or name** | Select the input method:* *Enter manually* * *Select from the list* |
| **Channel ID or name** | Enter (map) an updated Channel ID or name whose message you want to create.NoteYou must specify a public channel, private channel, or an IM channel. You can either pass the channel's name (#general) or encoded ID (C0123BE12L). |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel whose message you want to create. |
| **Private channel** | Select or map a private channel whose message you want to create. |
| **IM channel** | Select or map an IM channel whose message you want to create. |
| **Multiple IM channel** | Select or map a multiple IM channel whose message you want to create. |
| **Timestamp (Message ID)** | Enter (map) the message's time stamp value or the Message ID to whose text you want to update. |
| **Text** | Enter (map) the text content of the message you want to create.NoteFor detailed information about text formatting, please refer to the [Slack documentation](https://api.slack.com/reference/). |
| **Blocks** | Enter (map) the blocks to be combined with messages to create visually rich and compellingly interactive messages.NoteFor detailed information about text formatting, please refer to the [Slack documentation](https://api.slack.com/reference/block-kit/blocks). |
| **Link names** | Names and channels will not be linkified in the @username or #channel format unless you enable this option. For more information, refer to the [formatting spec](https://api.slack.com/docs/formatting). |
| **Parse message text** | Select whether to parse the message text.NoteDefines how messages are treated. |

[### Delete a Message](#delete-a-message-964634_body)Removes a message.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) a Channel ID of a channel whose messages you want to delete. |
| **Message ID (timestamp)** | Enter (map) a Message ID of a message to delete. |

Files
-----

You can watch, list, retrieve, download, upload, create and delete the files using the following modules.

[### Watch Files](#watch-files-964634_body)Triggers when a new file is added.



| **Connection** | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Type** | Select the file type you want to watch for:* *Posts* * *Snippets* * *Google docs* * *Images* * *Zips* * *Pdfs* |
| **Channel type** | Select the channel to filter the files from:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel to watch the files. |
| **Private channel** | Select or map a private channel to watch the files. |
| **User** | Select or map a user to watch the files. |
| **Multiple IM channel** | Select or map a multiple IM channel to watch the files. |
| **Created by** | Filter files to those created by the selected user. |
| **Limit** | Set the maximum number of files Make will return during one execution cycle. The default value is 2. |

[### List Files](#list-files-964634_body)Returns a list of files within a team.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Type** | Select the file type you want to retrieve:* *Posts* * *Snippets* * *Google* * *docs* * *Images* * *Zips* * *Pdfs* |
| **Channel type** | Select the channel to filter the files from:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel to watch the files. |
| **Private channel** | Select or map a private channel to watch the files. |
| **User** | Select or map a user to watch the files. |
| **Multiple IM channel** | Select or map a multiple IM channel to watch the files. |
| **Created by** | Filter files created by the selected user. |
| **Date from** | Set the start date you want to list files from. |
| **Date to** | Set the end date you want to list files until. |
| **Limit** | Set the maximum number of files Make will return during one execution cycle. The default value is 2. |

[### Get a File](#get-a-file-964634_body)Returns details about a file.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **File ID** | Enter (map) the ID of the file you want to retrieve details about. |

[### Download a File](#download-a-file-964634_body)Downloads a file.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **URL private download** | Enter (map) the URL Private download value from the Get a File module. |

[### Upload a File](#upload-a-file-964634_body)Creates or uploads a file.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channels** | Enter (map) the channel's details:  | **Channel type** | Select the channel where you want to upload the file:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* | | --- | --- | | **Public channel** | Select or map a public channel to upload a file. | | **Private channel** | Select or map a private channel to upload a file. | | **User** | Select or map a user to upload a file. | | **Multiple IM channel** | Select or map a multiple IM channel to upload a file. | |
| **File** | Enter (map) a file details:  | **File name** | Enter (map) the file name. | | --- | --- | | **Data** | Enter (map) the file data. | |
| **Title** | Enter (map) the title of the file. |
| **Thread ID (timestamp)** | Enter (map) the Thread ID to upload the file as a reply. |
| **Initial comment** | Enter (map) the message text introducing the file in the specified channel. |

[### Create a Text File](#create-a-text-file_body)Creates a text file.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channels** | Enter (map) the channel's details:  | **Channel type** | Select the channel where you want to upload the file:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* | | --- | --- | | **Public channel** | Select or map a public channel to create a file. | | **Private channel** | Select or map a private channel to create a file. | | **User** | Select or map a user to create a file. | | **Multiple IM channel** | Select or map a multiple IM channel to create a file. | |
| **File** | Enter (map) a file details:  | **File name** | Enter (map) the file name. | | --- | --- | | **Content** | Enter (map) the file data. | |
| **Title** | Enter (map) the title of the file. |
| **Thread ID (timestamp)** | Enter (map) the Thread ID to create the file as a reply. |
| **Initial comment** | Enter (map) the message text introducing the file in the specified channel. |

[### Delete a File](#delete-a-file-964634_body)Deletes a file.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **File ID** | Enter (map) the ID of the file you want to delete. |

Channels
--------

You can list, retrieve, list members, set the topic, set the purpose, join a channel, leave a channel, create, archive, and unarchive a channel using this module.

[### List Channels](#list-channels-964634_body)Returns a list of channels in a workspace.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Exclude archived** | Select whether to exclude archived channels in the results. |
| **Type** | Select the type of channels you want to retrieve.* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Limit** | Set the maximum number of channels Make will return during one execution cycle. The default value is 2. |
| **Next Cursor** | Set the cursor parameter equal to the next\_cursor value you received on the last request to retrieve the next portion of the collection. For information see the [cursor based pagination](https://api.slack.com/docs/pagination#cursors). |

[### Get a Channel](#get-a-channel-964634_body)Returns details about a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) the channel ID of the channel you want to retrieve. |

[### List Members in Channel](#list-members-in-channel_body)Returns users in the selected Channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* |
| **Public channel** | Select or map a public channel whose members you want to list. |
| **Private channel** | Select or map a private channel whose members you want to list. |
| **Limit** | Set the maximum number of members Make will return during one execution cycle. The default value is 2. |

[### Set the Topic of a Channel](#set-the-topic-of-a-channel_body)Changes the topic of a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **Public Channel** | Select or map a public channel whose topic you want to set. |
| **Private Channel** | Select or map a private channel whose topic you want to set. |
| **IM channel** | Select or map an IM channel whose topic you want to set. |
| **Multiparty IM Channel** | Select or map a multiparty IM channel whose topic you want to set. |
| **Public Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Private Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **IM channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Multiparty IM Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Topic** | Enter (map) the topic name for the channel. Does not support formatting or linkification. For example, `Apply topically for best effects`. |

[### Set the Purpose of a Channel](#set-the-purpose-of-a-channel_body)Changes the purpose of a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Input Method** | Select the input method:* *Select from a list* * *Search by the name* |
| **Public Channel** | Select or map a public channel whose topic you want to set. |
| **Private Channel** | Select or map a private channel whose topic you want to set. |
| **IM channel** | Select or map an IM channel whose topic you want to set. |
| **Multiparty IM Channel** | Select or map a multiparty IM channel whose topic you want to set. |
| **Public Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Private Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **IM channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Multiparty IM Channel** | Enter (map) a public channel whose topic you want to set. Alternatively, you can search a channel:  | **Name** | Enter (map) a name to search. | | --- | --- | | **Exclude Archived** | Select whether to exclude the archived channels. | |
| **Purpose** | Enter (map) the new special purpose for the channel. For example, `My More Special Purpose`. |

[### Join a Channel](#join-a-channel_body)Joints to an existing channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) the Channel ID of a channel you want to join. |

[### Leave a Channel](#leave-a-channel_body)Leaves a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) the Channel ID of a channel you want to leave. |

[### Create a Channel](#create-a-channel-964634_body)Creates a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Name** | Enter (map) the name of the public or private channel to create. |
| **Is private** | Select whether the channel is private. |

[### Archive a Channel](#archive-a-channel_body)Archives a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) the channel ID of the channel you want to archive. |

[### Unarchive a Channel](#unarchive-a-channel_body)Unarchives a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel ID** | Enter (map) the channel ID of the channel you want to unarchive. |

Reactions
---------

You can list, add, and remove a reaction using the following modules.

[### List Reactions](#list-reactions_body)Returns reactions a user made.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **User** | Select or map a user whose reactions you want to list. |
| **Limit** | Set the maximum number of reactions Make should return during one execution cycle. The default value is 2. |

[### Add a Reaction](#add-a-reaction_body)Adds a reaction to an item.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel to whose message you want to add a reaction. For example, `C1234567890`. |
| **Private channel** | Select or map a private channel to whose message you want to add a reaction. For example, `C1234567894`. |
| **User** | Select or map a user to whose message you want to add a reaction. |
| **Multiple IM channel** | Select or map a multiple IM channel to whose message you want to add a reaction. |
| **Message ID (timestamp)** | Enter (map) the Message ID or a timestamp of the message to add a reaction. For example, `1234567890.123456`. |
| **Reaction (emoji) name** | Enter (map) the Reaction (emoji) name. For example, `thumbsup`. |

[### Remove a Reaction](#remove-a-reaction_body)Removes a reaction.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel to whose message you want to remove a reaction. For example, `C1234567890`. |
| **Private channel** | Select or map a private channel to whose message you want to remove a reaction. For example, `C12345678904`. |
| **User** | Select or map a user to whose message you want to remove a reaction. |
| **Multiple IM channel** | Select or map a multiple IM channel to whose message you want to remove a reaction. |
| **Message ID (timestamp)** | Enter (map) the Message ID or a timestamp of the message to add a reaction. For example, `1234567890.123456`. |
| **Reaction (emoji) name** | Enter (map) the Reaction (emoji) name. For example, `thumbsup`. |

Stars
-----

You can add and remove stars using the following modules.

[### Add a Star](#add-a-star_body)Adds a star to a channel, message, file, or a file comment.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Add a star to** | Select whether you want to add a star to a channel, file, or file comment. |
| **Channel/File ID/File comment ID** | Enter respective IDs. You can star a message by selecting a *Channel* and entering the message *timestamp*. |

[### Remove a Star](#remove-a-star_body)Removes a star from the channel, message, file, or a file comment.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Add a star to** | Select whether you want to remove the star from a channel, file, or file comment. |
| **Channel/File ID/File comment ID** | Enter respective IDs of the objects you want to remove the star from. You can remove a star from the message by selecting a *Channel* and entering the message *timestamp*. |

Saved Items
-----------

You can save an item and remove the saved item using the following modules.

[### Save an Item](#save-an-item_body)Adds an Item to saved items.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Message ID (timestamp)** | Enter (map) a Message ID of a message whose item you want to save. |
| **File ID** | Enter (map) a File ID of a file to save. |

[### Remove Saved Item](#remove-saved-item_body)Removes a saved item.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Message ID (timestamp)** | Enter (map) a Message ID of a message whose item you want to remove. |
| **File ID** | Enter (map) a File ID of a file to remove. |

Pins
----

You can pin and unpin a message using the following modules.

[### Pin a Message](#pin-a-message-964634_body)Pins a message to a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel whose message you want to pin. |
| **Private channel** | Select or map a private channel whose message you want to pin. |
| **User** | Select or map a user whose message you want to pin. |
| **Multiple IM channel** | Select or map a multiple IM channel whose message you want to pin. |
| **Message ID (timestamp)** | Enter (map) the timestamp of the message to pin. For example, `1234567890.123456`. |

[### Unpin a Message](#unpin-a-message-964634_body)Unpins a message from a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* * *IM channel* * *Multiple IM channel* |
| **Public channel** | Select or map a public channel whose message you want to unpin. |
| **Private channel** | Select or map a private channel whose message you want to unpin. |
| **User** | Select or map a user whose message you want to unpin. |
| **Multiple IM channel** | Select or map a multiple IM channel whose message you want to unpin. |
| **Message ID (timestamp)** | Enter (map) the timestamp of the message to unpin. For example, `1234567890.123456`. |

Users
-----

You can watch, search, list, retrieve, invite and kick a user using the following modules.

[### Watch Users](#watch-users-964634_body)Triggers when a new user is added or an existing user has changed. Only emit the latest change since the last scenario run.



| **Connection** | [Establish a connection to your Slack user account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Limit** | Set the maximum number of users Make will return during one execution cycle. The default value is 2. |

When setting the schedule to run your Watch Slack Users scenario, the **Advanced Scheduling** option to choose a **Start Date** is restricted to Slack users with a [premium account](https://app.slack.com/plans/T042JM9R7).

![slack_schedulesettings.png](./../image/uuid-be079fef-d2dd-93ce-ac6e-32167003c128.png)[### Search for User](#search-for-user_body)Retrieves a single user by looking them up by their registered email address.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Email** | Enter the email address of the user you want to search for. |

[### List Users](#list-users-964634_body)Returns a list of all users in a workspace.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Limit** | Set the maximum number of users Make will return during one cycle. The default value is 2. |

[### Get a User](#get-a-user-964634_body)Returns details about a member to a workspace.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **User ID** | Enter (map) the User ID of the user you want to retrieve information about. |

[### Invite Users](#invite-users_body)Invites 1-30 users to a public or private channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* |
| **Public channel** | Select or map a public channel to add the users. |
| **Private channel** | Select or map a private channel to add the users. |
| **Users** | Select the users you want to add to the channel. |

[### Kick a User](#kick-a-user_body)Removes a user from a channel.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Channel type** | Select the channel type:* *Public channel* * *Private channel* |
| **Public channel** | Select or map a public channel whose user you want to remove. |
| **Private channel** | Select or map a private channel whose user you want to remove. |
| **Users** | Select the user you want to remove from the channel. |

Reminders
---------

You can list, retrieve, create, complete, and delete a reminder using the following modules.

[### List Reminders](#list-reminders-964634_body)Lists all reminders created by or for a given user.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Limit** | Set the maximum number of reminders Make will return during one execution cycle. The default value is 2. |

[### Get a Reminder](#get-a-reminder_body)Returns details about a reminder.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Reminder ID** | Enter (map) the ID of the reminder you want to retrieve information about. For example, `Rm12345678`. |

[### Create a Reminder](#create-a-reminder-964634_body)Creates a reminder.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Text** | Enter (map) the content to appear in the reminder. |
| **Time** | Enter (map) the time when this reminder should happen. Enter the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description. For example, `in 15 minutes` `every Thursday`. |
| **User** | Select or map the user you want to create a reminder for. |

[### Complete a Reminder](#complete-a-reminder_body)Completes a reminder.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Reminder ID** | Enter (map) the ID of the reminder you want to mark as complete. For example, `Rm12345678`. |

[### Delete a Reminder](#delete-a-reminder_body)Removes a reminder.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **Reminder ID** | Enter (map) the ID of the reminder you want to delete. For example, `Rm12345678`. |

Events
------

You can watch new events using the following module.

[### New Event](#new-event-964634_body)Triggers when a new message or other events are created.



| **Webhook name** | Enter (map) a name for the webhook. |
| --- | --- |
| **Event type** | Select the event type:* *New channel message* * *New private channel message* * *New IM message* * *New MP IM message* * *New reaction* * *New file* |
| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| **Channel** | Select or map a channel whose event you want to watch. |

Profile
-------

You can set status in events using the following module.

[### Set a Status](#set-a-status_body)Update a user’s current status.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| Status text | Enter (map) the status text. You can enter up to 100 characters. |
| Status emoji | Enter (map) the status emojis enabled for the slack team. For example, `:train:`. The list of possible emojis can be found in the [Slack Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/). |
| Status expiration | Enter (map) the Unix Timestamp of when the status will expire.NoteProviding `0` or omitting this field results in a custom status that will not expire. |

Other
-----

[### Make an API Call](#make-an-api-call-964634_body)Performs an arbitrary authorized API call.



| **Connection** | [Establish a connection to your Slack account](slack.html#connect-slack-to-make "Connect Slack to Make"). |
| --- | --- |
| **URL** | Enter a path relative to `https://slack.com/api/.` For example: `/list.conversations`NoteFor the list of available endpoints, refer to the [Slack API documentation](https://api.slack.com/). |
| **Method** | **GET**to retrieve information for an entry.**POST**to create a new entry.**PUT** to update/replace an existing entry.**PATCH** to make a partial entry update.**DELETE** to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

#### Example of Use - List Subaccounts

The following API call returns the subaccounts from your Slack account:

**URL:** 

`/1.0/subaccounts/list`

**Method:** 

`GET`

Matches of the search can be found in the module's Output under Bundles > Body. In our example, 4 subaccounts were returned:

