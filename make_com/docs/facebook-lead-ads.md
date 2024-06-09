Facebook Lead Ads
=================

With Facebook Lead Ads modules in Make, you can monitor leads and retrieve lead and form data from your Facebook Lead Ads account.

To use the Facebook Lead Ads modules, you must have a Facebook and a Facebook Business Manager account. You can create accounts at [facebook.com](https://www.facebook.com/) and [business.facebok.com](https://business.facebook.com/).

Connect Facebook Lead Ads to Make
---------------------------------

To establish the connection, you must:

1. [Establish the connection with Facebook Lead Ads to Make.](facebook-lead-ads.html#establish-the-connection-with-facebook-lead-ads-to-make "Establish the connection with Facebook Lead Ads to Make")
2. [Assign Make access in Facebook Business Manager](facebook-lead-ads.html#assign-make-access-in-facebook-business-manager "Assign Make access in Facebook Business Manager")
### Note

See our instructional video [FB Lead manual and troubleshooting](https://www.loom.com/share/0650f4fdc81146e78433aee47daa1b4a).

### Establish the connection with Facebook Lead Ads to Make

To establish the connection in Make:

1. Log in to your Make account, add a Facebook Lead Ads module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show advanced settings** and enter your custom app client credentials. For more information, refer to the [Facebook Authentication Guide](https://developers.facebook.com/docs/marketing-api/overview/authorization).

If requested, use the following Redirect URI when creating your custom app: `https://www.integromat.com/oauth/cb/facebook`.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Facebook Lead Ads modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

### Assign Make access in Facebook Business Manager

To grant Make access in Facebook Business Manager:

1. Log in to your [Facebook Business Manager](https://business.facebook.com/) account.
2. In the left sidebar, click **Settings**.
3. Go to **Integrations** > **Leads Access**.
4. Go to **CRMs,** click **Assign CRMs**, and select **Make** by clicking the checkbox.
5. Click **Assign**.
Build Facebook Lead Ads Scenarios
---------------------------------

### Note

You can start with a prebuilt template or build your scenario from scratch. You can find a template for a scenario using Facebook Lead Ads and Google Sheets [here](https://www.make.com/en/integrations/facebook-lead-ads/google-sheets).

After connecting the app, you can perform the following actions:

Leads* New Lead

### Note

You can use the [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing/) to test your **New Lead** module and see if it is receiving the form.
* Watch Leads
* Get Lead Details

Note: The form you want to retrieve the data from has to have been submitted at least once before, otherwise the form won't load in the Make module.
Utility* Get a Form
* Unsubscribe a Webhook

Note: Deleting a scenario will not automatically unsubscribe your Facebook Page from receiving event notifications from Facebook.
Other* List Leads
### Note

This app uses [webhooks](./../tools/webhooks.html "Webhooks") to trigger a scenario when an event occurs instantly. All webhook modules have an `instant` tag next to their name.

When you create a Facebook Lead Ads webhook in Make, it is attached automatically and requires no additional set up.

Troubleshooting
---------------

[### The New Lead module does not trigger](#the-new-lead-module-does-not-trigger_body)If the module does not trigger when the data has been sent to it, try the following steps:

1. Open your Facebook settings > [Business Integrations](https://www.facebook.com/settings?tab=business_tools&ref=settings), and remove the Make app.



| 61d5b22e5686b.gif |
| --- |
2. Go to Make, and remove the connection you use for the Facebook Lead Ads trigger from Make.

![61d5b230ddb58.png](./../image/uuid-3912abc1-1440-7825-38cc-c8bd4f0c08e5.png)
3. Create the connection again by following the steps in the [Establish the connection with Facebook Lead Ads to](urn:resource:component:2273772/section-idm4550942675556834130435842516) Make[.](urn:resource:component:2273772/section-idm4550942675556834130435842516) section.
4. Go to the [People Business Settings](https://business.facebook.com/settings/people/) if you are an individual, or to the [Partner Business Settings](https://business.facebook.com/settings/partners/) if you are a partner.
5. Select Make (in case of **Partner** settings), or your name (in case of **People** settings), and enable the following permissions:


	* **Manage Page** permission for the **Pages** asset.
	
	
	
	| 61d5b23214dc8.png |
	| --- |
	* **Manage Ad Account** for the **Ad Accounts** asset.
	
	
	
	| 61d5b233b798b.png |
	| --- |
6. Navigate to **Integrations** > **Leads Access,** and check that Make (for **Partners**) or you (for **People**) have access to your page.



| 61d5b235b4131.png |
| --- |
### Note

If you have tried all the steps we mentioned and you are still having trouble, it might be because of a problem with the Meta API. The best thing to do now is to get in touch with the Meta support team. They can offer further assistance and also give you the logs for the outgoing requests you made.

As an alternative, instead of using the New Lead module to retrieve all the leads instantly, you can use the Watch Leads module. It is important to note that the Watch Leads module requires scheduling and cannot be executed instantly.

[### The Make dropdown doesn't show some Facebook pages:](#the-make-dropdown-doesn-t-show-some-facebook-pages--964482_body)If some of your pages are not available in the Make modules, please follow the steps below:

1. Open the Facebook **Settings,** and click on **Business Integrations**, or use this link: <https://www.facebook.com/settings?tab=business_tools>
2. Open the Make app.



| 61d5b210ebcaa.png |
| --- |
3. Check off all of the pages you want to see in the Make modules



| 61d5b212e43b2.png |
| --- |
4. Save the changes by clicking the **Save** button.
[### The Scenario does not start after submitting a form](#the-scenario-does-not-start-after-submitting-a-form_body)1. Check whether the Make app is subscribed to your page by checking the [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing/). Once the webhook is correctly connected to If you still see an issue, open the Business Manager, and assign access to Makeyour page, you should see the WEBHOOK SUBSCRIPTION FOR THE SELECTED PAGE area as shown in the picture below:

![inline1295385969.png](./../image/uuid-76e37042-1018-b598-1061-79c21500aa2c.png)
2. If your scenario is set up correctly but does not start after submitting a form, please check in the Facebook Business manager to make sure that Make has access to your page.

To do so, click on the [Leads Access](https://business.facebook.com/settings/leads-accesses) tab, select a page, and click on the CRM to assign access for Make (if it is not already allowed).

If you still see an issue, open the Business Manager, and assign access to Make:



| mceclip0.png |
| --- |

If none of this works, please try to add a new Facebook connection, and follow the same steps.
[### 400: GraphMethodException (100): Unsupported get request.](#400--graphmethodexception--100---unsupported-get-request-_body)This error may occur for some users:

![61d5b23b6b5e3.png](./../image/uuid-7822a04b-1905-7e88-2366-b7c1dbbc2d83.png)Please use the Ignore error handler option (under advanced settings) to fix this error.



| facebook_lead_ads_1.gif |
| --- |

For example, when we collect the ad and Campaign ID instead of the module throwing an error and stopping the scenario the ignore error handler will take care of it.

Check the **Leads Access settings**. By default, all page admins have access to leads, but if a client specified users, to have access, and did not add your system user, you'll get this error. It can be accessed through **Business Settings > Integrations > Leads Access** and choose **People**, **CRM**, or **Partners** depending on your level of access. For more information, refer to [Facebook Support](https://developers.facebook.com/support/bugs/668040450371566) page.

### Note

If this page admin never customized leads, nor given access permission with the Leads Access Manager, then **ALL** page admins will have leads access permission.

If leads access permission is customized by business admins, then it depends on the business admin's configuration, whether a page basic admin has leads access permission or not. For more information, refer to [Facebook Lead Ads Support](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving/) page.

In this case, the user having a page admin role does not necessarily mean having leads access if there are business admins managing the page. So, the business admin will have to assign the lead asset to the page admin in the **Facebook Business Settings**.

If changing the relevant settings does not resolve the error, you need to reach out to Meta for further support. You can use our [DevTool](http://www.make.com/en/help/scenarios/integromat-devtool) to get additional information about the failed request and forward those logs to the Meta team.

[### OAuthException (200)](#oauthexception--200-_body)![61d5b23fb82da.png](./../image/uuid-4ab73e08-47da-ae28-54df-4d7a01f5b329.png)You may see this error message if your role on the page is **Advertiser or Analyst.** 

To solve this issue and use the module, you must be an **Admin, Moderator, or Editor** of the page from which you are trying to get leads ads.

