Gmail
=====

With Gmail modules in Make, you can manage the emails, email labels, and attachments in your Gmail account.

To use the Gmail modules, you must have a Gmail account. You can create an account at [myaccount.google.com](https://myaccount.google.com/).

Refer to the [Gmail API documentation](https://developers.google.com/gmail/api/reference/rest) for a list of available endpoints.

### Note

Make's use and transfer of information received from Google APIs to any other app will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

Connect Gmail to Make
---------------------

### Important

If you want to connect an email that ends with `@gmail` or `@googlemail`, you must create a custom OAuth client in Google Cloud Console and get your project client credentials to establish the connection in Make.

To establish the connection in Make:

1. Log in to your Make account, add a Gmail module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional for Gmail users with non-`@gmail` or `@googlemail` domains: Switch on the **Show advanced settings** toggle and enter your Google Cloud Console project client credentials. For more information, see the [Create and configure a Google Cloud Console project for Gmail section](gmail.html#create-and-configure-a-google-cloud-console-project-for-gmail "Create and configure a Google Cloud Console project for Gmail") below.
4. Click **Sign in with Google**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Gmail modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

### Create and configure a Google Cloud Console project for Gmail

To connect to Make using your own client credentials, you can create and configure a project in the Google Cloud Console.

### Important

This is required for emails that end with `@gmail` or `@googlemail`.

#### Create a Google Cloud Console project for Gmail

To create a Google Cloud Console project:

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. In the top menu, click **Select a project** > **New project**.
3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.
#### Enable APIs for Gmail

To enable the required APIs:

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for and enable the following API: **Gmail API**
#### Configure your OAuth consent screen for Gmail

To configure your OAuth consent screen:

1. Go to **APIs & Services** > **OAuth consent screen**.
2. Under **User Type**, select **External**.

For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).
3. Click **Create**.
4. Fill in the required fields with your information.
5. In the **Authorized domains** section, add `make.com` and `integromat.com`.
6. Click **Save and continue**.
7. In the **Scopes** page, click **Add or remove scopes**, add the following scopes, and click **Update**: `https://mail.google.com/`
8. Click **Save and continue**.
9. Optional: If your project will remain in the **Testing** publishing status, add test user emails on the **Test users** page, then click **Save and continue**.
#### Create your Gmail client credentials

To create your client credentials:

1. In the left sidebar, click **Credentials**.
2. Click **+ Create Credentials** > **OAuth client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the console.
5. In the **Authorized redirect URIs** section, click **+ Add URI** and enter the following redirect URI:

`https://www.integromat.com/oauth/cb/google-restricted`
6. Click **Create**.
7. Copy your **Client ID** and **Client secret** values and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Make.

Build Gmail Scenarios
---------------------

After connecting the app, you can perform the following actions:

### Triggers

[#### Watch Emails](#watch-emails-975546_body)Triggers when a new email is received to be processed according to specified criteria.



| **Connection** | Establish a connection to your Gmail account. |
| --- | --- |
| **Folder** | Select the email folder you want to watch. |
| **Filter type** | Select **Simple filter** to filter emails by selecting criteria, or **Gmail filter** to filter emails by entering the query. |
| **Criteria** | Select the option to filter watched emails by. |
| **Query** | Use [the Gmail search syntax](https://support.google.com/mail/answer/7190). To search for messages containing an icon of a specific color, use the following search query:* Yellow Star: `l:^ss_sy` * Blue Star: `l:^ss_sb` * Red Star: `l:^ss_sr` * Orange Star: `l:^ss_so` * Green Star: `l:^ss_sg` * Purple Star: `l:^ss_sp` * Red Bang: `l:^ss_cr` * Yellow Bang: `l:^ss_cy` * Blue Info: `l:^ss_cb` * Orange Guillment: `l:^ss_co` * Green Check: `l:^ss_cg` * Purple Question: `l:^ss_cp` |
| **Sender email address** | Enter the email addresses that you want to filter emails by. |
| **Subject** | Enter the characters string in the email subject that you want to filter emails by. |
| **Search phrase** | Enter the characters string in the email subject or body that you want to filter emails by. |
| **Mark email message(s) as read when fetched** | Select whether you want to mark retrieved emails as read. |
| **Maximum number of results** | Set the maximum number of results that Make will work with during one cycle. |

### Actions

[#### Copy an Email](#idp1189200_body)Copies an email or a draft into a selected folder.



| **Connection** |  |
| --- | --- |
| **Folder** | Select the email source folder that contains an email you want to copy. |
| **Destination folder** | Select the email destination folder where you want to copy an email to. |
| **Email ID (UID)** | Enter the ID of the email you want to copy. To get the Email ID (UID), use the **Email > Get Emails** module. You will see the value in the output. |

[#### Create a Draft](#create-a-draft-975546_body)Creates a new draft and adds it to a selected folder.



| **Connection** |  |
| --- | --- |
| **Folder** | Select the folder you want to add a draft to. |
| **To** | Enter the recipient's email address. |
| **Subject** | Enter the email draft subject. |
| **Content** | Enter the email message body. You can use HTML tags. |
| **Attachments** | | **File name** | Enter the name of the file to be uploaded, including the file extension. For example, `myFile.png`. | | --- | --- | | **Data** | Enter the file data. Refer to [our Help Center](./../mapping/working-with-files.html "Working with files") to learn how to work with files. | |
| **Copy recipient** | Enter the copy recipient's email address. (CC:) |
| **Blind copy recipient** | Enter the blind copy recipient's email address. (BCC:) |

[#### Delete an Email](#idp1189201_body)Removes an email or a draft from a selected folder.



| **Connection** |  |
| --- | --- |
| **Gmail Message ID** | Enter the ID of the message you want to delete. To get the Gmail Message ID, use the **Gmail > Watch Emails** module. You will see the value in **Labels** array, in the output. |
| **Permanently** | Select whether you want to move the email to the thrash folder or to permanently delete it. |

[#### Mark an Email as Read](#idp1189202_body)Marks an email or a draft in a selected directory as read by setting the "Read" flag.



| **Connection** |  |
| --- | --- |
| **Folder** | Select the folder that contains the email you want to mark as Read. |
| **Email ID (UID)** | Enter the ID of the email you want to copy. To get the Email ID (UID), use the **Email > Get Emails** module. You will see the value in the output. |

[#### Mark an Email as Unread](#idp1189203_body)Marks an email or a draft in a selected directory as read by setting the "Unread" flag.



| **Connection** |  |
| --- | --- |
| **Folder** | Select the folder that contains the email you want to mark as Unread. |
| **Email ID (UID)** | Enter the ID of the email you want to copy. To get the Email ID (UID), use the **Email > Get Emails** module. You will see the value in the output. |

[#### Modify Email Labels](#idp1189204_body)Modifies labels on the specified email message.



| **Connection** |  |
| --- | --- |
| **Gmail Message ID** | Enter the ID of the message whose labels you want to modify. To get the Gmail Message ID, use the **Gmail > Watch Emails** module. You will see the value in **Labels** array, in the output. |
| **Labels to add** | Select the labels you want to attach to the email. |
| **Labels to remove** | Select the labels you want to detach from the email. |

[#### Move an Email](#idp1189205_body)Moves a chosen email or a draft to a selected folder.



| **Connection** |  |
| --- | --- |
| **Folder** | Select the email source folder that contains an email you want to move. |
| **Destination folder** | Select the email destination folder where you want to move an email to. |
| **Email ID (UID)** | Enter the ID of the email you want to copy. To get the Email ID (UID), use the **Email > Get Emails** module. You will see the value in the output. |

[#### Send an Email](#send-an-email-975546_body)Sends a new email.



| **Connection** |  |
| --- | --- |
| **From** | Enter a custom sender email address.You may enter a custom name in quotes before a custom sender email address or an email address you've already connected with. For example, `[[email protected]](/cdn-cgi/l/email-protection)` or `"John Bush" [[email protected]](/cdn-cgi/l/email-protection)`. |
| **To** | Enter the recipient's email address. |
| **Subject** | Enter the email subject. |
| **Content** | Enter the email message body. You can use HTML tags. |
| **Attachments** | | **File name** | Enter the name of the file to be uploaded, including the file extension. For example, `myFile.png`. | | --- | --- | | **Data** | Enter the file data. Refer to [our Help Center](./../mapping/working-with-files.html "Working with files") to learn how to work with files. | | **Content ID** | Enter a Content ID to attach inline images. This allows you to create an ID for the attachment, which you can then use in HTML: `<img src="cid:ii_jrc3r9mw1">` where `ii_jrc3r9mw1` is a content ID. | |
| **Copy recipient** | Enter the copy recipient's email address. (CC:) |
| **Blind copy recipient** | Enter the blind copy recipient's email address. (BCC:) |

### Iterators

[#### Iterate Attachments](#idp1189206_body)Iterates through received attachments.



| **Source module** | Select the module that contains attachments you want to iterate. |
| --- | --- |

Common Problems
---------------

Here you can find solutions for the most common issues when working with Gmail in Make.

### Error 400: Failed to Verify a Connection

Your connection has expired and is no longer valid. You need to reauthorizae the connection every seven days. Refer to [Google OAuth documentation](https://developers.google.com/identity/protocols/oauth2#expiration) for more information.

To avoid reauthorization every seven days, publish your project in Google Cloud Console:

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. Go to **APIs & Service** > **OAuth consent screen**.
3. Under **Publishing status**, click **Publish app**.

### Note

If the **Needs verification** message appears, choose whether to go through the [Google verification process](https://support.google.com/cloud/answer/13463073?visit_id=638357423877979226-2405331664&rd=1#exceptions-ver-reqts) for the app or to connect to your unverified app. Currently connecting to unverified apps works in Make, but we cannot guarantee the Google will allow connections to unverified apps for an indefinite period.
### Error 403: Access Denied

You didn't add a test user for your project in Google Cloud Console, and the project has the **Testing** status. You need to add the email address associated with the Google account you want to connect with Make as a Test user.

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. Go to **APIs & Services** > **OAuth consent screen**.
3. Under **Test users**, **+ Add Users** and enter an email of a user that you want to create a connection for.
4. Click **Save**.
### Error 403: Access Not Configured

The **Gmail API** was disabled in the Google Cloud Console. You need to [enable it](gmail.html#connect-gmail-to-make "Connect Gmail to Make") again.

