SublimeSourceTree
=================

Very simple plugin to open [SourceTree](http://sourcetreeapp.com/) from [Sublime Text 2](http://www.sublimetext.com/2).

Installing
----------

**Using Git:** Clone the repository in your Sublime Text 2 Packages directory and restart Sublime Text 2:

    git clone https://bitbucket.org/PhillSparks/sublimesourcetree.git

Usage
-----

Open SourceTree and install the command line tool by clicking on the SourceTree menu and then on `Install Command Line Tools`; SourceTree will create an executable named `stree` inside `/usr/local/bin`.

Open the command palette and execute the ``SourceTree: Open SourceTree`` command to open the repository in which the currently opened file is located.

Sample user key binding to execute the command::

    { "keys": ["super+."], "command": "sourcetree_open" }

Configuration
-------------

Additional settings can be configured in the User File Settings:

`stree_path`: the path to the `stree` executable (default: `"/usr/local/bin/stree"`)

Changelog
---------
v1.0 (26-04-2012):

* Initial version

License
-------
See the LICENSE-MIT.txt file.
