Telegram Bot
============

With the Telegram Bot modules in Make, you can:

* edit, forward, delete, pin, and unpin messages, and send text message or replies
* send audio files, documents, images, albums, photos, stickers, videos, video notes, voice messages, and invoices
* send media by URL or ID
* edit media messages, and message captions
* download files
* create, revoke, and edit chat invite links
* watch, and list updates, and chats
* kick, promote, and restrict chat members
* list administrators in a chat
* retrieve number of members in chat
* call APIs
* answer inline queries
Getting Started with Telegram Bot
---------------------------------

### Prerequisites

* A configured Bot via **Telegram app.** You can download the Telegram Desktop app at [desktop.telegram.org](https://desktop.telegram.org/).
* In order to use the Telegram app, your mobile phone number has to be provided.
![61d6b8861b9ab.png](./../image/uuid-c1e7a717-93dd-01a0-ebbd-1616dd66d92e.png)### Configuring the Telegram Bot

1. Go to [https://telegram.me/BotFather.](https://telegram.me/BotFather)

![61d6b88764945.gif](./../image/uuid-e2046bc7-277f-38a1-686c-6810d065a51e.gif)2. To create a new bot type `/newbot` to the message box and press enter.

3. Enter the name of the user name of your new bot.

![61d6b88953d8e.gif](./../image/uuid-878f59aa-5050-92ee-e636-177b3670dd05.gif)You have received the message from BotFather containing the **token**, which you can use to connect Telegram Bot to Make.

To add your bot to your Telegram application, click the link in the message from BotFather or enter it manually to your browser. The link is `t.me/yourBotName`.

![61d6b88b74987.png](./../image/uuid-39208449-66c0-5edc-5685-3bafdc8346c3.png)### Adding Telegram Bot to your Scenario

Follow **Step 1** in the [Creating a scenario](https://www.integromat.com/en/help/creating-a-scenario) article (choose the **Telegram Bot** module instead of Twitter and Facebook module).

![61d6a9efb1ac0.png](./../image/uuid-ff7cc380-739c-abbb-8580-209367e5b79b.png)After the module is added to your scenario you can then see the *[Scenario editor](https://www.integromat.com/en/help/scenario-editor).*

Define what function you need your module to have. Here you can choose between three [types of modules](https://www.integromat.com/en/help/types-of-modules) – *Triggers,* *Actions,* and *Searches.*

Did you know?
-------------

You can find a lot of sample scenario templates with Telegram Bot modules at [www.make.com/en/integrations/telegram](https://www.make.com/en/integrations/telegram).

Messages
--------

### Send a Text Message or Reply

Sends a text message or a reply to your Telegram Desktop application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **User ID** | [To set the UserID, follow these instructions](telegram-bot.html#how-to-find-out-the-user-id "How to find out the user ID") |
| **Text** | Enter (or map) the text content of the message you want to send. |
| **Message Thread ID** | A Unique identifier for the forum's target message thread (topic). Applicable for forum supergroups only. |
| **Parse mode** | Specify how you want your text to be recognized. HTML or Markdown.Markdown syntax: ```  *bold text* _italic text_ [inline URL](http://www.example.com/) [inline mention of a user](tg://user?id=123456789) `inline fixed-width code` ```block_language pre-formatted fixed-width code block ```  ``` HTML syntax: ```  <b>bold</b>, <strong>bold</strong> <i>italic</i>, <em>italic</em> <a href="http://www.example.com/">inline URL</a> <a href="tg://user?id=123456789">inline mention of a user</a> <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre>  ``` |
| **Disable Notifications** | Select whether you want to send messages silently. iOS users will not receive a notification; Android users will receive a notification with no sound. |
| **Disable Link Previews** | Select whether you want to disable link previews for links in this message. |
| **Original Message ID** | The ID of the original message if the message is a reply. |
| **Enter/Assemble the Reply Markup Field** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object, including an inline keyboard, a custom reply keyboard, instructions to remove the reply keyboard, or instructions to force a reply from the user, e.g. `{"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}`.NoteThe keyboard cannot be used with channels. |

### Edit a Text Message

Edits text or game messages.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Edit** | Select the message type you want to edit. |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message ID** | Enter the Message ID you want to forward. |
| **Text** | Enter (or map) the text content of the message you want to send. |
| **Parse mode** | Specify how you want your text to be recognized. HTML or Markdown.Markdown syntax: ``` *bold text* _italic text_ [inline URL](http://www.example.com/) [inline mention of a user](tg://user?id=123456789) `inline fixed-width code` ```block_language pre-formatted fixed-width code block ``` ``` HTML syntax: ``` <b>bold</b>, <strong>bold</strong> <i>italic</i>, <em>italic</em> <a href="http://www.example.com/">inline URL</a> <a href="tg://user?id=123456789">inline mention of a user</a> <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre> ``` |
| **Disable Link Previews** | Select whether you want to disable link previews. |
| **Enter/Assemble the Reply Markup Field** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ```  {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}  ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page.NoteKeyboards cannot be used with channels. |

### Forward a Message

Forwards messages of any kind. This module can be used to forward messages only within Telegram.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **From chat ID** | Enter the Chat ID where the original message was sent (or channel username in the format @channelusername). |
| **Message ID** | Enter the message ID of the message you want to forward in the `from_chat_id` format. |
| **Disable Notifications** | Select whether you want to send the message silently. iOS users will not receive a notification; Android users will receive a notification with no sound. |

### Delete a Message

Deletes a message. A message can only be deleted if it was sent less than 48 hours ago.

### Caution

Only a message sent less than 48 hours ago can be deleted.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message ID** | Enter the Message ID.61d6b89a2aa0b.png |

[### Pin a Message](#pin-a-message-964643_body)Pins a message.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot"). |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions.](/document/preview/453850#UUID-b66d7b10-009d-f909-e186-bf30a177aba8)Restrict a Chat Member |
| **Message ID** | Enter the message ID you want to pin. |
| **Disable Notifications** | Select whether you want to disable the notifications. If selected **Yes**, sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |

[### Unpin a Message](#unpin-a-message-964643_body)Unpins a message.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot"). |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions.](/document/preview/453850#UUID-b66d7b10-009d-f909-e186-bf30a177aba8)Restrict a Chat Member |
| **Message ID** | Enter the message ID you want to unpin. |

Media
-----

[### Send an Audio File](#send-an-audio-file_body)Sends an audio file to your Telegram Desktop application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. For forum supergroups only. |
| **Caption** | Enter the caption of the audio. |
| **Send by** | Audio file to send. Pass a `file_id` as a string to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. Further details about sending audio files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page.For example, you can use your Dropbox to process the file.61d6b8994b380.png |
| **Parse Mode** | Select Markdown-style or HTML-style of the text, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Duration** | Enter the duration of the video sent in seconds. |
| **Performer** | Enter a performer. |
| **Title** | Enter a track name. |
| **Reply markup - additional interface options** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Content type** | Select or enter the MIME type of data. |

[### Send a Document or an Image](#send-a-document-or-an-image_body)Sends a document or an image to your Telegram Desktop application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. For forum supergroups only. |
| **Caption** | Enter the caption of the audio. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Parse mode** | Specify how you want your text to be recognized. HTML or Markdown.Markdown syntax: ```  *bold text* _italic text_ [inline URL](http://www.example.com/) [inline mention of a user](tg://user?id=123456789) `inline fixed-width code` ```block_language pre-formatted fixed-width code block ```  ``` HTML syntax: ```  <b>bold</b>, <strong>bold</strong> <i>italic</i>, <em>italic</em> <a href="http://www.example.com/">inline URL</a> <a href="tg://user?id=123456789">inline mention of a user</a> <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre>  ``` |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Content type** | Select or enter the MIME type of data. |
| **ID of the original message** | The ID of the original message if the message is a reply. |
| **Reply markup - additional interface options** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ```  {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}  ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Send an Album](#send-an-album_body)Sends a group of photos or videos as an album.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Media** | Select the items you want to add to your album. |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. Applicable only for forum supergroups only. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Enter/Assemble the Reply Markup Field** | Select the option to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Send a Photo](#send-a-photo_body)Sends a photo to your Telegram Desktop application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. For forum supergroups only. |
| **Caption** | Enter the caption of the video. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Parse mode** | Specify how you want your text to be recognized. HTML or Markdown.Markdown syntax: ``` *bold text* _italic text_ [inline URL](http://www.example.com/) [inline mention of a user](tg://user?id=123456789) `inline fixed-width code` ```block_language pre-formatted fixed-width code block ``` ``` HTML syntax: ``` <b>bold</b>, <strong>bold</strong> <i>italic</i>, <em>italic</em> <a href="http://www.example.com/">inline URL</a> <a href="tg://user?id=123456789">inline mention of a user</a> <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre> ``` |
| **ID of the original message** | ID of the original message if the message is a reply. |
| **Reply markup - additional interface options** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboard can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Send a Sticker](#send-a-sticker_body)Sends a .webp sticker to your Telegram Desktop application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. For forum supergroups only. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Disable Notifications** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Original Message ID** | ID of the original message if the message is a reply. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

### Send a Video

Sends a video file to your Telegram Desktop Application.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the target message thread (topic) of the forum. For forum supergroups only. |
| **Caption** | Enter the caption of the video. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Content type** | Select or enter the MIME type of data. |
| **Duration** | Enter the duration of the video sent in seconds. |
| **Width** | Enter the video width. |
| **Height** | Enter the video height. |
| **Enter/Assemble the Reply Markup Field** | Select if to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ```  {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Send a Video Note](#send-a-video-note_body)As of v4.0, Telegram clients support rounded square mp4 videos of up to one minute long. Use this method to send video messages.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the forum's target message thread (topic). For forum supergroups only. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Content type** | Select or enter the MIME type of data. |
| **Length** | Video width and height, i.e., the diameter of the video message. |
| **Duration** | Enter the duration of the sent video (in seconds). |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ```  {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Original Message ID** | ID of the original message if the message is a reply. |
| **Enter/Assemble the Reply Markup Field** | Select if to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object including an inline keyboard, a custom reply keyboard, instructions to remove the reply keyboard, or instructions to force a reply from the user, e.g. `{"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}`.Note: keyboard cannot be used with channels. |

[### Send a Voice Message](#send-a-voice-message-964643_body)Send a voice message.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message Thread ID** | A unique identifier for the forum's target message thread (topic). For forum supergroups only. |
| **Caption** | Enter the caption of the voice message. |
| **Send by** | Image file to send. Pass a file\_id as a string to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a string for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. Further details about sending files can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **Content type** | Select or enter the MIME type of data. |
| **Duration** | Enter the duration of the video sent in seconds. |
| **Enter/Assemble the Reply Markup Field** | Select if to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ```  {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}  ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Edit a Media Message](#edit-a-media-message_body)Edits photo or video messages.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Message ID** | Enter the message ID of the message you want to forward. |
| **Media type** | Select whether you want to edit a photo or video. |
| **Caption** | Enter the photo/video caption. |
| **Source file** | Define the source file you want to edit. [More information about working with files](./../mapping/working-with-files.html "Working with files"). |
| **Parse mode** | Specify how you want your text to be recognized. HTML or Markdown.Markdown syntax: ``` *bold text* _italic text_ [inline URL](http://www.example.com/) [inline mention of a user](tg://user?id=123456789) `inline fixed-width code` ```block_language pre-formatted fixed-width code block ``` ``` HTML syntax: ``` <b>bold</b>, <strong>bold</strong> <i>italic</i>, <em>italic</em> <a href="http://www.example.com/">inline URL</a> <a href="tg://user?id=123456789">inline mention of a user</a> <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre> ``` |
| **Enter/Assemble the Reply Markup Field** | Select whether to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object including an inline keyboard, a custom reply keyboard, instructions to remove the reply keyboard or instructions to force a reply from the user, e.g. `{"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}`.NoteKeyboard cannot be used with channels. |

[### Edit a Message Caption](#edit-a-message-caption_body)Edits a caption of a message.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** |  |
| **Message ID** |  |
| **Caption** |  |
| **Parse Mode** |  |
| **Enter/Assemble the Reply Markup Field** | Select whether to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object including an inline keyboard, a custom reply keyboard, instructions to remove the reply keyboard or instructions to force a reply from the user, e.g. `{"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]`}. Note: keyboard cannot be used with channels. |

[### Send an Invoice](#send-an-invoice-964643_body)Sends an invoice.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions.](/document/preview/453850#UUID-b66d7b10-009d-f909-e186-bf30a177aba8)Restrict a Chat Member |
| **Title** | Enter the product name for which you want to send invoice. |
| **Description** | Enter the product details. |
| **Payload** | A Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes. |
| **Provide Token** | Payment provider token, obtained via `@BotFather`. |
| **Currency** | Three-letter ISO 4217 currency code, see more on [currencies](https://core.telegram.org/bots/payments#supported-currencies). |
| **Prices** | Add the product label and price details. |
| **Max Tip Amount** | The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of `US$ 1.45` pass `Max Tip Amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0 |
| **Suggested Tip Amounts** | Add the tip amounts suggested for this invoice. |
| **Message Thread ID** | Enter the unique identifier for the target message thread (topic) of the forum (for forum supergroups only). |
| **Start Parameter** | Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter |
| **Provider data** | A detailed description of required fields should be provided by the payment provider. |
| **Photo URL** | Enter URL address of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. |
| **Need Name** | Select whether if you require the user's full name to complete the order |
| **Need Phone Number** | Select whether if you require the user's phone number to complete the order. |
| **Need Email** | Select whether if you require the user's email address to complete the order. |
| **Need Shipping Address** | Select whether if you require the user's shipping address to complete the order. |
| **Send Phone Number to Provider** | Select whehter if the user's phone number should be sent to the provider. |
| **Send Email to Provider** | Select whether if the user's email address should be sent to the provider. |
| **Is Flexible** | Select whether Pass true if the final price depends on the shipping method. |
| **Disable Notifications** | Select whether you disable notifications. IF so, sends the message silently. iOS users will not receive a notification; Android users will receive a notification with no sound. |
| **Original Message ID** | Enter the ID of the original message. |
| **Enter/Assemble the Reply Markup Field** | Select if to enter or assemble the reply markup field. |
| **Reply Markup** | Enter additional interface options that are a JSON-serialized object including an inline keyboard, a custom reply keyboard, instructions to remove the reply keyboard or instructions to force a reply from the user, e.g. `{"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]}`.NoteKeyboard cannot be used with channels. |

### Send media by URL or ID



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **Chat ID** | [To set the Chat ID, follow these instructions](telegram-bot.html#how-to-find-out-the-id-of-a-private-channel-group- "How to find out the ID of a private channel/group:") |
| **Media type** | Select whether you want to edit a photo or video. |
| **Caption** | Enter the photo/video caption. |
| **Send by** | Select a file. Set a file\_id as a string to send a file that exists on the Telegram servers (recommended), or select an HTTP URL as a string for Telegram to get a file from the Internet. |
| **Disable notification** | Select *Yes* to send messages silently. iOS users will not receive a notification, Android users will receive a notification with no sound. |
| **ID of the original message** | ID of the original message if the message is a reply. |
| **Reply markup - additional interface options** | Enter additional interface options that are a JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user, e.g.: ``` {"inline_keyboard":[[{"text":"Some button text 2","url":"https://botpress.org"}]]} or {"keyboard":[["Yes","No"],["Maybe"]]} ``` More information about custom keyboards can be found on the [Telegram Bot API](https://core.telegram.org/bots/api) page. |

[### Download a File](#download-a-file-964643_body)Downloads a file from the Telegram server.



| **Connection** | [Establish a connection to your Telegram Bot using the provided token](telegram-bot.html#configuring-the-telegram-bot "Configuring the Telegram Bot") |
| --- | --- |
| **File ID** | Enter the ID of the file already uploaded to the Telegram server.61d6b89b26705.png |

Chats and Updates
-----------------

Using the following modules, you can create, revoke, and edit chat invite link, lit and watch updates, and list chats.

[### Create a Chat Invite Link](#create-a-chat-invite-link_body)Creates an additional invite link for a chat.

[### Edit a Chat Invite Link](#edit-a-chat-invite-link_body)Edits a non-primary invite link created by the bot.

[### List Updates](#list-updates-964643_body)Retrieves a list of updates from the Telegram server. By default, updates starting with the earliest unconfirmed update are returned. If you want to list more, you need to set the offset. This module cannot be used with webhooks. To use this module, you must switch off and remove all your Telegram webhooks.

[### List Chats](#list-chats_body)List available Telegram chats. By default, chats starting with the earlier unconfirmed update are returned. If you want to list more, you need to set the offset. This module cannot be used with webhooks. To use this module, you must switch off and remove all your Telegram webhooks.

[### Revoke a Chat Invite Link](#revoke-a-chat-invite-link_body)Revokes an invite link created by the bot.

### Watch Updates

Triggers when there is a new update from your Telegram Desktop Application.

The *Watch updates* trigger cannot be combined with the Get Updates or Get Chats modules.



| **Webhook** | To add a webhook you need to establish a connection to your Telegram bot. Use the token provided by the BotFather (see the steps above, *Configuring the Telegram Bot*). |
| --- | --- |

![TelegramBotWatchUpdates-Forman.gif](./../image/uuid-97c647e2-04b6-892c-def8-6d5fed952486.gif)The connection between Telegram Bot and Make is now established. You can continue with other Telegram Bot *actions*.

Members
-------

Using the following modules, you can list administrators, retrieve members, kick, promote, and restrict chat members.

[### List Administrators in a Chat](#list-administrators-in-a-chat_body)Retrieves a list of administrators from a selected chat.

[### Get the Number of Members in a Chat](#get-the-number-of-members-in-a-chat_body)Use this module to get the number of members in a chat.

[### Kick a Chat Member](#kick-a-chat-member_body)Use this method to kick a user from a group, a supergroup, or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

[### Promote a Chat Member](#promote-a-chat-member_body)Promotes or demotes a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

[### Restrict a Chat Member](#restrict-a-chat-member_body)Restricts a user in a supergroup.

Other
-----

Using the following modules, you can call APIs, and answer inline queries.

[### Make an API Call](#make-an-api-call-964643_body)Performs an arbitrary authorized API call.

[### Answer an inline Query](#answer-an-inline-query_body)Sends answer to an inline query.

Troubleshooting
---------------

Check the following procedures if you are facing difficulties when using the Telegram bot app.

### How to find out the ID of a private channel/group:

One possible way to determine the ID of a private channel/group is as follows:

1. Create a new scenario
2. Place Telegram Bot >; Watch updates module in the scenario.
3. Configure the module by creating a webhook.
4. Execute the scenario.
5. Send a message to the private channel/group.
6. Verify the output of the module by clicking the bubble above the module.
7. Find the ID in the output bundle:

![2020-04-08-13_11_38-window.png](./../image/uuid-2eb5f5f1-88eb-250e-082e-2b273c540884.png)
### How to find out the user ID

To find out the ID of a Telegram user, forward their message to the **userinfobot**. Check out the following procedure for steps on how to do that:

1. Add the **userinfobot** to your Telegram app. You can do that by entering `@userinfobot` in the search bar and selecting the **userinfobot**.

![61d6b8959380c.gif](./../image/uuid-065f8e7b-39f9-3de5-8198-507b827e4e02.gif)
2. Go to the chat with the user you want to retrieve the ID from.
3. Forward his message to **userinfobot.**
4. Copy the User ID and paste it to the Make module.

![61d6b8978bfee.png](./../image/uuid-6a10ce31-221e-5b94-aef4-bc6d7a8b93d1.png)
### Adding Your Bot To the Channel:

1. Click the right mouse button on the channel name and select the *View channel info* option*.*
2. Click the *Add Member* icon next to the member number.

![61d6b89d19e85.png](./../image/uuid-05d46f27-b331-f859-4cba-12a7db02453c.png)
3. Start typing the name of your bot in the search field.
4. Click on the bot name to select the bot you want to add to the channel.

![61d6b89e298b1.png](./../image/uuid-913c4f24-ee0b-843a-2a3f-ab518d97e0d1.png)
5. Click the *INVITE* button.
6. Make the bot admin by clicking the respective button.

![61d6b89f18ca8.png](./../image/uuid-6a89ecdf-52c5-56c9-fd02-adcdc9f5f718.png)
7. Assign the permissions to your bot and click the *SAVE* button.

![61d6b89ff2684.png](./../image/uuid-1c3f8f03-baaf-1297-73af-eab190d72999.png)
The bot has been added to the channel.

### Testing a Public Channel

To test the public channel you need to obtain the *Chat ID.* The *Chat ID* is part of the channel link.

The *channel name* is **NOT** the channel *link*/*chat ID.*

If the public channel link is, for example, *t.me/IMTtest*, then `@IMTtest` is your ***Chat ID***.

![61d6b8a0e693f.png](./../image/uuid-1c64c350-71a9-8b66-bdd3-dc3b8ff08e02.png)Now, you can send a message to the public channel using the *Send a Text Message or a Reply* module.

![61d6b8a1c71bd.png](./../image/uuid-daeb0cb8-a30a-3d3c-a8ac-064a22632779.png)### Testing a Private Channel:

You need to obtain the Chat ID to test the private channel. There are three options to retrieve the ID:

* [Retrieve the ID from the web version of Telegram](telegram-bot.html#retrieving-the-id-from-the-web-version-of-telegram "Retrieving the ID From the Web Version of Telegram").
* Switch the private channel to the public channel, then retrieve the ID (by sending or receiving the message in Make) and switch back the channel type to *private*.
* Invite the bot `get_id_bot` to your private channel and using the `/my_id@get_id_bot` command.
### Retrieving the ID From the Web Version of Telegram

1. Log in to your Telegram account via [https://web.telegram.org](https://web.telegram.org/).
2. Click on the private channel you want to retrieve the chat ID for.

![61d6b8a2d953a.png](./../image/uuid-c7d9f9a7-7f28-fd3c-4b8b-716cc343f9ce.png)
3. Copy the number between the c letter and the underscore from the URL. If the URL is https://web.telegram.org/#/im?p=c1424271061\_11793697872942794544 then copy the 1424271061

![61d6b8a3cf316.png](./../image/uuid-318f36b7-9cb2-bc3e-6bcb-23f8467c47c0.png)
4. Paste the number to the desired field and **add the prefix**`-100`
5. The Chat ID of the private channel is then **-100***1424271061.*

You can now use the *ID* in the desired *Telegram Bot* module in *Make*.

![61d6b8a4cde72.png](./../image/uuid-f652a43a-fe3c-ec8d-a980-63d6e94eb4d7.png)
### Registration and Login

It is not required. You can sign in on the site, [telegram.org/auth](https://my.telegram.org/auth) where you can change your public settings. You will receive a key in your desktop application to submit your login.

### My bot is hitting limits, how do I avoid this?

When sending messages inside a particular chat, avoid sending more than one message per second. We may allow short bursts that go over this limit, but eventually you'll begin receiving 429 errors.

If you're sending bulk notifications to multiple users, the API will not allow more than 30 messages per second or so. Consider spreading out notifications over large intervals of 8—12 hours for best results.

Also note that your bot will not be able to send more than 20 messages per minute to the same group.

(source: <https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this>)

