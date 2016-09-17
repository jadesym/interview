# Problem Given By: Howard Grimberg of Amazon Web Services
# Optimal Solution Time: 15 min
"""
You have backup files for your standard hard drive, and you want to keep updates
for every single day, but you want to save space on your backup.

The backup files already existed in your backup hard drive in of all the files
in your standard hard drive like the following:
/mount/hdd/2016_1_01/a
/mount/hdd/2016_1_01/b
/mount/hdd/2016_1_02/a
/mount/hdd/2016_1_02/b

The goal is to reduce the amount of space that the backup uses by using
shortcuts/symlinks. Files tend to not be changed very often, so we don't want
to have copies of the same file in the backup.

Questions:
---------
How can we prevent copies of the same file?
Answer: Have symlinks/shortcuts pointing to the previous date file for
duplicate files

How can we do comparison between files quickly?
Answer: Hash the files SHA-256. It is much faster than comparing the files
byte by byte.

How do you deal with directories?
Answer: Use isDirectory or isFile and use BFS to DFS to compare all files
by their specific path name.

Solution:
Use a hashmap of path name to the previous hash to do quick comparisons
and lookups of files between different backup versions
"""
