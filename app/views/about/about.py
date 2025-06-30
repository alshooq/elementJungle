from pathlib import Path

def about():
    """
    Render the about page.
    """
    
    return (str(Path("about") / "index.html"))
