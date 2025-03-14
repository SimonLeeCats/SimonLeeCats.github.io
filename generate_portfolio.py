import json
from datetime import datetime, UTC
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Get the directory of the script
PROJECT_DIR = Path(__file__).parent

# Load JSON data
json_path = PROJECT_DIR / "portfolio.json"
if not json_path.exists():
    raise FileNotFoundError(f"Could not find portfolio.json in {PROJECT_DIR}")

with json_path.open(encoding="utf-8") as f:
    data = json.load(f)

# Add any extra context if needed
data["current_year"] = datetime.now(tz=UTC).year

# Load SVG files if applicable
if "social_links" in data:
    for link in data["social_links"]:
        if "svg_path" in link:
            svg_file_path = PROJECT_DIR / link["svg_path"]
            if svg_file_path.exists():
                with svg_file_path.open(encoding="utf-8") as svg_file:
                    link["svg_data"] = svg_file.read()
            else:
                print(f"Warning: SVG file {svg_file_path} not found.")

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(PROJECT_DIR), autoescape=True)
index_template = env.get_template("index_template.html")
resume_template = env.get_template("resume_template.html")

# Render the templates with data
html_output = index_template.render(**data)
resume_output = resume_template.render(**data)

# Write output files
(Path(PROJECT_DIR) / "index.html").write_text(html_output, encoding="utf-8")
(Path(PROJECT_DIR) / "resume.html").write_text(resume_output, encoding="utf-8")

print("Portfolio generated successfully!")
