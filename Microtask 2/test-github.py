#! /usr/bin/env python3

from perceval.backends.core.github import GitHub


repo = GitHub(owner='elastic', repository='logstash', api_token='61d317d94b4b93e654c1efcf0ffe68ffab95134e')
# # fetch all issues and print each title
for issue in repo.fetch():
    print(issue)