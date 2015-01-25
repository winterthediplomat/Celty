Celty : Miyuki x aria2c
=======================

This project uses RoxasShadow/Miyuki and aria2c to automatically track your favourite anime and download them.

Why did you start this project?
-------------------------------

I experienced some problems while using baretorrent, as torrent files were removed from watch directory. To make it worse, I lost several downloaded series.

A patch for Yamazaki (the library Miyuki uses to query torrent sources) was proposed in order to fix an annoying behaviour of another famous torrent client: it renames torrent files (adding a suffix), so Miyuki does not find them and re-downloads 'em again.
You can patch for one client, but you can't do that for every client out there.

As aria2c does not modify the downloaded torrents in Miyuki's watch directory, I thought it was the perfect candidate for a joint operation with the best dubb- ehm, command line anime tracker out there.

Dependencies
------------

* Libraries
  
  - pyyaml (for Miyuki conf file parsing)

* Third-party apps
  
  - aria2c
  
  - Miyuki

Be sure that aria2c is compiled with torrent and xml-rcp support.