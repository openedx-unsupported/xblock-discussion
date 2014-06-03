#!/usr/bin/env bash

cd `dirname $BASH_SOURCE` && cd ../
node_modules/.bin/coffee --compile --output discussion_app/static/discussion/js `find discussion_app/static/discussion/coffee/ -maxdepth 1 -type f -name "*.coffee"`
node_modules/.bin/coffee --compile --output discussion_app/static/discussion/js/models `find discussion_app/static/discussion/coffee/models -maxdepth 1 -type f -name "*.coffee"`
node_modules/.bin/coffee --compile --output discussion_app/static/discussion/js/views `find discussion_app/static/discussion/coffee/views -maxdepth 1 -type f -name "*.coffee"`
