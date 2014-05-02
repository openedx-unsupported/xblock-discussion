# Imports ###########################################################

import os
import pkg_resources

from django.template import Context, Template


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
