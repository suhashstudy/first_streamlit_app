import requests

def get_github_branches(username, repository, token):
    url = f'https://api.github.com/repos/{username}/{repository}/branches'

    headers = {'Authorization': f'bearer {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        branches = [branch['name'] for branch in response.json()]
        return branches
    elif response.status_code == 404:
        print("Repository not found")
    else:
        print(f"Status code: {response.status_code}")
        return None

def get_github_folders(username, repository, branch, token):
    url = f'https://api.github.com/repos/{username}/{repository}/contents?ref={branch}'

    headers = {'Authorization': f'bearer {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        folders = [content['name'] for content in response.json() if content['type'] == 'dir']
        return folders
    elif response.status_code == 404:
        print("Folder not found")
    else:
        print(f"Status code: {response.status_code}")
        return None

def get_github_files(username, repository, branch, folder, token):
    url = f'https://api.github.com/repos/{username}/{repository}/contents/{folder}?ref={branch}'

    headers = {'Authorization': f'bearer {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = [content['name'] for content in response.json() if content['type'] == 'file']
        return files
    elif response.status_code == 404:
        print("Files not found")
    else:
        print(f"Status code: {response.status_code}")
        return None

def get_file_content(username, repository, branch, folder, file_name, token):
    url = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{folder}/{file_name}'

    headers = {'Authorization': f'bearer {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        print("File not found.")
    else:
        print(f"Status code: {response.status_code}")
        return None

github_username = 'suhashstudy'
github_repository = 'Git_task'
github_token = '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'

branches = get_github_branches(github_username, github_repository, github_token)

if branches is not None:
    print(f"Branches in {github_repository}: {branches}")

    selected_branch = input("Enter the branch name: ")

    folders = get_github_folders(github_username, github_repository, selected_branch, github_token)

    if folders is not None:
        print(f"Folders in {github_repository}/{selected_branch}: {folders}")

        selected_folder = input("Enter the folder name: ")

        files = get_github_files(github_username, github_repository, selected_branch, selected_folder, github_token)

        if files is not None:
            print(f"Files in {github_repository}/{selected_branch}/{selected_folder}: {files}")

            selected_file = input("Enter the file name: ")

            file_content = get_file_content(github_username, github_repository, selected_branch, selected_folder, selected_file, github_token)

            if file_content is not None:
                print(f"Content of {github_repository}/{selected_branch}/{selected_folder}/{selected_file}:\n{file_content}")
