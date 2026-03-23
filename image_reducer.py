from PIL import Image
import os

OUTPUT_DIR = "resized"

def list_files_by_extension(directory, extension):
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files
        if file.lower().endswith(extension)
    ]

def detect_ratio(width, height, tolerance=0.05):
    ratio = width / height
    if abs(ratio - 4/3) < tolerance:
        return "4:3"
    elif abs(ratio - 3/2) < tolerance:
        return "3:2"
    elif abs(ratio - 16/9) < tolerance:
        return "16:9"
    return "autre"

def resize_proportionally(img, max_size):
    width, height = img.size
    if width >= height:
        return img.resize((max_size, int(height * max_size / width)), Image.LANCZOS)
    return img.resize((int(width * max_size / height), max_size), Image.LANCZOS)

def save_with_target_size(img, output_path, target_mb=3):
    quality = 95
    while quality >= 60:
        img.save(output_path, "JPEG", quality=quality, optimize=True)
        if os.path.getsize(output_path) / (1024 * 1024) <= target_mb:
            break
        quality -= 5

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

files = list_files_by_extension(os.getcwd(), ".jpg")

for path in files:
    img = Image.open(path)
    w, h = img.size

    orientation = "paysage" if w >= h else "portrait"
    ratio = detect_ratio(w, h)

    resized = resize_proportionally(img, 2048)

    name = os.path.basename(path)
    output_path = os.path.join(OUTPUT_DIR, name)

    save_with_target_size(resized, output_path)

    print(f"{name} → {orientation}, {ratio}")
