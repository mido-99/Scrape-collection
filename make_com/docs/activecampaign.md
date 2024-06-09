ActiveCampaign
==============

With Active Campaign modules in Make, you can manage the contacts, deals, campaigns, task, notes, events, automations, messages, calendar feeds, and accounts in your ActiveCampaign account.

To use the ActiveCampaign modules, you must have a paid account. For subscription information, refer to the [ActiveCampaign Pricing page](https://www.activecampaign.com/pricing).

Refer to the [ActiveCampaign API documentation](https://developers.activecampaign.com/reference/overview) for a list of available endpoints.

Connect ActiveCampaign to Make
------------------------------

To establish the connection, you must:

1. Obtain your API URL and API key in ActiveCampaign.
2. Establish the connection in Make.
### Obtain your API credentials in ActiveCampaign

To obtain your API key from your ActiveCampaign account:

1. Log in to your ActiveCampaign account.
2. In the left sidebar, click **Settings > Developer**.
3. Under **API Access**, copy the **API URL** and the **API key** value shown and store it in a safe place.

You will use these values in the **API Key** , **Account Name**, and **Domain** fields in Make.

### Establish the connection with ActiveCampaign in Make

To establish the connection in Make:

1. Log in to your Make account, add an ActiveCampaign module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. In the **API Key** field, enter the API key copied in the section above.
4. In the **Account Name** field, enter the account name. You can find it in the **API URL** copied in the section above. The account name goes before the domain: `your_account_name.api-us1.com`.
5. In the **Domain** dropdown list, select or enter the domain indicated in your **API URL**.
6. Click **Save**.
7. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more ActiveCampaign modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build ActiveCampaign Scenarios
------------------------------

After connecting the app, you can perform the following actions:

**Contacts**

* Create a Contact
* Create/Update a Contact
* Delete a Contact
* Get a Contact
* Create/Update a Contact's Custom Field Value
* Update Contact's List Status
* Add a Tag to a Contact
* Remove a Tag from a Contact
* List Contacts
* Get Current User
**Deals**

* Create a Deal
* Update a Deal
* Get a Deal
* Delete a Deal
* Move Deals to Another Deal Stage
* List Deals
**Campaigns**

* Get a Campaign
* List Campaigns
**Tasks**

* Create/Update a Task
* Delete a Task
**Notes**

* Create a Note
* Create a Deal Note
**Events**

* Create a New Event
* Enable/Disable Event Tracking
**Automations**

* List Automations
* Add a Contact to an Automation
* Get an Automation a Contact Is in
* Remove a Contact from an Automation
* List All Automations a Contact Is in
**Messages**

* Create a Message
**Calendar Feeds**

* Create/Update a Calendar Feed
* Delete a Calendar Feed
**Accounts**

* Create an Account
* Get an Account
* Delete an Account
* List Accounts
**Other**

* List Organizations
* Make an API Call
* Make a Legacy API Call
### Note

This app uses [webhooks](./../tools/webhooks.html "Webhooks") to trigger a scenario when an event occurs instantly. All webhook modules have an `instant` tag next to their name.

When you create an ActiveCampaign webhook in Make, it is attached automatically. Select events and source that you want to trigger your scenario.

