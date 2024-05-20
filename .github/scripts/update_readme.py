import os
import re
import requests

def fetch_stars(organization):
    """Fetches stars for all repos in the given organization."""
    headers = {
        'Authorization': f'token {os.getenv("API_TOKEN")}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(f'https://api.github.com/orgs/{organization}/repos', headers=headers)
    if response.status_code == 200:
        repos = response.json()
        if isinstance(repos, list):  # Ensure that repos is a list
            star_count = sum(repo['stargazers_count'] for repo in repos if not repo['fork'])
        else:
            print(f"Unexpected data type: {type(repos)}")
            star_count = 0
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print("Response:", response.text)  # Log the actual response to see what went wrong
        star_count = 0
    return star_count

def update_readme(star_count):
    """Updates README.md with the latest star count."""
    with open('README.md', 'r+') as file:
        # content = file.read()
        # content = re.sub(r'(Test\(S\):\s)\d*', r'\g<1>' + str(star_count), content)
        file.seek(0)
        file.write(f"\nTest: {star_count}")
        file.truncate()

if __name__ == "__main__":
    star_count = fetch_stars('sticknet')  # Replace with your organization's name
    update_readme(star_count)
