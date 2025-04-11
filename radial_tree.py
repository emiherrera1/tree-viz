import pandas as pd
import json
from pathlib import Path
import csv

def create_tree_dict():
    tree = {"name": "Content", "children": []}
    
    # Read the CSV data with explicit CSV reader
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip header
        header = next(reader)
        # Read all rows
        rows = list(reader)

    # Convert to DataFrame with explicit column names
    df = pd.DataFrame(rows, columns=[
        "Level 1 Sector",
        "Level 2 Category",
        "Level 3 Niche",
        "Level 4 Sub-Niche",
        "Level 5 Micro-Niche",
        "Level 6 Content Example",
        "Video Title"
    ])
    
    for _, row in df.iterrows():
        # Get values from each row
        l1 = row["Level 1 Sector"]
        l2 = row["Level 2 Category"]
        l3 = row["Level 3 Niche"]
        l4 = row["Level 4 Sub-Niche"]
        l5 = row["Level 5 Micro-Niche"]
        l6 = row["Level 6 Content Example"]
        title = row["Video Title"]
        
        # Process only if we have valid data
        if pd.isna(l1) or pd.isna(l2) or pd.isna(l3) or pd.isna(l4) or pd.isna(l5):
            continue
            
        # Create or get level 1 node
        l1_node = next((child for child in tree["children"] if child["name"] == l1), None)
        if not l1_node:
            l1_node = {"name": l1, "children": []}
            tree["children"].append(l1_node)
            
        # Create or get level 2 node
        l2_node = next((child for child in l1_node["children"] if child["name"] == l2), None)
        if not l2_node:
            l2_node = {"name": l2, "children": []}
            l1_node["children"].append(l2_node)
            
        # Create or get level 3 node
        l3_node = next((child for child in l2_node["children"] if child["name"] == l3), None)
        if not l3_node:
            l3_node = {"name": l3, "children": []}
            l2_node["children"].append(l3_node)
            
        # Create or get level 4 node
        l4_node = next((child for child in l3_node["children"] if child["name"] == l4), None)
        if not l4_node:
            l4_node = {"name": l4, "children": []}
            l3_node["children"].append(l4_node)
            
        # Create or get level 5 node
        l5_node = next((child for child in l4_node["children"] if child["name"] == l5), None)
        if not l5_node:
            l5_node = {"name": l5, "children": []}
            l4_node["children"].append(l5_node)
            
        # Add level 6 as leaf node with content (only if it exists)
        if pd.notna(l6) and pd.notna(title):
            l6_node = {
                "name": l6,
                "content": {
                    "title": title,
                    "type": "video"
                }
            }
            l5_node["children"].append(l6_node)
    
    return tree

# Create the tree data
tree_data = create_tree_dict()

# Save as JSON with proper formatting
with open('docs/tree_data.json', 'w', encoding='utf-8') as f:
    json.dump(tree_data, f, indent=2, ensure_ascii=False)

print("Tree data JSON generated successfully!")