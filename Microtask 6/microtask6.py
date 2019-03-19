#! /usr/bin/env python3
from graal.backends.core.cocom import CoCom
from graal.backends.core.colic import CoLic
SCANCODE = 'scancode'
CATEGORY_COLIC_SCANCODE = 'code_license_' + SCANCODE

# URL for the git repo to analyze
repo_uri = 'https://github.com/chaoss/grimoirelab-toolkit'

# directory where to mirror the repo
repo_dir = 'users/tanxin/github/graal-cocom'

# Cocom object initialization
cc = CoCom(uri=repo_uri, git_path=repo_dir)

# CoLic object initialization
cl = CoLic(uri=repo_uri, git_path=repo_dir, exec_path='/Users/tanxin/Downloads/scancode-toolkit-3.0.2/scancode')

# fetch all commits and try Cocom
for commit in cc.fetch():
    print(commit)
###
# fetch all commits and try scancode
for commit in cl.fetch(category=CATEGORY_COLIC_SCANCODE):
    print(commit)
###

