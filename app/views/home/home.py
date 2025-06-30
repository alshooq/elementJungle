from pathlib import Path

def home():
    """
    Render the home page.
    """
    
    return (str(Path("home") / "index.html"))
