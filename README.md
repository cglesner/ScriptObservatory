ScriptObservatory
=================

The goal of the ScriptObservatory project is to extend the idea behind the 
[SSL Observatory](https://www.eff.org/observatory) by recording and 
information about the **_live content_** people are seeing on
the internet.

Initially, the only objects that will be analyzed are JavaScript files. 
Eventually, it might be extended to include other types of content like 
flash objects and iframes. 

The long-term goal of the [website](https://www.scriptobservatory.org)
is for it to be a place where anyone can analyze the record of 
what snippets of code people have been sent while on the internet. The 
long-term goal for the 
[Chrome extension](https://github.com/andy11/ScriptObservatory#usage)
is to crowdsource the data collection and to (optionally) act as a 
**_content-aware_** script blocker, letting you have finer control 
over what runs on your computer. 


Usage
-----

(check back later)


How It Works
------------

The ScriptObservatory Chrome extension is notified every time your browser is 
about to make a request for an object that Chrome classifies as a "script". 
The extension stops the browser from making the request and makes its own request
instead. Once it receives the content, it calculates a hash of the data and 
passes the object back to the browser.

This way of grabbing the content isn't ideal and will hopefully be improved soon.
Documentation of design decisions can be found directly in the source code. 
([chrome-extension/extension.js](https://github.com/andy11/ScriptObservatory/blob/master/chrome-extension/extension.js)
would be a good place to start.)


Privacy
-------

With the ScriptObservatory Chrome extension installed, your browser will send these
four pieces of information to a remote server at regular intervals:
 1. The full URL of the script you downloaded
 2. The full URL of the parent webpage where the script was included
 3. The SHA-256 hash of the script's content
 4. The time you made this observation

Optionally, you can have the Chrome extension send the full content of the scripts you
download to the server too. This will be turned off by default in all released versions.

Here are some steps that have been made to make this process as trustworthy as possible:
 - The connection from you to the remote upload server will always be 
   [encrypted using SSL/TLS](https://www.ssllabs.com/ssltest/analyze.html?d=scriptobservatory.org). 
 - No IP addresses or User IDs are ever recorded in the database.
 - The source code for both the client and the server will always be available for you to 
   review. (See the 
   [chrome-extension/](https://github.com/andy11/ScriptObservatory/tree/master/chrome-extension) 
   and [backend/](https://github.com/andy11/ScriptObservatory/tree/master/backend) 
   directories to get started.)


Roadmap
-------

Milestone 3 (target date= 4/20):
 - Create bookmarklet for jumping to results for current site
 - Rework/reorganize database structure to allow fast searching of script URLs/hashes
 - Add pagination to results window
 - Autoscan queried websites with no prior results
 - Add button to chrome extension to toggle reporting on and off
 - Add button to chrome extension to view current page's analysis page
 - Allow blacklisting stats upload for websites in the chrome extension

Milestone 4 (target date= 4/30):
 - Add tests for backend API & chrome extension code
 - Have robobrowser automatically report all errors while browsing sites
 - Build a VM-based solution to sandbox the robobrowser
 - Make robobrowser's time of exit tied to when it POSTs the results, not onload()

Longer-term:
 - Support iframes
 - Support flash objects
 - Add interactive visualizations for collected data
 - Make sure there's no interference with other extensions / ad-blockers
 - Allow users to import web traffic from PCAP


Contributing
------------

If you have ideas/comments/suggestions, please submit them as Issues or Pull Requests. Thanks!

