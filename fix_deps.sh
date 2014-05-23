#!/bin/bash
# Some dependencies nees modification..

# template include disabled..
mv discussion_forum/templates/html/_filter_dropdown.html discussion_forum/templates/html/disabled_filter_dropdown.html

# remove the coffee files for the moment...
find discussion_forum/public/js -iname "*.coffee" -exec rm '{}' \;
