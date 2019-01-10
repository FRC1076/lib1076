# lib1076
Library of functions/tools/utilities that may get used in multiple projects each year

If you want to use this library in your project, you can add it to your repository in
the most convenient place.  (usually that means at the top level)   Trying to use
git submodule is kind of messy, unfortunately, so you might want to avoid that.

Plan is for this software to be "pip" installable so you'll have the stable version
available to you in the proper place.      Until we figure that out, you can just
check it out into your project and use it there.    Just don't "git add" it your project,
since we'll be maintaining this code in this repo.    More copies of it will not help
matters.

Here are the resources available (or planned):

Available

udp_channel.py  :  Makes it easy to create udp channel between (addr,port) pairs.
                   Useful default values make it easy to do self test on one system.
                   
Planned

deadzoned_controller.py  :   This is a drop in replacement for xbox controller with deadzoned
                             joystick.  Ultimately, it will have some calibration functions, some
                             user-specific preferences, etc...   But at first, just deadzoning.

