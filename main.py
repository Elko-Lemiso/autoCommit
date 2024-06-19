import os
from datetime import datetime, timedelta

# Configure the repository
repo_path = "/home/pluto/projects/autoCommit"
os.chdir(repo_path)

# Commit message
commit_message = "Automated commit"

# Start date
start_date = datetime(2024, 6, 19) 

pattern = [
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
]


for row in range(len(pattern)):
    for col in range(len(pattern[row])):
        if pattern[row][col] == 1:
            # Calculate the date for each commit
            commit_date = start_date + timedelta(days=row*7 + col)
            
            # Format the date for the GIT_COMMITTER_DATE environment variable
            formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

            # Create a dummy file to commit
            file_name = f"dummy_{row}_{col}.txt"
            with open(file_name, "w") as file:
                file.write("This is a dummy commit\n")

            # Add and commit the file with the specified date
            os.system(f'git add {file_name}')
            os.system(f'GIT_COMMITTER_DATE="{formatted_date}" git commit -m "{commit_message}" --date="{formatted_date}"')

# Push the commits to the remote repository
os.system('git push origin main')  # Adjust the branch name if needed