.. image:: https://api.travis-ci.org/zmsdev/Products.LDAPUserFolder4.svg?branch=master
   :target: https://travis-ci.org/zmsdev/Products.LDAPUserFolder4

==========================
 Products.LDAPUserFolder4
==========================
This product is a replacement for a Zope 4 user folder. It does not store its 
own user objects but builds them on the fly after authenticating a user against 
the LDAP database.


To dos
======
* fix tests: Python 3 str/bytes-handling was fixed in implementation against a real LDAP database, dataflake.fakeldap has to be reworked.
* publish on pypi
* reintegrate with dataflake/Products.LDAPUserFolder


Debugging problems
==================
All log messages are sent to the standard Zope event log 'event.log'. In 
order to see more verbose logging output you need to increase the log level 
in your Zope instance's zope.conf. See the 'eventlog' directive. Setting 
the 'level' key to 'debug' will maximize log output and may help pinpoint 
problems during setup and testing.
