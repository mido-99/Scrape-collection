Google Calendar
===============

With Google Calendar modules in Make, you can manage events and calendars in your Google Calendar account.

To use the Google Calendar modules, you must have a Google account. You can create an account at [accounts.google.com](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp).

Refer to the [Google Calendar API documentation](https://developers.google.com/calendar/api/v3/reference) for a list of available endpoints.

Connect Google Calendar to Make
-------------------------------

To establish the connection in Make:

1. Log in to your Make account, add a Google Calendar module to your scenario, and click **Create a Connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Switch on the **Show advanced settings** and enter your Google Cloud Platform Project client credentials. See the [Create and configure a Google Cloud Console project for Google Calendar](google-calendar.html#create-and-configure-a-google-cloud-console-project-for-google-calendar "Create and configure a Google Cloud Console project for Google Calendar") section below.
4. Click **Sign in with Google** and select your Google account.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Google Calendar modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

### Note

You may receive a connection error if your Google account has multiple APIs enabled in Google Cloud Platform. If so, create a new Google Cloud Platform Project and try to establish the connection again. See the [Create and configure a Google Cloud Console project for Google Calendar](google-calendar.html#create-and-configure-a-google-cloud-console-project-for-google-calendar "Create and configure a Google Cloud Console project for Google Calendar") section below for more information.

[Create and configure a Google Cloud Console project for Google Calendar
-----------------------------------------------------------------------](#create-and-configure-a-google-cloud-console-project-for-google-calendar_body)To connect to Make using your own client credentials, you can create and configure a project in the Google Cloud Console.

### Create a Google Cloud Console project for Google Calendar

To create a Google Cloud Console project:

1. Log in to [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. In the top menu, click **Select a project** > **New project**.
3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.
### Enable APIs for Google Calendar

To enable the required API:

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for and enable the following API: **Google Calendar API**.
### Configure your OAuth consent screen for Google Calendar

To configure your OAuth consent screen:

1. In the left sidebar, click **OAuth consent screen**.
2. Under **User Type**, select **External**.

For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).
3. Click **Create**.
4. Fill in the required fields with your information.
5. For **Authorized domains**, add `make.com` and `integromat.com`.
6. Click **Save and Continue**.
7. On the **Scopes** page, click **Add or Remove Scopes**, add your desired scopes, and click **Update**.
8. Click **Save and Continue**.
9. Optional: If your project will remain in the **Testing** publishing status, add test user emails on the **Test users** page, then click **Save and continue**.
### Create your Google Calendar client credentials

To create your client credentials:

1. In the left sidebar, click **Credentials**.
2. Click **+ Create Credentials** > **OAuth Client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the console.
5. In the **Authorized redirect URIs** section, click **+Add URI** and enter the following redirect URI: `https://www.integromat.com/oauth/cb/google`.
6. Click **Create**.
7. Copy your **Client ID** and **Client Secret** and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Make.
Build Google Calendar Scenarios
-------------------------------

After connecting the app, you can perform the following actions:

Event* Watch Events
* Search Events
* Get an Event
* Create an Event

Note: For the **Send notifications about the event creation** field, the **None** option should only be used for migration use cases.

For the **Recurrence** field, DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the **start** and **end** fields. This field is omitted for single events or instances of recurring events.

For adding Google Drive file attachments, use the same format as in `alternateLink` property of the Files resource in the Drive API.
* Duplicate an Event
* Update an Event
* Delete an Event
Calendar* List Calendars
* Get a Calendar
* Create a Calendar
* Update a Calendar
* Delete a Calendar
* Clear a Calendar
Access Control Rule* List Access Control Rules
* Get an Access Control Rule
* Create an Access Control Rule
* Update an Access Control Rule
* Delete an Access Control Rule
Other* Make an API Call
* Get Free/Busy Information
Common Problems
---------------

[### Trigger a specified amount of time before an event](#trigger-a-specified-amount-of-time-before-an-event_body)It is possible to trigger a scenario a specified amount of time before an event with the help of standard Google Calendar email reminders and the **Webhooks > Custom mailhook** module.

1. Use the **Google Calendar > Update an event** module to add an email reminder to your event:

![googleCalenderReminder.png](./../image/uuid-62c1776f-71a2-b183-01bd-b4a4bc59d2fb.png)
2. Create a new scenario starting with the **Webhooks > Custom mailhook** module. Copy the mailhook's email address. Save the scenario and execute it.
3. In Gmail, redirect the Google Calendar email reminders to the mailhook's email address:


	1. Open your [Gmail settings](https://mail.google.com/mail/u/0/#settings/general).
	2. Open the [Forwarding and POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop) tab.
	3. Click **Add a forwarding address**.
	
	![googleCalendarGmailForward.png](./../image/uuid-19f36aa3-0793-318d-313b-2efc251d0f15.png)
	4. Paste the copied mailhook's email address, press "Next", confirm by pressing "Proceed" in the popup window and close the dialog by pressing "OK".
	5. In Make, switch to the new scenario which should finish its execution by receiving the confirmation email.
	6. Click the bubble above the module to inspect the module's output.
	7. Expand the `Text` item and search for the Confirmation code:
	
	![googleCalendarConfCode.png](./../image/uuid-bff900ba-341d-8557-4e21-d1490c8b79be.png)
	8. Copy the Confirmation code.
	9. In Gmail, paste the Confirmation code in the edit box and click **Verify**:
	
	![googleCalendarVerify.png](./../image/uuid-5efeb3ab-b8aa-9e70-3fac-8eee675db1fa.png)
	10. Open the [Filters and Blocked Addresses](https://mail.google.com/mail/u/0/#settings/filters) tab.
	11. Click **Create a new filter**:
	
	![GoogleCalendarCreateFilter.png](./../image/uuid-6f9a4d17-47e5-f6c3-e188-da5f286f458d.png)
	12. Set up a filter for all emails coming from `[[email protected]](/cdn-cgi/l/email-protection)` and click **Create filter**:
	
	![googleCalendarFIlter.png](./../image/uuid-40712ad3-a188-d865-0366-e2f59797b9ab.png)
	13. Tick the "Forward it to:" checkbox and choose the mailhook's email address from the list:
	
	![googleCalendarForwardAddress.png](./../image/uuid-7d02b128-dddb-7bb5-daa7-bf786e9b20cd.png)
	14. Click **Create filter**.
4. In Make, you can add the **Text parser > Match pattern** module after the **Webhooks > Custom mailhook** module to parse the email's HTML code and obtain any information you need. For example, you can configure a module like this to obtain the event's ID:

Pattern: `<meta itemprop="eventId/googleCalendar" content="(?<evenitID>.*?)"/>` 

Text: The `HTML content` item output from the **Webhooks > Custom mailhook** module:

![googleCalendarTextParser.png](./../image/uuid-38055aee-3846-f283-8d15-048d0da46245.png)
[### Where are the Iterate attachments and Iterate attendees modules?](#where-are-the-iterate-attachments-and-iterate-attendees-modules-_body)Both modules are deprecated. To iterate desired values, please use the *Flow Control > Iterator* module.

