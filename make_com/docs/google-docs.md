Google Docs
===========

With Google Docs modules in Make you can monitor, create, edit, retrieve, download, and delete documents in your Google Docs account.

To use the Google Docs modules, you must have a Google account. You can create an account at [accounts.google.com](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp).

Refer to the [Google Docs API documentation](https://developers.google.com/docs/api/reference/rest) for a list of available endpoints.

### Note

Make's use and transfer of information received from Google APIs to any other app will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

Connect Google Docs to Make
---------------------------

To establish the connection in Make:

1. Log in to your Make account, add a Google Docs module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Switch on the **Show advanced settings** toggle and enter your Google Cloud Console project client credentials. For more information, see the [Create and configure a Google Cloud Console project for Google Docs section](google-docs.html#create-and-configure-a-google-cloud-console-project-for-google-docs "Create and configure a Google Cloud Console project for Google Docs") below.
4. Click **Sign in with Google**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Google Docs modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

[### Create and configure a Google Cloud Console project for Google Docs](#create-and-configure-a-google-cloud-console-project-for-google-docs_body)To connect to Make using your own client credentials, you can create and configure a project in the Google Cloud Console.

#### Create a Google Cloud Console project for Google Docs

To create a Google Cloud Console project:

1. Log in to the [Google Cloud Console](https://console.cloud.google.com/) using your Google credentials.
2. In the top menu, click **Select a project** > **New project**.
3. Enter a **Project name** and select the **Location** for your project.
4. Click **Create**.
5. In the top menu, check if your new project is selected in the **Select a project** dropdown. If not, select the project you just created.
#### Enable APIs for Google Docs

To enable the required APIs:

1. Open the left navigation menu and go to **APIs & Services** > **Library**.
2. Search for and enable the following APIs: **Google Docs API, Google Drive API**.
#### Configure your OAuth consent screen for Google Docs

To configure your OAuth consent screen:

1. In the left sidebar, click **OAuth consent screen**.
2. Under **User Type**, select **External**.

For more information regarding user types, refer to [Google's Exceptions to verification requirements documentation](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts).
3. Click **Create**.
4. Fill in the required fields with your information.
5. In the **Authorized domains** section, add `make.com` and `integromat.com`.
6. Click **Save and continue**.
7. In the **Scopes** page, click **Add or remove scopes**, add the following scopes, and click **Update**.


	* `https://www.googleapis.com/auth/userinfo.email`
	* `https://www.googleapis.com/auth/drive`
	* `https://www.googleapis.com/auth/documents`
	* `https://www.googleapis.com/auth/documents.readonly`
8. Click **Save and continue**.
9. Optional: If your project will remain in the **Testing** publishing status, add test user emails on the **Test users** page, then click **Save and continue**.
#### Create your Google Docs client credentials

To create your client credentials:

1. In the left sidebar, click **Credentials**.
2. Click **+ Create Credentials** > **OAuth client ID**.
3. In the **Application type** dropdown, select **Web application**.
4. Update the **Name** of your OAuth client. This will help you identify it in the console.
5. In the **Authorized redirect URIs** section, click **+ Add URI** and enter the following redirect URI: `https://www.integromat.com/oauth/cb/google`.
6. Copy your **Client ID** and **Client secret** values and store them in a safe place.

You will use these values in the **Client ID** and **Client Secret** fields in Make.

Build Google Docs Scenarios
---------------------------

After connecting the app, you can perform the following actions:

### Document

[#### Watch Documents](#watch-documents-968237_body)Triggers when a new document is created or modified in a specific folder.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Watch Documents** | Select whether you want to watch created or modified documents. |
| **Choose a Drive** | Select the drive that contains the documents you want to watch.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Folder ID** | Select the folder that contains the documents you want to watch. |
| **Limit** | Set the maximum number of documents Make will return in one execution cycle. |

[#### List Documents](#list-documents-968237_body)Retrieves a list of documents.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Choose a Drive** | Select the drive that contains the documents you want to list.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Folder ID** | Select the folder that contains the documents you want to list. |
| **Limit** | Set the maximum number of documents Make will return in one execution cycle. |

[#### Get Content of a Document](#idp1189212_body)Gets a content of a document.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Get Content of a Document** | Select to map the ID of the document you want to get or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive that contains the documents whose content you want to get.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to retrieve. |
| **Filter** | Select the type of content you want to receive in the outFor further mapping of filter objects in next modules, use **Inline Objects Array**. The Inline Objects Array objects are sorted in the same order they appear in the document. |

[#### Create a Document](#idp1189213_body)Creates a new Google document by adding the content in the HTML format.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Name** | Enter the name of a document. |
| **Content** | Enter the content of a document. You can use HTML tags. |
| **Choose a Drive** | Select the drive where you want to put a created document into.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **New Document's Location** | Select the folder where you want to save a document. |
| **Insert a Header** | Select whether you want to add a header to a document. |
| **Insert a Footer** | Select whether you want to add a footer to a document. |

[#### Create a Document from a Template](#idp1189214_body)Creates a copy of an existing template document and replaces any tags, for example, `{{!notfound:name}}`. This module allows replacing images by new images with URLs.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Create a Document from a Template** | Select to map the ID of the document you want to use as a template or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive where you want to put a created document into.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to use as the template for the new document. |
| **Values** | | **Tags** | Enter the tag associated with the documentation template. Do not use `{{}}`. | | --- | --- | | **Replaced Value** | Enter the value of the tag. | |
| **Images Replacement** | You may add the **alt text** to an image.  | **Image Object ID** | Enter the Image Object ID. To retrieve the ID, use the **Get Content of a Document** module. You can find the ID in **Inline Object Array**, in the module output. | | --- | --- | | **Image URL** | Enter the URL of the image that will replace the current image. | |
| **Title** | Enter the name for a new document. |
| **New Drive Location** | Select the drive where you want to save the document. |
| **New Document's Location** | Select the folder where you want to save a document. |

[#### Insert a Paragraph to a Document](#idp1189215_body)Inserts or appends a new paragraph to an existing document.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Select a Document** | Select to map the ID of the document for editing or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive that contains the documents you want to insert a paragraph into. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to edit. |
| **Insert a Paragraph** | Select the way you want to insert a paragraph.Select **By appending to the body of the document** to append the text to the current document body:  | **Appended Text** | Enter the text you want to append. Make copies the style of the new paragraph from the paragraph at the current insertion index, including lists and bullets. | | --- | --- |  Select **By appending to the end of the segment** to insert the text to the header or the footer:  | **Header ID** | Enter the header ID that you want to inset the text to. | | --- | --- | | **Insert Text** | Enter the text you want to insert. | | **Footer ID** | Enter the footer ID that you want to insert the text to. | | **Insert Text** | Enter the text you want to insert. | |
| **Specify the location** | If you selected **By specification of location** above, specify the location where you want to insert text.**By Index**  | **Index** | Enter the element index that you want to append the text to. To retrieve the ID, use the **Get Content of a Document** module. You can find the ID in the **Body** collection, in the module output. | | --- | --- | | **Inserted Text** | Enter the text you want to insert. |  **By Segment ID**: Select the header and footer where you want to insert the text content to and enter the very text. |

[#### Insert an Image to a Document](#idp1189216_body)Inserts a new image with a URL to a document.

Note: The maximum image size is 50 MB. The image resolution must not exceed 25 megapixels. Only PNG, JPEG, or GIF formats are supported.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Select a Document** | Select to map the ID of the document for editing or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive that contains the documents you want to insert an image into. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to edit. |
| **Insert an Image** | Select the way you want to insert an image.Select **By appending to the body of the document** to append an image to the current document body:  | **Image URL** | Enter the URL of the image you want to insert. | | --- | --- |  Select **By appending to the end of the segment** to insert an image to the header or the footer:  | **Header ID** | Enter the header ID that you want to inset the text to. | | --- | --- | | **Image URL** | Enter the URL of the image you want to insert. | | **Height Magnitude in Points** | Define the height of the inserted image. The new image will keep the aspect ratio. | | **Width Magnitude in Points** | Define the width of the inserted image. The new image will keep the aspect ratio. | | **Footer ID** | Enter the footer ID that you want to inset the text to. | | **Image URL** | Enter the URL of the image you want to insert. | | **Height Magnitude in Points** | Define the height of the inserted image. The new image will keep the aspect ratio. | | **Width Magnitude in Points** | Define the width of the inserted image. The new image will keep the aspect ratio. | |
| **Specify the Location** | If you selected **By specification of location** above, specify the location where you want to insert the text.**By Index**  | **Index** | Enter the element index that you want to append the text to. To retrieve the ID, use the **Get Content of a Document** module. You can find the ID in the **Body** collection, in the module output. | | --- | --- | | **Image URL** | Enter the URL of the image you want to insert. |  **By Segment ID**: Select the header and footer where you want to insert the image to and enter the link to the image. |

[#### Replace an Image with a New Image](#idp1189217_body)Replaces an existing image with a new image with a URL in the document. To fill the original image's bounds, the new image may be scaled or cropped.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Replace an Image** | Select to map the ID of the document for editing or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive that contains the documents with an image you want to replace. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to edit. |
| **Image URLs** | Enter the URL of the new image that will replace the existing one. Make displays image bodies as per images order in the document. |
| **Images Replacement** | Specify an image you want to replace alongside with a new image.  | **Image Object ID** | Enter the Image Object ID. To retrieve the ID, use the **Get Content of a Document** module. You can find the ID in **Inline Object Array**, in the module output. | | --- | --- | | **Image URL** | Enter the URL of the image that will replace the current image. | |

[#### Replace a Text in a Document](#idp1189218_body)Replaces an old text by a new text in a document.



|  |  |
| --- | --- |
| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| **Choose a Drive** | Select the drive that contains the documents with the text you want to replace. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to edit. |
| **Replace a Text** | Specify the text you want to replace alongside with a new text.  | **Old text to be replaced** | Enter the text you want to replace. | | --- | --- | | **New text to be inserted** | Enter a new text. | |

[#### Download a Document](#idp1189219_body)Downloads a document to a required format.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Choose a Drive** | Select the drive that contains the documents you want to download. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to download. |
| **Type** | Select the target file format of the downloaded document. |

[#### Delete a Document](#idp1189220_body)Deletes a document.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Choose a Drive** | Select the drive that contains the documents you want to delete. In the **Folder ID** field, select the drive.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document you want to delete. |

### Other

[#### Make an API Call](#make-an-api-call-968237_body)Performs an arbitrary authorized API call.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **URL** | Enter a path relative to `https://docs.googleapis.com/`. For example, `/v1/documents/{DocumentID}`.For the list of available endpoints, refer to the [Google Docs API Documentation](https://developers.google.com/docs/api/reference/rest). |
| **Method** | Select the HTTP method you want to use:* GET: To retrieve information for an entry. * POST: To create a new entry. * PUT: To update/replace an existing entry. * PATCH: To make a partial entry update. * DELETE: To delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

[#### Make All Links in a Document Clickable](#make-all-links-in-a-document-clickable_body)Makes all links in a document clickable.



| **Connection** | [Establish a connection to your Google Docs account.](google-docs.html "Google Docs") |
| --- | --- |
| **Make All Links in a Document** | Select to map the ID of the document that contains links or select the document from the dropdown menu. |
| **Choose a Drive** | Select the drive that contains the documents with links.The **Google Shared Drive** option is available only for Google Workspace users:  | **Use Domain Admin Access** | Request the list of drives that require admin access. | | --- | --- | | **Shared Drive** | Select the drive. | |
| **Document ID** | Select or map the document. |

