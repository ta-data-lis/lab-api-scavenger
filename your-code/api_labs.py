import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import numpy as np
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',100)


#token b67099f8dd152199dd77fd0f064def9418e613e4

url_repo = "https://api.github.com/repos/ironhack-datalabs/datalis0819/forks"
auth = HTTPBasicAuth('guillaume-aubert','b67099f8dd152199dd77fd0f064def9418e613e4')

response_repo = requests.get(url_repo, auth = auth)
response_repo_json=response_repo.json()
df_repo = pd.DataFrame(response_repo_json)

print(df_repo.columns)

#list of forks:
df_repo['full_name']

# 0               edxz7/datalis0819
# 1          Mariana427/datalis0819
# 2      EvelienDonkers/datalis0819
# 3         ta-data-lis/datalis0819
# 4                Inrx/datalis0819
# 5     filipamiralopes/datalis0819
# 6         janpotthoff/datalis0819
# 7         sofia-sousa/datalis0819
# 8               naivm/datalis0819
# 9            LindaRit/datalis0819
# 10          Ana-Andre/datalis0819
# 11         alonasorochynska/data2
# 12      carlarsmendes/datalis0819

#print languages:
print(set(df_repo['language']))
#{'Jupyter Notebook', None}

url_mysql = "https://api.github.com/repos/guillaume-aubert/lab-mysql-first-queries/commits?since=2020-07-01T15:31:51Z"

response_mysql = requests.get(url_mysql, auth = auth)
response_mysql_json=response_mysql.json()
df_mysql = pd.DataFrame(response_mysql_json)
df_normalize =  pd.json_normalize(response_mysql_json)

df= pd.DataFrame(df_normalize)

number_commit=df[['commit.author.name','commit.author.date']]
print(number_commit)

#  commit.author.name    commit.author.date
# 0   Guillaume Aubert  2020-07-06T16:14:11Z


#### How many commits I performed?

url_repos_gui = "https://api.github.com/users/guillaume-aubert/repos"

response_url_repos_gui = requests.get(url_repos_gui, auth = auth)
commits_gau_json=response_url_repos_gui.json()
df_commits_gau = pd.DataFrame(commits_gau_json)
df_normalize_commits_gau =  pd.json_normalize(commits_gau_json)

list_url = set(df_normalize_commits_gau['commits_url'])
list_url = [words[:-6] for words in list_url]

#adding time to retrieve only the last commit
#list_url = [words+"?since=2020-03-10T00:00:00Z" for words in list_url]
print(list_url)


def loop_url(list_url):
    number_commit = pd.DataFrame(['commit.author.name', 'commit.author.date'])
    for x in list_url:
        url_mysql = x
        response_mysql = requests.get(url_mysql, auth=auth)
        response_mysql_json = response_mysql.json()
        df_mysql = pd.DataFrame(response_mysql_json)
        df_normalize = pd.json_normalize(response_mysql_json)
        df = pd.DataFrame(df_normalize)
        number_commit = pd.concat([number_commit, df], ignore_index=True, sort=False)
    return number_commit[['commit.author.name', 'commit.author.date']].dropna()

#loop_url(list_url)

all_commits = loop_url(list_url)
conditions = all_commits['commit.author.name'] == 'Guillaume Aubert'
total_commits=all_commits[conditions]
total_commits_counts = len(total_commits.index) + 1

print ("The number of commits made by Guillaume is", total_commits_counts)

print(number_commit)


url_test='https://api.github.com/repos/guillaume-aubert/lab-lambda-functions/commits?since=2020-03-10T00:00:00Z'

response_mysql = requests.get(url_test, auth = auth)
response_mysql_json=response_mysql.json()
df_mysql = pd.DataFrame(response_mysql_json)
df_normalize =  pd.json_normalize(response_mysql_json)

df= pd.DataFrame(df_normalize)

#number_commit=df[['commit.author.name','commit.author.date']]
print(response_mysql)