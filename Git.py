import streamlit as st
import git

# Specify the remote URL of the repository
remote_url = 'https://github.com/suhashstudy/Git_task.git'

# Make a request to the Git API
response = requests.get(remote_url + '/api/v4/projects/1/branches')

# Parse the JSON response
branches = response.json()

# Display the list of branches in Streamlit
st.header('Git Branches')
for branch in branches:
    st.write(branch['name'])



