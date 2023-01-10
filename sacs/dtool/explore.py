
import re
import dtool_lookup_api.nested  as dl
from pprint import pprint
from ruamel.yaml import YAML
from ..utilities import fopen
default_backend = "s3://frct-simdata/"



# Example of use of the depency graph see also: https://github.com/IMTEK-Simulation/code-snippets/commit/44dd8585c09444514876c40c7843a5e694975040
def get_child_uuids_names(uuid):
    graph = dl.graph(uuid)
    return {entry['uuid']:entry["name"] for entry in graph if uuid in entry['derived_from'] }

def get_child_uuids(uuid):
    """
    get direct_child_uuids
    """
    graph = dl.graph(uuid)
    return [entry['uuid'] for entry in graph if uuid in entry['derived_from']]


def get_parent_uuids(uuid=None,uri=None,readme=None):
    if readme is None:
        try :
            readme = get_readme_dict(uuid=uuid,uri=uri)
        except Exception as err:
            print(f"Cannot obtain readme for uuid {uuid}")
            print(err)
            return set()
    else:
        yml = YAML()
        readme = yml.load(readme)

    try:
        uuids = set()
        try :
            uuids.update({i["uuid"] for i in readme["derived_from"]})
        except KeyError:
            pass
        try :
            uuids.update({readme["warmstart"]["uuid"]})
        except KeyError:
            pass
    except Exception as err:
        print(f"problem with uuid {uuid}")
        print("README #########################")
        pprint(readme)
        print("ERROR #########################")
        print(err)
    return uuids

def get_ancestor_uuids(uuid=None,uri=None):

    uuids_level1 = get_parent_uuids(uri=uri, uuid=uuid)
    uuids = uuids_level1.copy()
    for uuid in uuids_level1:
        uuids.update(get_ancestor_uuids(uuid=uuid))
    return uuids

def get_readme_dict(uuid=None, uri=None, dataset=None):
    if uuid:
        uri = default_backend + uuid
    if uri:
        return dl.readme(uri)

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

# useful in a grep command
UUID_v4_REGEX = '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}'
def extract_uuids_in_file(file, verbose=False):
    """
    Matches all uuids in the file based on their formatting

    Returns :
    ---------
    uuids : list of uuids
    """
    if verbose:
        log = print
    else:
        def log(*args):
            pass
    uuids = []
    with fopen(file, "r") as file:
        for line in file.readlines():
            result = re.search(UUID_v4_REGEX, line)
            if result is not None:
                log(line)
                uuids.append(result.group())
        return uuids
