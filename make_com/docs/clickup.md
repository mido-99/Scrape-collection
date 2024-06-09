ClickUp
=======

With ClickUp modules in Make, you can manage the tasks, lists, folders, spaces, targets, goals, comments, views, tags, checklists, tracked time, dependencies, and workspaces in your ClickUp account

To use the ClickUp modules, you must have a ClickUp account. You can create an account at <https://clickup.com/>.

Refer to the [ClickUp API documentation](https://clickup.com/api/) for a list of available endpoints.

Connect ClickUp to Make
-----------------------

To establish the connection in Make:

1. Log in to your Make account, add a ClickUp module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show advanced settings** and enter your custom app client credentials. For more information, refer to the [ClickUp OAuth app documentation](https://clickup.com/api/developer-portal/authentication/#step-1-create-an-oauth-app).

If requested, use the following Redirect URI when creating your custom app: `https://www.integromat.com/oauth/cb/oauth2`

ClickUp does not allow for the creation of multiple connections unless a different OAuth2 app is created for each connection.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more ClickUp modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build ClickUp Scenarios
-----------------------

After connecting the app, you can perform the following actions:

Task* Watch Tasks (triggers when a task or subtask event happens)
* Watch Tasks (triggers when a task or subtask is created or updated)
* List All Tasks
* List Subtasks for a Task
* List Filtered Tasks
* List All Task Members
* List Task Templates
* Get a Task
* Create a Task
* Create a Task (advanced)
* Create a Task from a Template
* Upload Task Attachment
* Edit a Task
* Edit a Task with Custom Fields
* Edit a Task with Custom Fields (advanced)
* Delete a Task
* Get Task's Time in Status
List* Watch Lists
* List All Lists
* List All Folderless Lists
* List all List Views
* List All List Members
* Get a List
* Create a List
* Create a Folderless List
* Edit a List
* Delete a List
Folder* Watch Folders
* List All Folders
* Get a Folder
* Create a Folder
* Edit a Folder
* Delete a Folder
Space* Watch Spaces
* List All Spaces
* Get a Space
* Create a Space
* Edit a Space
* Delete a Space
Target* Create a Target
* Edit a Target
* Delete a Target
Goal* List All Goals
* Get a Goal
* Create a Goal
* Edit a Goal
* Delete a Goal
Comment* List All Comments
* Post a View Comment
* Post List Comment
* Post a Task Comment
* Update a Comment
* Delete a Comment
View* List All Space Views
* List All Team Views
* List All Folder Views
* List All View Tasks
* Get a View
Tag* List All Space Tags
* Create a Space Tag
* Add Tag to a Task
* Remove Tag from a Task
* Edit a Space Tag
* Delete a Space Tag
Checklist* Create a Checklist
* Create a Checklist Item
* Edit a Checklist
* Edit a Checklist Item
* Delete a Checklist
* Delete a Checklist Item
Tracked Time 2.0* List Time Entries
* Get a Time Entry
* List Time Entry's Histories
* Create a Time Entry
* Start/Stop a Timer
* Update a Time Entry
* Delete a Time Entry
Tracked Time* List Tracked Time
* Add Tracked Time
* Edit Tracked Time
* Delete Time Tracked
Dependency* Add a Dependency
* Delete a Dependency
Workspace* List All Workspaces
* Get a Workspace
* Invite a User to a Workspace
Other* Make an API Call
* List All Accessible Custom Fields
### Note

This app uses [webhooks](./../tools/webhooks.html "Webhooks") to trigger a scenario when an event occurs instantly. All webhook modules have an `instant` tag next to their name.

When you create a ClickUp webhook in Make, it is attached automatically and requires no additional set up.

How To Obtain the Assignee's ID
-------------------------------

1. Open the **Create a Task** module and establish the connection.
2. Select the values for **Workspace > Space > Folder > List** to display the assignees.
3. Select the assignee whose ID you want to view and click the **Map** toggle icon.

![clickupAssigneeID.gif](./../image/uuid-70ab9f6d-e4be-0c03-cf54-c0a44e877eea.gif)
The selected user ID displays.

You can select multiple users. The user IDs are displayed separated by a comma in the order of their names in the **Assignees** field.

