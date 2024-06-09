WordPress
=========

With WordPress modules in Make, you can manage posts, categories, comments, media, users, tags, and taxonomies in your WordPress account.

To use the WordPress modules, you must have a WordPress account with the [Make Connector plugin](https://wordpress.org/plugins/integromat-connector/) enabled. You can get a WordPress account at [wordpress.org](https://wordpress.org/).

Refer to the [WordPress API documentation](https://developer.wordpress.org/rest-api/reference/) for a list of available endpoints.

Connect WordPress to Make
-------------------------

To establish the connection, you must:

1. [Install the Make Connector plugin in WordPress.](wordpress.html#install-the-make-connector-plugin-in-wordpress "Install the Make Connector plugin in WordPress")
2. [Obtain your API key in WordPress.](wordpress.html#obtain-your-api-key-in-wordpress "Obtain your API key in WordPress")
3. [Establish the connection in Make.](wordpress.html#establish-the-connection-with-wordpress-in-make- "Establish the connection with WordPress in Make.")
### Install the Make Connector plugin in WordPress

To connect your WordPress account to Make, the Make Connector plugin must be installed in your WordPress installation.

1. Go to the [Make Connector plugin page](https://wordpress.org/plugins/integromat-connector/) in WordPress and download the Make Connector plugin.
2. Login to your WordPress administration and click **Plugins**.
3. Click **Add New**.
4. Click **Upload plugin**, browse, and select the plugin zip file that you downloaded in step 1 above.
5. Click **Install now**.
6. After the installation is complete, click **Activate Plugin**.

You have now successfully installed the Make Connector plugin.

### Obtain your API key in WordPress

To obtain your API key from your WordPress account:

1. Log in to your WordPress account.
2. Open the Make Connector plugin, copy the provided **API key**, and store it in a safe place.

You will use this value in the API Key field in Make.

### Establish the connection with WordPress in Make.

To establish the connection in Make:

1. Log in to your Make account, add a WordPress module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. In the **WordPress REST API base url** field, enter the REST API base URL of your WordPress site. For example, `https://my-wordpress-site.com/wp-json`
4. In the **API Key** field, enter the API key copied above.
5. Click **Save**.
6. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more WordPress modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build WordPress Scenarios
-------------------------

After connecting the app, you can perform the following actions:

Posts* Watch Posts
* Watch Posts Updated
* Create a Post
* Update a Post
* Delete a Post
* Get a Post
* Search Posts
Categories* Watch Categories
* Create a Category
* Update a Category
* Delete a Category
* Get a Category
* Search Categories
Comments* Watch Comments
* Create a Comment
* Update a Comment
* Delete a Comment
* Get a Comment
* Search Comments
Media Items* Watch Media Items
* Create a Media Item
* Update a Media Item
* Delete a Media Item
* Get a Media Item
* Search Media Items
Users* Watch Users
* Create a User
* Update a User
* Delete a User
* Get a User
* Search Users
Tags* Watch Tags
* Create a Tag
* Update a Tag
* Delete a Tag
* Get a Tag
* Search Tags
Taxonomies* Search for Specific Taxonomies
Other* Make an API Call
[Custom Fields
-------------](#custom-fields-968742_body)To work with custom fields you want to include in your module output, you need to activate the desired fields in the Make Connector plugin.

1. Ensure that the [Make Connector plugin is installed](wordpress.html#install-the-make-connector-plugin-in-wordpress "Install the Make Connector plugin in WordPress").
2. Click **Make (Integromat) > Custom API Fields**.

![61d6be70b20f2.gif](./../image/uuid-1a1983cc-e92c-a179-81cd-1ae3ce3967bc.gif)
3. Select the desired custom fields you want to include in the module output.
4. Click **Save Settings**.

The selected custom fields are now available in the module output.

