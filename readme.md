# BRIGHT-RESPONSE


## Purpose
to make a generic trigger-response agent in Python for Raspberry Pi. Will mostly work on Linux-based NAS/PCs too.

Use it to set-up "tweet to start machine X" systems

* triggers
	* Twitter/Facebook/RSS 
	* SMS: receive text (via Twilio)
	* Button: (via Raspberry GPIO)
	* time: every day/hour/15 minutes

- responses
	- Screen: video/image/text
	- Sound: play WAV/MP3
	- Twitter: reply/refollow
	- Facebook: post
	- Web: POST/GET
	- Physical: push a button/close a circuit (via Raspberry GPIO)

## Requires
* Python 2.7 - [python.org](http://www.python.org/download/)
* Raspberry Pi (for some functions) - [raspberrypi.org](http://www.raspberrypi.org/)

## Included projects
* tweepy: Twitter library for Python - for Twitter triggers/responses - on [github.com](https://github.com/tweepy/tweepy)
* feedparser: for reading RSS/Atoim feeds - on [code.google.com](https://code.google.com/p/feedparser/)
* geopy: for calculating geo distance - on [github.com](https://github.com/geopy/geopy/)
* twilio-python: for using Twilio telephony triggers/response - on [github.com](https://github.com/twilio/twilio-python)