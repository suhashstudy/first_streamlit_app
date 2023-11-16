import streamlit as st
import requests

def get_github_branches(username, repository, token):
    # Construct the API URL for branches
    url = f'https://api.github.com/repos/{username}/{repository}/branches'

    # Set the Authorization header with the PAT
    headers = {'Authorization': f'token {token}'}

    # Make a GET request to the GitHub API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and return the list of branches
        branches = [branch['name'] for branch in response.json()]
        return branches
    elif response.status_code == 404:
        st.error("Repository not found. Please check the username and repository name.")
    else:
        st.error(f"Failed to retrieve branches. Status code: {response.status_code}")
        st.error(f"Response content: {response.content.decode('utf-8')}")
        return None

# Replace these values with your GitHub username, repository, and personal access token
github_username = 'suhashstudy'
github_repository = 'Git_task'
github_token = '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'

branches = get_github_branches(github_username, github_repository, github_token)

if branches is not None:
    st.success(f"Branches in {github_repository}: {branches}")
