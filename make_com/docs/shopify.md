Shopify
=======

With Shopify modules in Make, you can manage the orders, products, product variants, product images, collects, custom collections, customers, articles, pages, refunds, fulfillments, fulfillment orders, fulfillment services, inventories, abandoned checkouts, transations, discounts, metafields, payments, and themes in your Shopify account.

To use the Shopify modules, you must have a Shopify account. You can create an account at [www.shopify.com/signup](https://www.shopify.com/signup).

Refer to the [Shopify API documentation](https://shopify.dev/docs/api/admin-rest) for a list of available endpoints.

Connecting Shopify to Make
--------------------------

Shopify offers two types of connections:

* [Standard OAuth connection (displayed as **Shopify** in the Create connection dialog) - use this by default](shopify.html#UUID-cf3ac83e-b8e5-03fd-7f7e-196bf4c34ff5_procedure-idm4577201683660833194210367188 "Connecting Shopify using the standard connection type")
* [Custom app (displayed as **Shopify (custom or private apps)**) - use this if the standard connection does not work](shopify.html#UUID-cf3ac83e-b8e5-03fd-7f7e-196bf4c34ff5_procedure-idm4577202046072033194232012212 "Connecting Shopify using a Shopify private or custom app")
To connect your Shopify account to Make, follow these steps:

Connecting Shopify using the standard connection typeUse the Shopify connection type by default. If creating the connection causes errors, use the custom or private app connection type.

1. Insert a Shopify module into a scenario. Under Connection, click **Add**.


	* The Create a Connection dialog appears.
	
	![61d6b0ba0e363.png](./../image/uuid-92350fa7-763a-9d59-110c-c711de085b20.png)
2. In the **Connection type**, select **Shopify**.
3. Type a **Connection name**.
4. Enter the **Myshopify.com subdomain** of your store.


	* For example, if the URL of your store is `https://mystore.myshopify.com`, the subdomain to enter in the connection dialog is `mystore`.
5. Click **Save**.


	* The system opens Shopify in a new window. Shopify asks you to log in and install the Make app and approve its access to your store data.
6. In the Shopify **Install** dialog, review the privacy and permissions details, and then click **Install unlisted app**.

![61d6b0bb34b8f.png](./../image/uuid-310a2cd8-80ab-efd1-a7a0-459e2ab1d46f.png)
Connecting Shopify using a Shopify private or custom appUse the **Shopify (custom or private app)** connection type if the standard Shopify connection type does not work for you.

This connection type requires creating a custom app in your Shopify store.

1. Log in to your Shopify store, click **Apps**, then click **App and sales channel settings**.

![shopify_app_settings.png](./../image/uuid-61eda1b3-c193-0e7d-96b9-2aa34855c961.png)
2. On the **Apps and channels** screen, click **Develop apps**.

![shopify_develop_apps.png](./../image/uuid-3324b5e9-9b61-c64e-10d2-53efda42f0b6.png)
3. Click **Allow custom app development**, then confirm this action again by clicking **Allow custom app development** on the next screen.


	* This will allow you to create an API token that you will use when creating the connection in Make.
4. Click **Create an app**.
5. Type an **App name**, select an **App developer**, and click **Create app**.
6. Click **Configuration**, then click **Configure** next to **Admin API integration**.

![shopify_app_configuration_api.png](./../image/uuid-8da2034d-1dfd-0763-7713-ca3bda03bf64.png)
7. On the Admin API integration screen, select scopes (permissions) that represent the actions you will need Make to perform. Then click **Save**.
8. Switch to the **API credentials** tab and under **Access tokens**, click **Install app**. In the dialog that appears, confirm the action by clicking **Install app**.


	* Shopify creates an Admin API access token. Click **Reveal token once** and copy the token. You will enter this token into Make in the next step.![shopify_reveal_token.png](./../image/uuid-faaabfc1-143f-2aa5-e4ac-63352d4d3d22.png)
9. In Make, add a Shopify module to a scenario. Under **Connection**, click **Add**, then fill in the required details shown in the following image.

![shopify_connection_custom.png](./../image/uuid-79999624-b18f-6cfd-c562-c5fe64dade3a.png)
10. Click **Save**.
[Public App Connection
---------------------](#public-app-connection_body)Use this to connect your Public App created in your [Partner Dashboard](https://partners.shopify.com/organizations).

To create an app:

1. From your Partner Dashboard, click *Apps* > *Create* app.
2. Provide an app name, URL, and Redirect URLs.
3. Click **Create app**. You are directed to your app's overview page, where you can view the API key and API secret that you will need for the module's connection configuration.


| **Connection Type** | `Shopify (public apps)`. |
| --- | --- |
| **Connection name** | Enter the name of the connection. |
| **Domain** | Enter the name of your Shopify domain. If your Shopify store address is https://*mystore*.myshopify.com, enter "*mystore*". |
| **Client ID** | Enter the API key for the app, as defined in the Partner Dashboard. |
| **Client Secret** | Enter the API secret key for the app, as defined in the Partner Dashboard. |
| **Scope** | Specify needed scopes. If you requested both the read and write access scopes for a resource, then enter only for the write access scope. The read access scope is omitted because it’s implied by the write access scope. For example, if your request included `scope=read_orders,write_orders`, then check only for the `write_orders` scope.See the [list of admin scopes](https://shopify.dev/docs/admin-api/access-scopes). |

[Private App Connection
----------------------](#private-app-connection_body)To establish a private app connection, you need to create a private app to obtain the *API Key* and *Password*.

1. Log in to your Shopify administration (`https://{yourShopifyDomain}.myshopify.com/admin`).

2. Navigate to **Apps** > **Manage private apps**.

![61d6b0c7a680d.gif](./../image/uuid-dabcae40-88eb-c4a1-46eb-5b0b03437b6d.gif)3. Click the **Create new private app** button (![61d6b0ca33a38.png](./../image/uuid-8bcc758b-6ebf-adf3-a613-a1d1a65c0030.png)).

4. Fill in the required fields, click **Save**, and **Create App**.

![61d6b0cb6fd7b.gif](./../image/uuid-93fcc0e0-ff80-85cb-0738-55ad6fbc4ef5.gif)5. Find the generated **API Key** and **Password** in the Admin API section.

![61d6b0cf6eeb4.png](./../image/uuid-5767ac98-bd17-7da2-1c33-a78366a4ed0a.png)6. Go to **Make,** and open the **Make an API Call** module's **Create a Connection** dialog for the Shopify private app.

7. Enter the *Domain* (if your Shopify online store address is, for example, *xyz*.myshopify.com, enter only "*xyz*".) and *API Key* and *Password* provided in step 5 to the respective fields, and click the *Continue* button to establish the connection.

The connection has been established. You can set up the private app's **Make an API Call** module.

Build Shopify Scenarios
-----------------------

After connecting the app, you can perform the following actions:

Orders* Create an Order
* Create a Draft Order

Note: In the output, the Shipping Line field is sometimes empty because the user must have at least one item in the item list that requires shipping.

If not specified, the item is treated as not requiring shipping, and Shopify ignores Shipping Lines.
* Import a B2B Order

Only available for stores on the Shopify Plus plan.
* Update an Order
* Delete an Order
* Close an Order
* Reopen an Order
* Cancel an Order
* Get an Order
* Count Orders
* Search for Orders
* Watch Orders
* Search for Risks
Products* Create a Product
* Update a Product
* Delete a Product
* Get a Product
* Search for Products
* Watch Products
Product Variants* Create a Product Variant
* Update a Product Variant
* Delete a Product Variant
* List Product Variant
* Get a Product Variant
Product Images* Upload a Product Image
* Delete a Product Image
* List Product Images
Collects* Create a Collect
* Delete a Collect
* Search for Collects
* Get a Collect
Custom Collections* Search for Custom Collections
* Create a Custom Collection
* Get a Custom Collection
* Update a Custom Collection
* Delete a Custom Collection
Customers* Create a Customer
* Update a Customer
* Delete a Customer
* Get a Customer
* Search for Customers
* Watch Customers
* List Customer Addresses
* Send an Invitation
Articles* Create an Article
* Update an Article
* Delete an Article
* Get an Article
* Search for Articles
* Watch Articles
Pages* Create a Page
* Update a Page
* Delete a Page
* Get a Page
* Search for Pages
* Watch Pages
Refunds* Get a Refund
* Search for Refunds
Fulfillments* List Fulfillments for a Fulfillment Order
* Create a Fulfillment for Fulfillment Orders

Note: Before you create a fulfillment, get to know some concepts related to Fulfillments:


	+ [Order](https://help.shopify.com/en/api/reference/orders/order)
	+ [Location](https://help.shopify.com/en/api/reference/inventory/location)
	+ [Fulfillment](https://help.shopify.com/api/reference/shipping_and_fulfillment/fulfillment)
	+ [FulfillmentService](https://help.shopify.com/api/reference/shipping_and_fulfillment/fulfillmentservice)
* Update a Fulfillment Tracking
* Search for Fulfillments
* Get a Fulfillment
* Create a Fulfillment Event
Fulfillment Order* Search Assigned Fulfillment Orders
* List Fulfillment Orders
* Get a Fulfillment Order
* Cancel a Fulfillment Order
* Hold a Fulfillment Order
* Release a Fulfillment Order Hold
* Relocate a Fulfillment Order
* Send a Fulfillment Request
* Send a Cancellation Request
Fulfillment Service* Create a Fulfillment Service
* Update a Fulfillment Service
* Delete a Fulfillment Service
* Accept a Fulfillment Request
* Reject a Fulfillment Request
* Accept a Cancellation Request
* Reject a Cancellation Request
* Close a Fulfillment Order
Inventory* Search for Inventory Levels
* Adjust an Inventory Level
* Update an Inventory Level
* Connect an Inventory Item
* Delete an Inventory Level
* Search for Inventory Items
* Update an Inventory Item
Abandoned Checkouts* Search for Abandoned Checkouts
* Watch Abandoned Checkouts
Transactions* Create a Transaction
* Search for Transactions
Discounts* Search for Discount Codes
* Create a Discount Code
* Update a Discount Code
* Delete a Discount Code
* Create a Price Rule
Metafields* Search for Metafields
* Get a Metafield
* Create a Metafield
* Update a Metafield
* Delete a Metafield
Payments* Search for Disputes
* Search for Payouts
Themes* List Assets
* Create or Update an Asset
* Get an Asset
* Delete an Asset
Other* Make an API Call
* Make a GraphQL API Call
* New Event
### Note

This app uses webhooks to trigger a scenario when an event occurs instantly. All webhook modules have an instant tag next to their name.

When you create a Shopify webhook in Make, it is attached automatically and requires no additional set up.

Common Issues
-------------

### Errors: [API] This action requires merchant approval for <XXXX\_XXXX> scope

You need to create a new connection with a [required scope](https://shopify.dev/api/usage/access-scopes).

Unfortunately, when you create a new connection, all previously used scopes are removed from your account, and only scopes added in the latest connection are used for all your connections (including the previously created connections).

Include **all** needed scopes in the new connection.

