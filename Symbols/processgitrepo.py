from git import Repo
import os

# Step 1: Load repo
# chmod +x /workspaces/cleanslate/Symbols/processgitrepo.py
repo_path = "/workspaces/cleanslate/Symbols/nginx"  # Replace with your repo folder name
repo = Repo(repo_path)

print("Repo loaded successfully!")  # Ensure the repo is loaded

# Step 4: Iterate Over Files
def iterate_files(repo_path):
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path

# Step 5: Assess and Score Files
def assess_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return len(lines)  # Score based on line count
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

# Step 6: Aggregate Scores
def score_repository(repo_path):
    total_score = 0
    for file_path in iterate_files(repo_path):
        file_score = assess_file(file_path)
        print(f"File: {file_path}, Score: {file_score}")
        total_score += file_score
    return total_score

# Calculate total score for the repository
repo_score = score_repository(repo_path)
print(f"Total repository score: {repo_score}")
