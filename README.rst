Event Tweets
============

Statistical analysis of events on Twitter based on pre-defined parameters. Given a timespan, 1+ Twitter accounts and key phrases to check for, it will determine the number of mentions of those terms.

Data model
----------

Event
~~~~~

* Label
* Start date / time
* End date / time (optional)

Account Group
~~~~~~~~~~~~~

* Label


Account
~~~~~~~

* Event
* Twitter username
* Group(s)

Term Group
~~~~~~~~~~

* Label

Term
~~~~

* Event
* String
* Group(s)

Tweet
~~~~~

* Event
* Content
* Account

Term Match
~~~~~~~~~~

* Tweet
* Term
