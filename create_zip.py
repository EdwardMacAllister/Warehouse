import os
import zipfile


def create_zip(zip_filename, directory_to_zip):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_to_zip):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_to_zip))


if __name__ == "__main__":
    project_folder = os.path.dirname(os.path.abspath(__file__))
    zip_filename = os.path.join(project_folder, 'project.zip')

    create_zip(zip_filename, project_folder)
    print(f"Project zipped as: {zip_filename}")
