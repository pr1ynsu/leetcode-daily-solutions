import requests
import datetime
import os

# Get today's date
today = datetime.datetime.now().strftime('%Y-%m-%d')

# GraphQL query to get daily question
query = {
    "query": """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        question {
          title
          titleSlug
          difficulty
        }
      }
    }
    """
}

response = requests.post("https://leetcode.com/graphql", json=query)
data = response.json()
question = data['data']['activeDailyCodingChallengeQuestion']['question']

title = question['title']
slug = question['titleSlug']
difficulty = question['difficulty']
url = f"https://leetcode.com/problems/{slug}/"

# Create folder and write file
folder = f"daily/{today}-{slug}"
os.makedirs(folder, exist_ok=True)

with open(f"{folder}/README.md", "w") as f:
    f.write(f"# {title} ({difficulty})\n")
    f.write(f"**Problem Link:** [{url}]({url})\n")

print("✅ Daily question saved to folder.")
