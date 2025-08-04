import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    """
    Resolves the absolute path to a resource file.

    Supports both standard Python execution and PyInstaller-packed (.exe) environments.
    Automatically detects the runtime environment and returns the correct file path
    for accessing bundled resources (e.g. icons, images, config files).

    Args:
        relative_path (str): Relative path to the desired resource (e.g. 'view/assets/main.png').

    Returns:
        Path: Absolute path to the resource file on disk.
    """
    try:
        base_path = Path(sys._MEIPASS)  # type: ignore
    except AttributeError:
        base_path = Path(__file__).resolve().parent
        if not (base_path / relative_path).exists():
            base_path = Path.cwd()
    return base_path / relative_path
