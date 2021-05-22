import yaml
import pprint as pp
from Utilities import PathAccessor as pa
with open(pa.get_yml_path('config.yml'), 'r') as f:
    parse_yml = yaml.safe_load(f)

pp.pprint(parse_yml['person']['likes'])