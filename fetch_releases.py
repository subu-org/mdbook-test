import requests

# Replace with your GitHub repository details
repo_owner = "subu-org"
repo_name = "mdbook-test"

# Fetch the latest release
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
response = requests.get(url)
release_data = response.json()

# Check if 'name' key exists in the response
if 'name' in release_data:
    release_name = release_data['name']
else:
    release_name = "Unknown Release"

# Extract relevant information
release_tag = release_data.get("tag_name", "Unknown Tag")
release_url = release_data.get("html_url", "#")
release_date = release_data.get("published_at", "").split("T")[0]  # Format date

# Create a Markdown string for the release
release_markdown = f"- **Latest Release: [{release_name} ({release_tag})]({release_url})** - {release_date}\n"

# Read the existing SUMMARY.md
with open("src/SUMMARY.md", "r") as file:
    summary_content = file.read()

# Insert the release information at the top of SUMMARY.md
updated_summary = f"# Summary\n\n{release_markdown}\n{summary_content.split('# Summary', 1)[-1]}"

# Write the updated content back to SUMMARY.md
with open("src/SUMMARY.md", "w") as file:
    file.write(updated_summary)
