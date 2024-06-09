Calendly
========

The Calendly modules enable you to monitor or retrieve events, invitees, event types, and memberships in your Calendly account.

* [See the change log between Calendly [v2] and Calendly [1]](calendly.html#changelog-964691 "Changelog")
Getting Started with Calendly
-----------------------------

Prerequisites

* A Calendly account — you can create one at [calendly.com/signup](https://calendly.com/signup).
Connecting Calendly to Make
---------------------------

1. Go to Make and open the Calendly module's *Create a connection* dialog.

![calendlyConnect.gif](./../image/uuid-51ddd378-30f2-b39f-3df7-619ccd7c1f57.gif)2. Enter a name for the connection to the *Connection name* field and click *Continue*.

After you click the *Continue* button, Make will redirect you to the Calendly website where you will be prompted to grant Make access to your account.

3. Confirm the dialog by clicking the *Connect to Calendly* button.

![61d5a9c306363.png](./../image/uuid-cead981a-8b6d-48d5-9a43-c136332c0bf4.png)The connection has been established.

Event
-----

### Watch Events

Triggers when an event is created or canceled.

1. Add the *Watch Events* module to your Make scenario.

2. Select events you want to watch.

3. Select or enter the *Organization URI* (requires) and *User URI* (optional) to filter returned data by. Click *Save*.

![61d5a9c4ad9b4.gif](./../image/uuid-37d82347-5390-ba99-f8d3-1350604cdb99.gif)You can retrieve *Organization URI* and *User URI* using the *List Organization Memberships* module:

![calendlyListSettings.png](./../image/uuid-b9de096d-8ba6-b543-0e82-1dd6f68df76d.png)![calendlyListBundle.png](./../image/uuid-48cc0026-3963-367a-fae2-a99f0582d491.png)Now, every time the specified event occurs, the Watch Events module in your Make scenario is triggered.

[### List Events](#list-events-964691_body)Retrieves events in your account by filter settings.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Organization URI** | Enter the organization URI to specify the organization to filter results by. |
| **User URI** | Enter the user URI to specify the user to filter results by. |
| **Invitee Email** | Enter the email address of the invitee to return events that are scheduled with the invitee associated with this email address. |
| **Min Start Time** | Enter the time and date to include events with start times after this time. |
| **Max Start Time** | Enter the time and date to include events with start times prior to this time. |
| **Sort** | Select the sort order of results by the specified field and direction. |
| **Status** | Filter results by the event status – whether the scheduled event is active or canceled. |
| **Limit** | Set the maximum number of events Make will return during one execution cycle. |

[### List Event Invitees](#list-event-invitees_body)Retrieves invitees of the specified event.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Event** | Select the event you want to retrieve invitees for. |
| **Email** | Enter the email address of the invitee to filter results. |
| **Sort** | Select the sort order of results by the specified field and direction. |
| **Status** | Filter results by the invitee status – whether the invitee is still active or canceled. |
| **Limit** | Set the maximum number of invitees Make will return during one execution cycle. |

[### List Event Types](#list-event-types_body)Returns all event types associated with a specified user.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **User URI** | Select the user to retrieve event types associated with the user. |
| **Sort** | Select the sort order of results by the specified field and direction. |
| **Limit** | Set the maximum number of event types Make will return during one execution cycle. |

[### Get an Event](#get-an-event-964691_body)Retrieves event details.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Event** | Select the event or map the ID of the event you want to retrieve details for. |

[### Get an Event Invitee](#get-an-event-invitee_body)Retrieves details about an Invitee (person invited to an event).



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Enter an Event Invitee** | Select whether to specify an invitee manually or select from the drop-down menu. |
| **Invitee URI** | Select the event or enter (map) the Invitee URI. |

[### Get an Event Type](#get-an-event-type_body)Retrieves event type details.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Event Type** | Select event type or enter (map) event type URI. |

Schedule
--------

[### Create a Scheduling Link](#create-a-scheduling-link_body)Creates a scheduling link.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Maximum Event Count** | Enter the maximum number of events that can be scheduled using this scheduling link. |
| **Event Type** | Select event type or enter (map) event type URI. |

Organization
------------

[### List Organization Memberships](#list-organization-memberships_body)Retrieves the organization memberships for all users belonging to an organization.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Organization URI** | Enter the organization URI to retrieve all users that belong to the organization. |
| **User URI** | Enter the user URI to look up a user's membership in an organization. |
| **Email** | Enter the email address to filter results by. |
| **Limit** | Set the maximum number of organization memberships Make will return during one execution cycle. |

[### Get an Organization Membership](#get-an-organization-membership_body)Retrieves user's organization membership details.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Organization Membership** | Select or enter the organization membership URI you want to retrieve details for. |

[### Invite a User to Organization](#invite-a-user-to-organization_body)Invites a user to an organization.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **Organization URI** | Enter (map) the organization URI where you want to add a user to. |
| **Email Address** | Enter the email address of the person you want to invite to the organization. |

[### Make an API Call](#make-an-api-call-964691_body)Allows you to perform a custom API call.



| **Connection** | [Establish a connection to your Calendly account](calendly.html#connecting-calendly-to-make "Connecting Calendly to Make"). |
| --- | --- |
| **URL** | Enter a path relative to `https://api.calendly.com`For example: `/users/me`For the list of available endpoints, refer to the [Calendly API Documentation](https://calendly.stoplight.io/docs/api-docs/YXBpOjM5NQ-calendly-api). |
| **Method** | Select the HTTP method you want to use:* **GET:** to retrieve information for an entry. * **POST:** to create a new entry. * **PUT:** to update/replace an existing entry. * **PATCH:** to make a partial entry update. * **DELETE:** to delete an entry. |
| **Headers** | Enter the desired request headers. You don't have to add authorization headers; we added those for you. |
| **Query String** | Enter the request query string. |
| **Body** | Enter the body content for your API call. |

[### Example of Use - List Organization Event Types](#example-of-use---list-organization-event-types_body)The following API call returns all event types that belong to the organization in your Calendly account:

**URL:**

`/event_types`

**Method:**

`GET`

**Query string:**

Key: `organization`

Value: {organization URI}

![calendlyAPISettings.png](./../image/uuid-6a470930-c0cd-220e-43b3-75b3094308cb.png)The result can be found in the module's Output under Bundle > Body > collection.

In our example, 4 event types were returned:

![calendlyAPIOutput.png](./../image/uuid-1784f2fe-f0ea-0d13-c43a-86c16d673727.png)Changelog
---------

New modules:

* Create a Scheduling Link
* Get an Event
* Get an Event Invitee
* Get an Event Type
* Get an Organization Membership
* Invite a User to Organization
* List Event Invitees
* List Events
* List Event Types
* List Organization Memberships
* Make an API Call
Changes:

* Watch Cancellations module deprecated, you can use the improved Watch Events
* Watch Invitee Events module deprecated
* Watch Events now also allows for filtering of Invitee Canceled, before it was only Invitee Created
