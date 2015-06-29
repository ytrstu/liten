Planned Roadmap by version
  * 0.1:  Write robust unit tests, make sure most bugs are eliminated and common usage scenarios are covered.
    * 0.1.3:  ~~Get rid of cruft, add entry point to scripts.~~
    * 0.1.4:  ~~Add support for --delete option which eliminates duplicates in a directory.~~
    * 0.1.5:  ~~Supply multiple directories to follow.~~
    * No further work.  This version is stable.
  * 0.2: New Architecture and Features, Alpha API
    * Enhanced Python API with more features accessible from library
    * Identify duplicates not only in pairs, but also in groups of 3 or more
    * Integrate Project with pathtool architecture:  http://code.google.com/p/pathtool/
    * Add a destructive left or right merge option.
    * Format string for CSV report entries
  * 0.3:  Cached Searches, Stable API
    * Project will integrate code from my other project pylesystem to allow cached searches of duplicates, and visualization of data via web tool.  http://code.google.com/p/pylesystem/
    * Enhanced reporting capabilities, such as CSV/PDF/HTML reports
    * Search all local disks (windows)
    * Add ability to follow symbolic links
    * Add ability to ignore certain filesystems
    * Integrate CLI plugin architecture
  * 0.4:  GUI Interface
  * 1.0: FeatureCreep (need tuits and explanations)
    * Create hardlinks or symlink option