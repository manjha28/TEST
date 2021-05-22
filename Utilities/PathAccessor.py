import os

def get_json_path(filename, verbose=False):
    if verbose:
        print("Working directory of project ", os.getcwd())
    json_path = '../JSON'
    re_path = os.path.relpath(json_path, os.getcwd())
    path = os.path.join(re_path, filename)
    if verbose:
        print(re_path)
        print("Final JSON path", path)
    return path

def get_yml_path(filename,verbose=False):
    if verbose:
        print("Working directory of project ", os.getcwd())
    yml_path = '../Dependencies'
    re_path = os.path.relpath(yml_path, os.getcwd())
    path = os.path.join(re_path, filename)
    if verbose:
        print(re_path)
        print("Final YAML path", path)
    return path