#! /usr/bin/env python3
from flake8.api import legacy as flake8
from graal.graal import GraalRepository
from perceval.backends.core.git import Git
import random

repo_url = input("Enter url: ")
repo_dir = input("Enter dir: ")
worktree_path = input("Enter worktree path: ")
# Git object, pointing to repo_url and repo_dir for cloning
ggit = Git(uri=repo_url , gitpath=repo_dir)

# clone the repository (if it doesn't exist locally)
ggit.fetch_items(category='commit')

commits = list(ggit.fetch())
# hash of random commit
commit = random.choice(commits)
_hash = commit['data']['commit']
print(_hash)
# or input the hash of certain commit
# _hash = input("Enter hash: ")

gral_repo = GraalRepository(uri=repo_url, dirpath=repo_dir)

gral_repo.worktree(worktree_path)
# checkout the commit
gral_repo.checkout(_hash)
style_guide = flake8.get_style_guide()
files = worktree_path
# generate report by flake8
report = style_guide.check_files([files])
print(report.get_statistics(('E', 'W', 'F')))
print(report.total_errors)

# repo_url = https://github.com/chaoss/grimoirelab-perceval
# repo_dir = git/grimoirelab-perceval.git
# worktree_path = "/Users/tanxin/PycharmProjects/git"
