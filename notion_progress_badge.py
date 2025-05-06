import requests
import os

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DB_ID"]
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def fetch_tasks():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS)
    data = response.json()
    
    total = len(data["results"])
    completed = sum(1 for task in data["results"] if task["properties"]["Status"]["select"]["name"] == "Complete")
    return completed, total

def generate_badge(completed, total):
    percent = int((completed / total) * 100) if total > 0 else 0
    badge = f"![Progress](https://img.shields.io/badge/Progress-{percent}%25-brightgreen)"
    
    with open("README.md", "r") as f:
        content = f.read()
    
    new_content = content.replace(
        "![Progress](https://img.shields.io/badge/Progress-PLACEHOLDER-brightgreen)", 
        badge
    )

    with open("README.md", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    done, total = fetch_tasks()
    generate_badge(done, total)
