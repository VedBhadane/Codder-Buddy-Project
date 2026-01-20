import os
from langchain_core.tools import tool

# Get the absolute path of the folder where main.py is located
# This ensures we don't accidentally write to a temp folder or System32
BASE_PROJECT_DIR = os.getcwd()
GENERATED_DIR = os.path.join(BASE_PROJECT_DIR, "generated_project")


@tool
def write_file(path: str, content: str):
    """Writes content to a file. Overwrites if exists. Creates directories if needed."""
    try:
        # 1. Ensure the generated_project folder exists
        if not os.path.exists(GENERATED_DIR):
            os.makedirs(GENERATED_DIR)
            print(f"[[DEBUG]] Created directory: {GENERATED_DIR}")

        # 2. Construct the full file path
        # If the agent provides 'generated_project/index.html', fix it to just 'index.html'
        clean_path = path.replace("generated_project/", "").replace("generated_project\\", "")
        full_path = os.path.join(GENERATED_DIR, clean_path)

        # 3. Create subdirectories if needed (e.g. css/style.css)
        file_dir = os.path.dirname(full_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        # 4. Write the file
        print(f"[[DEBUG]] Saving file to: {full_path}")
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully wrote to {clean_path}"

    except Exception as e:
        print(f"[[ERROR]] Failed to write file: {e}")
        return f"Error writing file: {str(e)}"


@tool
def read_file(path: str) -> str:
    """Reads content from a file."""
    try:
        clean_path = path.replace("generated_project/", "").replace("generated_project\\", "")
        full_path = os.path.join(GENERATED_DIR, clean_path)

        if not os.path.exists(full_path):
            return f"Error: File {clean_path} does not exist."

        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def list_files(directory: str = ".") -> str:
    """Lists files in the project folder."""
    try:
        if not os.path.exists(GENERATED_DIR):
            return "No generated_project folder found."

        files_list = []
        for root, _, files in os.walk(GENERATED_DIR):
            for file in files:
                # Show relative path
                rel_path = os.path.relpath(os.path.join(root, file), GENERATED_DIR)
                files_list.append(rel_path)

        return "\n".join(files_list) if files_list else "No files found."
    except Exception as e:
        return f"Error listing files: {str(e)}"


@tool
def get_current_directory() -> str:
    """Returns the current directory."""
    return GENERATED_DIR