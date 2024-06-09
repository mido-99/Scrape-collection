Stripe
======

With Stripe modules in Make, you can manage the payment intents, customers, refunds, payouts, balance, invoices, invoice items, payment links in your Stripe account.

To use the Stripe modules, you must have a Stripe account. You can create an account at [dashboard.stripe.com/register](https://dashboard.stripe.com/register).

Refer to the [Stripe API documentation](https://docs.stripe.com/api) for a list of available endpoints.

Connect Stripe to Make
----------------------

To establish the connection, you must:

1. [Obtain your API key in Stripe](urn:resource:component:2438321/section-idm4586212815076834333296271564).
2. [Establish the connection in Make](urn:resource:component:2438321/section-idm4549301338262434333299722114)
### Obtain your API key in Stripe

To obtain your API key from your Stripe account:

1. Log in to your Stripe account.
2. In the upper right corner, click **Developers**.
3. Go to the **API keys** tab.
4. In the **Restricted keys** section, click **+ Create restricted key**.
5. Select the **Providing this key to another website** option. Click **Continue**.
6. In the **Name** field, type `Make`. In the **URL** field, type `https://make.com`. Then do one of the following:


	* Click **Create restricted key**. Proceed to the step 8.
	* Define permissions for your restricted API key. Proceed to the step 7.
7. Optional: Select **Customize permissions for this key**. Click **Continue**.


	1. Optional: In the **Key name**, insert the name for the API key.
	2. Select the access level for needed permissions.
	3. Click **Create key**.
8. Copy the **API key** value shown and store it in a safe place.
9. Click **Done**.

You will use this value in the **Key** field in Make.

### Establish the connection with Stripe in Make

To establish the connection in Make:

1. Log in to your Make account, add a Stripe module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
2. Optional: In the **Connection name** field, enter a name for the connection.
3. In the **Key** field, enter the API key copied in the section above.
4. Click **Save**.
5. If prompted, authenticate your account and confirm access.

You have successfully established the connection. You can now edit your scenario and add more Stripe modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Triggers
--------

You do not have to add the webhooks in the Stripe as it is automatically done for you once you add and save an instant trigger module to your scenario.

[### Watch Events](#watch-events-968690_body)Triggers when a given event occurs.



| **Webhook Name** | Enter a name for the webhook. |
| --- | --- |
| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| **Group** | Select the group and the events which you want to watch. |
| **Connect** | Select the checkbox if you want this endpoint should receive events from connected accounts (true), or from your account (false). |
| **Force different API Version** | Enter the version of the API to which events to be sent that this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version. |

### Note

This app uses webhooks to trigger a scenario when an event occurs instantly. All webhook modules have an `instant` tag next to their name.

When you create a Stripe webhook in Make, it is attached automatically and requires no additional set up.

Universal
---------

[### Make an API Call](#make-an-api-call-968690_body)Performs an arbitrary authorized API call.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **URL** | Enter a path relative to `https://api.stripe.com/`. For example: `/v1/charges`NoteFor the list of available endpoints, refer to the [Stripe API Documentation](https://stripe.com/docs). |
| **Method** | Select the HTTP method you want to use:* **GET:** to retrieve information for an entry. * **POST:** to create a new entry. * **PUT:** to update/replace an existing entry. * **PATCH:** to make a partial entry update. * **DELETE:** to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we already did that for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

[### Example of Use - List Events](#example-of-use---list-events-968690_body)The following API call returns all the events from your Stripe account:

**URL:**

`/v1/events`

**Method:**

`GET`

![61d6b7948948f.png](./../image/uuid-a282933b-38ca-25e6-2eb8-a4f76091d029.png)Matches of the search can be found in the module's **Output** under *Bundle > Body > data*.

In our example, 10 events were returned:

![61d6b795915b4.png](./../image/uuid-144f9059-26cd-38ac-5681-868cc1c00705.png)Payment Intents
---------------

[### List Payment Intents](#list-payment-intents_body)Retrieves a list of payment intents or filters by customer ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Enter the Customer ID whose payment intents you want to list. You can search the customer using their email address. |
| **Limit** | Set the maximum number of payment intents Make should return during one scenario execution cycle. |

[### Create a Payment Intent](#create-a-payment-intent_body)Creates a Payment Intent.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Amount** | Enter the amount to be collected by this Payment Intent. A positive integer represents how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). For example, 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency. The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits. For example, a value of 99999999 for a USD charge of $999,999.99. |
| **Currency** | Enter the three-digit currency applicable for the payment intent. |
| **Description** | Enter the details of the payment intent. |
| **Receipt Email** | Enter the email address to which the payment intent recipient should be sent. |
| **Confirm this Payment Intent immediately** | Select whether you want to confirm the payment intent immediately. |
| **Payment Method Types** | Select the payment methods for this payment intent. |
| **Customer ID** | Select the Customer ID to whom this payment intent receipt should go. |
| **Payment Method** | Select the payment method:* *Choose an existing Payment Method* * *Create a Payment Method and attach it to this Payment Intent* |
| **Line 1** | Enter the recipient's street address. |
| **Line 2** | Enter the recipient's street address. |
| **Postal Code** | Enter the recipient's area postal code. |
| **City** | Enter the recipient's city name. |
| **State** | Enter the recipient's state name. |
| **Country Code** | Enter the recipient's country code. |
| **Recipient Name** | Enter the recipient's name. |
| **Carrier** | Enter the courier service name. For example, `FedEx`. |
| **Phone** | Enter the recipient's phone number. |
| **Tracking Number** | Enter the courier tracking number. |
| **Statement Descriptor** | Enter the details of the payment intent. For non-card charges, you can use this value as the complete description that appears on your customer’s statements. A maximum of 22 characters is allowed. |
| **Statement Descriptor Suffix** | Enter the statement details that appear on the customer's statement. Concatenated with the statement descriptor prefix and statement descriptor to form the complete statement descriptor. A maximum of 22 characters is allowed. |
| **Idempotency Key** | Enter the ID that you associate with the cart or customer session in your application - when creating the Payment Intent to avoid erroneously creating duplicate Payment Intents for the same purchase. |
| **Capture Method** | Select the payment intent capture method:* *Automatic* * *Manual* |
| **Confirmation Method** | Select the payment intent confirmation method:* *Automatic* * *Manual* |
| **Use Stripe SDK** | Select whether you want to Stripe SDK for sending a confirmation about the payment intent. This is applicable only for Stripe Connect and only when using iOS or Android SDKs to handle additional authentication steps. |
| **Transfer Group** | Enter the transfer group associated with the payment intent. This field is only applicable if you are using Stripe Connect. |
| **Application Fee Amount** | Enter the application fee amount for the payment intent. This is applicable for Stripe Connect Only. For more information, see the Payment Intents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| **On Behalf Of** | Enter the Stripe Account ID to whom the payment intent belongs. This field is for Stripe Connect Only. For more information, see the Payment Intents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| **Destination** | Enter the destination account details. |
| **Amount** | Enter the amount of this payment intent to send to the destination account. |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

[### Retrieve a Payment Intent](#retrieve-a-payment-intent_body)Retrieves the details of a Payment Intent that has previously been created.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Intent ID** | Select the Payment Intent ID whose details you want to retrieve. You can find the Payment Intent ID on the Payments page. |

[### Confirm a Payment Intent](#confirm-a-payment-intent_body)Confirms a payment intent by its ID. Upon confirmation, the payment intent will attempt to initiate a payment.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Intent ID** | Select the Payment Intent ID whose details you want to retrieve. You can find the Payment Intent ID on the Payments page. |
| **Receipt Email** | Enter the email address to which the payment intent recipient should be sent to. |
| **Payment Method** | Select the payment method option to attach to this Payment Intent:* *Choose an existing payment method* * *Create a Payment Method and attach it to this Payment Intent* |
| **Payment Method ID** | Select the Payment Method ID to attach to the payment intent. |
| **Setup Future Usage** | Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the Payment Intent’s Customer if present, after the Payment Intent, is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes. |
| **Type** | Select the payment method. For example, `Alipay`. |
| **Line 1** | Enter the recipient's billing street address. |
| **Line 2** | Enter the recipient's billing street address. |
| **Postal Code** | Enter the recipient's area postal code. |
| **City** | Enter the recipient's city name. |
| **State** | Enter the recipient's state name. |
| **Country Code** | Enter the recipient's country code. |
| **Email** | Enter the billing address contact's email address. |
| **Name** | Enter the billing address contact's name. |
| **Phone** | Enter the billing address's phone number. |
| **Metadata** | Add a set of Key-Pair values for the payment intent. |
| **Line 1** | Enter the recipient's shipping street address. |
| **Line 2** | Enter the recipient's street address. |
| **Postal Code** | Enter the recipient's area postal code. |
| **City** | Enter the recipient's city name. |
| **State** | Enter the recipient's state name. |
| **Country Code** | Enter the recipient's country code. |
| **Recipient Name** | Enter the recipient's name. |
| **Carrier** | Enter the courier service name. For example, `FedEx`. |
| **Phone** | Enter the recipient's phone number. |
| **Tracking Number** | Enter the courier tracking number. |
| **Payment Method Types** | Select the payment methods for this payment intent. For example, card, `SOFORT`. |
| **Preferred Languages** | Select the preferred language for the Bancontact payment method. |
| **Enabled** | Select whether the payment installation configuration is enabled for this payment intent. This applies only to Mexico Only. For more information, see the [installments integration guide](https://stripe.com/docs/payments/installments). |
| **Network** | Select the payment network. For example, `American Express`. |
| **Request 3D Secure** | Select the option for 3D secure payment:* *Automatics* * *Any* Stripe strongly recommends that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your fraud engine, provide this option. Read the guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and the SCA Engine. |
| **Preferred Language** | Select the preferred language for the SOFORT payment method. |
| **Off Session** | Select whether the customer is not in your checkout flow during this payment attempt, and therefore is unable to authenticate. This parameter is intended for scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). |
| **Error On Requires Act-On** | Select whether to fail the payment attempt if the Payment Intent transitions into required action. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). |
| **Mandate** | Select an option to mandate the payment intent:* *Input an Existing Mandate ID* * *Create a Mandate* |
| **Mandate ID** | Enter the Mandate ID to be used for this payment only. The ID is your account's secret key. |
| **Type** | Select the mandated type:* *Offline* * *Online* |
| **IP Address** | Enter the IP address from which the Mandate was accepted by the customer. |
| **User Agent** | Enter the user agent of the browser from which the Mandate was accepted by the customer. |
| **Accepted At** | Enter the time at which the customer has accepted the mandate. |
| **Return URL** | Enter the URL address to redirect the customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. |

[### Capture a Payment Intent](#capture-a-payment-intent_body)Captures an existing uncaptured payment intent by its ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Intent ID** | Enter the Payment Intent ID you want to capture. You can search for the payment Intent ID using Customer ID. |
| **Amount to Capture** | Enter the amount to capture from the Payment Intent. The amount must be less than or equal to the original amount. Any additional amount will be automatically refunded. Defaults to the full `amount_capturable` if not provided. |
| **Statement Descriptor** | Enter the details of the payment intent that appears on the card statement. For non-card charges, you can use this value as the complete description that appears on your customer’s statements. The description must be at most 22 characters long. |
| **Statement Descriptor Suffix** | Enter the details of the payment intent that appears on the card statement. For non-card charges, you can use this value as the complete description that appears on your customer’s statements. Must be at most 22 characters long. |
| **Application Fee Amount** | Enter the amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner’s Stripe account. The amount of the application fee collected will be capped at the total payment amount. This is applicable to Stripe Connect only. For more information, see the Payment Intents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts). |
| **Amount** | The amount that will be transferred automatically when a charge succeeds. The amount is capped at the total transaction amount and if no amount is set, the full amount is transferred. |

[### Update a Payment Intent](#update-a-payment-intent_body)Updates the specified payment intent by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Intent ID** | Select the Payment Intent ID whose details you want to retrieve. You can find the Payment Intent ID on the Payments page. |
| **Amount** | Enter the amount to charge in the smallest currency unit. For example, 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency. The minimum amount is $0.50 US or equivalent in charge currency.The amount must be lower than or equal to 99999999. |
| **Receipt Email** | Enter the email address to which the payment intent recipient should be sent to. |
| **Payment Method** | Select the payment method option to attach to this Payment Intent:* *Choose an existing payment method* * *Create a Payment Method and attach it to this Payment Intent* |
| **Payment Method ID** | Select the Payment Method ID to attach to the payment intent. |
| **Setup Future Usage** | Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the Payment Intent’s Customer if present, after the Payment Intent, is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes. |
| **Type** | Select the payment method. For example, `Alipay`. |
| **Line 1** | Enter the recipient's billing street address |
| **Line 2** | Enter the recipient's billing street address. |
| **Postal Code** | Enter the recipient's area postal code. |
| **City** | Enter the recipient's city name. |
| **State** | Enter the recipient's state name. |
| **Country Code** | Enter the recipient's country code. |
| **Email** | Enter the billing address contact's email address. |
| **Name** | Enter the billing address contact's name. |
| **Phone** | Enter the billing address phone number. |
| **Metadata** | Add a set of Key-Pair values for the payment intent. |
| **Line 1** | Enter the recipient's shipping street address. |
| **Line 2** | Enter the recipient's street address. |
| **Postal Code** | Enter the recipient's area postal code. |
| **City** | Enter the recipient's city name. |
| **State** | Enter the recipient's state name. |
| **Country Code** | Enter the recipient's country code. |
| **Recipient Name** | Enter the recipient's name. |
| **Carrier** | Enter the courier service name. For example, `FedEx`. |
| **Phone** | Enter the recipient's phone number. |
| **Tracking Number** | Enter the courier tracking number. |
| **Payment Method Types** | Select the payment methods for this payment intent. For example, `card`, `SOFORT`. |
| **Preferred Languages** | Select the preferred language for the Bancontact payment method. |
| **Enabled** | Select whether the payment installation configuration is enabled for this payment intent. This applies only to Mexico Only. For more information, see the [installments integration guide](https://stripe.com/docs/payments/installments). |
| **Network** | Select the payment network. For example, American Express. |
| **Request 3D Secure** | Select the option for 3D secure payment:* *Automatics* * *Any* Stripe strongly recommends that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your fraud engine, provide this option. Read the guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and the SCA Engine. |
| **Preferred Language** | Select the preferred language for the SOFORT payment method. |
| **Off Session** | Select whether the customer is not in your checkout flow during this payment attempt, and therefore is unable to authenticate. This parameter is intended for scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). |
| **Error On Requires Act-On** | Select whether to fail the payment attempt if the Payment Intent transitions into required action. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). |
| **Mandate** | Select an option to mandate the payment intent:* *Input an Existing Mandate ID* * *Create a Mandate* |
| **Mandate ID** | Enter the Mandate ID to be used for this payment only. The ID is your account's secret key. |
| **Type** | Select the mandated type:* *Offline* * *Online* |
| **IP Address** | Enter the IP address from which the Mandate was accepted by the customer. |
| **User Agent** | Enter the user agent of the browser from which the mandate was accepted by the customer. |
| **Accepted At** | Enter the time at which the customer has accepted the mandate. |
| **Return URL** | Enter the URL address to redirect the customer back to after they authenticate or cancel their payment on the payment method’s app or site. If you prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. |

[### Cancel a Payment Intent](#cancel-a-payment-intent_body)Cancels a payment intent by its ID. For Payment.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Intent** | Enter the Payment Intent ID you want to delete. You can search for the payment Intent ID using the Customer ID through their email address. |

Customers
---------

[### Search Customers](#search-customers-968690_body)Retrieves a list of customers filtered by criteria.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Email** | Enter the customer's email address. |
| **Filter** | Select the filters to search the customer based on the selected option. For example, `created date`. |
| **Limit** | Set the maximum number of customers Make should return during one scenario execution cycle. |

[### List All Customers](#list-all-customers_body)Retrieves a list of customers.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Email** | Enter the email address to list the customers with the specified email. |
| **Created At** | Select the filters to search the customer based on the selected option. For example, `before`. |
| **Timestamp** | Enter the date and time to list the customer created on, before, or after the specified time. |
| **Limit** | Set the maximum number of customers Make should return during one scenario execution cycle. |

[### Create a Customer](#create-a-customer-968690_body)Creates a new Customer object.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Description** | Enter the details of the customer. |
| **Email** | Enter the customer's email address. |
| **Name** | Enter the customer's name. |
| **Phone** | Enter the customer's phone number |
| **Line 1** | Enter the customer's shipping street address. |
| **Line 2** | Enter the customer's shipping street address. |
| **Postal Code** | Enter the customer's area postal code. |
| **City** | Enter the customer's city name. |
| **State** | Enter the customer's state name. |
| **Country** | Enter the customer's country name. |
| **Name** | Enter the contact's name at the shipping address. |
| **Phone** | Enter the shipping address contact phone number. |
| **Payment Method ID** | Enter the customer's Payment Method ID. |
| **Metadata** | Add a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| **Balance** | Enter an integer amount in paise/cents that represent the customer’s current balance. This amount affects the customer’s future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice. |
| **Coupon ID** | Enter the customer's Coupon ID. If you provide a coupon code, the customer will have a discount applied on all recurring charges. Charges you create through the API will not have a discount. |
| **Invoice Prefix** | Enter the prefix for the customer used to generate unique invoice numbers. The prefix must be 3–12 uppercase letters or numbers. |
| **Custom Fields** | Add the custom fields and values for the customer. For example, `Permanent Address`. |
| **Default Payment Method ID** | Enter the default Payment Method ID of the customer. This is used in customers' invoices. |
| **Footer** | Enter the information that appears in the footer of the invoice. |
| **Next Invoice Sequence** | Enter the sequence to be used on the customer's next invoice. |
| **Preferred Locales** | Add the customer's preferred communication languages. |
| **Promotion Code ID** | Enter the customer's Promotion Code ID used to avail of discounts. The customer will have a discount applied on all recurring payments. Charges created through the API will not have a discount. |
| **Source ID** | Enter the Source ID from where the customer is registering with. When using payment sources created via the Token or Sources APIs, the passing source will create a new source object, make it the new customer default source, and delete the old customer default if one exists. |
| **Tax Exempt** | Select the tax exemption option applicable to the customer:* *None* * *Exempt* * *Reverse* |
| **TAX ID Data** | Add the customer's Tax ID data:**Type**Select the tax type. For example, EU-VAT.**Tax ID**Enter the customer's Tax ID. |

[### Retrieve a Customer](#retrieve-a-customer_body)Retrieves the details of an existing customer.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Select the Customer ID whose details you want to retrieve. |

[### Update a Customer](#update-a-customer-968690_body)Updates a specified customer by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Select the Customer ID whose details you want to update. |

See the [Create a Customer](stripe.html#create-a-customer-968690 "Create a Customer") for field descriptions.

[### Delete a Customer](#delete-a-customer-968690_body)Permanently deletes a customer. It cannot be undone.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Select the Customer ID you want to delete. |

Refunds
-------

[### List All Refunds](#list-all-refunds_body)Returns a list of all refunds you've previously created.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Charge** | Select the charge whose refunds you want to list. |
| **Limit** | Set the maximum number of refunds Make should return during one scenario execution cycle. |

[### Create a Refund](#create-a-refund-968690_body)Creates a new refund.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Charge** | Select the charge for which you want to create a refund. |
| **Amount** | Enter the amount to be refunded. A positive integer in the [smallest currency unit](https://support.stripe.com/questions/which-zero-decimal-currencies-does-stripe-support). For example, 100 cents to charge $1.00 or 100 to charge ¥100, a 0-decimal currency representing the amount to refund. You can only refund up to the unrefunded amount remaining of the charge. |
| **Reason** | Select the reason for the refund. For example, duplicate. |
| **Refund Applicable Fee** | Select whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. |
| **Reverse Transfer** | Select whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge. |
| **Metadata** | Enter a set of key-value pairs that you can attach to a `Refund` object. This can be useful for storing additional information about the refund in a structured format. You can unset individual keys if you POST an empty value for that key. You can clear all keys if you POST an empty value for `metadata`. |

[### Retrieve a Refund](#retrieve-a-refund_body)Retrieves the details of an existing



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Refund** | Enter the refund identifier whose details you want to retrieve. |

[### Update a Refund](#update-a-refund_body)Updates the specified payout by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Refund** | Select the charge for which you want to create a refund. |
| **Metadata** | Enter a set of key-value pairs that you can attach to a `Refund` object. This can be useful for storing additional information about the refund in a structured format. You can unset individual keys if you POST an empty value for that key. You can clear all keys if you POST an empty value for `metadata` |

Payouts
-------

[### List All Payouts](#list-all-payouts_body)Returns a list of existing payouts sent to third-party bank accounts or that Stripe has sent you.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Destination** | The ID of an external account - only return payouts sent to this external account. |
| **Limit** | Set the maximum number of payouts Make should return during one scenario execution cycle.Enter a number between 1 and 1000. |
| **Created At** | Select the filters to search the payouts based on the selected option. For example, `before`. |
| **Timestamp** | Enter the date and time to list the payouts created on, before, or after the specified time. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Arrival Date** | Select the filters to search the payouts based on the selected option. For example, `before`. |
| **Timestamp** | Enter the date and time to list the payouts created on, before, or after the specified time. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Status** | Select the status of the payout you want to list:* *Pending* * *Paid* * *Failed* * *Canceled* |

[### Create a Payout](#create-a-payout_body)To send funds to your own bank account. you create a new payout object.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Amount** | Enter the payout amount. Enter a positive integer in the [smallest currency unit](https://support.stripe.com/questions/which-zero-decimal-currencies-does-stripe-support). For example, 100 cents to charge $1.00 or 100 to charge ¥100, a 0-decimal currency representing how much to payout. |
| **Currency** | Enter the three-character currency applicable for the payout. For example, `USD`. |
| **Description** | Enter the details of the payout. |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| **Method** | The method used to send this payout:* *Standard* * *Instant* The instant is only supported for payouts to debit cards.For more information, see [Instant payouts for marketplaces](https://stripe.com/blog/instant-payouts-for-marketplaces). |
| **Source Type** | Select the source for payout. For example, `Bank account`, `card`, `Alipay account`. |
| **Statement Descriptor** | Enter the information that appears on the customer's statement. |

[### Cancel a Payout](#cancel-a-payout_body)Cancels a previously created payout.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payout** | Enter the payout identifier you want to cancel. |

[### Retrieve a Payout](#retrieve-a-payout_body)Retrieves the details of an existing payout.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payout** | Enter the payout identifier whose details you want to retrieve. |

[### Update a Payout](#update-a-payout_body)Updates the specified payout by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payout** | Enter the payout identifier you want to update. |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Balance
-------

[### Retrieve Balance](#retrieve-balance_body)Retrieves the current account balance.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |

[### List All Balance History](#list-all-balance-history_body)Returns a list of transactions that have contributed to the Stripe account balance.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Limit** | Set the maximum number of balance histories Make should return during one scenario execution cycle. |
| **Currency** | Enter the three-character currency code to list the balance history for the selected currency. |
| **Payout** | Enter the Payout ID whose balance history you want to list. For automatic Stripe payouts only, it returns transactions that were paid out on the specified payout ID. |
| **Type** | Select the option whose balance history you want to list. For example, `charge`. |
| **Created At** | Select the filters to list the balance history based on the selected option. For example, `before`. |
| **Created Timestamp** | Enter the date and time to list the balance history created on, before, or after the specified time. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Available** | Select the filters to list the balance history based on the selected option. For example, `before`. |
| **Available Timestamp** | Enter the date and time to list the balance history available on, before, or after the specified time. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |

[### Retrieve a Balance Transaction](#retrieve-a-balance-transaction_body)Retrieves the balance transaction with the given ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **ID** | Enter the identifier of the balance transaction to be retrieved. Usually starts with `txn_`. |

Invoices
--------

[### Search Invoices](#search-invoices-968690_body)Retrieves a list of invoices filtered by criteria.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **List By** | Select the option to list the invoices:* *Customer* * *Invoice* |
| **Customer ID** | Enter the Customer ID whose invoices you want to list. |
| **Invoice ID** | Enter the Invoice ID whose details you want to list. |
| **Pending** | Select whether to list only the pending invoices. |
| **Filter** | Select the filters to list the invoices based on the selected option. For example, `created date`. |
| **Limit** | Set the maximum number of invoices Make should return during one scenario execution cycle. |

[### List All Invoice Line Items](#list-all-invoice-line-items_body)Retrieves a list of invoice line items by the invoice ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Enter the Invoice ID whose line items you want to list. |
| **Limit** | Set the maximum number of invoices Make should return during one scenario execution cycle. |

[### Create an Invoice](#create-an-invoice-968690_body)Creates a new invoice by the customer ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Select the Customer ID for whom invoice you want to create the invoice. |
| **Auto Advance** | Select whether you want Stripe to perform an [automatic collection](https://stripe.com/docs/invoicing/overview#auto_advance) of the invoice. When left unselected, the invoice’s state will not automatically advance without explicit action. |
| **Collection Method** | Select the option for invoice collection method:* *Charge Automatically* * *Send Invoice* |
| **Days Until Due** | Enter the number of days from when the invoice is created until it is due. Applicable only when the collection method is selected as Send Invoices. |
| **Due Date** | Enter the date on which the payment for the invoice is due. Applicable only when collection method is Send Invoices. |
| **Description** | Enter the invoice details. |
| **Subscription ID** | Enter the Subscription ID of the invoice. If left blank, the created invoice will include all pending invoice items for the customer. If set, the created invoice will only include pending invoice items for that subscription and pending invoice items not associated with any subscription. The subscription’s billing cycle and regular subscription events won’t be affected. |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| **Application Fee Amount** | Enter the application fee in cents that will be applied to the invoice and transferred to the application owner’s Stripe account. The request must be made with an OAuth key or the Stripe-Account header to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/invoicing/connect#collecting-fees). |
| **Custom Fields** | Add the custom fields for the invoice:* **Field Name:** Enter the name of the custom field. You can enter a maximum of 30 characters. * **Value:** Enter the value of the custom field. You can enter a maximum of 30 characters. |
| **Default Payment Method ID** | Enter the default payment method ID for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings. |
| **Default Tax Rates ID** | Enter the Default Tax Rate ID. |
| **Discounts** | Add the discounts applicable for the invoice: **Coupon ID** Select the Coupon ID applicable for the invoice. **Discount ID** Enter an existing discount ID on the object (or one of its ancestors) to reuse. |
| **Footer** | Enter the text that appears at the footer of the invoice. |
| **Statement Descriptor** | Enter the text that appears in the customer's invoice statement. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item’s product’s `statement_descriptor`. |
| **Destination** | Enter the account to which the invoice amount to be transferred. |
| **Amount** | Enter the amount to be transferred. |

[### Retrieve an Invoice](#retrieve-an-invoice_body)Retrieves the details of an existing invoice with the given ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Select the Invoice ID whose details you want to retrieve. |

[### Update an Invoice](#update-an-invoice-968690_body)Updates the specified invoice by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Select the Invoice ID whose details you want to update. You can search the invoices by Customer ID, Subscription ID, Status, and Collection Method |
| **Auto Advance** | Select whether you want Stripe to perform an [automatic collection](https://stripe.com/docs/invoicing/overview#auto_advance) of the invoice. When left unselected, the invoice’s state will not automatically advance without explicit action. |
| **Collection Method** | Select the option for invoice collection method:* *Charge Automatically* * *Send Invoice* |
| **Days Until Due** | Enter the number of days from when the invoice is created until it is due. Applicable only when the collection method is selected as Send Invoices. |
| **Due Date** | Enter the date on which the payment for the invoice is due. Applicable only when collection method is Send Invoices. |
| **Description** | Enter the invoice details. |
| **Subscription ID** | Enter the Subscription ID of the invoice. If left blank, the created invoice will include all pending invoice items for the customer. If set, the created invoice will only include pending invoice items for that subscription and pending invoice items not associated with any subscription. The subscription’s billing cycle and regular subscription events won’t be affected. |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| **Application Fee Amount** | Enter the application fee in cents that will be applied to the invoice and transferred to the application owner’s Stripe account. The request must be made with an OAuth key or the Stripe-Account header to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/invoicing/connect#collecting-fees). |
| **Custom Fields** | Add the custom fields for the invoice:* **Field Name:** Enter the name of the custom field. You can enter a maximum of 30 characters. * **Value:** Enter the value of the custom field. You can enter a maximum of 30 characters. |
| **Default Payment Method ID** | Enter the default payment method ID for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription’s default payment method, if any, or to the default payment method in the customer’s invoice settings. |
| **Default Tax Rates ID** | Enter the Default Tax Rate ID. |
| **Discounts** | Add the discounts applicable for the invoice: **Coupon ID** Select the Coupon ID applicable to the invoice. **Discount ID** Enter an existing discount ID on the object (or one of its ancestors) to reuse. |
| **Footer** | Enter the text that appears at the footer of the invoice. |
| **Statement Descriptor** | Enter the text that appears in the customer's invoice statement. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item’s product’s `statement_descriptor`. |
| **Destination** | Enter the account to which the invoice amount is to be transferred. |
| **Amount** | Enter the amount to be transferred. |

[### Finalize a Draft Invoice](#finalize-a-draft-invoice_body)Finalizes a draft invoice by its ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Select the draft Invoice ID you want to finalize. |

[### Void an Invoice](#void-an-invoice-968690_body)Voids a finalized invoice with the given ID. This cannot be undone.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Select the Invoice ID you want to void. |

[### Delete a Draft Invoice](#delete-a-draft-invoice_body)Permanently deletes a drat invoice. Use the *Void an Invoice* module for a finalized invoice.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice ID** | Select the draft Invoice ID you want to delete. |

Invoice Items
-------------

[### Search Invoice Items](#search-invoice-items_body)Retrieves a list of invoice items filtered by criteria.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **List By** | Select the option to list the invoice items:* *Customer* * *Invoice* |
| **Customer ID** | Enter the Customer ID whose invoice items you want to list. |
| **Invoice ID** | Enter the Invoice ID whose invoice items you want to list. |
| **Pending** | Select whether to list only the pending invoice items. |
| **Filter** | Select the filters to list the invoice items based on the selected option. For example, `created date`. |
| **Limit** | Set the maximum number of invoice items Make should return during one scenario execution cycle. |

[### Create an Invoice Item](#create-an-invoice-item_body)Creates a new invoice item to be added to a draft invoice.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Customer ID** | Enter the Customer ID whose invoice item you want to create. |
| **Input an Amount** | Select the option to input the invoice amount:* *By a Total Amount* * *By a Unit Amount and Quantity* * *By an Existing Price Object* |
| **Amount** | Enter the invoice item amount. Enter the cents of the charge to be applied to the upcoming invoice. Passing in a negative amount will reduce the `amount_due` on the invoice. |
| **Price Object** | Select the price object option:* *Input an Existing Price ID* * *Create a New Price Object* |
| **Product ID** | Select the Product ID whose items invoice you are creating. |
| **Price ID** | Enter the Price ID of the price object. |
| **Quantity** | Enter the number of items to add to the invoice. |
| **Currency** | Enter the three-character currency code applicable to the invoice. For example, `USD`. |
| **Description** | Enter the description of the invoice to display in the invoice for easy tracking. |
| **Start** | Enter the start date of the time period for the invoice. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **End** | Enter the last of the time period for the invoice and it must be greater than or equal to the start. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| **Discountable** | Select whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations. |
| **Tax Rates ID** | Enter the tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice does not apply to this invoice item. Pass an empty string to remove previously-defined tax rates. |

[### Retrieve an Invoice Item](#retrieve-an-invoice-item_body)Retrieves the details of an existing invoice item with the given ID.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice Item ID** | Enter the Invoice Item ID whose details you want to retrieve. |

[### Update an Invoice Item](#update-an-invoice-item_body)Updates the specified invoice item by setting the values of the parameters passed.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice Item ID** | Enter the Invoice Item ID whose details you want to update. |
| **Input an Amount** | Enter an amount in paise/cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount. |
| **Description** | Enter the description of the invoice to display in the invoice for easy tracking. |
| **Start** | Enter the start date of the time period for the invoice. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **End** | Enter the last of the time period for the invoice and it must be greater than or equal to the start. See the [list of supported date and time formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Metadata** | Enter a set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| **Discountable** | Select whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations. |
| **Tax Rates ID** | Enter the tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates. |

[### Delete an Invoice Item](#delete-an-invoice-item_body)Permanently deletes an invoice item that is not attached to invoices, or if it's attached to a draft invoice.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Invoice Item ID** | Enter the Invoice Item ID you want to delete. |

[Other
-----](#other-968690_body)You can list payment link lines using the following module.

### List Payment Link Lines

Retrieves all lines of the specified payment link.



| **Connection** | [Establish a connection to your Stripe account](stripe.html#connect-stripe-to-make "Connect Stripe to Make"). |
| --- | --- |
| **Payment Link ID** | Select or map the Payment Link ID whose link lines you want to list. |
| **Limit** | Set the maximum number of payment link lines Make will return during one execution cycle. |

