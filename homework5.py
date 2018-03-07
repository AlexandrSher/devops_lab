#!/bin/python
'''homework3'''
# pylint: disable= invalid-name

import argparse
import getpass
import requests

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-a", "--a", action="store_true",
                    help='Author of repository')
parser.add_argument("-n", "--n", action="store_true",
                    help="Files/dir name in repository")
parser.add_argument("-c", "--c", action="store_true",
                    help='Commits message of repository')
parser.add_argument("-b", "--b", action="store_true",
                    help='Branches name of repository')
parser.add_argument("-p", "--p", action="store_true",
                    help='Pull request of repository')
parser.add_argument("-cm", "--cm", action="store_true", help='All comments')
parser.add_argument("user", help='GitHub username')
parser.add_argument("repo", help='GitHub Repository')
args = parser.parse_args()
user = args.user
repo = args.repo
pass_wd = getpass.getpass("Enter passwd:")
key1 = ''
key2 = ''
key3 = ''
key4 = ''
url = ''
i = 0

if args.a:
    key1 = 'author'
    key2 = 'login'
    url = "https://api.github.com/repos/" + repo + "/stats/contributors"
elif args.n:
    key1 = 'name'
    url = "https://api.github.com/repos/" + repo + "/contents"
elif args.c:
    key1 = 'commit'
    key2 = 'message'
    url = "https://api.github.com/repos/" + repo + "/commits"
elif args.b:
    key1 = 'name'
    url = "https://api.github.com/repos/" + repo + "/branches"
elif args.cm:
    key1 = 'body'
    url = "https://api.github.com/repos/" + repo + "/comments"
elif args.p:
    key1 = 'head'
    key2 = 'user'
    key3 = 'login'
    url = "https://api.github.com/repos/" + repo + "/pulls?&per_page=100"

response = requests.get(url, auth=(user, pass_wd))


try:
    while True:
        if not key1:
            print(response.json()[i])
        elif not key2:
            print(response.json()[i].get(key1))
        elif not key3:
            print(response.json()[i].get(key1).get(key2))
        elif not key4:
            print(response.json()[i].get(key1).get(key2).get(key3))
        i += 1

except Exception:  # pylint: disable=broad-except
    pass

