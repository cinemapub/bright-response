BRIGHT-RESPONSE
===============


* purpose: to make a generic trigger-response agent for Raspberry Pi. Will mostly work on Linux-based NAS/PCs too.

* triggers
	* Twitter
	* Facebook
	* RSS: 
	* SMS: receive text (via Twilio)
	* time: every day/hour/15 minutes

* responses
	* Screen: video/image/text
	* Sound: play WAV/MP3
	* Twitter: reply/refollow
	* Facebook: post
	* Web: POST/GET
	* GPIO: push a button/close a circuit (Raspberry Pi only)

* requires
	* Python
	* Tweepy: Twitter library for Python
	  https://github.com/tweepy/tweepy
	* Twilio Python Helper
	  http://www.twilio.com/docs/python/install

	  