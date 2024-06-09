Dropbox
=======

With Dropbox modules in Make, you can manage the files and folders in your Dropbox account.

To use the Dropbox modules, you must have a Dropbox account. You can create an account at [www.dropbox.com/register](https://www.dropbox.com/register).

Refer to the [Dropbox API documentation](https://www.dropbox.com/developers/documentation/http/documentation) for a list of available endpoints.

Connect Dropbox to Make
-----------------------

To establish the connection in Make:

1. Log in to your Make account, add a Dropbox module to your scenario, and click **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. Optional: Click **Show advanced settings** and enter your custom app client credentials. For more information, refer to [Dropbox OAuth Guide](https://developers.dropbox.com/oauth-guide).

If requested, use the following Redirect URI when creating your custom app: `https://www.integromat.com/oauth/cb/dropbox`.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Dropbox modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Build Dropbox Scenarios
-----------------------

After connecting the app, you can perform the following actions:

Trigger Files* Watch Files
Get Files/Folders* Search Files/Folders
* Download a File
* List All Files/Subfolders in a Folder
* List File Revisions
Create & Update File/Folder* Upload a File
* Create a Folder
* Create/Overwrite a Text File
* Create/Update a Share Link
* Restore a File
* Move a File/Folder
* Rename a File/Folder
* Delete a File/Folder
* Copy a File/Folder
File Requests* Create a File Request
* Get a File Request
* Update a File Request
* Delete Closed File Requests
* List File Requests
Other* Make an API Call
Common problems
---------------

[### Unable to upload or update a file](#unable-to-upload-or-update-a-file-968222_body)There are several situations when uploading or updating a file fails:

* The uploaded file is too big and exceeds the maximum file size allowed for your Dropbox plan or you have used all of your Dropbox account's storage quota. You will either need to delete existing files from your Dropbox account or upgrade your plan.
* The previously selected folder, to which the file is being uploaded to, no longer exists. The scenario gets stopped and you will need to select the target folder again.
[### Image referenced via a shared link does not render](#image-referenced-via-a-shared-link-does-not-render_body)The URL returned by the **Dropbox > Create a shared link** does not link directly to an image, but to a Dropbox page - see <https://www.dropbox.com/help/desktop-web/force-download> for further details. To force the image to download, replace the trailing `?dl=0` with `?dl=1`. To force the image to render (e.g. in a Web browser or in Facebook Messenger), append `&raw=1` to the URL.

If you need to get the direct/raw link of your image which you can use for your website or for other Make modules you need to modify the initial shared URL in the following way:

Let's say your initial URL is:

`https://www.dropbox.com/s/ia8qtvs20f3a5ux/Screen%20Shot%202018-10-15%20at%204.21.11%20PM.png?dl=0`

1. replace *www* with *dl*

2. remove *?dl=0*

Your final URL should be:

`https://dl.dropbox.com/s/ia8qtvs20f3a5ux/Screen%20Shot%202018-10-15%20at%204.21.11%20PM.png`

To do it automatically, use the **replace()** function twice:

to replace *www* with *dl*



| 61d5afa1965f9.png |
| --- |

and

to remove *?dl=0*



| 61d5afa324f7b.png |
| --- |

To do it in one step, combine these functions:



| 61d5afa4b8018.png |
| --- |

You can use this code. Just copy it and paste it into the field and replace variable with the URL.

{{replace(replace(1.url; "?dl=0"; ""); "www"; "dl")}}

