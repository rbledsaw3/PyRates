import os

def get_file_path(relative_path: str) -> str:
    """
    Get the absolute path to a file given its relative path from the project root.

    Args:
        relative_path(str): The relative path to the file from the project root.

    Returns:
        str: The absolute path to the file.

    Raises:
        TypeError: If the relative path is not a string.
    """

    if not isinstance(relative_path, str):
        raise TypeError("The relative path must be a string")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    return os.path.join(project_root, relative_path)
