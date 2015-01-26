Celty : Miyuki x aria2c
=======================

Celty mixes the power of `aria2c <http://aria2.sourceforge.net/>`_ and the simplicity of `Miyuki <http://github.com/RoxasShadow/Miyuki>`_ to bring you the ultimate automatic anime downloader.

Why did you start this project?
-------------------------------

I experienced some problems while using baretorrent: torrent files were removed from watch directory. To make it worse, I lost several downloaded series in this "put/removed torrents" dance.

A patch for Yamazaki (the library Miyuki uses to query torrent sources and download torrent files) was proposed in order to fix an annoying behaviour of another famous torrent client: it renames torrent files (adding a suffix), so Miyuki does not find them and re-downloads 'em again.
You can patch for one client, but you can't do that for every client out there.

As aria2c does not modify the downloaded torrents in Miyuki's watch directory, I thought it was the perfect candidate for a joint operation with the best dubb- ehm, command line anime tracker out there.

Dependencies
------------

* Libraries
  
  - pyyaml (for Miyuki conf file parsing)

  - click (command line handling)

  - alfateam123/pyaria2 (use "-r requirements.txt" with pip!)

They will be installed automatically when installing Celty.

* Third-party apps
  
  - aria2c
  
  - Miyuki

Be sure that aria2c is compiled with torrent and xml-rcp support.