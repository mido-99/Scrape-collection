Google Forms
============

With Google Forms modules in Make, you can search, create, retrieve, and update forms and move forms to trash, watch, list, and retrieve responses, and watch, search, add, update, and delete responses in Google Forms.

To use the Google Forms modules, you must have a Google account. You can create an account at [docs.google.com/forms/](http://docs.google.com/forms/).

To upgrade to a new version of the Google Forms app, you need to upgrade all modules manually by [Replacing Legacy Modules with New Modules](https://www.integromat.com/en/help/replacing-legacy-modules-with-new-modules).

Refer to the [Google Forms API Documentation](https://developers.google.com/forms/api/reference/rest) for a list of available endpoints.

### Note

Make's use and transfer of information received from Google APIs to any other app will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

Connect Google Forms to Make
----------------------------

To establish the connection in Make:

1. Log in to your Make account, add a Google Forms module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Switch on the **Show advanced settings** toggle and enter your Google Cloud Console project client credentials. For more information, see the [Create and configure a Google Cloud Console project for Google Forms section](google-forms.html#create-a-google-cloud-console-project-for-google-forms "Create a Google Cloud Console project for Google Forms") below.
4. Click the **Sign in with Google**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Google Form modules. If your connection needs reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[### Create and configure a Google Cloud Console project for Google Forms](#create-and-configure-a-google-cloud-console-project-for-google-forms_body)To connect to Make using your own client credentials, you can create and configure a project in the Google Cloud Console.

#### Create a Google Cloud Console project for Google Forms

To create a Google Cloud Console project:

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. In the top menu, click **Select a project** > **New project**.
3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.
#### Enable APIs for Google Forms

To enable the required APIs:

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for and enable the following APIs: **Google Resource Manager API** and **Google Drive API**.
#### Configure your OAuth consent screen for Google Forms

To configure your OAuth consent screen:

1. In the left sidebar, click **OAuth consent screen**.
2. Under **User Type**, select **External**.

For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).
3. Click **Create**.
4. Fill in the required fields with your information.
5. In the **Authorized domains** section, add `make.com` and `integromat.com`.
6. Click **Save and continue**.
7. In the **Scopes** page, click **Add or remove scopes**,add the following scopes, and click **Update**.


	* `https://mail.google.com`
	* `https://www.googleapis.com/auth/drive`
	* `https://www.googleapis.com/auth/userinfo.email`
	* `https://www.googleapis.com/auth/spreadsheets`
8. Click **Save and continue**.
9. Optional: If your project will remain in the **Testing** publishing status, add test user emails on the **Test users** page, then click **Save and continue**.

Note: If you are using custom apps with publishing state, **Testing**, then you must set up the access token NOT TO be forced to re-authenticate every week after expiration.

However, our tests have shown that it is currently possible to set your Publishing Status to In Production to avoid this weekly re-authentication.

For more information, see  [Setting up OAuth consent screen](https://support.google.com/cloud/answer/10311615#zippy=%2Ctesting). To set up app token and authentication, see [Using OAuth 2.0 for Web Server applications](https://developers.google.com/identity/protocols/oauth2/web-server).
#### Create your Google Forms client credentials

To create your client credentials:

1. In the left sidebar, click **Credentials**.
2. Click **+ Create Credentials** > **OAuth client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the console.
5. In the **Authorized redirect URIs** section, click **+ Add URI** and enter the following redirect URI: `https://www.integromat.com/oauth/cb/google/`.
6. Copy your **Client ID** and **Client secret** values and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Make.

Build Google Forms Scenarios
----------------------------

After connecting the app, you can perform the following actions:

Form* Search Forms
* Create a Form
* Get a Form
* Update a Form

Note: For **Item Changes**, **Location** refers to the item's position on the list of all form items. The very first item is 0, the second item is 1, and so on. To add an item at the very beginning of your form, use 0 as the location.
* Move a Form to Trash
Response* Watch Responses
* List Responses
* Get a Response
Legacy* Watch Responses in Google Sheets



| **Value render option** | **Formatted value**: Values will be calculated and formatted in the reply according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `$1.23`.**Unformatted value**: Values will be calculated, but not formatted in the reply. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `1.23`.**Formula**: Values will not be calculated. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `=A1`. |
| --- | --- |
| **Date and time render option** | Specifies how dates, times, and duration should be represented in the output. This is ignored if Value render option (above) is set to `Formatted value`. |
* Search Responses in Google Sheets



| **Value render option** | **Formatted value**: Values will be calculated and formatted in the reply according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `$1.23`.**Unformatted value**: Values will be calculated, but not formatted in the reply. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `1.23`.**Formula**: Values will not be calculated. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return `=A1`. |
| --- | --- |
| **Date and time render option** | Specifies how dates, times, and duration should be represented in the output. This is ignored if Value render option (above) is set to `Formatted value`. |
* Search Responses in Google Sheets (advanced)

Note: For the **Filter** field, define the search query using the [Google Charts Query Language](https://developers.google.com/chart/interactive/docs/querylanguage).

E.g. `select * where C = "John"` to retrieve all values for the row where the C column is "John".
* Add a Response in Google Sheets

Note: For the **Timestamp** column, use the following value: `formatDate(now;DD/MM/YYYY HH:mm;UTC)`
* Update a Response in Google Sheets

Note: For the **Value input option** field, **Raw** will not parse the values entered by the user and are stored as-is. **User entered** will parse the value as if the user typed them into the UI. Numbers will remain numbers, but strings may be converted to numbers, dates, etc., following the same rules that are applied when entering text into a cell via the Google Sheets UI.
* Delete a Response in Google Sheets
Other* Make an API Call
