import os
from file_loader import extract_file

ROOT = "docs"
CATEGORIES = ["characters", "acs", "locations", "events", "lore", "plot_threads", "brainstorming"]

def create_category(category):
    path = os.path.join(ROOT, category)
    os.makedirs(path, exist_ok=True)
    return path

def create_markdown_from_file(category, name, file_path):
    path = create_category(category)
    filename = os.path.join(path, f"{name.replace(' ', '_')}.md")
    content = extract_file(file_path)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {name}\n\n")
        f.write(content)
    print(f"Created from file: {filename}")

def create_index():
    with open(os.path.join(ROOT, "index.md"), "w") as f:
        f.write("# Project Index\n\n")
        for category in CATEGORIES:
            f.write(f"## {category.capitalize()}\n")
            files = os.listdir(os.path.join(ROOT, category))
            for fname in files:
                f.write(f"- [{fname.replace('.md', '').replace('_', ' ')}]({category}/{fname})\n")
            f.write("\n")
    print("Updated: docs/index.md")

if __name__ == "__main__":
    print("Place your files in 'input_files/'.")
    print(f"Supported categories: {', '.join(CATEGORIES)}")
    category = input("Enter category: ")
    name = input("Enter file name (without extension): ")
    ext = input("Enter file extension (docx, pdf, pptx, xlsx, csv, txt): ")
    file_path = f"input_files/{name}.{ext}"
    if os.path.exists(file_path):
        create_markdown_from_file(category, name, file_path)
        create_index()
    else:
        print(f"File {file_path} does not exist.")
