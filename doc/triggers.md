# TRIGGER SYNTAX

## Example trigger definition
Example of a trigger definition in an job INI file:

```INI
[trigger:unique_name]
;; some comment
type="twitter_hashtag"
tw_text="#specialhashtag"
max_distance="1km"
valid_hours="13:00-23:59"
valid_days ="1;3-7"
valid_notbefore="2013-01-01"
valid_notafter ="2013-12-31"
```

## Title

- The title fields should always composed as follows: `[trigger:{name of trigger}]`.
- It is possible to have multiple triggers in a job INI. These will be treated as `trigger1 OR trigger2 OR ...`.
- By convention, each trigger block should have a unique name


## Required parameters

### Trigger type

This will define the type of trigger. Depending on the machine where it is running (PC, NAS, Raspberry Pi), or the configured services (Twitter/Facebook/Twilio) some trigger types will not be available.

- `twitter_follow`: 
	- triggers for every new follower on Twitter of @myaccount
	- required parameters: tw_account="@myaccount"
 	- returned fields: `{twitter_user}, {date_time}`
- `twitter_mention`:
	- triggers for every Twitter mention of @myaccount
	- required parameters: tw_account="@myaccount"
 	- returned fields: `{twitter_user}, {twitter_message}, {geolocation}, {date_time}`
- `twitter_hashtag`:
	- triggers for every Twitter mention of #hashtag
	- required parameters: tw_text="#hashtag"
 	- returned fields: `{twitter_user}, {twitter_message}, {geolocation}, {date_time}`
- `rss_newitem`:
	- triggers for every item in a RSS feed (for easy integration with other services)
	- required parameters: URL
 	- returned fields: `{item_title}, {item_description}, {item_author}, {geolocation}, {date_time}`
- `time_event`: 
	- triggers at a certain moment, with optional recurrency
	- required parameters: @myaccount
	- optional parameters: recurrence (every month, week, day, hour, X min)
 	- returned fields: `{date_time}`
- `rpi_button`: 
	- triggered by button push (only for Raspberry Pi GPIO)
	- required parameters: PIN no
 	- returned fields: `{PIN no}, {date_time}`
- *Future triggers to consider*
	- `facebook_follow`	: new follower of FB page
	- `facebook_post`	: new post on FB page
	- `facebook_share`	: new share of FB Page
	- `twilio_insms`	: incoming SMS (via Twilio)
 	- `twilio_incall`	: incoming call (via Twilio)
	- `email_receive`	: incoming email (via POP3)


### Parameter

Depending on the type of trigger, one or more parameters should be given.


## Optional filters

### valid_hours

Allows for disabling the service during certain hours of the day.

Examples:

- `valid_hours="10-22"`: valid from 10:00 until 22:00
- `valid_hours="10-11,15-20"`: valid from 10:00 until 11:00, and again from 15:00 until 20:00
- `valid_hours="10:15-23:59"`: valid from 10:15 until 23:59

### valid_days

Allows for disabling the service during days of the week. 1 = Monday, ..., 7 = Sunday

Examples:

- `valid_days="1-5"`: valid from Monday until Friday
- `valid_days="1,3,5"`: valid on Monday, Wednesday and Friday

### valid_notbefore

Allows for disabling the service before a certain date (e.g. for the start of a campaign)

Examples:

- `valid_notbefore="2013-09-01"`: valid from 1 Sept (included)

### valid_notafter

Allows for disabling the service after a certain date (e.g. for the end of a campaign)

Examples:

- `valid_notafter="2013-12-31"`: valid until 31 Dec (included)

### max_distance

Allow for limiting the trigger to actions done within a certain distance of a certain point (e.g. the physcial machine, an event space)

Only works for trigger_types that have geolocation metadata (like Twitter's [Tweet Location](http://support.twitter.com/articles/78525-faqs-about-the-tweet-location-feature) ), and uses either a custom location  for this trigger or (by default) the location of the server (defined in machine config). 

Examples:

- `max_distance="1km"`: only trigger if action happened within 1km
- `max_distance="500m"`: only trigger if action happened within 500m



