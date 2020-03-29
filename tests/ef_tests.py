import json
import yaml
from yaml.scanner import ScannerError
import subprocess
import ci
import global_vars

# def validate_yaml():
#     for f in ci.changed_files:
#         if f.endswith('.yml') or f.endswith('yaml'):
#             with open(f, 'r') as stream:
#                 try:
#                     yaml.safe_load(stream)
#                 except ScannerError as e:
#                     ci.errors[f] = e

def validate_yaml():
    for f in global_vars.changed_files:
        if f.endswith('.yml') or f.endswith('yaml'):
            lint = subprocess.run(["yamllint", "-d relaxed", "--no-warnings", f], capture_output=True)
            try:
                lint.check_returncode()
            except subprocess.CalledProcessError:
                global_vars.errors[f] = lint.stdout.decode("utf-8")


def validate_json():
    for f in global_vars.changed_files:
        if f.endswith('.json'):
            with open(f, 'r') as stream:
                try:
                    json.load(stream)
                except Exception as e:
                    global_vars.errors[f] = e
