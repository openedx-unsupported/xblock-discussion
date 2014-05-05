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

# temporary, really...
JS = [
'public/js/models/discussion_user.js',
'public/js/content.js',
'public/js/discussion.js',
'public/js/main.js',
'public/js/views/response_comment_view.js',
'public/js/views/thread_response_show_view.js',
'public/js/views/discussion_user_profile_view.js',
'public/js/views/new_post_inline_vew.js',
'public/js/views/thread_response_edit_view.js',
'public/js/views/discussion_thread_view_inline.js',
'public/js/views/thread_response_view.js',
'public/js/views/discussion_thread_view.js',
'public/js/views/discussion_thread_list_view.js',
'public/js/views/discussion_thread_show_view.js',
'public/js/views/discussion_thread_edit_view.js',
'public/js/views/discussion_content_view.js',
'public/js/views/response_comment_show_view.js',
'public/js/views/discussion_thread_profile_view.js',
'public/js/views/new_post_view.js',
'public/js/views/response_comment_edit_view.js',
'public/js/discussion_router.js',
'public/js/utils.js',
'public/js/templates.js',
'public/js/discussion_module_view.js',
'public/js/discussion_filter.js',
#'public/js/tooltip_manager.js'
]

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
        fragment = Fragment()
        fragment.add_content(render_template('templates/html/discussion.html', {
            'discussion_id': self.discussion_id
        }))

        fragment.add_css_url(self.runtime.local_resource_url(
            self,
            'public/css/discussions-inline.css'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/URI-min.js')
        )
        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/jquery-leanModal-min.js')
        )
        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/underscore-min.js')
        )
        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/backbone-min.js')
        )
        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/mustache.js')
        )

        for js in JS:
            fragment.add_javascript_url(self.runtime.local_resource_url(self, js))

        fragment.add_javascript(render_template('public/js/discussion_block.js', {
            'course_id': self.xmodule_runtime.course_id
        }))

        fragment.initialize_js('DiscussionBlock')

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
