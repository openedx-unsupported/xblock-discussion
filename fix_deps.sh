#!/bin/bash
# Some dependencies nees modification..

# Fix filenames of javascript vendor files.
# xblock issue, a resource can only contain a "." for the extension.
WD=discussion_forum/public/js/vendor
for file in $WD/*.*;
do
    NEW_FILENAME=$(echo $file | sed 's/\.[^\.]*$//' | sed 's/\./-/g').$(echo $file | sed 's/^.*\.//')
    [ $NEW_FILENAME != $file ] && mv $file $NEW_FILENAME
done


# template include disabled..
mv discussion_forum/templates/html/_filter_dropdown.html discussion_forum/templates/html/disabled_filter_dropdown.html

# remove the coffee files for the moment...
find discussion_forum/public/js -iname "*.coffee" -exec rm '{}' \;
