from datetime import date
from unittest.mock import patch
from HW4a import get_github_repos, get_github_user_commits_count, get_user_repositories_with_commits
import unittest

def my_brand():
    print("=*=*=*= Eshan Sharma =*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 04a - Develop with the Perspective of the Tester in mind =*=*=*= \n")
    print("=*=*=*=", date.today(), "=*=*=*= \n")

class TestGetGitHubRepos(unittest.TestCase):
    @patch('username.fetch_data_from_github')
    @patch('username.count_commits')
    def test_get_user_repositories_with_commits(self, mock_count_commits, mock_fetch_data_from_github):
        mock_fetch_data_from_github.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]
        mock_count_commits.side_effect = [3, 5]

        result = get_user_repositories_with_commits('testuser')

        self.assertEqual(result, [
            {"Repo": "repo1", "Number of commits": 3},
            {"Repo": "repo2", "Number of commits": 5}
        ])

my_brand()

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
