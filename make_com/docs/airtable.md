Airtable
========

The Airtable modules allow you to monitor records and submitted forms or search, retrieve, create, update, and delete records in your Airtable account.

To get started with Airtable, create an account at [airtable.com/signup.](https://airtable.com/signup)

Refer to the [Airtable REST API Documentation](https://airtable.com/api) for a list of available endpoints.

Connect Airtable to Make
------------------------

You can connect Airtable apps in Make in three ways:

* [Connect using OAuth](airtable.html#connect-using-oauth "Connect using OAuth")
* [Connect using Personal Access Token](airtable.html#connect-using-personal-access-token "Connect using Personal Access Token")
* [Connect using API Key](airtable.html#connect-using-api-key "Connect using API Key") (deprecated January 2024)
Connect using OAuth
-------------------

To connect Airtable using OAuth:

1. Log in to your Make account, open the Airtable module scenario, click the **Add** button next to the **Connection type** field, and select **Airtable OAuth**.

![airtable-24.png](./../image/uuid-c1cde636-a61b-b3e3-7663-df6eec1aece3.png)
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show Advanced Settings** and enter the client credentials created in the section, [Obtain OAuth Credentials](airtable.html#obtain-oauth-credentials "Obtain OAuth Credentials").
4. Click **Save**.
5. In the Authentication screen, click **Add a base** and select the base to which you want to grant access.

![airtable-21.png](./../image/uuid-9ca34efe-401b-03fd-8355-d817d053d0ed.png)
6. Click **Grant access**.

![airtable-22.png](./../image/uuid-46937687-76f9-c026-1864-d1282aa3a755.png)

You have successfully connected the Airtable app with Make.

[Obtain OAuth Credentials
------------------------](#obtain-oauth-credentials_body)Providing OAuth credentials is optional.

When you select the connection type as OAuth, authorize your account without the need to provide OAuth credentials.

To obtain OAuth credentials:

1. Log in to your Airtable account.
2. Click **Profile** > **Developer hub**.

![Airtable_2.png](./../image/uuid-d82a79b6-3eeb-00c4-84bb-7cac0b1b82d4.png)
3. Click **OAuth integrations** > **Register new OAuth integration**.

![Airtable_4.png](./../image/uuid-cedd631f-fd99-15aa-a4b3-3dd88ddb1cba.png)
4. Enter the name for the integration and OAuth redirect URL as `https://www.integromat.com/oauth/cb/airtable3`.

![Airtable_5.png](./../image/uuid-6ea18053-ed6d-8763-d059-a67041e9004b.png)
5. Click **Generate client secret**.

![Airtable_6.png](./../image/uuid-62199b76-a68b-6898-5bc2-01fc6ca8b05d.png)
6. Copy the Client ID and Client Secret to a safe place.

![Airtable_7.png](./../image/uuid-c37a336c-2fcb-eb58-8c31-ac03e4a0f25d.png)
7. Select the scopes, enter the support information, and click **Save changes**.

![airtableScopes.png](./../image/uuid-e448a5a7-7b56-fe86-7967-62c72bd09e54.png)![Airtable_3.png](./../image/uuid-a8f1e5e0-629b-68eb-1e09-369d9c1e5307.png)

You have successfully created OAuth credentials.

Connect using Personal Access Token
-----------------------------------

You can connect Airtable apps using personal access token values from your Airtable account.

1. Log in to your Airtable account.
2. Click **Your Profile Icon** > **Developer hub**.

![Airtable_2.png](./../image/uuid-d82a79b6-3eeb-00c4-84bb-7cac0b1b82d4.png)
3. Click **Personal access tokens > Create new token.**

![Airtable_11.png](./../image/uuid-918033d5-e3e0-a255-eaf7-9745ca56911d.png)
4. Enter a name for the access token, select the Scopes, Access, and click **Create token**.

Note: Users should choose at least the following most frequently required scopes: `data.records:read`, `data.records:write`, and `schema.bases:read`
5. Copy the Personal Access Token to a safe place, and click **Done**.
6. Log in to your Make account, open the Airtable module scenario, click the **Add** button next to the **Connection type** field, and select the connection type as **Airtable Token or Key**.

![airtable-24.png](./../image/uuid-c1cde636-a61b-b3e3-7663-df6eec1aece3.png)
7. Optional: In the **Connection name** field, enter a name for the connection.
8. Select the token type as **Personal Access Token** and enter the token copied in step 5 above.
9. Optional: Click **Show Advanced Settings**and select the proxy service in the **Proxy** field.

### Note

By choosing a Proxy, you understand and confirm that your Airtable data, including personal access tokens, will be routed through a third-party service.
10. Click **Save**.

You have successfully established the connection. You can now edit your scenario and add more Airtable modules. If your connection needs reauthorization, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[Connect using API Key
---------------------](#connect-using-api-key_body)You can connect Airtable apps using an API Key from your Airtable account.

### Caution

API keys will be deprecated by the end of January 2024. After this date, API keys will stop working, and you will have to migrate to personal access tokens.

1. Log in to your Airtable account.
2. Click **Your Profile Icon** > **Developer hub**.

![Airtable_2.png](./../image/uuid-d82a79b6-3eeb-00c4-84bb-7cac0b1b82d4.png)
3. Click **API key** and copy the API key to a safe place.

![Airtable_11.png](./../image/uuid-918033d5-e3e0-a255-eaf7-9745ca56911d.png)
4. Log in to your Make account, open the Airtable module scenario, click the **Add** button next to the **Connection type** field, and select the connection type as **Airtable Token or Key**.

![airtable-24.png](./../image/uuid-c1cde636-a61b-b3e3-7663-df6eec1aece3.png)
5. Optional: In the **Connection name** field, enter a name for the connection.
6. Select the token type as **API Key** and enter the token copied in step 3 above.
7. Optional: Click **Show Advanced Settings**and select the proxy service in the **Proxy** field.

### Note

By choosing a Proxy, you understand and confirm that your Airtable data, including API keys, will be routed through a third-party service.
8. Click **Save**.

You have successfully established the connection. You can now edit your scenario and add more Airtable modules. If your connection needs reauthorization, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build Airtable Scenarios
------------------------

After connecting the app, you can perform the following actions:

Records
-------

You can watch, create, update, search, retrieve, upsert, delete records, and watch responses using the following modules.

[### Watch Records](#watch-records-964541_body)Returns all newly created or updated records in a view (required **Created Time** or **Last Modified Time** fields).



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base that contains the table you want to watch for records. |
| **Table** | Select the table you want to watch for new records. |
| **Trigger configuration** | **Trigger field**Select the `Created Time` option to watch for new records or the `Last Modified Time` option to watch for modified records.If you do not have a `Created Time` or `Last Modified Time` field in your scheme, we ask you to create one. Without this field, the trigger will not work correctly.61d5a7b5d47d6.gif**Label field**: used as a label for a record. For example, **Status** dialog.Airtable_trigger_field.png |
| **Limit** | The maximum number of records Make will return during one execution cycle. |
| **View** | Select the view to watch the records. If selected, it will return the records only in that view. |
| **Formula** | Enter the formula to filter records. For more details, refer to the [Formula field reference documentation](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference).The formula will be evaluated for each record, and if the result is not `0`, `false`, `""`, `NaN`, `[]`, or `#Error!`, includes the record in the response.If combined with the `view` parameter, it returns only records in that view that satisfy the formula.For example, to only include records where Name isn't empty, pass in `NOT({Name} = '')` as a parameter like this:`filterByFormula=NOT%28%7BName%7D%20%3D%20%27%27%29` |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Watch Responses](#watch-responses_body)Triggers when a new response is submitted.

### Warning

Available for paid ***Pro Plan*** only. See the [Airtable pricing page](https://airtable.com/pricing).

The webhook URL needs to be generated in Make and added to the form configuration in the Airtable.

1. Add the Watch Responses module to your Makescenario.
2. Generate and copy the webhook URL.

![Airtable_webhook_.gif](./../image/uuid-5a6a77e8-25b0-c132-69df-c7fc07884beb.gif)
3. Log in to your Airtable account.
4. Open the *Base* and the *table* you want for the form and create a *Form view*.

![61d5a7c07e2c4.gif](./../image/uuid-01a1e015-be71-4fe8-2e70-4d3fa0513e4b.gif)
5. Set the form as needed, scroll down the form, and enable the *Redirect to URL after the form is submitted* option.

![61d5a7c446f88.png](./../image/uuid-0ba91ca6-9ad3-a057-2abb-c80c87a32697.png)
6. Enter the Webhook URL generated in step 2 to the displayed dialog box and add the *?record\_id={record\_id}* just after the webhook URL to include the *Record ID* in the module's output, then click Save. The resulting URL will, for example, look like this:

*https://hook.eu1.make.com/tgnp28pewooafbdgobvbh225hmocbn85?record\_id={record\_id}*

![61d5a7c61cdbc.png](./../image/uuid-61bd60c6-982a-4816-a0ba-b2a384f4f1b6.png)
7. Go back to your Makescenario and run the *Watch Responses* module **only** to load the Record ID from Airtable and to be able to map that field into the other modules.

Note: Airtable only supports sending the `record_id` parameter.
8. Submit the form in Airtable where the *Redirect to URL after the form is submitted* option is enabled and the Webhook URL is added (step 6 above).

The Watch Responses module is triggered and loads the Record ID.

![61d5a7c7b5df4.gif](./../image/uuid-7d8fed27-06f7-091f-9a46-4d59df4ecdf6.png)
9. Add the *Airtable > Get a Record* module just after the *Airtable > Watch Responses* module and map the *record\_id* to the *Record ID* field.

![Airtable_record_ID.png](./../image/uuid-329e4c78-3f76-ee21-59ad-ddf47bc2ff5f.png)
Every time the form is submitted, the *Watch Responses* module in your Makescenario is triggered, and the *Get a Record* module returns the submitted form details.

[### Search Records](#search-records-964541_body)Searches for specific records or returns all records.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select or map the base that contains the table you want to search for records. |
| **Table** | Select the table you want to search for records. |
| **Formula** | Enter the formula to filter records. For more details about formulae, refer to the [Formula field reference documentation](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference). The formula will be evaluated for each record, and if the result is not `0`, `false`, `""`, `NaN`, `[]`, or `#Error!`, includes the record in the response.If combined with the `view` parameter, returns only the records in that view that satisfy the formula.For example, to only include records where Name isn't empty, pass in `NOT({Name} = '')` as a parameter like this:`filterByFormula=NOT%28%7BName%7D%20%3D%20%27%27%29` |
| **Sort** | Specify sorting, if needed. The higher item in the list has precedence. |
| **View** | Select or map the view for the search results. |
| **Output Fields** | Add the fields you want to receive in the output. If no field is provided, all fields will be returned. It can be the field's name, for example, `Email`, or the field's ID, for example, `fldzuOSozlM84fYV3`. |
| **Limit** | Set the maximum number of records Make will return during one execution cycle. The default value is 10. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Get a Record](#get-a-record-964541_body)Retrieves a single record by its ID.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base that contains the table with the record whose details you want to retrieve. |
| **Table** | Select the table that contains the record whose details you want to retrieve. |
| **Record ID** | Enter (map) the Record ID whose details you want to retrieve. Alternatively, you can use the search option to select the record. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Create a Record](#create-a-record-964541_body)Creates a new record in a Airtable.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base containing the table you want to create a record. |
| **Table** | Select the table in which you want to create a record. |
| ***Record*** | Enter values to the desired fields. [See also Airtable's guide to basic field types](https://support.airtable.com/hc/en-us/articles/203229705-Guide-to-the-basic-field-types). |
| **Smart links** | Enable this option if you want to enter names instead of record IDs to fields that link to another table. The record is automatically created in the linked table if there is no match. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Update a Record](#update-a-record-964541_body)Updates a record by its ID.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base containing the table whose records you want to update. |
| **Table** | Select the table whose record you want to update. |
| **Records ID** | Enter (map) the Record ID you want to update. You can retrieve the ID, for example, using the *Search Records* or *Watch Records* module. Alternatively, you can use the **Search** button to select the Record ID. |
| ***Record*** | Enter values in the fields you want to update. [See also Airtable's guide to basic field types](https://support.airtable.com/hc/en-us/articles/203229705-Guide-to-the-basic-field-types).NoteTo delete the content of the field, use the `erase` function.Airtable_erasing_a_field.png2019-05-06-15_11_20-window.png |
| **Smart links** | Enable this option if you want to enter names instead of record IDs to fields that link to another table. The record is automatically created in the linked table if there is no match. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Upsert a Record](#upsert-a-record_body)Creates a new or updates an existing record.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base containing the table you want to update or create a record. |
| **Table** | Select the table where you want to create or update a record. |
| **Record ID** | Enter (map) the ID of the record you want to update. If no ID is entered, it will create a new record. You can retrieve the ID, for example, using the *Search Records* or *Watch Records* module. Alternatively, you can use the **Search** button to select the Record ID.If you enter an ID that does not exist, an error occurs, and no action is performed. |
| ***Record*** | Enter values in the fields you want to update or create. [See also Airtable's guide to basic field types](https://support.airtable.com/hc/en-us/articles/203229705-Guide-to-the-basic-field-types). |
| **Smart links** | Enable this option if you want to enter names instead of record IDs to fields that link to another table. The record is automatically created in the linked table if there is no match. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

[### Delete a Record](#delete-a-record-964541_body)Deletes a record by its ID.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select the base that contains the table you want to delete a record from. |
| **Table** | Select the table you want to delete the record from. |
| **Record ID** | Enter the ID of the record you want to delete. You can retrieve the ID, for example, using the *Search Records* or *Watch Records module*. Alternatively, you can use the **Search** button to select the Record ID. |

[### Create a Record (Advanced)](#create-a-record--advanced-_body)Creates a record with mapped fields.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Enter the base that contains the table you want to create a record in. |
| **Table** | Enter the table you want to create a record in. |
| **Record Fields as Array** | Add the **Column ID** and **Field** value by selecting the field type for the record you want to create. |
| **Smart links** | Enable this field to enter the user name in the linked record fields instead of record IDs to select an existing record or create a new one if it doesn't exist and use it to add new options in single/multiple select fields. |

[### Update a Record (Advanced)](#update-a-record--advanced-_body)Updates a record with mapped fields.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Enter the base that contains the table whose record details you want to update. |
| **Table** | Enter the table whose record details you want to update. |
| **Record ID** | Enter the Record ID whose details you want to update. |
| **Record Fields** | Add a new **Column ID** and **Field** value by selecting the field type you want to update. |
| **Smart links** | Enable this field to enter the user name in the linked record fields instead of record IDs to select an existing record or create a new one if it doesn't exist and use it to add new options in single/multiple select fields. |

[### Search Records (Advanced)](#search-records--advanced-_body)Searches for specific records or returns all records. Advanced module for mapping.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base ID** | Enter the Base ID that contains the table whose records you want to search. |
| **Table** | Enter the table whose records you want to search. |
| **Sort** | A list of sort objects that specifies the way you want to order the records. For example, **asc**. |
| **View** | The name or ID of a view of the records in the table. |
| **Formula** | A [formula](https://support.airtable.com/docs/formula-field-reference) is used to filter records. The formula will be evaluated for each record, and if the result is not `0`, `false`, `""`, `NaN`, `[]`, or `#Error!` includes the record in the response. |
| **Output Fields** | Add the fields you want to receive in the output. If no field is provided, all fields will be returned. It can be the field's name, for example, `Email`, or the field's ID, for example, `fldzuOSozlM84fYV3`. |
| **Limit** | Set the maximum number of records Make will return during one execution cycle. |
| **Use Column ID** | Select whether to use column ID instead of column name for mapping.This enables persistence over the column name change. Enabling this option allows to replace entity keys in the response; instead of entity names specified as parameter keys, their identifiers will be specified. Changing this value will break all existing mappings in this scenario. |

Other
-----

You can list bases, table schemas, and call APIs using the following modules.

[### Make an API Call](#make-an-api-call-964541_body)Allows you to perform a custom API call.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **URL** | Enter a path relative to `https://api.airtable.com/`. For example, `/v0/{base_id}/{table_id}`.NoteFor the list of available endpoints, refer to the [Airtable REST API Documentation](https://airtable.com/api). |
| **Method** | Select the HTTP method you want to use:* **GET**to retrieve information for an entry. * **POST**to create a new entry. * **PUT**to update/replace an existing entry. * **PATCH**to make a partial entry update. * **DELETE**to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

#### Example of Use - List Records

The following API call returns all records in the specified table in your Airtable account:

**URL**:

`/v0/{base_id}/{table_id}`

**Method**:

`GET`

![Airtable_api_call.png](./../image/uuid-fda0bf2b-9632-8d5c-04ca-f518e4786e2b.png)Search results can be found in the module's **Output** under **Bundle > Body > records**. 

In our example, 4 records were returned:

![Airtable_api_bundles.png](./../image/uuid-a7be47ed-ca03-b75d-5ff5-adc892e170a5.png)[### List Bases](#list-bases_body)Returns the detailed list of all bases.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Limit** | Set the maximum number of bases Make will return during one execution cycle. |

[### List Table Schemas](#list-table-schemas_body)Returns the schema of the tables in the specified base.



| **Connection** | Establish a connection to your Airtable account. |
| --- | --- |
| **Base** | Select or map the base whose table schemas you want to list. |
| **Limit** | Set the maximum number of table schemas Make will return during one execution cycle. |

### Note

When changing data types for fields, please perform a hard refresh of the form to ensure that the new data types will be displayed.

To perform a hard refresh, click the three dots at the upper right of the module and select **Refresh form**.

![airtable_refresh.png](./../image/uuid-5cd5ebac-fd32-42ef-bf4a-4568570b7ea0.png)