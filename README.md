# lib1076
Library of functions/tools/utilities that may get used in multiple projects each year

If you want to use this library in your project, you should add it to your repository in
the most convenient place.  (usually that means at the top level).

You add it this way so that you end up with a correct link to the repo for the library.

  git submodule add https://github.com/FRC1076/lib1076.git lib1076
  
That ensures that you can pick up changes to the library, switch to different branches, etc...
You can also make and commit changes from within your project, but the changes will go to
the original repository (as it should).

Here are the resources available so far for general use:

udp_channel.py  :  Makes it easy to create udp channel between (addr,port) pairs.
                   Useful default values make it easy to do self test on one system.
