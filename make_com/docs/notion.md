Notion
======

With the Notion modules in Make, you can watch, retrieve, create, append, and update databases, database items, pages, page content, search for objects, list users, and make API calls.

To use the Notion modules, you must have a Notion account. Your Notion account must have admin permissions to establish the connection in Make. You can create a Notion account at [notion.so](https://www.notion.so/signup).

Refer to the [Notion API documentation](https://developers.notion.com/reference/intro) for a list of available endpoints.

Connect Notion to Make
----------------------

Make provides two ways to connect the Notion app:

* [Notion Internal connection](notion.html#establish-a-notion-internal-connection "Establish a Notion Internal Connection")
* [Notion Public connection](notion.html#establish-a-notion-public-connection "Establish a Notion Public Connection")
### Establish a Notion Internal Connection

To establish a Notion internal connection:

1. Log in to your Notion account.
2. Click **Settings & Members** > **Connections** > **Develop or manage integrations** from the sidebar or go to the [My integrations page](https://www.notion.so/my-integrations).



| Notion_Connections.png |
| --- |
3. Click **New Integration**.



| Notion_New_Integration.png |
| --- |
4. Select the **Associate workspace**, fill in the integration **Name**, upload a logo (optional), choose the **Associated workspace**, and click **Submit**.
5. Go to **Capabilities**, update the requested capabilities, and click **Save changes**.



| Notion_Capabilities.png |
| --- |
6. Go to **Secrets**, click **Show** next to your internal integration token, and copy the token. Store your token in a safe place.



| Notion_Show_Key.png |
| --- |
7. Log in to your Make account and add a Notion module to your scenario, and click **Create a connection**.
8. In the **Connection type** dropdown, select **Notion Internal**.
9. Optional: In the **Connection name** field, enter a name for the connection.
10. In the **Internal Integration Token** field, paste the token copied in Step 6.
11. Click **Save**.

You have successfully established the connection. You can now edit your scenario and add more Notion modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

If the databases are not visible in the **Database ID** > **Search** field, follow the instructions in [Add Databases to be visible in Make](notion.html#add-databases-to-be-visible-in-make-964748 "Add Databases to be visible in Make") to add them.

### Establish a Notion Public Connection

To establish a Notion public connection:

1. Log in to your Make account and add a Notion module to your scenario, and click **Create a connection**.
2. In the **Connection type** dropdown, select **Notion Public**.
3. Optional: In the **Connection name** field, enter a name for the connection.
4. Optional: Click **Show Advanced Settings** and enter your client credentials. See [Obtain Notion Client Credentials](notion.html#obtain-notion-client-credentials "Obtain Notion Client Credentials").
5. Click **Save**.
6. If prompted, authenticate your account, click **Select pages**, select the pages you want Make to have access to, and click **Allow access**.

You have successfully established the connection. You can now edit your scenario and add more Notion modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

### Obtain Notion Client Credentials

To obtain client credentials:

1. Log in to your Notion account.
2. Click **Settings & Members** > **Connections** > **Develop or manage integrations** from the sidebar or go to the [My integrations page](https://www.notion.so/my-integrations).



| Notion_Connections.png |
| --- |
3. Click **New Integration**.



| Notion_New_Integration.png |
| --- |
4. Select the **Associate workspace**, fill in the integration **Name**, upload a logo (optional), choose the **Associated workspace**, and click **Submit**.
5. Go to **Capabilities**, update the requested capabilities, and click **Save changes**.



| Notion_Capabilities.png |
| --- |
6. Go to **Distribution** and click the toggle to make the integration public.



| Notion_Public_toggle_2.png |
| --- |
7. Fill in your organization information and click **Submit**.



| **Redirect URIs** | Enter the redirect URI:`https://www.integromat.com/oauth/cb/notion2` |
| --- | --- |
| **Company name** | Name of your company or organization. You may use your own name if this does not apply. |
| **Website or homepage** | Used to link to your integration’s website or homepage in your integration page and authentication screens. |
| **Tagline** | Optional: A short description of the integration. |
| **Privacy policy** | URL address used to link to your integration’s privacy policy in your integration page and authentication screens. |
| **Terms of use** | URL address used to link to your integration’s terms of use in your integration page and authentication screens. |
| **Support email** | Used to link to your integration’s support email in your integration page and authentication screens. |
| **Notion URL for optional template** | Optional. URL must be for a public Notion page. Use this field if you'd like to duplicate a template into a user's workspace during OAuth. |
8. Click **Continue** in the **Switch to Public integration?** prompt.
9. Copy the **OAuth client ID** and **OAuth client secret** and save them in a safe place. You will not be able to view the **OAuth client secret** more than once.



| Notion_OAuth_Secrets.png |
| --- |

You have successfully created your client credentials.

### Add Databases to be visible in Make

For the Notion internal connection, by default, Notion databases do not appear in the **Database ID** field > **Search** option. You must manually add them to the Make app from your Notion account.



| msedge_xN4IuRm1rS.gif |
| --- |

To add databases from your Notion account to Make app:

1. Log in to your Notion account.
2. Enter into the database you want to add to Make , click on **...** in the top right corner, click **Add connections**, search for and click on the integration you previously created, and click **Confirm**.



| Notion_Add_Database.png |
| --- |

The database is successfully shared and you can now see it in a module's **Database ID > Search** field.



| p3nnx3BAli.png |
| --- |

### Retrieve added databases and pages after establishing the connection

### Note

If new databases or pages are added to the Notion account, you must revoke the connection in your Notion account and reauthorize the connection in Make to retrieve the added databases or pages.

To retrieve the newly added databases and pages:

1. Log in to your Notion account.
2. Click **Settings & members** > **Connections** > **...** > **Disconnect all users**.



| Notion_Disconnect.png |
| --- |
3. Go to your Make account **Connections** page, search for your Notion connection, and click **Reauthorize**.



| msedge_2Ufl0UimNc.gif |
| --- |

You can now see the newly added databases or pages in your Notion Make connection.

Build Notion Scenarios
----------------------

After connecting the app, you can perform the following actions:

Database Item* Watch Database Items
* Get a Database Item

Note: Add the **List Page Property Items** module to retrieve the complete details of a property item if the output variable contains the `has_more` value. This means you must paginate to retrieve all the property item's property values in the page object as Notion imposes a 25-page reference limit.
* Create a Database Item
* Append a Database Item Content
* Update a Database Item
Database/Page* Watch Databases/Pages
* Search Objects
* Get a Database
* Get a Page
* Create a Database
* Create a Page
* Update a Database
* Update a Page
Page Content* Watch Page Contents
* List Page Contents
* List Page Property Items

Note: Can be used with the following property types: title, text, relation, and person.

Use this module when a property on a database item or page output contains the `has more` value, indicating there are more than 25 items in that field and you much paginate to retrieve all items in that column.
* Get a Page Content
* Append a Page Content
* Update a Page Content

Note: In the **Type** field, select the page content type that corresponds to the **Page Content ID**. If an incorrect **Type** is selected, an error will appear. The page content type cannot be changed using this module.
* Delete a Page Content
Other* Make an API Call
* List Users
