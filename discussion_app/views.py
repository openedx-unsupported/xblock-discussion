import os
import re
import pkg_resources

from mako.template import Template as MakoTemplate
from mako.lookup import TemplateLookup

from django.template import Context, loader
from django.http import HttpResponse

from django.templatetags.static import static

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

# Update this after building a new version of the minified JS file.
JS_SHA = '25b31111c077'

JS_URLS = [
    # VENDOR
    'discussion/js/vendor/split.js',
    'discussion/js/vendor/i18n.js',
    'discussion/js/vendor/URI.min.js',
    'discussion/js/vendor/jquery.leanModal.min.js',
    'discussion/js/vendor/jquery.timeago.js',
    'discussion/js/vendor/underscore-min.js',
    'discussion/js/vendor/backbone-min.js',
    'discussion/js/vendor/mustache.js',
    '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.4.0/MathJax.js?config=TeX-MML-AM_HTMLorMML-full',
    'discussion/js/vendor/Markdown.Converter.js',
    'discussion/js/vendor/Markdown.Sanitizer.js',
    'discussion/js/vendor/Markdown.Editor.js',
    'discussion/js/vendor/mathjax_delay_renderer.js',
    'discussion/js/vendor/customwmd.js',

    # DISCUSSION
    'discussion/js/tooltip_manager.js',
    'discussion/js/models/discussion_user.js',
    'discussion/js/content.js',
    'discussion/js/discussion.js',
    'discussion/js/main.js',
    'discussion/js/discussion_filter.js',
    'discussion/js/views/discussion_content_view.js',
    'discussion/js/views/response_comment_view.js',
    'discussion/js/views/thread_response_show_view.js',
    'discussion/js/views/discussion_user_profile_view.js',
    'discussion/js/views/new_post_inline_vew.js',
    'discussion/js/views/thread_response_edit_view.js',
    'discussion/js/views/discussion_thread_view.js',
    'discussion/js/views/discussion_thread_view_inline.js',
    'discussion/js/views/thread_response_view.js',
    'discussion/js/views/discussion_thread_list_view.js',
    'discussion/js/views/discussion_thread_show_view.js',
    'discussion/js/views/discussion_thread_edit_view.js',
    'discussion/js/views/response_comment_show_view.js',
    'discussion/js/views/discussion_thread_profile_view.js',
    'discussion/js/views/new_post_view.js',
    'discussion/js/views/response_comment_edit_view.js',
    'discussion/js/discussion_router.js',
    'discussion/js/utils.js',
    'discussion/js/templates.js',
    'discussion/js/discussion_module_view.js'
]

CSS_URLS = [
    'discussion/css/discussion-app.css',
    'discussion/css/vendor/font-awesome.css'
]

def asset_url(name):
    return name if re.match('^(https?:)?//', name) else static(name)

def get_template_dir():
    return TEMPLATE_DIR

def get_js_urls():
    return [asset_url(path) for path in JS_URLS]

def get_css_urls():
    return [asset_url(path) for path in CSS_URLS]

def get_minified_js_urls():
    urls = ['//cdnjs.cloudflare.com/ajax/libs/mathjax/2.4.0/MathJax.js?config=TeX-MML-AM_HTMLorMML-full',
            static('discussion-xblock.{}.min.js'.format(JS_SHA))]
    return urls

# TODO Remove the all following lines, was used for testing as a standalone app.
STATIC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
_template_lookup = TemplateLookup(TEMPLATE_DIR)

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))

# dummy, for testing as a standalone app against a mock server API.
def inline_test(request):
    js_test_deps = '<script type="text/javascript" src="{}"></script>'.format(static('js/vendor/jquery.min.js'))


    return HttpResponse(u"""
    <html>
    <head>
        <title>Inline Test</title>
    {js_test_deps}
    {css_links}
    {js_links}
    </head>
    <body>
    {body}
    {js_body}
    </body>
    </html>
    """.format(
        js_test_deps=js_test_deps,
        css_links=get_css_links(),
        js_links=get_js_links(),
        body=get_inline_body(discussion_id="foo"),
        js_body=get_js_body()
        )
    )

def get_inline_body(discussion_id):
    t = _template_lookup.get_template('discussion/_discussion_module.html')
    return t.render_unicode(discussion_id=discussion_id)

def get_css_links():
    return os.linesep.join('<link rel="stylesheet" type="text/css" href="{}"/>'.format(url) for url in self.get_css_urls())

def get_js_filenames():
    return [pkg_resources.resource_filename('discussion', path) for path in VENDOR_JS_URLS]

def get_js_links():
    return os.linesep.join('<script type="text/javascript" src="{}"/>'.format(url) for url in self.get_js_urls())

def get_js_body():
    js_dir = os.path.join(STATIC_DIR, 'discussion/js')
    js_urls = []
    for root, dirs, filenames in os.walk(js_dir):
        prefix = root[len(STATIC_DIR+1):]
        for filename in filenames:
            if filename.endswith('.js'):
                path = os.path.join(prefix, filename)
                print [root, prefix, filename, path]
                js_urls.append(static(path))
    tags = os.linesep.join('<script type="text/javascript" src="{}"></script>'.format(url) for url in js_urls)
    # moved to discussion_forum... will be deleted anyway
    return tags + os.linesep + render_mustache_templates()
