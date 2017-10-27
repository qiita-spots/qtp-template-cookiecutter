# -----------------------------------------------------------------------------
# Copyright (c) {% now 'local', '%Y' %}, {{cookiecutter.author}}.
#
# Distributed under the terms of the {{cookiecutter.license}} License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from qiita_client import QiitaTypePlugin, QiitaArtifactType

from .validate import validate
from .summary import generate_html_summary

# TODO:  Define the supported artifact types
# Here is an example on how to create a type
# artifact_types = [
#     QiitaArtifactType('BIOM', 'BIOM table', False, False,
#                       [('biom', True), ('directory', False), ('log', False),
#                        ('preprocessed_fasta', False)])]
# Below is the API of the QiitaArtifactType class:
# QiitaArtifactType(TYPE_NAME, TYPE_DESCRIPTION, CAN_BE_SUBMITED_TO_EBI,
#                   CAN_BE_SUBMITED_TO_VAMPS, LIST_OF_ACCEPTED_FILEPATH_TYPES)
# Where the list of accepted filepaths is a list of 2-tuples in which the
# first element of the tuple is the filepath type and the seconf element
# is a boolean indicating if the filepath type is required to successfully
# create an artifact of the given type

# Initialize the plugin
plugin = QiitaTypePlugin('{{cookiecutter.project_name}} type', '0.0.1',
                         'Qiita Type Plugin: {{cookiecutter.project_name}}',
                         validate, generate_html_summary,
                         artifact_types)
