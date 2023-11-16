import streamlit as st
import git

# Initialize the git repository
repo = git.Repo('.')

# Get a list of all branches
branches = repo.heads

# Display the list of branches in Streamlit
st.header('Git Branches')
if branches is not None:
    selected_branch = st.selectbox("Select Git Branch", branches)
    st.success(f"Selected branch: {selected_branch}")
