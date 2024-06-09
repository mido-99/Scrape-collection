Microsoft 365 Email
===================

With Microsoft 365 Email modules in Make, you can watch for, search for, retrieve, create and send, update, forward, reply, move and delete messages, create and send draft messages, and retrieve, add, and download attachments.

To use the Microsoft 365 Email modules, you must have a Microsoft Office account. You can create an account at [office.com](https://www.office.com/).

Refer to the [Microsoft 365 Email API documentation](https://learn.microsoft.com/en-us/graph/api/resources/message?view=graph-rest-1.0) for a list of available endpoints.

[See the changelog for the Microsoft 365 Email App](microsoft-365-email.html#change-log-between-microsoft-365-email--v2--and-microsoft-365-email--v1- "Change log between Microsoft 365 Email [v2] and Microsoft 365 Email [v1]")

Connect Microsoft 365 Email to Make
-----------------------------------

To establish the connection using your Microsoft account:

1. Log in to your Make account, add a Microsoft 365 Email module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show advanced settings** and enter your custom app client credentials.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Microsoft 365 Email modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build Microsoft 365 Email Scenarios
-----------------------------------

After connecting the app, you can perform the following actions:

Message* Watch Messages

**Required Permissions**: Mail.Read
* Watch Messages in a Shared Folder

**Required Permissions**: Mail.Read.Shared
* Search Messages

**Required Permissions**: Mail.Read

### Keyword Query Language

Use Keyword Query Language (KQL) search syntax to build your search queries in Microsoft modules. For more information, see [Microsoft Graph help](https://learn.microsoft.com/en-us/graph/api/resources/search-api-overview?view=graph-rest-1.0#keyword-query-language-kql-support).
* Get a Message

**Required Permissions**: Mail.Read
* Create and Send a Message

**Required Permissions**: Mail.Send, Mail.ReadWrite
* Forward a Message

**Required Permissions**: Mail.Send
* Reply to a Message

**Required Permissions**: Mail.Send, Mail.ReadWrite
* Move a Message

**Required Permissions**: Mail.ReadWrite
* Delete a Message

**Required Permissions**: Mail.ReadWrite
Draft Message* Create a Draft Message

**Required Permissions**: Mail.ReadWrite
* Send a Draft Message

**Required Permissions**: Mail.ReadWrite, Mail.Send
* Update a Message

**Required Permissions**: Mail.ReadWrite
Attachment* List Attachments

**Required Permissions**: Mail.Read
* Add an Attachment

**Required Permissions:** Mail.ReadWrite
* Download an Attachment

**Required Permissions**: Mail.Read
Other* Make an API Call

**Required Permissions**: Mail.ReadWrite
Change log between Microsoft 365 Email [v2] and Microsoft 365 Email [v1]
------------------------------------------------------------------------

* New modules - Search Messages, Get a Message, Update a Message, List Attachments, Download an Attachment, and Make an API Call
