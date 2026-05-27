import subprocess
import os
import sys

def tex_to_html(tex_file, output_dir=None):
    # Vérification du fichier
    if not os.path.isfile(tex_file):
        raise FileNotFoundError(f"Fichier introuvable : {tex_file}")

    # Nom de base
    tex_file = os.path.abspath(tex_file)
    base_name = os.path.splitext(os.path.basename(tex_file))[0]

    # Dossier de sortie
    if output_dir is None:
        output_dir = os.path.dirname(tex_file)
    else:
        os.makedirs(output_dir, exist_ok=True)

    # Commande make4ht
    cmd = [
        "make4ht",
        "-u",              # unicode
        "-d", output_dir,  # dossier de sortie
        tex_file
    ]

    print("▶ Conversion en cours...")
    print("Commande :", " ".join(cmd))

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✔ Conversion réussie")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Erreur lors de la conversion")
        print(e.stderr)
        sys.exit(1)

    html_file = os.path.join(output_dir, base_name + ".html")

    if os.path.isfile(html_file):
        print(f"📄 Fichier HTML généré : {html_file}")
    else:
        print("⚠️ HTML non trouvé, vérifie les logs.")

    return html_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python tex2html.py fichier.tex [dossier_sortie]")
        sys.exit(1)

    tex_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    tex_to_html(tex_file, output_dir)
