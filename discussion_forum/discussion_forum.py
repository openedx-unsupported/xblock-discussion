# Imports ###########################################################

import os
import logging
import uuid
import datetime

from uuid import uuid4

from lxml import etree
from StringIO import StringIO

from xblock.core import XBlock
from xblock.fields import Scope, String, DateTime
from xblock.fragment import Fragment

from .utils import (
    load_resource,
    render_template,
    render_mako_templates
)

from discussion_app.views import get_js_urls, get_css_urls, render_mustache_templates

# Globals ###########################################################

log = logging.getLogger(__name__)

# Classes ###########################################################

class DiscussionXBlock(XBlock):
    discussion_id = String(scope=Scope.settings, default=None)

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

    def get_new_uuid(self):
        return uuid4().hex

    @property
    def course_id(self):
        # TODO really implement this
        if hasattr(self, 'xmodule_runtime'):
            return self.xmodule_runtime.course_id
        return 'foo'

    def student_view(self, context=None):
        fragment = Fragment()

        # TODO Where should we read those permission values?
        fragment.add_content(render_template('templates/discussion.html', {
            'discussion_id': self.discussion_id,
            'has_permission_to_create_thread': True,
            'has_permission_to_create_comment': True,
            'has_permission_to_openclose_thread': True,
            'has_permission_to_create_subcomment': True,
        }))

        fragment.add_javascript(render_template('static/discussion/js/discussion_block.js', {
            'course_id': self.course_id
        }))

        fragment.add_content(render_mustache_templates())

        fragment.add_content(render_mako_templates())

        for url in get_js_urls():
            fragment.add_javascript_url(url)

        for url in get_css_urls():
            fragment.add_css_url(url)

        fragment.initialize_js('DiscussionBlock')

        return fragment

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):  # pylint: disable=unused-argument
        """
        """

        # TODO find a better solution..
        # TODO can studio do something like that without going to edit and save?
        # Set the discussion_id
        if self.discussion_id is None:
            self.discussion_id = self.get_new_uuid()

        fragment = Fragment()
        log.info("submitted: {}".format(data))
        self.display_name = data.get("display_name", "Untitled Discussion Topic")
        self.discussion_category = data.get("discussion_category", None)
        self.discussion_target = data.get("discussion_target", None)
        return {"display_name": self.display_name, "discussion_category": self.discussion_category, "discussion_target": self.discussion_target}

    def studio_view(self, context=None):
        fragment = Fragment()
        context = {
            "display_name": self.display_name,
            "discussion_category": self.discussion_category,
            "discussion_target": self.discussion_target
            }
        log.info("rendering template in context: {}".format(context))
        fragment.add_content(render_template('templates/html/discussion_edit.html', context))
        fragment.add_javascript_url(self.runtime.local_resource_url(
            self,
            'static/discussion/js/discussion_edit.js'
        ))

        fragment.initialize_js('DiscussionEditBlock')
        return fragment

    # TODO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Discussion XBlock",
             """<vertical_demo>
                <discussion-forum/>
                </vertical_demo>
             """),
        ]
