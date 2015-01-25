Celty: Troubleshooting
======================

Aria2c-related problems
-----------------------

### I suspect my aria2c is broken... ###

Try this procedure: open a shell and paste `aria2c --version | grep "Enabled Features"`. If you don't find `XML-RPC` and `BitTorrent` in that list... you may want to either download a newer build or recompile aria2c with _both_ xml-rpc and torrent support (check aria2c compiling notes if necessary).

### Did I install aria2c? ###

Dunno lol. It has to be in your `PATH` environment variable.  
If you're on Linux/Cygwin, use `which aria2c` to check it.  
On Windows, open `Control Panel > System and Security > System > Advanced System Settings`, then click on `Environment variables` and check if `PATH` contains the folder that contains the recompiled/downloaded aria2c executable.

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

### I have the same problem, but I'm on a Linux box! ###

Install "psmisc" with your favourite package manager.