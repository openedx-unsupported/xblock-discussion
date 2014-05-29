Discussion XBlock
=================

This is an initial prototype for redesigning Discussion. This project is in the early stages of
development and is not ready for general use.

Installation
------------

From the xblock-discussion repository, and within the Python virtual environment you used to setup
the XBlock workbench or the LMS, install the requirements:

```bash
pip install -r requirements.txt
```

Since XBlock and xblock-discussion are both in development, it is recommended to use the XBlock
revision specified in the workbench/LMS requirements.txt file. The main XBlock repository is not
always ready to use in edx-platform and you might experience some issues.

Enabling in Studio
------------------

You can enable the discussion xblock in studio through the advanced settings:

1. From the main page of a specific course, click on *Settings*, *Advanced Settings* in the top
menu.
2. Check for the *advanced_modules* policy key, and add *"discussion-forum"* in the policy value
list. Note that the use of *discussion-forum* instead of *discussion* is currently a limitation
because *discussion* is reserved to the xmodule, which is still supported.
3. Click on the *Save changes* button.

Development
-----------

Node.js and npm are required modify the coffeescript files, which are then compiled into javascript.

Install the node.js coffeescript module:

```bash
npm install
```

When needed, re-compile the javascript files:

```bash
./scripts/coffee.sh
```

Running Tests
-------------

(available soon)

Quality Check
-------------

Note that the code doesn't pass pylint at the moment. Will be fixed soon.

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

The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted.

Please see ``LICENSE`` for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org

Mailing List and IRC Channel
----------------------------

You can discuss this code on the
`edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_ or
in the `edx-code` IRC channel on Freenode.
