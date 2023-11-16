import streamlit as st
import git

# Specify the remote URL of the repository
remote_url = 'https://github.com/suhashstudy/Git_task.git'

# Initialize the git repository from the remote URL
repo = git.Repo.clone_from(remote_url, temp_dir=True)

# Get a list of all branches
branches = repo.heads

# Display the list of branches in Streamlit
st.header('Git Branches')
for branch in branches:
    st.write(branch.name)
