Instagram for Business
======================

With Instagram for Business modules in Make, you can manage the events, insights, media, users, comments, and stories in your Instagram for Business account.

To use the Instagram for Business modules, you must have a Facebook account that can perform admin-equivalent [tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) on a Facebook page that has been [connected to the Instagram account](https://developers.facebook.com/docs/instagram-api/overview#pages) you want to access and an Instagram Business account. You can create an Instagram account on [instagram.com](https://www.instagram.com), and then switch the profile to a Business account. Please refer to the [Set Up a Business Account on Instagram](https://help.instagram.com/502981923235522/robots.txt) guide.

Refer to the [Instagram for Business API documentation](https://developers.facebook.com/docs/instagram-api) for a list of available endpoints.

Connect Instagram for Business to Make
--------------------------------------

To establish the connection in Make:

1. Log in to your Make account, add an Instagram for Business module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show advanced settings** and enter your custom app client credentials. For more information, refer to the [Meta for Developers Long-Lived Access Token documentation](https://developers.facebook.com/docs/instagram-basic-display-api/guides/long-lived-access-tokens).

If requested, use the following Redirect URI when creating your custom app: `https://www.integromat.com/oauth/cb/facebook`.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Instagram for Business modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build Instagram for Business Scenarios
--------------------------------------

After connecting the app, you can perform the following actions:

Event* Watch Events
Insights* Get User Insights
* Get Media Insights

Insights data is unavailable to Instagram users with fewer than 100 followers.
Media* Watch Media
* Watch Public User Media
* Create a Photo Post

Instagram Business accounts connected to a Page that requires [Page Publishing Authorization (PPA)](https://www.facebook.com/business/tools/ads-manager) cannot be published until PPA has been completed.

Photos must be hosted on a publicly accessible URL and you cannot host your videos on Google Drive even if the file is shared publicly because Instagram API is not able to download files from Google Drive. The same applies to Dropbox URLs.

The username should not start with `@`, it must match the pattern `/^(?!@)/` .
* Create a Reel Post

Instagram Business accounts connected to a Page that requires [Page Publishing Authorization (PPA)](https://www.facebook.com/business/tools/ads-manager) cannot be published until PPA has been completed.

Photos or videos must be hosted on a publicly accessible URL and you cannot host your videos on Google Drive even if the file is shared publicly because Instagram API is not able to download files from Google Drive. The same applies to Dropbox URLs.

The username should not start with `@`, it must match the pattern `/^(?!@)/` .
* Create a Carousel Post

Instagram Business accounts connected to a Page that requires [Page Publishing Authorization (PPA)](https://www.facebook.com/business/tools/ads-manager) cannot be published until PPA has been completed.

Photos or videos must be hosted on a publicly accessible URL and you cannot host your videos on Google Drive even if the file is shared publicly because Instagram API is not able to download files from Google Drive. The same applies to Dropbox URLs.

The username should not start with `@`, it must match the pattern `/^(?!@)/` .
* List Media
* List Public User Media
* Get Media
* Download a Media
* Get Album Media
Users* Get Public User Info
Comments* List Media Comments
* List Comment Replies
* Create a Comment
* Create a Reply
Stories* List Stories
### Note

This app uses [webhooks](./../tools/webhooks.html "Webhooks") to trigger a scenario when an event occurs instantly. All webhook modules have an `instant` tag next to their name.

When you create an Instagram for Business webhook in Make, it is attached automatically and requires no additional set up.

