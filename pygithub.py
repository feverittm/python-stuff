from github import Github
import os
from pprint import pprint

# Github API documents on Pull Request information:
# https://developer.github.com/v3/pulls/comments/#list-comments-in-a-repository

# Authentication is via github user name and an associated access key
#
# in our case the 'owner' is the owning github bucket: cirrostratus
# and the 'repo' is the name of the repository: dbt_idst

# curl -u floyd-moore:cdca1de00a6d839082d99eb69423f6e217f544c6 https://github.azc.ext.hp.com/api/v3/orgs/cirrostratus/repos
# curl -u floyd-moore:cdca1de00a6d839082d99eb69423f6e217f544c6 https://github.azc.ext.hp.com/api/v3/repos/cirrostratus/dbt_idst/pulls/135/comments

# Github Enterprise with custom hostname
token = os.environ.get('GITHUB_TOKEN')

g = Github(base_url="https://github.azc.ext.hp.com/api/v3", login_or_token=token)

repo = g.get_repo("cirrostratus/dbt_idst")
pr = repo.get_pull(149)
print(pr.number, pr.title)
for cmt in pr.get_issue_comments():
    pprint(cmt)

#branches = repo.get_branches()
#for br in branches:
#    pprint(br)
#branch = repo.get_branch(branch="feature/pbdps-43326")
#pprint(branch)
