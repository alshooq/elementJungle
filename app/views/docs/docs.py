from pathlib import Path

def docs():
    """
    Render the docs page.
    """
    
    return (str(Path("docs") / "index.html"))
