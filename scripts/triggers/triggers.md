# TRIGGER SCRIPTS

## Definition

These are the scripts used in the `[trigger]`part of the jobs. They always be used using the following 'interface':


    [scriptname] "param1" "param2"
    return value can be 
		0  : return without errors, but no trigger was fired (for synchronous triggers)
		1  : return without errors, and the trigger was fired
		N  : where N > 1 (optional) trigger was fired N times
		-1 : error in program (e.g. USB device not connected ...)   

    stdout: list of output variables, 1 per line, in the form
		key1=val1
		key2=val2
    
The program only returns when the trigger is fired, otherwise it just waits.

when the trigger fires, and the program returns with its data (see examples), then the job will run and a number of actions will be executed. After all actions are terminated, the trigger script is run again, and it will wait again.


## Trigger types

The scripts can be in Python, php, bash or any executable/binary format.

### Virtual (web services)

* Email: incoming email with optional filter on title
* RSS Feed: new item with optional filter on word/tag/category
* Twitter:
	* tweet with #hashtag
	* tweet for @myaccount
	* direct message to @myaccount
* Foursquare: 
	* check-in at this location
* Facebook: 
	* follow page
	* new post
	* new photo
* Instagram: 
	* new photo by user
	* new photo at location
* Tumblr
	* new post
* Twilio: 
	* incoming SMS
	* incoming call

### Physical (local sensors)

* *Generic*: push key X (e.g. space bar)
* *Raspberry*: 
	* push button
	* camera motion detection
	* temperature under/above treshold

## Examples:

### Example 1

	rss_on_update.py "http://www.example.com/rss.xml"

 waits for a new item to appear in the RSS feed, and when it does it returns the following lines:

	date=2014-01-08T16:22:08+0100
	url=http://www.example.com
	title=this is the title
	author=author@example.com
	category=News (optional)
	tags=news,belgium,tech (optional)

### Example 2
	
	pi_on_button_push.py 18

waits for button 18 to be pushed, and when it does, returns the following lines:

	date=2014-01-08T16:22:08+0100
	button=18

### Example 3

	twitter_trigger.py -geo 5km "@myhandle" "#promo"

will poll for a tweet like "@myhandle yes, I saw your #promo" that was made in a radius of 5km around the location of the server, and when it finds one, returns with the following lines

	date=2014-01-08T16:22:08+0100
	from=@twittercontact
	geo=lat;long
	text=@myhandle yes, I saw your #promo

