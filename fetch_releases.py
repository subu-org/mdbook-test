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

# Print the release information
print(f"Latest Release: {release_name}")
print(f"Tag: {release_tag}")
print(f"URL: {release_url}")

# Read the template file
with open("theme/index-TEMPLATE.hbs", "r") as template_file:
    template_content = template_file.read()

# Replace the placeholder with the latest release version
updated_content = template_content.replace("RELEASE_VERSION", release_tag)

# Write the updated content to the new index.hbs file
with open("theme/index.hbs", "w") as output_file:
    output_file.write(updated_content)
