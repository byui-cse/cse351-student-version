# Run this to auto create folder structure; there are multiple versions of this without the student repo currently.
import os

parent_dir = os.getcwd()
subfolders = ['canvas', 'prep', 'team', 'prove']  
files = ['prep.md', 'prepare.md', 'prove.md', 'team.md']

for i in range(1, 15):
    # Create lesson folders
    lesson_num = str(i).zfill(2)
    lesson_dir = f'lesson_{lesson_num}'
    lesson_path = os.path.join(parent_dir, lesson_dir)

    if not os.path.exists(lesson_path):
        os.mkdir(lesson_path)

    # Create subfolders 
    for subfolder in subfolders:
        subfolder_path = os.path.join(lesson_path, subfolder)
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)

    # Create files in canvas folder
    canvas_path = os.path.join(lesson_path, 'canvas')
    for file in files:
        file_path = os.path.join(canvas_path, file)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()