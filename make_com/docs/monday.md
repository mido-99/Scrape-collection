Monday
======

With Monday modules in Make, you can retrieve, update, and watch column values, create, duplicate, retrieve, delete and/or list boards, groups, teams, users, items, updates, subscribers, and/or files, and execute GraphQL queries.

To get started with the Monday app, create an account at [auth.monday.com/users/sign\_up](https://auth.monday.com/users/sign_up).

Refer to the [Monday API documentation](https://developer.monday.com/api-reference/docs) for a list of available endpoints.

Connect Monday to Make
----------------------

To connect Monday to Make, you must obtain an API Key from your Monday account.

1. Log in to your [Monday account](https://auth.monday.com/auth/login_monday/).
2. Click your profile icon > **Admin**.
3. Navigate to the **API** section.
4. To use a new token, click **Create a new API Token**, copy the **Personal API Token**, and store it in a safe place.

To use an existing token, copy the **Personal API Token** and store it in a safe place.
5. Log in to your Make account, add a Monday module to your scenario, and click **Create a connection**.
6. Optional: In the **Connection name** field, enter a name for the connection.
7. In the **API Key** field, enter the details copied in Step 4 and click **Save**.

You have successfully established the connection. You can now edit your scenario and add more Monday modules. If your connection needs reauthorization, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build Monday Scenarios
----------------------

After connecting the app, you can perform the following actions:

Column Values* Get an Item's Column Value
* Update Column Values of a Specific Item
* Watch Item's Column Value
* Watch Column's Values Based on changedAt
* Watch Board's Column Values
Boards* Add a Column to a Board
* Create a Board
* Create a Group
* Duplicate a Group
* Duplicate a Board
* Get a Board
* Get a Group
* List Boards
* List Board's Groups
Tags* Create or Get a Tag
Users* Get a Team
* Get a User
* List Teams
* List Users
* Watch Team's Users
* Watch Users
Items* Create an Item
* Create a Subitem
* Duplicate an Item
* Delete or Archive an Item
* Get an Item
* Move an Item Between Groups
* List Board's Items
* List Group's Items
* List Items
* Search Items in the Board by Column Values
* Watch Board's Items
* Watch Item's Name
* Watch Group's Items
* Watch Items
* Watch Board's Items by Column Values
Updates* Create an Update
* List Updates
* List Item's Updates
* List Replies to Item's Updates
* Watch Item's Updates
* Watch Board's Updates
Subscribers* List Item's Subscribers
* List Board Subscribers
* Watch Board's Subscribers
* Add Board Subscribers
* Remove Board Subscribers
Files* List Files
* Add a File to an Update
* Add a File to a File Column Value
* Download a File
Activities* List Board Activity Logs
Other* Execute a GraphQL Query
[Execute a GraphQL Query
-----------------------](#execute-a-graphql-query-964747_body)Allows you to perform a custom API call.



| **Connection** | [Establish a connection to your Monday account](monday.html#connect-monday-to-make "Connect Monday to Make"). |
| --- | --- |
| **Method** | Select the method of the API call you want to use. Monday supports both methods:* **GET** * **POST** |
| **Query** | Enter the desired GraphQL query. See [Monday API documentation](https://monday.com/developers/v2) for examples and available queries.Example: `mutation { change_column_value ( board_id: 364921717, item_id: 364921724, column_id: "text", value: "\"ABCD\"" ) { id } }`CautionWhen you copy the query from the API documentation examples, the module may throw the RuntimeError due to a Parse error:  | mceclip0-22.png | | --- |    | mceclip0-23.png | | --- |  `WORKAROUND: Copy and paste the query to Notepad or a similar text editor that removes formatting and then copy and paste it to the Query field.` |
| **Variables** | GraphQL has a first-class way to factor dynamic values out of the query, and pass them as a separate dictionary. These values are called *variables*. Please find more information about using variables in the [Monday API documentation](https://api.developer.monday.com/docs#using-grpahql-section-variables) and in the [GraphQL documentation](https://graphql.org/learn/queries/#variables).Example:  | **Method** | `POST` | | --- | --- | | **Query** | `mutation MyUpdateText($newText:JSON!) { change_column_value ( board_id: 364921717, item_id: 364921724, column_id: "text", value: $newText ) { id } }` | | **Variables** | See the screenshot below. Please note the **quotation marks** around the value. |    | 61d6a9cb73cc0.png | | --- | |

