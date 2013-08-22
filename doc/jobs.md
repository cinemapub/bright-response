# JOB DEFINITION

## Purpose
- Jobs are a combination of 1 or more trigger definitions with 1 or more responses definitions.
- When the service starts, all the jobs in the `config/jobs/` folder are read, set-up and activated.


## Syntax

A job is defined in a text-based INI layout.

```INI
[trigger:name_of_trigger]
type="twitterstream_hashtag"
keyword="#specialhashtag"

valid_hours="[11:00;23:55]"
valid_days="[1;5]"
valid_period="[2013-01-01;2013-12-31]"

[response:reply]
type="twitter_reply"
text="{@twhandle} Thank you for your feedback"

[response:thankyou1]
type="screen_text"
text="Thank you {@twhandle} for your feedback"
duration="10"

[response:video]
type="screen_video"
path="/share/videos/response.mp4"

[response:thankyou1]
type="screen_text"
text="Hope you enjoyed it, {@twhandle}"
duration="10"
```

## More info

* check [triggers.md] for a detailed overview of triggers
* check [responses.md] for a detailed overview of responses
