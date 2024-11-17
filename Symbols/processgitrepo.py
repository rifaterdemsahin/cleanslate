from git import Repo

# Load repo
repo_path = "nginx"  # Replace with your repo folder name
repo = Repo(repo_path)

print("Repo loaded successfully!")  # Ensure the repo is loaded