HubSpot CRM
===========

With HubSpot CRM modules in Make, you can manage the events, records, contacts, engagements, files, and form submissions in your HubSpot CRM account.

To use the HubSpot CRM modules, you must have a HubSpot CRM user account. You can create a user account at [https://app.hubspot.com/signup-hubspot](https://app.hubspot.com/signup-hubspot/).

To use HubSpot CRM webhooks and a few other features, you must have a HubSpot CRM developer account. You can create a developer account at <https://app.hubspot.com/signup-hubspot/developers>.

Refer to the [HubSpot API Documentation](https://developers.hubspot.com/docs/api/overview) for a list of available endpoints.

Connect Hubspot CRM to Make
---------------------------

To establish the connection in Make:

1. Log in to your Make account, add a Hubspot CRM module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**. You will need to have a developer account and use advanced settings for this feature. For more information, see [Connect Hubspot CRM to Make using advanced settings](hubspot-crm.html#connect-hubspot-crm-to-make-using-advanced-settings "Connect Hubspot CRM to Make using advanced settings") below.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Click **Save**.
4. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Hubspot CRM modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[Connect Hubspot CRM to Make using advanced settings
---------------------------------------------------](#connect-hubspot-crm-to-make-using-advanced-settings_body)The following modules require a [Hubspot CRM developer account](https://developers.hubspot.com/get-started) and a connection using advanced settings:

* Watch Notifications (uses a webhook)
* Create a Timeline Event
* List Timeline Event Templates
To establish the connection using advanced settings, you must:

1. [Create a Hubspot CRM custom application.](hubspot-crm.html#create-a-hubspot-crm-custom-application "Create a Hubspot CRM custom application")
2. [Obtain your Hubspot CRM developer API key and User ID.](hubspot-crm.html#obtain-your-hubspot-crm-developer-api-key-and-user-id "Obtain your Hubspot CRM developer API key and User ID")
3. [Establish an OAuth connection between Hubspot CRM and Make .](hubspot-crm.html#establish-an-oauth-connection-between-hubspot-crm-and-make "Establish an OAuth connection between Hubspot CRM and Make")
### Create a Hubspot CRM custom application

To create a custom application:

1. Log in to your [HubSpot developer account](https://developers.hubspot.com/).
2. If you do not have any existing apps, click on **Create an app** . If you have existing apps, click on **Manage apps** > **Create app**.
3. In the **App Info** tab, enter the following details:



| **Public app name** | Enter the app name. |
| --- | --- |
| **App logo (Optional)** | Click the **Upload** button to add an image. |
| **Description (Optional)** | Enter the app details. |
4. In the **Auth** tab, enter the following details:



| **Install URL (OAuth)** | Leave this field blank. |
| --- | --- |
| **Redirect URLs** | Enter `https://www.make.com/oauth/cb/hubspotcrm` |
| **Scopes** | This is only required if you are using the Watch Notifications module, as this module requires a webhook.Add required scopes based on the subscriptions you will watch for. Refer to the [Required Permissions for Hubspot CRM Webhooks](hubspot-crm.html#required-permissions-for-hubspot-crm-webhooks "Required Permissions for HubSpot CRM Webhooks") **Custom App Scopes** column for the required scopes to include.If you are not using a webhook module, you can leave this section blank. |
5. Click **Save changes**.
6. Scroll up to the **App credentials** section, copy the **Client ID** and **Client Secret** values, and store them in a safe place.

![msedge_6q09tj1HZW.png](./../image/uuid-a3803a41-9484-3783-2a5c-f58572995811.png)

You now have the client credentials to use when creating your OAuth connection in Make .

### Note

Each HubSpot CRM Custom Application can only be associated with one webhook URL. To watch for multiple events (subscriptions), add all desired subscriptions when configuring the module in Make.

Refer to your HubSpot CRM subscription for information regarding how many Custom Applications you can create.

### Obtain your Hubspot CRM developer API key and User ID

To obtain your API key and User ID:

1. In your [HubSpot developer](https://developers.hubspot.com/) account, click on the **Apps** tab in the top menu.
2. Click **Get HubSpot API key**.
3. If you have an existing API key, click **Show key** and copy the key value. If you do not have an existing key, click the **Create key** button and copy the key value. Store it in a safe place.
4. Copy your **User ID** and store it in a safe place.

You now have the **API key** and **User ID** values to use when creating your webhook's OAuth connection in Make .

### Establish an OAuth connection between Hubspot CRM and Make

To establish your OAuth connection:

1. Log in to your Make account, add a Hubspot CRM module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Click **Show advanced settings**.
4. In the **HubSpot Developer API Key** and **User ID** fields, enter the values you saved in [Obtain your Hubspot CRM developer API key and User ID](hubspot-crm.html#obtain-your-hubspot-crm-developer-api-key-and-user-id "Obtain your Hubspot CRM developer API key and User ID") above.
5. In the **Client ID** and **Client Secret** fields, enter the client credentials you a saved in [Create a Hubspot CRM custom application](hubspot-crm.html#create-a-hubspot-crm-custom-application "Create a Hubspot CRM custom application") above.
6. Click **Save**.
7. If prompted, authenticate your account and confirm access.
8. Select the associated user account to connect to and click **Choose Account**.
9. Confirm access by clicking **Connect app**.
10. If you are using a webhook module, in the **Subscriptions** field of the module, add or map the **Subscription Type** to watch for.

Note: Make sure you add all desired subscriptions (and their scopes) as this field cannot be updated at a later time.
11. Click **Save**.

You have successfully established the connection. You can now edit your scenario and add more HubSpot CRM modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[### Required Permissions for HubSpot CRM Webhooks](#required-permissions-for-hubspot-crm-webhooks_body)When using the **Watch Notifications**`instant` module, the following permissions must be added as HubSpot CRM custom app **Scopes** and OAuth connection **Custom Scopes**.



| **Subscription** | **Custom App Scopes** | **Connection Custom Scopes** |
| --- | --- | --- |
| Company - created | `crm.objects.companies` Read | CRM Companies Read |
| Company - deleted | `crm.objects.companies` Read | CRM Companies Read |
| Company - specified property is changed | `crm.objects.companies` Read | CRM Companies Read |
| Contact - created | `crm.objects.contacts` Read | CRM Contacts Read |
| Contact - deleted | `crm.objects.contacts` Read | CRM Contacts Read |
| Contact - deleted for privacy compliance reasons | `crm.objects.contacts` Read | CRM Contacts Read |
| Contact - specified property is changed | `crm.objects.contacts` Read | CRM Contacts Read |
| Deal - created | `crm.objects.deals` Read | CRM Deals Read |
| Deal - deleted | `crm.objects.deals` Read | CRM Deals Read |
| Deal - specified property is changed | `crm.objects.deals` Read | CRM Deals Read |

For permission information regarding additional subscriptions, refer to the [HubSpot Developer Webhook subscriptions documentation](https://developers.hubspot.com/docs/api/webhooks#webhook-subscriptions).

### Legacy API

If you are using the legacy version of HubSpot, refer to the [HubSpot Legacy Docs Webhooks documentation](https://legacydocs.hubspot.com/docs/methods/webhooks/webhooks-overview) for permission information.

HubSpot CRM Video Tutorial
--------------------------

This tutorial explains how to build a scenario that grabs new contacts from HubSpot CRM, inserts their information into a Google Docs Template, uploads the compiled document to Dropbox, and sends it via Gmail.

Build Hubspot CRM Scenarios
---------------------------

After connecting the app, you can perform the following actions:

CRM Objects* Watch CRM Objects
* Search for CRM Objects
Records (Deals, Contacts, Companies)* Get a Record Property
Custom Objects* Create a Custom Object Record
* Get a Custom Object Record
* Update a Custom Object Record
* Delete a Custom Object Record
Contacts* Watch Contacts Added to a List
* Watch Contacts
* Add Contacts to a List
* Remove a Contact from a List
* List Contacts
* Create a Contact
* Update a Contact
* Get a Contact
* Search for Contacts
* Merge Contacts
* Delete a Contact
Deals* Watch Deals
* Create a Deal
* Update a Deal
* Get a Deal
* List Deal/Ticket Pipelines
* Search for Deals
* Delete a Deal
Companies* Watch Companies
* Create a Company
* Update a Company
* Get a Company
* Search for Companies
* Delete a Company
Engagements* Watch Engagements
* Create an Engagement
* Delete an Engagement
Events and NotificationsThese modules require a [Hubspot CRM developer account](https://developers.hubspot.com/get-started) and a [connection using advanced settings](hubspot-crm.html#connect-hubspot-crm-to-make-using-advanced-settings "Connect Hubspot CRM to Make using advanced settings").

* Watch Notifications
* Create a Timeline Event
* List Timeline Event Templates
Files* Watch Files
* Create a Folder
* List Files
* Upload a File
* Update File Properties
* Delete a File
* Delete a Folder
Users* Get an Owner
* List Owners
Tickets* Watch Tickets
* Create a Ticket
* Update a Ticket
* Get a Ticket
* Search for Tickets
* Delete a Ticket
Forms* Watch Submissions for a Form
* Get a File Uploaded via Form
* List Forms
* Submit Data to a Form
Workflows* Add a Contact to a Workflow
* Remove a Contact from a Workflow
SubscriptionsNote: You cannot subscribe a contact to an email address that is already subscribed.

* Watch Subscriptions Timeline for a Portal
* Subscribe Contact
* Unsubscribe a Contact
Associations* Create an Association
* List Associations
* Delete an Association
Other* Make an API Call
### Numeric Value Character Limit

HubSpot imposes a 18 digit character limit for numeric values and automatically truncates values that exceed the limit. For example, when you filter by a custom field with more than 18 digits, the API will automatically truncate the number to 18 digits.

[Disconnect Make from HubSpot CRM
--------------------------------](#disconnect-make-from-hubspot-crm_body)To disconnect the Make app from your HubSpot CRM account:

1. Log in to your [HubSpot account](https://app.hubspot.com/signup-hubspot/developers?step=landing_page).
2. Go to the [App Marketplace](https://ecosystem.hubspot.com/marketplace/apps) and click Manage Apps.



| msedge_l7k6OsRWQy.png |
| --- |
3. Under the **Connected apps** section, in the app you want to disconnect, click **Actions > Uninstall**.



| msedge_ud9oqiNHZD.png |
| --- |

The app has been disconnected.

