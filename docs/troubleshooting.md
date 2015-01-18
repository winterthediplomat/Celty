Celty: Troubleshooting
======================

Testing
-------

### Which platforms did you test Celty on? ###

I'm developing Celty on cygwin. I'll add TravisCI asap to add Ubuntu 12.04 (Linux) to the supported platforms. I don't own a Mac, I don't guarantee it even starts. (And you should install gentoo.)

### I'm on Cygwin, and killall is not found! Dotachin, what should I do? ###

On cygwin, "killall" is not installed by default. You have to

* open cygwin setup  
* locate "System/psmisc" package in your list
* install it

Now your test should run correctly.

### I have the same problem, but I'm on a Linux box!

Install "psmisc" with your favourite package manager.