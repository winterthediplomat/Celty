Celty : Miyuki x aria2c
=======================

Celty mixes the power of `aria2c <http://aria2.sourceforge.net/>`_ and the simplicity of `Miyuki <http://github.com/RoxasShadow/Miyuki>`_ to bring you the ultimate automatic anime downloader.

What does it do?
----------------

.. image:: https://cdn.mediacru.sh/q/qvBAHdEvhkXK.png

In short, it uses an ad-hoc modified Miyuki configuration file to locate where it downloaded your animu torrents, starts an aria2 instance and loads all the torrents, saving them in your favourite folders. More notes on the needed modifications can be found at docs/miyuki_conf_changes.md

What do I have to do?
---------------------

1. Modify your Miyuki configuration to include at least this, in the global section

.. code:: yaml

   download:
     - downloadDir: /my/download/dir
     - seedTime: 10 #optional, default is 0 (zero)

2. run `celty start path/to/miyuki.conf`

3. wait a bit

4. enjoy your animu

Please note that Celty does not start Miyuki: you have to launch it manually.

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

Be sure that aria2c is compiled with torrent and xml-rcp support. Ruby is needed for running Miyuki.