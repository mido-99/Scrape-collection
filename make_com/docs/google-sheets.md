Google Sheets
=============

With Google Sheets modules in Make, you can manage rows, cells, sheets, spreadsheets, values, and conditional formats in your Google Sheets account.

To use Google Sheets modules, you must have a Google account. You can create one at [accounts.google.com.](https://accounts.google.com) To use instant trigger modules, you must have the [Make Google Sheets extension](google-sheets.html#connectinginstant-triggers--perform-a-function-watch-changes-using-the-make-google-sheets-add-on "Connecting Instant Triggers (Perform a Function, Watch Changes) using the Make Google Sheets Add-on").

Refer to the [Google Sheets API documentation](https://developers.google.com/sheets/api/reference/rest) for a list of available endpoints.

### Note

Make's use and transfer of information received from Google APIs to any other app will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

Connect Google Sheets to Make
-----------------------------

To establish the connection in Make:

1. Log in to your Make account, add a Google Sheets module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Switch on the **Show advanced settings** toggle and enter your Google Cloud Console project client credentials. For more information, see the [Create and configure a Google Cloud Console project for Google Sheets section](google-sheets.html#create-and-configure-a-google-cloud-console-project-for-google-sheets "Create and configure a Google Cloud Console project for Google Sheets") below.
4. Click **Sign in with Google**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Google Sheets modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[### Create and configure a Google Cloud Console project for Google Sheets](#create-and-configure-a-google-cloud-console-project-for-google-sheets_body)To connect to Make using your own client credentials, you can create and configure a project in the Google Cloud Console.

#### Create a Google Cloud Console project for Google Sheets

To create a Google Cloud Console project:

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. In the top menu, click **Select a project** > **New project**.
3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.
#### Enable APIs for Google Sheets

To enable the required APIs:

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for and enable the following APIs: **Google Sheets API** and **Google Drive API**.
#### Configure your OAuth consent screen for Google Sheets

To configure your OAuth consent screen:

1. In the left sidebar, click **OAuth consent screen**.
2. Under **User Type**, select **External**.

For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).
3. Click **Create**.
4. Fill in the required fields with your information.
5. In the **Authorized domains** section, add `make.com` and `integromat.com`.
6. Click **Save and continue**.
7. In the **Scopes** page, click **Add or remove scopes**, add the following scopes, and click **Update**.


	* `https://www.googleapis.com/auth/spreadsheets`
	* `https://www.googleapis.com/auth/drive`
8. Click **Save and continue**.
9. Optional: If your project will remain in the **Testing** publishing status, add test user emails on the **Test users** page, then click **Save and continue**.
### Note

**Publishing Status**

**Testing**: If you keep your project in the **Testing**status, you will be required to reauthorize your connection in Make every week. To avoid weekly reauthorization, update the project status to **In production**.

**In production:**If you update your project to the **In production** status, you will not be required to reauthorize the connection weekly. To update your project's status, go to the **OAuth consent screen** and click **Publish** app. If you see the notice Needs verification, you can choose whether to go through the Google verification process for the app or to connect to your unverified app. Currently connecting to unverified apps works in Make, but we cannot guarantee the Google will allow connections to unverified apps for an indefinite period.

For more information regarding the publishing status, refer to the Publishing status section of [Google's Setting up your OAuth consent screen help](https://support.google.com/cloud/answer/10311615#zippy=).

#### Create your Google Sheets client credentials

To create your client credentials:

1. In the left sidebar, click **Credentials**.
2. Click **+ Create Credentials** > **OAuth client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the console.
5. In the **Authorized redirect URIs** section, click **+ Add URI** and enter the following redirect URI: `https://www.integromat.com/oauth/cb/google/`.
6. Copy your **Client ID** and **Client secret** values and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Make.

Connecting Instant Triggers ([Perform a Function](google-sheets.html#perform-a-function "Perform a Function"), [Watch Changes](google-sheets.html#watch-changes-964718 "Watch Changes")) using the Make Google Sheets Add-on
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to use instant triggers, you must install the Make add-on in your spreadsheet and establish a connection between the Make module and Google Sheets.

### Note

This add-on works only if you open the Google spreadsheet in a browser and make changes there. It will not work when the spreadsheet is filled by Google Forms or other tools.

[### Make for Google Sheets add-on installation](#make-for-google-sheets-add-on-installation_body)1. Open the spreadsheet where you want to install the extension.
2. Go to **Extensions >  Add-ons > Get add-ons**

![Google_Sheets_Add_on_connect_1.png](./../image/uuid-f39dc3a3-ebfb-8e38-17f7-44735c46c704.png)
3. Search for the **Make for Google Sheets** add-on.
4. Click the **Make for Google Sheets** add-on.
5. Click **Install**.
6. Click **Continue** and **Allow** to grant access rights.
7. You have now installed the **Make for Google Sheets** add-on.
[### Connecting the Instant Trigger module to a Google Sheets spreadsheet](#connecting-the-instant-trigger-module-to-a-google-sheets-spreadsheet_body)1. Copy the provided webhook address to the clipboard and click **OK**.

![Google_Sheets_watch_webhook_1.png](./../image/uuid-4a8e155b-e183-35a6-60f5-364987ad8cd4.png)![Google_Sheets_watch_webhook_2.png](./../image/uuid-6a3673f9-515a-e3f7-05b5-1e2070198263.png)![Google_Sheets_watch_webhook_3.png](./../image/uuid-d6d00aa1-1b77-e508-a3d9-76bb73bd4a1c.png)
2. Open your spreadsheet.
3. Open the **Make for Google Sheets** add-on settings.

![Google_Sheets_add_on_settings.png](./../image/uuid-012e7549-5d2f-e558-b468-b1b6647cc35a.png)
4. Paste the webhook URL you have copied in step 1 to the **Webhook URL** field in the Watch Updates settings section or **Perform a Function** section, depending upon which module you are using.
5. Click **Save**.

### Note

If clicking **Save** does not work, try the steps again in an Incognito browser window, preferably Chrome (Specifically for Mac users)
Triggers
--------

[### Watch New Rows](#watch-new-rows-964718_body)Retrieves values from every newly added row in the spreadsheet.

The module retrieves **only** new rows that have not been filled in before. The trigger will not process an overwritten row.

### Tip

You can trigger a scenario in Make using a custom button in Google Sheets. See [here](google-sheets.html#add-a-custom-button-in-a-sheet-to-trigger-a-scenario "Add a Custom Button in a Sheet to Trigger a Scenario") for more information.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Choose a Method** | Select a method to choose the spreadsheet whose rows you want to watch. |
| **Choose a Drive** | Select Google Drive, where you have the spreadsheet whose rows you want to watch. |
| **Spreadsheet ID** | Choose the Spreadsheet ID whose rows you want to watch. |
| **Spreadsheet** | Select the spreadsheet that contains the sheet you want to watch. |
| **Table contains headers** | Select whether the spreadsheet contains the header row. If the *Yes* option is selected, the module doesn't retrieve the header row as output data, and variables in the output are then called by the headers. If the *No* option is selected, the module retrieves the first table row, and the output variables are called simply A, B, C, D, etc. |
| **Row with headers** | Enter the range of the header row, e.g., `A1:F1`. |
| **Value render option** | **Formatted value**The values in the reply will be calculated and formatted according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` will return  `"$1.23".`**Unformatted value**The values will be calculated but not formatted in the reply. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then `A2` will return the number `"1.23"`.**Formula**The values will not be calculated. The reply will include the formulas. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then A2 will return `"=A1"`. |
| **Date and time render option** | **Serial number**Instructs date, time, datetime, and duration fields to be outputted as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (to the left of the decimal) counts the days since December 30th, 1899. The fractional portion (to the right of the decimal) counts the time as a fraction of the day. For example, January 1st, 1900 at noon would be 2.5. 2 because it's 2 days after December 30th, 1899, and .5 because noon is half a day. February 1st, 1900 at 3 pm would be 33.625. This correctly treats the year 1900 as not a leap year.**Formatted string**Instructs date, time, datetime, and duration fields to be outputted as strings in their given number format (which depends on the spreadsheet's locale). |
| **Limit** | Set the maximum number of results that Make will work with during one execution cycle. |

### Caution

If the worksheet contains a blank row, no rows after the blank row will be processed!

[### Watch Changes](#watch-changes-964718_body)This module watches for changes in all the cells of a spreadsheet. It means that when you update numerous cells in one row, one by one, Make will then receive multiple updated events.

### Note

The module only watches for changes made in the Google Sheets app by the user. Script executions and API requests do not trigger this module. The module does not watch for newly added rows to the sheet.

### Tip

You can trigger a scenario in Make using a custom button in Google Sheets. See [here](google-sheets.html#add-a-custom-button-in-a-sheet-to-trigger-a-scenario "Add a Custom Button in a Sheet to Trigger a Scenario") for more information.



| **Webhook** | Establish a connection to the spreadsheet using the add-on. |
| --- | --- |

[### Perform a Function](#perform-a-function_body)Make allows you to use the **custom function**  `MAKE_FUNCTION` in Google Sheets similarly to built-in functions like `AVERAGE, SUM,` etc. It allows you to perform the function in Make and return the result back to the sheet. The function `MAKE_FUNCTION` accepts as many parameters as you need.

[### Perform a Function Example](#perform-a-function-example_body)

| **Sample sheet** | The **Total-EUR** amount SUM will be converted, according to the current exchange rate, to the **Total - USD** amount and will be inserted into the desired field using Make.61d5b533b0eeb.png |
| --- | --- |

1. Create a scenario. Use the following modules:


	* **Google Sheets > Perform a Function**
	* **Currency > Convert an Amount Between Currencies**
	* **Google Sheets > Perform a Function - Responder**![Google_sheets_perform_function_scenario.png](./../image/uuid-433924ed-a1df-c9f8-5e8b-839f5afd07a8.png)
	1. **Google Sheets > Perform a Function**
	
	Generate a webhook and [paste it into the Make add-on in Google Sheets.](google-sheets.html#how-to-perform-a-custom-function- "How to perform a custom function?")
	
	![Google_Sheets_perform_function_webhook.png](./../image/uuid-815480e2-1929-1920-274b-4e358b4e7447.png)
	2. **Currency > Convert an Amount between Currencies**
	
	Converts the mapped EUR amount to USD.
	
	![Google_Sheets_currency_settings.png](./../image/uuid-856f3034-2a51-3eda-d522-168ef90e0709.png)
	3. **Google Sheets > Perform a Function - Responder**
	
	Inserts the converted amount into the sheet cell.
	
	![Google_Sheets_perform_a_function_responder.png](./../image/uuid-56046cb7-044f-2d7c-7507-95eba087c667.png)
2. Run the scenario
3. Enter the `MAKE_FUNCTION` into the desired cell to load the converted amount.

![61d5b5390e16d.gif](./../image/uuid-3ad043fc-8d85-1d2d-8f11-af1bc4f444bc.gif)When the user changes the amount, the `MAKE_FUNCTION` re-calculates the **Total - USD** according to the current exchange rate:

![61d5b53b0adfa.gif](./../image/uuid-679fcfcd-17aa-1fae-e877-d8a537d39447.gif)
[### How to perform a custom function?](#how-to-perform-a-custom-function-_body)You can simply use the function like built-in functions in Google Sheet.

![61d5b531ad6ee.png](./../image/uuid-f4353df6-ed07-c7be-0bb1-e4392dda1c5d.png)Create a new scenario with the following modules:

* **Perform a Function** - the module receives the parameters passed to the function
* **Perform a Function - Responder** - the module returns the result of the function execution back to the sheet


|  | Google_Sheets_paste_webhook.png |
| --- | --- |

Actions
-------

[### Add a Row](#add-a-row-964718_body)Adds a row to a sheet.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Choose a Method** | Select an option to choose the spreadsheet in which you want to add a row. |
| **Choose a Drive** | Select Google Drive to choose the spreadsheet in which you want to add a row. |
| **Spreadsheet ID** | Enter the Spreadsheet ID in which you want to add a row. Alternatively, you can search the spreadsheet by clicking **Search Spreadsheets**. |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet Name** | Enter a sheet name in which you want to add a row. |
| **Column range** | Select the column range that you want to work with. |
| **Unformatted** | Select or map whether to insert a row unformatted. |
| **Values** | Enter (map) the desired cells of the row you want to add. |
| **Value input option** | **User entered**The values will be parsed as if the user typed them into the UI. Numbers will remain numbers, but strings may be converted to numbers, dates, etc., following the same rules that are applied when entering text into a cell via the Google Sheets UI.**Raw**The values the user has entered will not be parsed and will be stored as-is. |
| **Insert data option** | **Insert rows**Rows are inserted for the new data.ExampleGoogle_sheets_insert_row.pngWhat happens when the *Insert rows* option is selected (the *Add a Row* module is executed 3 times):61d5b53d9f87b.gif**Overwrite**The new data overwrites the existing data in the areas where it is written. (Note: adding data to the end of the sheet will still insert new rows or columns so the data can be written.)ExampleGoogle_sheets_overwrite.pngWhat happens when the *Overwrite* option is selected (the *Add a Row* module is executed 3 times):61d5b5404b3b2.gif |

[### Update a Row](#update-a-row-964718_body)This module allows you to change the cell content in a selected row.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Choose a Method** | Select an option to choose the spreadsheet whose rows you want to update. |
| **Choose a Drive** | Select Google Drive to choose the spreadsheet whose rows you want to update. |
| **Spreadsheet ID** | Enter the Spreadsheet ID whose rows you want to update. Alternatively, you can search the spreadsheet by clicking the **Search Spreadsheets**. |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to update a row in. |
| **Row number** | Enter the number of the row you want to update. |
| **Values** | Enter (map) the values in the desired cells of the row you want to change (update). |
| **Value input option** | **User entered**The values will be parsed as if the user typed them into the UI. Numbers will remain numbers, but strings may be converted to numbers, dates, etc. following the same rules that are applied when entering text into a cell via the Google Sheets UI.**Raw**The values the user has entered will not be parsed and will be stored as-is. |

[### Clear a Row](#clear-a-row_body)Deletes values from a specified row.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to delete data from. |
| **Row number** | Enter the number of the row you want to delete, e.g. `23`. |

[### Delete a Row](#delete-a-row-964718_body)Deletes a specified row.

### Note

To delete multiple rows based on filter criteria please see the [Deleting Multiple Rows](google-sheets.html#deleting-multiple-rows "Deleting Multiple Rows") section.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to delete a row from. |
| **Row number** | Enter the number of the row you want to delete, e.g. `23` or map the number from a preceding module, e.g. *Search Rows*. |

[### Get a Cell](#get-a-cell_body)Retrieves a value from a selected cell.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet that contains the cell you want to retrieve data from. |
| **Cell** | Enter the ID of the cell you want to retrieve data from, e.g. `A6`. |

[### Update a Cell](#update-a-cell_body)

| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Cell** | Enter the ID of the cell you want to update, e.g. `A5`. |
| **Value** | Enter the new value. |
| **Value input option** | **User entered**The values will be parsed as if the user typed them into the UI. Numbers will remain numbers, but strings may be converted to numbers, dates, etc., following the same rules that are applied when entering text into a cell via the Google Sheets UI.**Raw**The values the user has entered will not be parsed and will be stored as-is. |

[### Clear a Cell](#clear-a-cell_body)Deletes a value from a specified cell.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to delete a cell from. |
| **Cell** | Enter the ID of the cell you want to delete, e.g. `A5`. |

[### Add a Sheet](#add-a-sheet_body)Creates a new sheet in a selected spreadsheet.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Properties** | **Title**Enter the name of the new sheet.**Index**Enter the sheet position. The default is `0` (places the sheet in the first place). |

[### Create a Spreadsheet](#create-a-spreadsheet_body)

| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Title** | Enter the name of a new spreadsheet. |
| **Locale** | The locale of the spreadsheet in one of the following formats:* an ISO [639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code such as `en`, * an [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) language code such as `haw`, if no 639-1 code exists, * a combination of the ISO language code and country code, such as `en_US`. |
| **Recalculation interval** | The amount of time to wait before volatile functions are recalculated:**On change**Volatile functions are updated upon every change.**On change and every minute**Volatile functions are updated upon every change and every minute.**On change and hourly**Volatile functions are updated upon every change and hourly. |
| **Time zone** | Select the time zone of the spreadsheet. |
| **Number format** | Select the default format of all cells in the spreadsheet.  | `TEXT` | Text formatting, e.g  `1000. 12` | | --- | --- | | `NUMBER` | Number formatting, e.g,  `1,000.12` | | `PERCENT` | Percent formatting, e.g  `10. 12%` | | `CURRENCY` | Currency formatting, e.g  `$1,000.12` | | `DATE` | Date formatting, e.g  `9/26/2008` | | `TIME` | Time formatting, e.g  `3:59:00 PM` | | `DATE time` | Date+Time formatting, e.g  `9/26/08 15:59:00` | | `SCIENTIFIC` | Scientific number formatting, e.g  `1. 01E+03` | |
| **Sheets** | [Add sheets](google-sheets.html#add-a-sheet "Add a Sheet") to the new spreadsheet. |

[### Perform a Function - Responder](#perform-a-function---responder_body)This module is to be used together with the Perform a Function module.



| **Response type** | Select whether you insert text or a number into the sheet. |
| --- | --- |
| **Value** | Map the value from the previous module you want to insert into the sheet. |

[### Delete a Sheet](#delete-a-sheet_body)Deletes a specified sheet from a spreadsheet.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select or map the Google spreadsheet that contains the sheet you want to delete. |
| **Sheet** | Select or map the sheet you want to delete. |

[### Make an API Call](#make-an-api-call-964718_body)Allows you to perform a custom API call.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **URL** | Enter a path relative to `https://sheets.googleapis.com/v4/`.For example: `/spreadsheets/{{spreadsheetID}}`.NoteFor the list of available endpoints, refer to the [Google Sheets API Documentation](https://developers.google.com/sheets/api/reference/rest). |
| **Method** | Select the HTTP method you want to use:* **GET** - to retrieve information for an entry. * **POST** - to create a new entry. * **PUT** - to update/replace an existing entry. * **PATCH** - to make a partial entry update. * **DELETE** - to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

[#### Example of Use - Get Spreadsheet](#example-of-use---get-spreadsheet_body)The following API call returns specified spreadsheet details.

**URL:**

`/spreadsheets/{{spreadsheetID}}`

**Method:**

`GET`

![Google_Sheets_api_call.png](./../image/uuid-c0a9366f-f807-7bcf-4051-bdd5871d3dcd.png)The result can be found in the module's **Output** under *Bundle* > *Body:*

![Google_Sheets_api_bundle.png](./../image/uuid-f481a996-3740-f8b0-49a9-6512ffebba6e.png)[### Create a Spreadsheet from a Template](#create-a-spreadsheet-from-a-template_body)Creates a new spreadsheet from a template sheet.



| **Connection** | Establish a connection to your Google Sheets account. |
| --- | --- |
| **Enter a Template Spreadsheet ID** | Select or map the Template Spreadsheet ID from which you want to create the spreadsheet. |
| **Choose a Drive** | Select or map the drive where you want to create the spreadsheet. |
| **Template Spreadsheet ID** | Select the template from which you want to create the spreadsheet.If the spreadsheet contains tags like `{{name}}`, they are retrieved below.Your file MUST contain at least one tag for this module to work. |
| **Title** | Enter a name for the spreadsheet. |
| **New Drive Location** | Select or map the drive to store the new spreadsheet. |
| **New Document's Location** | Select or map the folder, where the new spreadsheet should be placed. |

[### Copy a Sheet](#copy-a-sheet_body)Copies a sheet to another spreadsheet.



| **Connection** | Establish a connection to your Google Spreadsheets account. |
| --- | --- |
| **Choose a Method** | Select or map the option to choose the spreadsheet that you want to copy. |
| **Choose a Drive** | Select or map the drive location where the spreadsheet that you want to copy is located. |
| **Spreadsheet ID** | Select or map the Spreadsheet ID you want to copy. |
| **Destination Drive Location** | Select or map the drive location where you want to store the copied spreadsheet. |
| **Destination Spreadsheet ID** | Select or map the copied Spreadsheet ID. |

[### Clear Values from a Range](#clear-values-from-a-range_body)Clears a specified range of values from a spreadsheet.



| **Connection** | Establish a connection to your Google Spreadsheet account. |
| --- | --- |
| **Enter a Spreadsheet ID and Sheet Name** | Select an option to choose the spreadsheet and sheet name whose value you want to clear.* Enter manually * Select from all * Select by path |
| **Spreadsheet ID** | Enter the Spreadsheet ID from which you want to clear the values. |
| **Sheet Name** | Enter a sheet name from which you want to clear the values. |
| **Range** | Enter the range you want to get. For example, **A1:D25**. |

[### Add a Conditional Format Rule](#add-a-conditional-format-rule_body)Creates a new conditional format rule at the given index. All subsequent rules indexes are incremented.



| **Connection** | Establish a connection to your Google Spreadsheets account. |
| --- | --- |
| **Enter a Spreadsheet and Sheet ID** | Select an option to choose the spreadsheet and sheet name to which you want to create a format rule.* Enter Manually * Select from all * Select by path |
| **Spreadsheet ID** | Enter the Spreadsheet ID to which you want to create the conditional format rule. |
| **Sheet ID** | Enter the Sheet ID to which you want to create the conditional format rule. |
| **Range** | Enter the range of rows and columns to which you want to apply the conditional rule format. For example, **A1:D25**. |
| **Index** | The zero-based index where the rule should be inserted. |
| **Format Rule** | Select or map the rule for the conditional format rule. |
| **Condition** | Select or map the condition and enter the value for the format rule. For more information, see the [boolean and gradient conditions](https://developers.google.com/apps-script/reference/spreadsheet/conditional-format-rule-builder). |
| **Cell Format** | Select or map the cell background color. |
| **Text Format** | Set the text format such as foreground color, bold, italic or strikethrough. |

[### Delete a Conditional Format Rule](#delete-a-conditional-format-rule_body)Deletes a conditional format rule at the given index. All subsequent rule indexes are decremented.



| **Connection** | Establish a connection to your Google Sheets account. |
| --- | --- |
| **Enter a Spreadsheet and Sheet ID** | Select an option to choose the spreadsheet and sheet name to which you want to create a format rule.* Enter Manually * Select from all * Select by path |
| **Spreadsheet ID** | Enter the Spreadsheet ID whose conditional format rule you want to delete. |
| **Sheet ID** | Enter the Sheet ID whose conditional format rule you want to delete. |
| **Index** | The zero-based index of the rule to be deleted |

Searches
--------

[### Search Rows](#search-rows-964718_body)Searches rows using the filter options.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to search the rows in. |
| **Table contains headers** | Select whether the spreadsheet contains the header row. If the *Yes* option is selected, the module doesn't retrieve the header row as output data and variables in the output are then called by the headers. If the *No* option is selected, the module also retrieves the first table row, and variables in the output are then called simply A, B, C, D, etc. |
| **Filter** | Set the filter for the row to be searched by.Set filter values. You can also use logical operators, AND/OR in order to specify your selection.Example:In the following dialog, the row which contains the number 1 or 2 in the "column2" column will be searched.Google_Sheets_search_rows_filter_for_table.png |
| **Field Type** | Select or map the field type to search the rows that match the specified type:* *Date* * *Number* * *String* |
| **Value render option** | **Formatted value**The values in the reply will be calculated and formatted according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then `A2` will return  `"$1.23".`**Unformatted value**The values will be calculated, but not formatted in the reply. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then `A2` will return the number `"1.23"`.**Formula**The values will not be calculated. The reply will include the formulas. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then A2 will return `"=A1"`. |
| **Date and time render option** | **Serial number**Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (to the left of the decimal) counts the days since December 30th 1899. The fractional portion (to the right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5. 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3 pm would be 33.625. This correctly treats the year 1900 as not a leap year.**Formatted string**Instructs date, time, datetime, and duration fields to be outputted as strings in their given number format (which is dependent on the spreadsheet's locale). |

[### Search Rows (Advanced)](#search-rows--advanced-_body)

| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to search the rows in. |
| **Query** | Searches rows using Google Charts Query Language. The language is similar to SQL and it is possible to make complex queries. Unfortunately, the response doesn't contain IDs of returned rows. Due to Google Charts, the service is intended for data visualization where the row numbers aren't needed. You can find more information about the query language in the [documentation](https://developers.google.com/chart/interactive/docs/querylanguage).Google_Sheets_advanced_search_example_1.png |

[### Get Range Values](#get-range-values_body)Retrieves range content.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select the Google spreadsheet. |
| **Sheet** | Select the sheet you want to get the range content from. |
| **Range** | Enter the range you want to get, e.g. `A1:D25`. |
| **Table contains headers** | **Row with headers**Enter the range of the table headers, e.g. `A1:F1`. If you leave the field empty, Make will suppose that the header is in the first row of the specified range. |
| **Value render option** | **Formatted value**The values in the reply will be calculated and formatted according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then `A2` will return  `"$1.23".`**Unformatted value**The values will be calculated, but not formatted in the reply. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then `A2` will return the number `"1.23"`.**Formula**The values will not be calculated. The reply will include the formulas. For example, if `A1` is  `1.23`  and `A2` is `=A1` and formatted as currency, then A2 will return `"=A1"`. |
| **Date and render option** | **Serial number**Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (to the left of the decimal) counts the days since December 30th 1899. The fractional portion (to the right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5. 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3 pm would be 33.625. This correctly treats the year 1900 as not a leap year.**Formatted string**Instructs date, time, datetime, and duration fields to be outputted as strings in their given number format (which is dependent on the spreadsheet's locale). |

[### List Sheets](#list-sheets_body)Retrieves a list of all sheets in a spreadsheet.



| **Connection** | Establish a connection to the spreadsheet using your Google account. |
| --- | --- |
| **Spreadsheet** | Select or map the Google spreadsheet you want to retrieve sheets from. |

Tips & Tricks
-------------

[### Deleting Multiple Rows](#deleting-multiple-rows_body)To delete multiple rows based on filter criteria use the **Search Rows** module linked to the **Delete a Row** module as in the following example:

1. 1. Add the **Search Rows** module and the **Delete a Row** module to the scenario.



| 61d5b546a39c7.png |
| --- |
2. Let's assume that you have a table where you need to delete all rows where column *A* equals *Y*.



| 61d5b547ca98b.png |
| --- |
3. Open the **Search Rows** module settings and set the fields as follows:



| **Filter**`A` Equal to `Y`**Sort order**`Descending`**Order by**`Row number` | Google_Sheets_search_rows_filter.png |
| --- | --- |

### Caution

Make sure that the **Sort order** and **Order by** fields are set as above, otherwise values will not be deleted correctly from the table!
4. Add the **Delete a Row** module to the scenario and connect it to the **Search Row** module.
5. Map the **Row number item** from the **Search Rows** module to the Delete a Row module's **Row number** field.

![Google_Sheets_map_delete_row.png](./../image/uuid-6ba52cff-bd61-b1c0-9987-c6e940b5f0c0.png)
6. Run the scenario to delete values that match the filter criteria from the sheet.

![61d5b54cb4ece.gif](./../image/uuid-28e7cd5e-3213-ae3a-de87-17a2a659e7b0.gif)
[### How to Get Empty Cells from a Google Sheet](#how-to-get-empty-cells-from-a-google-sheet_body)Use the **Search Rows (Advanced)** module and use this formula to get empty columns.


```

               select * where E is null
            
```
![Google_sheets_adv_search_rows.png](./../image/uuid-ab9cfd7e-3d50-03c4-fd6b-dcb19d7279f9.png)Here **"E"** is the column and **"is null"** is the condition. You can create a more advanced query using [Google Query Lang](https://developers.google.com/chart/interactive/docs/querylanguage)

[### Add a Custom Button in a Sheet to Trigger a Scenario](#add-a-custom-button-in-a-sheet-to-trigger-a-scenario_body)1. In Make, insert the **Webhook > Custom webhooks** module/trigger into the scenario and configure it (see [Webhooks](./../tools/webhooks.html "Webhooks")).

Note: Once you have configured the custom webhook module, be sure to save the scenario .
2. Copy the webhook's URL.
3. Execute the scenario.
4. In Google Sheets, choose **Insert > Drawing** from the main menu bar.
5. Click the **Text box** icon:

![mceclip0-21.png](./../image/uuid-9b2000f5-7232-32c9-a777-5db52218ebbc.png)
6. Design a button and click **Save and Close** in the top-right corner:

![mceclip1-8.png](./../image/uuid-6f196bb3-0b81-421e-b7e6-afb367ef0d32.png)
7. The button will be placed in your worksheet. Click the three vertical dots in the button's top-right corner:

![mceclip2-14.png](./../image/uuid-c274e33a-432f-9b35-ab7b-939cbd423267.png)
8. Choose **Assign script** from the menu.
9. Enter the name of your script (function). For example, `runscenario`and click OK:

![mceclip3-5.png](./../image/uuid-163fdb3c-95cc-c3eb-155f-ca9e7b15d3f5.png)
10. Choose **Extensions > Apps Script** from the main menu bar.
11. Insert the following code:


	* The name of the function must correspond to the name you specified in step 9.
	* Replace the `https://hook.make.com/xxx...xxx`URL with the webhook's URL you copied in step 2.
	
	
	```
	
	                           function runScenario() {
	  UrlFetchApp.fetch("https://hook.make.com/xxx...xxx");
	}
	                        
	```
12. Press **Ctrl+S** to save the script file, enter a project name, and click **OK**.
13. Switch back to Google Sheets and click your new button.
14. Grant the required authorization to the script:

![mceclip4-7.png](./../image/uuid-fbe95ba0-ace7-91ad-0b5f-1922dc3bdd0d.png)![mceclip5-7.png](./../image/uuid-ff01f19b-c84c-deb9-2e43-34b0a584d532.png)
15. In Make, verify that the scenario has successfully executed.
### Note

This will only trigger a scenarioscenario to run when Scheduling is enabled. The linked webhook URL will not return any data but instead will trigger the scenario to run and allow the connected modules to return data.

[### Storing Dates in a Spreadsheet](#storing-dates-in-a-spreadsheet_body)If you store a [**Date**](https://www.integromat.com/en/help/item-data-types) value in a spreadsheet without any formatting,

![Google_Sheets_Update_Now.png](./../image/uuid-f25689cb-2876-062d-78a2-569c143758bd.png)it will appear as text in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) in the spreadsheet. However, Google Sheets formulas or functions that work with dates do not understand this text. E.g. formula `=A1+10` will display the following error:

![61d5b550dcbf8.png](./../image/uuid-8bd638b4-ec78-c414-da3f-0f9f065784e1.png)To help the GS to understand the date, format it with the formatDate(.) function. The correct format passed to the function as the second argument depends on the spreadsheet's locale settings. Choose **File** ▶ **Spreadsheet settings** from the main menu to verify/set the locale:

![61d5b551cd616.png](./../image/uuid-8e65c6cb-a30b-2828-86e6-7e8787f76686.png)Once you have verified/set the proper locale, determine the corresponding date and time format by choosing **Format ▶ Number** from the main menu. The format is displayed next to the **Date time** menu item:

![61d5b552f0373.png](./../image/uuid-2ea72bad-d233-00d1-6a79-321752fa7479.png)The following example shows the use of `M/D/YYYY HH:mm:ss` format for the United States locale:

![Google_Sheets_Date_formula.png](./../image/uuid-b76b3fb6-61f3-7a74-3067-3f77964b7fcc.png)[### Exploiting Google Sheets Functions](#exploiting-google-sheets-functions_body)If you miss a built-in function but it is featured by Google Sheets, you may exploit it.

[### Posting and Getting Images from Google Sheets](#posting-and-getting-images-from-google-sheets_body)When getting an image from Google Sheets, first make sure you enter the image as a formula. For example:`=IMAGE("https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg")` making use of the =IMAGE(...)

![61d5b554e1588.png](./../image/uuid-607e470a-c954-e582-7cf7-7fa4188aceda.png)After you have done so, open the Google Sheets module (e.g. **Watch Rows, Search Rows, Get a Cell**) and select **Show advanced settings**. Then select the Formula option in the **Value render option** field.

The output will be as shown below:

![61d5b555d5863.png](./../image/uuid-1b4bee4b-a620-519b-8c7f-05059438bab6.png)
```

               Then you can extract the URL using the replace function.







The output will be just the URL. 
            
```
To be able to post an image, make sure to enter the `=IMAGE(...)` formula that will be used in the cell and then enter the Image URL address.

![61d5b557395cf.png](./../image/uuid-418cf0b7-0e34-c3ed-a101-af4d68efad9f.png)[Usage Limits
------------](#usage-limits_body)If the error **429: RESOURCE\_EXHAUSTED** occurs, you have exceeded the API rate limit.

The Google Sheets API has a limit of 500 requests per 100 seconds per project, and 100 requests per 100 seconds per user. Limits for reads and writes are tracked separately. There is no daily usage limit.

See more details at [developers.google.com/sheets/api/limits](https://developers.google.com/sheets/api/limits).

### Note

**Did you know?**

You can find over 100 predefined Google Sheets sample templates in our [template gallery](https://www.make.com/en/templates).

