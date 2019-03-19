#! /usr/bin/env python3

from perceval.backends.core.github import GitHub


repo = GitHub(owner='elastic', repository='logstash', api_token='***')
# # fetch all issues and print each title
for issue in repo.fetch():
    print(issue)
