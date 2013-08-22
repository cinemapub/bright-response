# RESPONSE SYNTAX

## Example response definition
Example of a response definition in an job INI file:

```INI
[response:unique_name]
;; some comment
type="twitter_post"
tw_account="@myaccount"
tw_text="Thank you {twitter_user} for your feedback"
```

## Title

- The title fields should always composed as follows: `[response:{name of response}]`.
- It is possible to have multiple responses in a job INI. These will be executed in sequence of their definition. Some response types will have a duration (show text for 10 seconds, show video) while others will be almost instantaneous (push button, tweet a message, ...)
- By convention, each response block should have a unique name


## Required parameters

### Response type

This will define the type of response. Depending on the machine where it is running (PC, NAS, Raspberry Pi), or the configured services (Twitter/Facebook/Twilio) some response types will not be available.

- `twitter_post`: 
	- post a message on Twitter
	- required parameters: tw_account="@myaccount", tw_text="some text using {field}"
- `twitter_follow`: 
	- follow a user on Twitter
	- required parameters: tw_account="@myaccount"
- `screen_text`:
	- show a message on the screen
	- required parameters: text="some text using {field}",duration
	- optional parameters: font-family, font-size, color
- `screen_image`:
	- show an image on the screen
	- required parameters: URL/path, duration
- `screen_video`:
	- show a video on the screen
	- required parameters: URL/path, duration (or default: video length)
- `screen_browse`:
	- show a web page on the screen
	- required parameters: URL/path, duration
- `audio_play`:
	- play a sound (wav/mp3)
	- required parameters: URL/path
- `camera_grabimg` 
	- grab an image from an attached (web)cam
	- required parameters: camera path, output file
- `camera_grabvid` 
	- grab a video from an attached (web)cam
	- required parameters: camera path, output file, duration
- `rpi_gpioset` 
	- 'push a button' i.e. bring a pin high (only for Raspberry Pi GPIO)
	- required parameters: PIN no, duration

- *Future triggers to consider*
	- twilio_outsms
	- twilio_outcall
	- facebook_post
	- facebook_message
	- email_send
	- web_geturl
	- web_posturl