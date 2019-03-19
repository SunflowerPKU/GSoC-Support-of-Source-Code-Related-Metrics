#! /usr/bin/env python3
import sys
import requests

# input the url of the target GitHub repository
origin_url = input("Enter origin url: ")
repo_url = 'https://archive.softwareheritage.org/api/1/origin/git/url/'+origin_url+'/'
# get a webpage
r = requests.get(repo_url)
repo_dic = r.json()
# do not find the target repository
if 'exception' in repo_dic:
    print('The repository is not available on SoftwareHeritage.')
else:
    # print the date of the last visit
    url_visit = repo_dic['origin_visits_url']
    url_visit = 'https://archive.softwareheritage.org' + url_visit
    web_visit = requests.get(url_visit)
    visit = web_visit.json()
    print(visit[0]['date'])
