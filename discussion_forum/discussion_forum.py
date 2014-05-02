# Imports ###########################################################

import logging
import uuid
import datetime
from uuid import uuid4

from lxml import etree
from StringIO import StringIO

from xblock.core import XBlock
from xblock.fields import Scope, String, DateTime
from xblock.fragment import Fragment

from .utils import load_resource, render_template, get_scenarios_from_path


# Globals ###########################################################

log = logging.getLogger(__name__)


# Classes ###########################################################

class DiscussionXBlock(XBlock):
    discussion_id = String(scope=Scope.settings, default=uuid4().hex)
    display_name = String(
        display_name="Display Name",
        help="Display name for this module",
        default="Discussion",
        scope=Scope.settings
    )
    data = String(
        help="XML data for the problem",
        scope=Scope.content,
        default="<discussion></discussion>"
    )
    discussion_category = String(
        display_name="Category",
        default="Week 1",
        help="A category name for the discussion. This name appears in the left pane of the discussion forum for the course.",
        scope=Scope.settings
    )
    discussion_target = String(
        display_name="Subcategory",
        default="Topic-Level Student-Visible Label",
        help="A subcategory name for the discussion. This name appears in the left pane of the discussion forum for the course.",
        scope=Scope.settings
    )
    sort_key = String(scope=Scope.settings)

    def student_view(self, context=None):
        fragment = Fragment(render_template('templates/html/discussion.html', {
            'discussion_id': self.discussion_id
        }))

        fragment.add_css_url(self.runtime.local_resource_url(
            self,
            'public/css/discussion-old.css'
        ))

        fragment.add_css_url(self.runtime.local_resource_url(
            self,
            'public/css/discussions-inline.css'
        ))
        return fragment

    def studio_view(self, context):
        """
        Editing view in Studio
        """
        fragment = Fragment()
        # fragment.add_content(render_template('templates/html/discussion_edit.html', {
        #     'self': self,
        #     'xml_content': self.xml_content or self.default_xml_content,
        # }))
        # fragment.add_javascript(load_resource('public/js/discussion_edit.js'))
        # fragment.add_css(load_resource('public/css/discussion_edit.css'))

        # fragment.initialize_js('DiscussionEditXBlock')

        return fragment
