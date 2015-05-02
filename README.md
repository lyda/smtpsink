# smtpsink

An SMTP sink.  It accepts all email (with a list of addresses to reject)
and then saves them to a file.  At no time does it send any emails.

A web UI allows the user to review when emails were received and a REST
API allows the user to programmatically check the same info.

# Dependencies
* [bottle](http://bottlepy.org/)

# Installation

```bash
$ sudo pip install smtpsink
```

# Documentation
See http://lyda.github.io/smtpsink/ for complete API information (also contained in the `doc` directory).

# Example Usage

This must be run as root. It needs to listen on port 25 for incoming emails.
