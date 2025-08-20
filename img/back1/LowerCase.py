import os

folder = r"D:\Documents\GitHub\Odyssey-Calc\img\pokesprite"  # change this to your folder

for filename in os.listdir(folder):
    if filename.lower().endswith(".png"):
        # make filename lowercase
        new_name = filename.lower()
        
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} --> {new_name}")