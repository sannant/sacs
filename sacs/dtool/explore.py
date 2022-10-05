
import dtool_lookup_api.nested  as dl

def get_child_uuids_names(uuid):
    graph = dl.graph(uuid)
    return {entry['uuid']:entry["name"] for entry in graph if uuid in entry['derived_from'] }

def get_readme_dict(uuid):
    # TODO: heuristics to give options to provide uuid, uri etc...
    return dl.readme(default_backend + uuid)

def summarize_readme(readme_path=None,
                     readme_string=None,
                     readme_dict=None,
                     uuid=None,
                     uri=None,
                     keys=['project'],
                    ):

    if uuid:
        uri = default_backend + uuid
    if uri:
        readme_dict = dl.readme(uri)
        # dictionary

    # TODO: other initialisation options

    key_values = {}
    for keystring in keys:
        # Navigate down the nested hierarchy
        item = readme_dict
        for key in keystring.split("."):
            item = item[key]

        key_values.update({ keystring : item})

    return key_values
