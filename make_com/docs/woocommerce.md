WooCommerce
===========

WooCommerce modules in Make, you can monitor, create, retrieve, update, delete, and search coupons, customers, orders, order notes, products, and product attributes, terms, categories, and variations.

To get started with WooCommerce, you must have a WooCommerce account and a WooCommerce WordPress plugin installed.

Refer to the [WooCommerce API documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/#introduction) for a list of available endpoints.

Connect WooCommerce to Make
---------------------------

To connect your WooCommerce account to Make,you must generate the **Consumer Key** and **Consumer Secret** in your WooCommerce account.

1. Log in to your WordPress dashboard.
2. In the left sidebar, click **WooCommerce** > **Settings**.
3. Click on the **Advanced** tab.
4. Go to Legacy API, check the **Enable the Legacy REST API** checkbox, and click **Save changes**.
5. Continue to the REST API section and click the **Add Key** button.
6. Enter the description of your connection and select the **Read/Write** option from the permissions drop-down menu.
7. Click on the **Generate API Key** button.
8. When the page refreshes, copy the **Consumer Key** and **Consumer Secret** and store them in a safe place.
9. Log in to your Make account, add a WooCommerce module to your scenario, and click **Create a connection**.

Note: If you add a module with an `instant` tag, click **Create a webhook**, then **Create a connection**.
10. In the **Consumer Key** and **Consumer Secret** fields, enter the credentials you copied in Step 8.
11. In the **Eshop URL** field, enter the URL of your Eshop, including HTTPS. For example, `https://my-eshop.com`.
12. Click **Save**.

### Note

SSL must be enabled on your WordPress site.

### Note

Use [pretty permalinks](https://premium.wpmudev.org/blog/wordpress-permalinks/). Change the permalinks settings under *Settings* > *Permalinks*.

You have successfully established the connection. You can now edit your scenario and add more WooCommerce modules. If your connection requires reauthorization at any point, follow the connection renewal steps [here](./../connections/connecting-to-services.html "Connecting an application").

Triggers
--------

(Reference: [https://woocommerce.github.io/woocommerce-rest-api-docs/](https://woocommerce.github.io/woocommerce-rest-api-docs/#introduction))

[### New event](#new-event-968697_body)Triggers when a coupon, customer, order, or product is created, updated, or deleted.



| **Webhook name** | Enter a name for the webhook. E.g. *Order Created Webhook*. |
| --- | --- |
| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| **Topic** | Select the action that triggers the module. |

[### Watch Coupons](#watch-coupons_body)Triggers when a new coupon is created.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Limit** | Set the maximum number of coupons Make will return during one cycle. |

[### Watch Customers](#watch-customers-968697_body)Triggers when a new customer is created.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Role** | Select the specific role of the user you want to retrieve. |
| **I want to watch** | Select whether to retrieve only new users or new **and** updated users. |
| **Limit** | Set the maximum number of users Make will return during one cycle. |

[### Watch Orders](#watch-orders-968697_body)Triggers when a new order is created.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Limit** | Set the maximum number of orders Make will return during one cycle. |

[### Watch Products](#watch-products-968697_body)Triggers when a new product is created.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Limit** | Set the maximum number of products Make will return during one cycle. |

Action
------

[### Create a Coupon](#create-a-coupon-968697_body)Creates a new coupon.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make"). |
| --- | --- |
| **Code** | Enter a coupon code. |
| **Amount** | Enter the amount of discount. Should always be numeric, even if setting a percentage. |
| **Discount type** | Select a type of applied discount. |
| **Description** | Enter a description for the coupon. |
| **Date expires** | Enter the date when the coupon expires. List of supported date formats. |
| **Individual use** | If enabled, the coupon can only be used individually. Other applied coupons will be removed from the cart. |
| **Product IDs** | Enter product IDs the coupon can be used on. |
| **Excluded product IDs** | Enter product IDs the coupon cannot be used on. |
| **Usage limit** | Define how many times the coupon can be used (in total). |
| **Usage limit per user** | Define how many times the coupon can be used (per customer). |
| **Limit usage to X items** | Set a maximum number of items in the cart the coupon can be applied to. |
| **Free shipping** | If this option is enabled and if the free shipping method requires a coupon, this coupon will enable free shipping. |
| **Product categories** | Select (or map) product categories (IDs) the coupon applies to. |
| **Excluded product categories** | Select (or map) product categories (IDs) the coupon does **not** apply to. |
| **Exclude sale items** | If this option is enabled the coupon will not be applied to items that have sale prices. |
| **Minimum amount** | Enter the minimum order amount that needs to be in the cart before the coupon applies. |
| **Maximum amount** | Enter the maximum order amount allowed when using the coupon. |
| **Email restrictions** | Enter email addresses that can use this coupon. |
| **Meta data** | Enter the key-value metadata for the coupon. |

[### Create a Customer](#create-a-customer-968697_body)Creates a new customer.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make"). |
| --- | --- |
| **Username** | Set the customer login name. |
| **Password** | Set the customer password |
| **First name** | Enter the customer's first name. |
| **Last name** | Enter the customer's last name. |
| **Billing address** | Enter the billing address properties. |
| **Shipping address** | Enter the shipping address properties. |
| **Meta data** | Enter the key-value metadata for the coupon. |

[### Create an Order](#create-an-order-968697_body)Creates a new order.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Parent Order ID** | Enter the parent order ID. |
| **Status** | Set the order status. |
| **Currency** | Select the currency for the order. |
| **Customer ID** | Enter the ID of the customer who created the order. `0` = guest. |
| **Customer Note** | The note that is left by a customer during checkout. |
| **Billing address** | Enter the billing address properties. For the *Country* field, please use [ISO 3166-1 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). |
| **Shipping address** | Enter the shipping address properties. For the *Country* field, please use [ISO 3166-1 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). |
| **Payment Method** | Select one of the payment methods. |
| **Transaction ID** | Enter the unique transaction ID. |
| **Line items** | Add desired line items. For more details refer to the WooCommerce API documentation. |
| **Shipping Lines** | Enter shipping line properties. For more details refer to the WooCommerce API documentation. |
| **Fee Lines** | Add fee lines if needed. For more details refer to the WooCommerce API documentation. |
| **Coupon Lines** | Enter coupon codes and discount totals. |
| **Set paid** | If the option *Yes* is selected, the order is set as paid. It will set the status to *processing* and reduce stock items. The default value is set to *No*. |
| **Meta data** | Enter the key-value metadata for the order. |

[### Create an Order Note](#create-an-order-note_body)Adds a note to the order.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make"). |
| --- | --- |
| **Order ID** | Enter (map) the ID of the order you want to add a note to. |
| **Note** | Enter the content of the note. |
| **Note will be shown to customers** | If this option is enabled, the note will be for customers (with notification). If disabled, the note will be set as private – only for your reference. |

[### Create a Product](#create-a-product-968697_body)For more details about WooCommerce products refer to [Adding and Managing Products](https://docs.woocommerce.com/document/managing-products/) on the WooCommerce documentation site.

Adds a new product.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make"). |
| --- | --- |
| **Name** | Enter a product name. |
| **Slug** | Set the product slug for the URL. |
| **Type** | Select a product type. Options: *simple, grouped, external* and *variable*. Default is *simple*. |
| **Status** | Set the product status by selecting from the drop-down menu. |
| **Featured** | Select the *Yes* option to set the product as featured. |
| **Catalog visibility** | Select where the created product will be visible. |
| **Description** | Enter the product description. |
| **Short description** | Enter the short description of the product. |
| **SKU** | Enter the stock-keeping unit. |
| **Regular price** | Enter the regular price of the product. |
| **Sale price** | Enter the sale price of the product. |
| **Date on sale from** | The start date of the sale price, in the site's timezone. [The list of supported date formats](./../mapping/date-examples.html "Examples of date format:"). |
| **Date on sale to** | The end date of the sale price, in the site's timezone. [The list of supported date formats.](./../mapping/date-examples.html "Examples of date format:") |
| **Virtual** | Select the *Yes* option if the product is virtual. |
| **Downloadable** | Select the *Yes* option if the product is downloadable. |
| **Downloads** | Add files to be downloaded.File nameName of the file that is shown to a customer.File URLEnter the URL or absolute path to the file which customers will get access to. URLs should be already encoded. |
| **Download limit** | Enter the number of times downloadable files can be downloaded after purchase. |
| **Download expiry** | Enter the number of days until access to downloadable files expires. |
| **External URL** | Product external URL. Only for external products. |
| **Button text** | Button text for the external product. Only for external products. |
| **Tax status** | Select whether the taxable status of the product is `taxable`, `shipping` or `none`. |
| **Tax class** | Select to tax class of the product. |
| **Stock management at product level** | Select whether you want to manage the stock or not. |
| **Stock quantity** | Enter the stock quantity (*Stock management at product level* option must be enabled). |
| **In stock** | Select *Yes* to list the product as `in stock`, or *No* to list the product as `out of stock` on the frontend. |
| **Backorders** | If managing stock, this controls if backorders are allowed. |
| **Sold individually** | Select the *Yes* option to allow one item to be bought in a single order. |
| **Weight** | Enter the product weight. |
| **Dimensions** | Enter the product length, width, and height. |
| **Shipping class** | Select the shipping class of the product. |
| **Reviews allowed** | Select *Yes* to allow product reviews. |
| **Up-sell IDs** | Enter the IDs of the recommended (up-sells) products. |
| **Cross-sell IDs** | Enter the IDs of the products you want to promote in the cart. |
| **Product parent IDs** | Enter the product parent ID. |
| **Purchase note** | Optional note to send the customer after purchase. |
| **Categories** | Select product categories. |
| **Tags** | Add tag(s) to the product. |
| **Images** | Add images of the product. |
| **Menu order** | Enter the custom ordering position. |
| **Attributes** | Use this to add product attributes (e.g. color, size, etc.). |
| **Metadata** | Enter the key-value metadata for the product |

[### Create Products (batch)](#create-products--batch-_body)Allows you to create multiple products.



| **Products** | Add one or more products.Find fields description in the [Create a product section](woocommerce.html#create-a-product-968697 "Create a Product") above. |
| --- | --- |

[### Create a Product Variation](#create-a-product-variation_body)Creates a variation of the specified product.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter (map) the ID of the product that you want to create a variation for. |

Please find the field descriptions in the [Create a product section](woocommerce.html#create-a-product-968697 "Create a Product") above.

[### Delete a coupon](#delete-a-coupon-968697_body)Deletes a specified coupon.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make"). |
| --- | --- |
| **Coupon ID** | Enter (map) the ID of the coupon you want to delete. |

[### Delete a Customer](#delete-a-customer-968697_body)Deletes a specified customer.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Customer ID** | Enter (map) the ID of the customer you want to delete. |

[### Delete an Order](#delete-an-order-968697_body)Deletes a specified order.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Order ID** | Enter (map) the ID of the order you want to delete. |

[### Delete an Order Note](#delete-an-order-note_body)Deletes a specified order.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Order ID** | Enter (map) the ID of the order that contains a note you want to delete. |
| **Note ID** | Enter (map) the ID of the note you want to delete. |

[### Delete a Product](#delete-a-product-968697_body)Deletes a specified product.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter (map) the ID of the product you want to delete. |

[### Delete Products (batch)](#delete-products--batch-_body)Deletes multiple products.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product IDs** | Add (map) IDs of the products you want to delete. |

[### Delete a Product Variation](#delete-a-product-variation_body)Deletes a variation of a specified product.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter (map) the ID of the product that contains a variation you want to delete. |
| **Variation ID** | Enter (map) the ID of the variation you want to delete. |

[### Get a Coupon](#get-a-coupon-968697_body)Retrieves coupon details.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Coupon ID** | Enter (map) the ID of the coupon you want to retrieve information about. |

[### Get a Customer](#get-a-customer-968697_body)Retrieves customer details.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Customer ID** | Enter (map) the ID of the customer you want to retrieve information about. |

[### Get an Order](#get-an-order-968697_body)Retrieves specified order details.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Customer ID** | Enter (map) the ID of the order you want to retrieve information about. |

[### Get an Order Note](#get-an-order-note_body)Retrieves specified order note details.



| **Connection** | [Establish a connection to your WooCommerce account](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Order ID** | Enter (map) the ID of the order that contains a note you want to retrieve information about. |
| **Note ID** | Enter (map) the ID of the note you want to retrieve information about. |

[### Get a Product](#get-a-product-968697_body)Retrieves specified product details.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter (map) the ID of the product you want to retrieve information about. |

[### Get a Product Variation](#get-a-product-variation_body)Retrieves details of a specified product variation.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter (map) or search for the ID of the product that contains a variation you want to retrieve information about. |
| **Variation ID** | Enter (map) the ID of the variation you want to retrieve information about. |

[### Update a Coupon](#update-a-coupon-968697_body)Updates an existing coupon.



| **Coupon ID** | Enter (map) the ID of the coupon you want to modify. |
| --- | --- |

Please find the description of the module fields in the [Create a Coupon](woocommerce.html#create-a-coupon-968697 "Create a Coupon") section.

[### Update a Customer](#update-a-customer-968697_body)Updates customer details.



| **Customer ID** | Enter (map) the ID of the customer whose details you want to modify. |
| --- | --- |

Please find the description of the module fields in the [Create a Customer](woocommerce.html#create-a-customer-968697 "Create a Customer") section.

[### Update an Order](#update-an-order-968697_body)Changes the order details.



| **Order ID** | Enter (map) the ID of the order which details you want to modify. |
| --- | --- |

Please find the description of the module fields in the [Create an Order](woocommerce.html#create-an-order-968697 "Create an Order") section.

[### Update an Order Status](#update-an-order-status_body)Allows you to change the status of a specified order.



| **Order ID** | Enter (map) the ID of the order which status you want to change. |
| --- | --- |
| **Status** | Select a new status of the order.If the error 404 "*Failed to load data*" is displayed, try using the [Update an Order](woocommerce.html#update-an-order-968697 "Update an Order") module to change the order status. The Update an Order Status module is intended for users with custom order status and requires Order Status Manager plugin.  | 61d6baeeab727.png | | --- | |

[### Update a Product](#update-a-product-968697_body)Allows you to modify product details.



| **Product ID** | Enter (map) the ID of the product you want to update. |
| --- | --- |

Please find the description of the module fields in the [Create a Product](woocommerce.html#create-a-product-968697 "Create a Product") section.

Update Products (batch)

Allows you to modify details of multiple products.



| **Products** | Add the products you want to modify.Please find the description of the module fields in the [Create a Product](woocommerce.html#create-a-product-968697 "Create a Product") section. |
| --- | --- |

[### Update a Product Variation](#update-a-product-variation_body)Allows you to modify details of a product variation.



| **Product ID** | Enter (map) the ID of the product that has a variation you want to update. |
| --- | --- |
| **Variation ID** | Enter (map) the ID of the variation you want to update. |

Searches
--------

[### Search for a Customer](#search-for-a-customer_body)Performs a search among customers.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Search** | Enter the search term. |
| **Email** | Filter results by email. |
| **Role** | Filter search results by a specific user role. |
| **Number of results** | Set the maximum number of returned users. |

[### List Order Notes](#list-order-notes_body)Retrieves notes for the specified order.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Order ID** | Enter the ID of the order you want to retrieve notes from. |

[### List Product Variations](#list-product-variations_body)Retrieves variations of the specified product.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Product ID** | Enter the ID of the product that contains the variations you want to retrieve. |

[### Search for a Coupon](#search-for-a-coupon_body)Performs a search for a coupon.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Search** | Enter the search term. |
| **Email** | Filter results by the coupon code. |
| **Number of results** | Set the maximum number of returned coupons. |

[### Search for an Order](#search-for-an-order_body)Performs a search for an order.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Search** | Enter the search term. |
| **Customer ID** | Enter (map) the ID of the customer you want to filter results by. |
| **Product ID** | Enter (map) the ID of the product you want to filter results by. |
| **Status** | Select the status of the order you want to filter results by. |
| **Number of results** | Set the maximum number of returned orders. |

[### Search for a Product](#search-for-a-product_body)Performs a search for a product based on defined filter settings.



| **Connection** | [Establish a connection to your WooCommerce account.](woocommerce.html#connect-woocommerce-to-make "Connect WooCommerce to Make") |
| --- | --- |
| **Search** | Enter the search term. |
| **Slug** | Enter the product slug you want to filter results by. |
| **Category** | Select the category of the product you want to filter results by. |
| **Tag** | Select the tag of the product you want to filter results by. |
| **Status** | Select the status of the product you want to filter results by. |
| **SKU** | Enter the stock-keeping unit you want to filter results by. |
| **In stock** | Select whether you want to search for products that are in stock or not. |
| **On sale** | Select whether you want to search for products that are on sale or not. |
| **Featured product** | Select whether you want to search for products that are featured or not. |
| **Min price** | Enter the minimum price of the searched product. |
| **Max price** | Enter the maximum price of the searched product. |
| **Attribute** | Select the attribute and **Attribute term** of the product. |
| **Number of results** | Set the maximum number of returned products. |

