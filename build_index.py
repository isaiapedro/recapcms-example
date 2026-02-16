import os
import json

# Configuration
CONTENT_DIR = 'content/portfolio'
OUTPUT_FILE = 'portfolio.json'

data = []

print(f"🚀 Starting ETL process on {CONTENT_DIR}...")

# 1. Loop through all Markdown files created by CMS
if os.path.exists(CONTENT_DIR):
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CONTENT_DIR, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 2. Simple Parsing (Extracting YAML Frontmatter)
                # We look for lines starting with "title:" and "image:"
                entry = {}
                try:
                    for line in content.split('\n'):
                        if line.startswith("title:"):
                            entry['title'] = line.replace("title:", "").strip().strip('"')
                        elif line.startswith("image:"):
                            entry['image'] = line.replace("image:", "").strip().strip('"')
                            
                    if 'image' in entry:
                        data.append(entry)
                        print(f"  -> Processed: {entry.get('title', 'Untitled')}")
                except Exception as e:
                    print(f"  x Error parsing {filename}: {e}")
else:
    print(f"⚠️ Warning: Directory {CONTENT_DIR} not found. Did you create a collection yet?")

# 3. Save as JSON
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"✅ Success! Generated {OUTPUT_FILE} with {len(data)} items.")