# Imports ###########################################################

import os
import logging
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
    render_mako_template,
    render_mustache_templates
)

from discussion_app.views import get_js_urls, get_css_urls

# Globals ###########################################################

log = logging.getLogger(__name__)

# Classes ###########################################################


@XBlock.needs('discussion')
class DiscussionXBlock(XBlock):
    FIELDS_TO_INIT = ('discussion_id',)

    discussion_id = String(scope=Scope.settings, default=lambda: uuid4().hex)

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

    @property
    def course_id(self):
        # TODO really implement this
        if hasattr(self, 'xmodule_runtime'):
            return self.xmodule_runtime.course_id
        return 'foo'

    def student_view(self, context=None):
        fragment = Fragment()

        if getattr(self.xmodule_runtime, 'is_author_mode', False):
            fragment.add_content(render_mako_template(
                'templates/discussion/_discussion_inline_studio.html',
                {'discussion_id': self.discussion_id}
            ))
            fragment.add_css(load_resource('static/discussion/css/discussion-studio.css'))
            return fragment

        discussion_service = self.xmodule_runtime.service(self, 'discussion')
        context = discussion_service.get_inline_template_context(self.discussion_id)
        context['discussion_id'] = self.discussion_id
        fragment.add_content(render_mako_template(
            'templates/discussion/_discussion_inline.html',
            context
        ))

        fragment.add_javascript(render_template('static/discussion/js/discussion_block.js', {
            'course_id': self.course_id
        }))

        fragment.add_content(render_mustache_templates())

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
        fragment.add_content(render_template('templates/discussion_inline_edit.html', context))
        fragment.add_javascript(load_resource('static/discussion/js/discussion_inline_edit.js'))

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


@XBlock.needs('discussion')
class DiscussionCourseXBlock(XBlock):

    display_name = String(
        display_name="Display Name",
        help="Display name for this module",
        default="Discussion Course",
        scope=Scope.settings
    )

    def student_view(self, context=None):
        fragment = Fragment()

        if getattr(self.xmodule_runtime, 'is_author_mode', False):
            fragment.add_content(render_mako_template(
                'templates/discussion/_discussion_course_studio.html'
            ))
            fragment.add_css(load_resource('static/discussion/css/discussion-studio.css'))
            return fragment

        discussion_service = self.xmodule_runtime.service(self, 'discussion')

        context = discussion_service.get_course_template_context()
        fragment.add_content(render_mako_template(
            'templates/discussion/_discussion_course.html',
            context
        ))

        # fragment.add_javascript(render_template('static/discussion/js/discussion_block.js', {
        #     'course_id': self.course_id
        # }))

        fragment.add_content(render_mustache_templates())

        for url in get_js_urls():
            fragment.add_javascript_url(url)

        for url in get_css_urls():
            fragment.add_css_url(url)

        #fragment.initialize_js('DiscussionBlock')

        return fragment

    def studio_view(self, context=None):
        fragment = Fragment()

        return fragment
