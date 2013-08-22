# TRIGGER SYNTAX

## Example
Example of a trigger definition in an job INI file:

```INI

[trigger:name_of_trigger]
type="twitter_hashtag"
parameter="#specialhashtag"
max_distance="1km"
valid_hours="13:00-23:59"
valid_days ="1;3-7"
valid_notbefore="2013-01-01"
valid_notafter ="2013-12-31"

```

# Description

## Title

## Fields

### type=""
This is the 