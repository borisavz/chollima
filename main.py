import os

from textx import metamodel_from_file, generator
from textxjinja import textx_jinja_generator

def transform_names(var):
    return var.name

THIS_FOLDER = os.path.dirname(__file__)

metamodel = metamodel_from_file('chollima.tx')

model = metamodel.model_from_file('test.ext')

context = {
    'entities': []
}

for entity in model.entities:

    context['entities'].append(entity)

template_folder = os.path.join(THIS_FOLDER, 'template')

# Run Jinja generator
textx_jinja_generator('./template', '/home/borisavz/Desktop', context, True, transform_names=transform_names)