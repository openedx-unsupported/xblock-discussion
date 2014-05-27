#!/bin/bash
# Some dependencies nees modification..

# template include disabled..
mv discussion_app/templates/discussion/_filter_dropdown.html discussion_app/templates/discussion/disabled_filter_dropdown.html

# remove the coffee files for the moment...
find discussion_forum/public/js -iname "*.coffee" -exec rm '{}' \;
