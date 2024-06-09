OpenAI (ChatGPT, Whisper, DALL-E)
=================================

With OpenAI (ChatGPT, Whisper, DALL-E) modules in Make, you can create chat or prompt completions, edits, and moderations, generate images, and call APIs.

To get started with OpenAI, you need an [OpenAI account](https://chat.openai.com/auth/login).

### Note

Make modules support GPT-3.5, and GPT-4 models provided the user has access. If you do not have access, please [join the waitlist](https://openai.com/waitlist/gpt-4) to get access when capacity is available.

[GPT-4](https://platform.openai.com/docs/models/gpt-4) is currently in a limited beta version and is only accessible to those who have been granted access.

Connect OpenAI to Make
----------------------

To connect OpenAI to Make, you must obtain an API Key and Organization ID from your account.

1. Log in to your OpenAI (ChatGPT, Whisper, DALL-E) account.
2. Click on your profile icon in the top right corner > **View API Keys**.

![OpenAI1.png](./../image/uuid-a99f4c41-0079-5417-1e58-3a0bccfec834.png)
3. Click **Create new secret key**, give the key a name (optional), and click **Create secret key**.
4. Copy the secret key, store it in a safe place as you will not be able to view it again, and click **Done**.
5. Go to your [account settings](https://beta.openai.com/account/org-settings) page and copy your **Organization ID** to your clipboard.

![openai-2.png](./../image/uuid-839be048-9cfc-9e60-cefd-ebb298c69ab0.png)
6. Log in to your Make account, add an OpenAI (ChatGPT, Whisper, DALL-E) module to a scenario, and click **Create a connection**.
7. Optional: In the **Connection name** field, enter a name for the connection.
8. In the **API Key** field, enter the secret key copied in step 4.
9. In the **Organization ID** field, enter the organization ID copied in step 5 and click **Save**.

You have successfully established the connection. You can now edit your scenario and add more OpenAI (ChatGPT, Whisper, DALL-E) modules. If your connection needs reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Actions
-------

[### Analyze Image(s) - Vision](#analyze-image-s----vision-1760423_body)Accepts an array of images as an input and provides an analysis result for each of the images following the instructions specified in the prompt.

### Note

If you do not have access to the GPT-4 models, please [join the waitlist](https://openai.com/waitlist/gpt-4) to get access when capacity is available.

[GPT-4](https://platform.openai.com/docs/models/gpt-4) is currently in a limited beta version and is only accessible to those who have been granted access.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Prompt** | Enter instructions for how to analyze the image(s). |
| **Images** | Add or map the images you want to analyze.You can add images by entering an **Image URL** or **Image file** data.**Image URL**: Enter the URL address to a public resource of the image. For example, `https://getmyimage.com/myimage.png`.**Image file**: Map or select the binary data of the image. You can retrieve the binary data of an image using the **HTTP: Get a file** module, or another app such as **Dropbox**. |
| **Model** | Select or map the model you want to use.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Max Token** | Enter the maximum number of tokens to use for the completion. The default value is 300. |
| **Temperature** | Specify the sampling temperature to use.Higher temperatures generate more diverse and creative responses. For example, `0.8`. Lower temperatures generate more focused and well-defined responses. For example, `0.2`. The default value is `1`.The value must be lower than or equal to 2. |
| **Top P** | Specify the Top P value to use nucleus sampling. This will consider the results of the tokens with probability mass. The default value is `1`.The value must be lower than or equal to 1. |
| **Number** | Enter the number of responses to generate. If more than 1 response is generated, the results can be found in the module's output within **Choices**. The default value is `1`. |

[### Create a Completion (GPT-3, GPT-3.5, GPT-4)](#idp1189231_body)Creates a completion for the provided prompt or chat.

See the [OpenAI model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility) section for the list of supported models.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Select Method** | Select a method to create a completion. |
| **Model** | Select or map the model you want to use.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Messages** | Add the messages for which you want to create the completion by selecting the **Role** and entering the **Message Content**.For more information about chat completion, refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/chat). |
| **Max Token** | The maximum number of tokens to generate in the completion. The default value is 16. |
| **Temperature** | Specify the sampling temperature to use.A higher value means the model will take more risks. Try 0.9 for more creative applications and 0 (argmax sampling) for ones with a well-defined answer. Defaults to 1. |
| **Top P** | An alternative to sampling with temperature is called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. Defaults to 1. |
| **Number** | The number of completions to generate for each prompt. Defaults to 1. |
| **Frequency Penalty** | Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. This value must be a number between -2 and 2. |
| **Presence Penalty** | Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. This value must be a number between -2 and 2. |
| **Token Probability** | Add the token probability by selecting the **Token** and **Probability**. The **Probability** must be a number between -100 and 100. |
| **Response Format** | Choose the format for the response. |
| **Seed** | This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Refer to the `system_fingerprint` response parameter to monitor changes in the backend.For more information, refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/chat). |
| **Stop Sequences** | Add up to 4 sequences where the API will stop generating further tokens. |
| **Other Input Parameters** | Add any additional input parameters by selecting the **Parameter Name** , the **Input Type**, and entering the **Parameter Value**.For more information, refer to the [OpenAI documentation](https://platform.openai.com/docs/guides/chat). |

[### Create a Moderation](#create-a-moderation-1760423_body)Classifies if text violates OpenAI's Content Policy.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Input** | Enter the text for which you want to create the moderation. The module will classify the content against OpenAI's Content Policy. |

[### Edit an Image](#edit-an-image-1760423_body)Edits or extends an image.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Image** | Enter an image to edit. The file must be in PNG format, less than 4 MB, and square. If a Mask file is not provided, the image must have transparency, which will be used as the mask. |
| **Prompt** | Enter details of the images you want to edit. The maximum number of characters allowed is 1000. |
| **Mask** | Enter an additional image with fully transparent areas (where alpha is zero). The transparent areas indicate where the Image will be edited. The file must be in PNG format, less than 4 MB, and the same dimensions as Image above. |
| **Number** | Enter the number of images to generate. Enter a number between 1 and 10. |
| **Size** | Select or map the size of the images to generate. It must be one of `256x256`, `512x512`, or `1024x1024`. |
| **Response Format** | Select or map the format in which the generated images are returned.If you select `Base64-encoded` PNG, the raw PNG image can be obtained by using the IML function, `toBinary(<module_no>.data[].b64_json; base64)` in the subsequent modules. |

[### Generate an Image](#generate-an-image-1760423_body)Generates an image with DALL E given a prompt.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Model** | Select or map the model you want to use.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Prompt** | Enter details of the images you want to generate. The maximum number of characters allowed is 1000 if your model is Dall-E 2 and 4000 if your model is Dall-E 3. |
| **Size** | Select or map the size of the images to generate. It must be one of `256x256`, `512x512`, or `1024x1024`. |
| **Number** | Enter the number of images to generate. Enter a number between 1 and 10. |
| **Response Format** | Select or map the format in which the generated images are returned.If you select `Base64-encoded` PNG, the raw PNG image can be obtained by using the IML function, `toBinary(<module_no>.data[].b64_json; base64)` in the subsequent modules. |
| **Quality** | Select the quality of the generated image. HD generates images with finer details and greater consistency across the image. |

[### Create a Translation (Whisper)](#create-a-translation--whisper--1760423_body)Creates a translation of an audio into English.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **File Name** | Enter the name of the file you want to translate. |
| **File Data** | Enter the data of the file you want to translate. |
| **Model** | Select or map the model you want to use. Refer to the [OpenAI Audio API documentation](https://platform.openai.com/docs/api-reference/audio) for information on available models.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Prompt** | Enter text to guide the model's style or continue a previous audio segment. (Optional) The prompt should be in English. |
| **Temperature** | Enter a sampling temperature between 0 and 1. Higher values, such as 0.8, will make the output more random. Lower values, such as 0.2, will make it more focused and deterministic. |

[### Create a Transcription (Whisper)](#create-a-transcription--whisper--1760423_body)Creates a transcription of an audio to text.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **File Name** | Enter the name of the file you want to transcribe. |
| **File Data** | Enter the data of the file you want to transcribe. |
| **Model** | Select or map the model you want to use. Refer to the [OpenAI Audio API documentation](https://platform.openai.com/docs/api-reference/audio/create) for information on available models.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Prompt** | Enter text to guide the model's style or continue a previous audio segment. (Optional) The prompt should be in the same language as the audio. |
| **Temperature** | Enter a sampling temperature between 0 and 1. Higher values, such as 0.8, will make the output more random. Lower values, such as 0.2, will make it more focused and deterministic. |
| **Language** | Enter the two letter ISO code of the input audio's language. |

[### Transform a Text to a Structured Data](#transform-a-text-to-a-structured-data-1760423_body)Identifies specified information in a prompt's raw text and returns it as structured data.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Model** | Select or map the model you want to use to transform text into structured data.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Text to Parse** | Enter the text containing the data that you want to transform. |
| **Prompt** | Enter a short description explaining what type of data should be extracted from the text entered above. |
| **Structured Data Definition** | Enter parameters or map the way in which the structured data should be returned.  | **Parameter Name** | Enter a name for the parameter. Adhere to the following rules:1. The first character must be either a letter or an underscore.2. Do not include any commas or spaces.3. Do not use any special symbols, other than an underscore. | | --- | --- | | **Description** | Enter a short description of the parameter.This description is part of the prompt, so the more clear your description, the more accurate the response.For example, if would like OpenAI to search for coordinates in the text, you can enter `Latitude and Longitude of the location`. | | **Data Type** | Select or map the data type format in which the parameter is returned.If there will be multiple occurrences of similar data types, select an **Array** option. For example, if there are coordinates of multiple locations to be returned, select **Array (text)** . | | **Value Examples** | Enter or map examples of possible values to be returned. The more examples you provide, the more accurate the response will be. | | **Is Parameter Required?** | Select or map whether the parameter is required.When selecting `yes`, OpenAI will be forced to generate a value in the output, even if no value is detected in the text. | |
| **Object Definitions** | Enter parameters or map the way in which the objects should be returned.  | **Object Name** | Enter a name for the object. Adhere to the following rules:1. The first character must be either a letter or an underscore.2. Do not include any commas or spaces.3. Do not use any special symbols, other than an underscore. | | --- | --- | | **Description** | Enter a short description of the object.For example, if would like OpenAI to search for coordinates in the text, you can enter `Latitude and Longitude of the location`. | | **Properties** | Enter object property details.  | **Parameter Name** | Enter a name for the object parameter. Adhere to the following rules:1. The first character must be either a letter or an underscore.2. Do not include any commas or spaces.3. Do not use any special symbols, other than an underscore. | | --- | --- | | **Description** | Enter a short description of the object parameter.For example, if would like OpenAI to search for coordinates in the text, you can enter `Latitude and Longitude of the location`. | | **Data Type** | Select or map the data type format in which the object parameter is returned.If there will be multiple occurrences of similar data types, select an **Array** option. For example, if there are coordinates of multiple locations to be returned, select **Array (text)** . | | **Is Parameter Required?** | When selecting `yes`, OpenAI will be forced to generate a value in the output, even if no value is detected in the text. | | |

[### Generate an Audio](#idp1189232_body)Generates an audio file based on the text input and settings specified.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Input** | Enter text to generate into audio.The text must be between 1 and 4096 characters long. |
| **Model** | Select or map the model you want to use.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **Voice** | Select or map the voice to use in the audio. For voice samples, see the [OpenAI Voice Options guide](https://platform.openai.com/docs/guides/text-to-speech/voice-options). |
| **Output Filename** | Enter a name for the generated audio file. Do not include the file extension. |
| **Response Format** | Select or map the file format for the generated audio file. |
| **Speed** | Enter a value for the speed of the audio.This must be a number between 0.25 and 4. |

[### Message an Assistant](#idp1189233_body)Sends a message to the selected assistant and gets a response. Optionally, saves the message to the specified thread (conversation).



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **Message** | Enter the message to send to the Assistant. |
| **Assistant** | Select or map the assistant you would like to use. |
| **Thread ID** | Enter the Thread ID where the message will be stored.To find your Thread ID, go to the OpenAI Playground, open your assistant, and the Thread ID will be visible.If **Thread ID** is left empty, we will create a new thread. You can find the new thread's Thread ID value in the module's response. |
| **Model** | Select or map the model you want to use.NoteEnsure you have access to the model you want to work with. Only models available for the account are listed for selection. |
| **File IDs** | Select or map a File ID to be used in the message. To select a file, you must first upload the files to OpenAI. This is useful in cases where there are tools like `retrieval` and `code_interpreter` that can access and use files enabled in the assistant or in the **Tools** parameter.You can use the **OpenAI: Upload a File** module to upload files. |
| **Tools** | Specify tools in order to override the tools the assistant can use when generating the response. |
| **Instructions** | Enter instructions in order to override the default system message of the assistant when generating the response. |

[### Upload a File](#idp1189234_body)Uploads a file that will be available for further usage across the OpenAI platform.



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **File Name** | Enter the name of the file to be uploaded, including the file extension. For example, `myFile.png`.Supported file types depend on the option selected in the **Purpose** field below. The **Fine Tune** purpose supports only .jsonl files.See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) to learn more about the supported file types. |
| **File Data** | Enter the file data to be uploaded. You can retrieve file data using the **HTTP: Get a file** module. |
| **Purpose** | Select or map the purpose. Select **Assistants** for [Assistants](https://platform.openai.com/docs/api-reference/assistants) and [Messages](https://platform.openai.com/docs/api-reference/messages) and **Fine Tune** for [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning). |

[### Make an API Call](#make-an-api-call-1760423_body)Performs an arbitrary authorized API call.

### Note

For the list of available endpoints, see [OpenAI ChatGPT API Documentation](https://platform.openai.com/docs/api-reference/introduction).



| **Connection** | [Establish a connection to your OpenAI account.](urn:resource:component:2261129/section-idm4588983532288033045131432393) |
| --- | --- |
| **URL** | Enter a path relative to `https://api.openai.com`. For example, `/v1/models`. |
| **Method** | **GET**to retrieve information for an entry.**POST**to create a new entry.**PUT**to update/replace an existing entry.**PATCH**to make a partial entry update.**DELETE**to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

#### Examples of Use - List Models

The following API call returns all pages from your OpenAI account.

**URL:**`/v1/models`

**Method:** `GET`

![openai-5.png](./../image/uuid-1ea05b35-4f5c-635a-7668-00b5d03ba463.png)The search matches can be found in the module's Output under **Bundle > Body > data**. 

In our example, 69 models were returned:

![openai-4.png](./../image/uuid-d167c437-1865-6946-247a-60ef03c00770.png)