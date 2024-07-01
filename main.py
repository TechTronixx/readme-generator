from pathlib import Path

def get_project_name():
    return input("Enter the project name: ")

def get_author_name():
    return input("Enter the author name: ")

def get_project_description():
    return input("Enter the project description: ")

def get_additional_features():
    return input("Enter additional features (comma-separated): ")

def get_additional_credits():
    return input("Enter additional credits: ")

def choose_readme_type():
    print("Choose the type of readme you want to generate:")
    print("1. Simple ")
    print("2. Detailed ")
    print("3. Documentation Based ")
    choice = input("Enter your choice (1/2/3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")
    return int(choice)

def generate_table_of_contents(sections):
    table_of_contents = []
    for section in sections:
        section_title = section.split("## ")[1]
        table_of_contents.append(f"- [{section_title}](#{section_title.lower().replace(' ', '-')})")
    return table_of_contents

def write_readme(project_name, author_name, description, features, credits, sections, table_of_contents, readme_type):
    if readme_type == 1:  # Simple README
        content = [
            f"# {project_name}",
            description,
            "\n",
            "## Table of Contents",
            "\n",
            "\n".join(table_of_contents)
        ]
    elif readme_type == 2:  # Detailed README
        content = [
            f"# {project_name}",
            description,
            "\n",
            "## Table of Contents",
            "\n",
            "\n".join(table_of_contents),
            "\n",
            f"## Features\n{features}",
            f"## Credits\n{credits}"
        ]
    elif readme_type == 3:  # Documentation README
        content = [
            f"# {project_name} Documentation",
            "\n",
            "## Introduction",
            description,
            "\n",
            "## Features",
            f"\n{features}",
            "\n",
            "## Installation",
            "Provide installation instructions here.",
            "\n",
            "## Usage",
            "Provide usage examples and instructions here.",
            "\n",
            "## Tech Used",
            f"\n{features}",
            "\n",
            "## Credits",
            f"\n{credits}"
        ]
    
    readme_path = Path("README.md")
    with readme_path.open("w") as readme:
        readme.write("\n\n".join(content))

def main():
    project_name = get_project_name()
    author_name = get_author_name()
    project_description = get_project_description()
    additional_features = get_additional_features()
    additional_credits = get_additional_credits()
    
    readme_type = choose_readme_type()
    
    sections = [
        "## Description",
        "## Features",
        "## Demo",
        "## Install",
        "## Tech Used",
        "## Credits"
    ]
    table_of_contents = generate_table_of_contents(sections)
    
    write_readme(project_name, author_name, project_description, additional_features, additional_credits, sections, table_of_contents, readme_type)
    print(f"README.md has been generated.")

if __name__ == "__main__":
    main()
