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
    repos = response.json()
    star_count = sum(repo['stargazers_count'] for repo in repos if not repo['fork'])
    return star_count

def update_readme(star_count):
    """Updates README.md with the latest star count."""
    with open('README.md', 'r+') as file:
        content = file.read()
        content = re.sub(r'(?<=\bStars from Org:\s)\d+', str(star_count), content)
        file.seek(0)
        file.write(content)
        file.truncate()

if __name__ == "__main__":
    star_count = fetch_stars('sticknet')  # Replace with your organization's name
    update_readme(star_count)
