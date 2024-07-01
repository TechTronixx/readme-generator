from pathlib import Path

def get_project_name():
    return input("Enter the project name: ")

def get_author_name():
    return input("Enter the author name: ")

def get_project_description():
    return input("Enter the project description: ")

def get_additional_features():
    features = input("Enter additional features, separated by commas: ")
    bullet_choice = input("Do you want to display features as bullet points? (y/n): ").lower()
    if bullet_choice == 'y':
        features_list = features.split(',')
        bullet_points = "\n".join([f"- {feature.strip()}" for feature in features_list])
        return bullet_points
    else:
        return features

def get_additional_credits():
    return input("Enter additional credits: ")

def get_technologies_used():
    technologies = input("Enter technologies used in the project (comma-separated): ")
    bullet_points = "\n".join([f"- {tech.strip()}" for tech in technologies.split(',')])
    return bullet_points

def choose_readme_type():
    print("Choose the type of README you want to generate:")
    print("1. Simple: Ideal for small projects or quick overviews. Provides a concise structure focusing on project essentials.")
    print("2. Detailed: Suitable for medium-sized projects. Includes comprehensive sections on features and credits, offering a more detailed overview.")
    print("3. Documentation: Best for large or complex projects. Offers extensive documentation including installation instructions, usage examples, technology stack details, and credits.")
    
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

def write_readme(project_name, author_name, description, features, credits, technologies, sections, table_of_contents, readme_type):
    if readme_type == 1:  # Simple README
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
            "## Demo",
            "Provide demo details.",
            "\n",
            "## Tech Used",
            f"\n{technologies}",
            "\n",
            "## Credits",
            f"\n{credits}"
        ]
    
    readme_path = Path("README.md")
    with readme_path.open("w") as readme:
        readme.write("\n".join(content).strip() + "\n")
    print(f"README.md has been generated! Feel free to edit as needed.")

def main():
    project_name = get_project_name()
    author_name = get_author_name()
    project_description = get_project_description()
    additional_features = get_additional_features()
    additional_credits = get_additional_credits()
    technologies_used = get_technologies_used()  # Added
    
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
    
    write_readme(project_name, author_name, project_description, additional_features, additional_credits, technologies_used, sections, table_of_contents, readme_type)

if __name__ == "__main__":
    main()
