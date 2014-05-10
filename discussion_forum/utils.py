# Imports ###########################################################

import os
import pkg_resources

from django.conf import settings
from django.template import Context, Template

from mako.template import Template as MakoTemplate

# Functions #########################################################

def load_resource(resource_path):
    """
    Gets the content of a resource
    """
    resource_content = pkg_resources.resource_string(__name__, resource_path)
    return unicode(resource_content)

def render_template(template_path, context={}):
    """
    Evaluate a template by resource path, applying the provided context
    """
    template_str = load_resource(template_path)
    template = Template(template_str)
    return template.render(Context(context))

def render_mustache_templates(mustache_dir):

    def is_valid_file_name(file_name):
        return file_name.endswith('.mustache')

    def read_file(file_name):
        return open(mustache_dir + '/' + file_name, "r").read().decode('utf-8')

    def template_id_from_file_name(file_name):
        return file_name.rpartition('.')[0]

    def process_mako(template_content):
        return MakoTemplate(template_content).render_unicode()

    def make_script_tag(id, content):
        return u"<script type='text/template' id='{0}'>{1}</script>".format(id, content)

    return u'\n'.join(
        make_script_tag(template_id_from_file_name(file_name), process_mako(read_file(file_name)))
        for file_name in os.listdir(mustache_dir)
        if is_valid_file_name(file_name)
    )

def render_mako_templates(template_dir):
    """
    Render all template files in a directory and return the content. A file is considered a template
    if it starts with '_' and ends with '.html'.
    """

    def is_valid_file_name(file_name):
        return file_name.startswith('_') and file_name.endswith('.html')

    def read_file(file_name):
        return open(template_dir + '/' + file_name, "r").read().decode('utf-8')

    def template_id_from_file_name(file_name):
        return file_name.rpartition('.')[0]

    def process_mako(template_content):
        return MakoTemplate(template_content).render_unicode()

    def make_script_tag(id, content):
        return u"<script type='text/template' id='{0}'>{1}</script>".format(id, content)

    return u'\n'.join(
        make_script_tag(template_id_from_file_name(file_name), process_mako(read_file(file_name)))
        for file_name in os.listdir(template_dir)
        if is_valid_file_name(file_name)
    )

def get_scenarios_from_path(scenarios_path, include_identifier=False):
    """
    Returns an array of (title, xmlcontent) from files contained in a specified directory,
    formatted as expected for the return value of the workbench_scenarios() method
    """
    base_fullpath = os.path.dirname(os.path.realpath(__file__))
    scenarios_fullpath = os.path.join(base_fullpath, scenarios_path)

    scenarios = []
    if os.path.isdir(scenarios_fullpath):
        for template in os.listdir(scenarios_fullpath):
            if not template.endswith('.xml'):
                continue
            identifier = template[:-4]
            title = identifier.replace('_', ' ').title()
            template_path = os.path.join(scenarios_path, template)
            if not include_identifier:
                scenarios.append((title, load_resource(template_path)))
            else:
                scenarios.append((identifier, title, load_resource(template_path)))

    return scenarios

def load_scenarios_from_path(scenarios_path):
    """
    Load all xml files contained in a specified directory, as workbench scenarios
    """
    return get_scenarios_from_path(scenarios_path, include_identifier=True)
