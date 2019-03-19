#! /usr/bin/env python3
from perceval.backends.core.git import Git
# URL for the git repo to analyze
repo_url = 'https://github.com/chaoss/grimoirelab-perceval'
# directory for letting Perceval clone the git repo
repo_dir = 'users/tanxin/github/perceval.git'
# Git object, pointing to repo_url and repo_dir for cloning
repo = Git(uri=repo_url , gitpath=repo_dir)
# fetch all commits and print each author
for commit in repo.fetch():
    print(commit['data']['Author'])
