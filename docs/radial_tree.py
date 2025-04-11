import pandas as pd
import json
from pathlib import Path

# Read the CSV data
df = pd.read_csv('data.csv', quoting=pd.io.common.QUOTE_DOUBLE)

def create_tree_dict():
    tree = {"name": "Content", "children": []}
    
    for _, row in df.iterrows():
        # Get values from each row
        l1, l2, l3, l4, l5, l6, title, url, desc = row
        
        # Find or create level 1 node
        l1_node = next((child for child in tree["children"] if child["name"] == l1), None)
        if not l1_node:
            l1_node = {"name": l1, "children": []}
            tree["children"].append(l1_node)
        
        # Find or create level 2 node
        l2_node = next((child for child in l1_node["children"] if child["name"] == l2), None)
        if not l2_node:
            l2_node = {"name": l2, "children": []}
            l1_node["children"].append(l2_node)
        
        # Find or create level 3 node
        l3_node = next((child for child in l2_node["children"] if child["name"] == l3), None)
        if not l3_node:
            l3_node = {"name": l3, "children": []}
            l2_node["children"].append(l3_node)
        
        # Find or create level 4 node
        l4_node = next((child for child in l3_node["children"] if child["name"] == l4), None)
        if not l4_node:
            l4_node = {"name": l4, "children": []}
            l3_node["children"].append(l4_node)
        
        # Find or create level 5 node
        l5_node = next((child for child in l4_node["children"] if child["name"] == l5), None)
        if not l5_node:
            l5_node = {"name": l5, "children": []}
            l4_node["children"].append(l5_node)
        
        # Add level 6 as leaf node with content
        if pd.notna(l6):
            l6_node = {
                "name": l6,
                "content": {
                    "title": title if pd.notna(title) else "",
                    "url": url if pd.notna(url) else "",
                    "description": desc if pd.notna(desc) else ""
                }
            }
            l5_node["children"].append(l6_node)
    
    return tree

# Create the tree data
tree_data = create_tree_dict()

# Save as JSON
with open('docs/tree_data.json', 'w', encoding='utf-8') as f:
    json.dump(tree_data, f, indent=2, ensure_ascii=False)

print("Tree data JSON generated successfully!")