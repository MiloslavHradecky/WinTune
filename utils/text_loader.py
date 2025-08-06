from utils.resources import resource_path

def get_description(module_name: str) -> str:
    """
    Loads textual description for the given module from assets/descriptions.

    Args:
        module_name (str): Name of the module (e.g. 'services', 'network')

    Returns:
        str: Content of the description file, or default message if not found.
    """
    try:
        file_path = resource_path(f"view/assets/descriptions/{module_name}.txt")
        with open(file_path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[!] Popis pro modul '{module_name}' nebyl nalezen."
