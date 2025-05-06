from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))

user_info = notion.users.list()
print("✅ Connected to Notion! Users:", user_info)
