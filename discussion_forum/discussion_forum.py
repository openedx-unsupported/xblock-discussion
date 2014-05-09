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
    render_mako_templates,
    render_mustache_templates
)


# Globals ###########################################################

log = logging.getLogger(__name__)

# temporary, really...
JS = [
'public/js/models/discussion_user.js',
'public/js/content.js',
'public/js/discussion.js',
'public/js/main.js',
'public/js/discussion_filter.js',
'public/js/views/discussion_content_view.js',
'public/js/views/response_comment_view.js',
'public/js/views/thread_response_show_view.js',
'public/js/views/discussion_user_profile_view.js',
'public/js/views/new_post_inline_vew.js',
'public/js/views/thread_response_edit_view.js',
'public/js/views/discussion_thread_view.js',
'public/js/views/discussion_thread_view_inline.js',
'public/js/views/thread_response_view.js',
'public/js/views/discussion_thread_list_view.js',
'public/js/views/discussion_thread_show_view.js',
'public/js/views/discussion_thread_edit_view.js',
'public/js/views/response_comment_show_view.js',
'public/js/views/discussion_thread_profile_view.js',
'public/js/views/new_post_view.js',
'public/js/views/response_comment_edit_view.js',
'public/js/discussion_router.js',
'public/js/utils.js',
'public/js/templates.js',
'public/js/discussion_module_view.js',
#'public/js/tooltip_manager.js'
]

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

        fragment.add_content(render_template('templates/html/discussion.html', {
            'discussion_id': self.discussion_id
        }))

        # TODO clean the resources... add a get_css()/get_javascript functions and loop...
        fragment.add_css_url(self.runtime.local_resource_url(
            self,
            'public/css/vendor/font-awesome.css'
        ))

        fragment.add_css_url(self.runtime.local_resource_url(
            self,
            'public/css/discussion.css'
        ))

        # TODO Not use where this one was used yet...
        # fragment.add_css_url(self.runtime.local_resource_url(
        #     self,
        #     'public/css/discussions-inline.css'
        # ))

        fragment.add_javascript(render_template('public/js/discussion_block.js', {
            'course_id': self.course_id
        }))

        fragment.add_content(render_mustache_templates(
            os.path.join(os.path.dirname(__file__) + '/templates/mustache')
        ))

        fragment.add_content(render_mako_templates(
            os.path.join(os.path.dirname(__file__) + '/templates/html')
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/split.js')
        )

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/i18n.js')
        )

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/URI-min.js')
        )

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/jquery-leanModal-min.js')
        )

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/jquery-timeago.js')
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

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/mathjax-MathJax-c9db6ac/MathJax.js'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/Markdown-Converter.js'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/Markdown-Sanitizer.js'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/Markdown-Editor.js'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/mathjax_delay_renderer.js'
        ))

        fragment.add_javascript_url(
            self.runtime.local_resource_url(self, 'public/js/vendor/customwmd.js'
        ))

        for js in JS:
            fragment.add_javascript_url(self.runtime.local_resource_url(self, js))

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
