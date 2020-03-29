from git import Repo
import os

repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
repo = Repo(repo_path)

# Read by all tests
changed_files = [item.a_path for item in repo.index.diff('master')]

# Dict of all errors returned by tests (key=file, value=err)
# This is to defer raising any errors until all tests are executed.
errors = {}
