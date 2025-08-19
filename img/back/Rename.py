import os

folder = r"D:\Downloads\HexManiacAdvance_x64.0.5.6.debug\pokesprite"  # change this to your folder

for filename in os.listdir(folder):
    if filename.lower().endswith(".png"):
        # remove .png
        base = filename[:-4]
        # strip trailing underscores and spaces
        base = base.rstrip('_ ').strip()
        # take text after the last underscore
        parts = base.split('_')
        # get the last non-empty part
        last_part = next((p for p in reversed(parts) if p.strip()), "")
        # clean up any extra spaces
        new_name = last_part.strip() + ".png"
        
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} --> {new_name}")