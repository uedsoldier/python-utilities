import yaml
import io
from termcolor import colored

def yaml_to_dict(yaml_file):
    try:
        # Read YAML file
        with open(yaml_file, 'r') as stream:
            return yaml.safe_load(stream)
    except Exception as e:
        print(colored(e,'red'))

def dict_to_yaml(dict,yaml_file):
    try:
        # Write YAML file
        with io.open(yaml_file, 'w', encoding='utf8') as outfile:
            yaml.dump(dict, outfile, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        print(colored(e,'red'))
    