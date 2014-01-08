# ACTION SCRIPTS

## Definition

These are the scripts used in the `[action]`  parts of the joib definitions. They always be used using the following 'interface':


    [scriptname] "param1" "param2"
    return value can be 
		0  : return without errors, 
		-1 : error 

    stdin: (optional) free text input
    stdout: list of output variables, 1 per line, in the form
		key1=val1
		key2=val2
    
The program does a certain action and comes back with a error level (return value).


## Action types

### Virtual (web services)

* Email: 
	* send mail
* Twitter:
	* tweet
* Facebook: 
	* post text
	* post photo
* Twilio: 
	* Send SMS
	* Call script

### Physical (local)

* Raspberry
	* make contact (e.g. to start LED)
	* show image for N seconds
	* start video

## Examples

	pi_turn_on 8

turn on Raspberry Pi contact 8 (e.g. start a light)

	show_video countdown.mp4

show video on main screen

	show_image congrats.png 20

show image for 20 seconds

	post_twitter "@customer thanks for your tweet #promocampaign"

tweet a message

