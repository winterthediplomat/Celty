Celty: Miyuki configuration file changes
========================================

*Celty* needs to know where it has to download your favourite series.  
At the moment, the only way to say it is to write this information into Miyuki configuration files.

You can add the following information, both at a _global_ level (outside the `series` section) and _per series_ level:

* downloadDir
  where you want to download your episodes.

* seedTime
  specify seeding time in _minutes_.

Look at `tests/celty.conf` for an example Miyuki configuration file.