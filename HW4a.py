from datetime import date
import urllib.request
import json

def my_brand():
    print("=*=*=*= Eshan Sharma =*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 04a - Develop with the Perspective of the Tester in mind =*=*=*= \n")
    print("=*=*=*=", date.today(), "=*=*=*= \n")

def get_github_repos(user_id):
    url = "https://api.github.com/users/" + user_id + "/repos"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

def get_github_user_commits_count(user_id, repo_name):
    url = "https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return len(data)

def get_user_repositories_with_commits(user_id):
    repos = get_github_repos(user_id)
    repo_list = []
    for repo in repos:
        repo_name = repo["name"]
        commits_count = get_github_user_commits_count(user_id, repo_name)
        repo_list.append({"Repo": repo_name, "Number of commits": commits_count})
    return repo_list

userID = input("Enter your GitHub ID: ")
repo_list = get_user_repositories_with_commits(userID)

for repo in repo_list:
    print("Repo: " + repo["Repo"] + " Number of commits: " + str(repo["Number of commits"]))