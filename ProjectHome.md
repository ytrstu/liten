### Command Line Tool and Library To Eliminate Duplicates and Facilitate Intelligent Merging of Data Structures. ###

**Warning**:  Be extremely cautious when using this tool.  You could potentially delete a file that your operating system needs to run.  Please do not just run this on the root level of your hard drive with --delete.  First run a report, look at it, and then decide what to delete based on that report, perhaps on a directory by directory basis.

# News #
2008-12-26 **Liten 0.1.5 is released**

  * fixed bug that required three duplicates to make a match
  * new feature that allows specifying several directories to search

Changes for latest development version can be found in [CHANGELOG.txt](http://code.google.com/p/liten/source/browse/CHANGELOG.txt)

# Installation #
With Python 2.5 or later
```
python -m easy_install liten
```

You can also download the script, and just run it.  If you do not develop with Python this may be the best choice until it's packaged for your specific OS.

http://liten.googlecode.com/files/liten-0.1.5-script.py

The previous version in an OS X Leopard Package is here:

**Over 1,100 downloads in less than 30 days since release**

http://liten.googlecode.com/files/liten-0.1.4.2-macosx-10.5-intel.dmg

# Documentation #
You can access documentation for your Liten version directly from Python:
```
>>> import liten
>>> help(liten)
...
```

Latest documentation for released version can be found here:
http://pypi.python.org/pypi/liten

The latest development documentation is usually available at:
http://liten.googlecode.com/hg/docs/liten_documentation.html

See RoadMap wiki page if you're interested in Liten development.

# Acknowledgements #
Thanks to:
  * Noah Gift for coding initial Liten version and releasing it under MIT license.

  * Rick Copeland
  * Titus Brown
  * Shannon Behrens
  * Anatoly Techtonik
and others for ideas, patches and enhancements.