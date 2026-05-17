from pathlib import Path
import subprocess

SOURCE_DIR = Path("tex")
OUTPUT_DIR = Path("html")

CSS_FILE = "../css/style.css"
TEMPLATE_FILE = "template.html"

OUTPUT_DIR.mkdir(exist_ok=True)

for tex_file in SOURCE_DIR.glob("*.tex"):

    output_file = OUTPUT_DIR / f"{tex_file.stem}.html"

    command = [
        "pandoc",
        str(tex_file),
        "--standalone",
        "--mathjax",
        f"--css={CSS_FILE}",
        f"--template={TEMPLATE_FILE}",
        "-o",
        str(output_file)
    ]

    print("-" * 60)
    print(f"Conversion de : {tex_file.name}")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"HTML généré : {output_file}")
    else:
        print("ERREUR")
        print(result.stderr)
