Discussion XBlock
=================

This is an initial prototype for redesigning Discussion. This project
is in the early stages of development and is not ready for general
use. The XBlock currently only works with the edx-solutions' forks of
[edx-platform](https://github.com/edx-solutions/edx-platform) and
[cs_comments_service](https://github.com/edx-solutions/cs_comments_service). The
patches are in the process of being merged upstream, so this will
eventually not be required anymore.

Installation
------------

From the xblock-discussion repository, and within the Python virtual
environment you used to setup the XBlock workbench or the LMS, install
the requirements:

```bash
pip install -r requirements.txt
```

Since XBlock and xblock-discussion are both in development, it is
recommended to use the XBlock revision specified in the workbench/LMS
`requirements.txt` file. The main XBlock repository is not always
ready to use in edx-platform and you might experience some issues.

Enabling in Studio
------------------

You can enable the discussion xblock in studio through the advanced
settings:

1. From the main page of a specific course, click on *Settings*,
   *Advanced Settings* in the top menu.
2. Check for the *advanced_modules* policy key, and add
   `"discussion-forum"` in the policy value list. Note that the use of
   `discussion-forum` instead of `discussion` is currently a limitation
   because `discussion` is reserved to the xmodule, which is still
   supported.

3. Click on the *Save changes* button.

To also use the xblock for the course discussion:

1. Add `"discussion-course"` to *advanced_modules* the same way as
   described above.
2. Create a new section with the name *DISCUSSION_TAB*.
3. Under the new secion -- after creating subsections -- add a new
   *Advanced... discussion-course* unit.
4. Publish changes.

Usage
-----

To add the discussion block to a unit, choose *Discussion* from the
*Advanced Components* list in the studio.

![Studio View](https://raw.githubusercontent.com/edx-solutions/xblock-discussion/aad91f12b37c47728bd545ffc63e8de79d421aa3/doc/img/studio-view.png)

Clicking the *Edit* button opens up a form that will let you change some
basic settings:

![Edit View](https://raw.githubusercontent.com/edx-solutions/xblock-discussion/aad91f12b37c47728bd545ffc63e8de79d421aa3/doc/img/edit-view.png)

The students will be able to post comments on the unit:

![Student View Initial](https://raw.githubusercontent.com/edx-solutions/xblock-discussion/aad91f12b37c47728bd545ffc63e8de79d421aa3/doc/img/student-view-1.png)

![Student View Post](https://raw.githubusercontent.com/edx-solutions/xblock-discussion/aad91f12b37c47728bd545ffc63e8de79d421aa3/doc/img/student-view-2.png)

![Student View List](https://raw.githubusercontent.com/edx-solutions/xblock-discussion/aad91f12b37c47728bd545ffc63e8de79d421aa3/doc/img/student-view-3.png)

Development
-----------

Node.js and npm are required to be able to compile and combine the
coffeescript files into a single minified javascript file.

Install the node.js coffeescript module:

```bash
npm install
```

When needed, re-compile the javascript files:

```bash
./scripts/buildjs.sh
```

This will produce a new minified file under
`discussion_app/static/discussion-xblock.$SHA.min.js`, where `$SHA` is
the SHA hash of the file's contents.

When you re-compile the javascript files, you need to update the value
of the `JS_SHA` variable in `discussion_app/views.py`.

If you add new JavaScript/CoffeeScript files, you need to add them to
the list in `scripts/buildjs.sh` in order to include them in the
compiled file.

Running Tests
-------------

(available soon)
/
Quality Check
-------------

Note that the code doesn't pass pylint at the moment. Will be fixed
soon.

Install pylint:

```bash
pip install pylint==0.28.0
```

Check for quality violations:

```bash
pylint apps
```

Disable quality violations on a line or file:

```python
# pylint: disable=W0123,E4567
```

License
-------

The code in this repository is licensed under version 3 of the AGPL
unless otherwise noted.

Please see `LICENSE` for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email
security@edx.org.

Mailing List and IRC Channel
----------------------------

You can discuss this code on the
[edx-code Google Group](https://groups.google.com/forum/#!forum/edx-code)
or in the `#edx-code` IRC channel on Freenode.
