import os
import shutil


def static_to_public():
    delete_public_files()
    copy_to_static("./static", "./public")


def delete_public_files():
    public = "./public"
    if os.path.exists(public):
        for filename in os.listdir(public):
            file_path = os.path.join(public, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print(f"deleting {file_path} file")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"deleting {file_path} folder")
            except Exception as error:
                print("Failed to delete %s. Reason: %s" % (file_path, error))


def copy_to_static(path, destination):
    if os.path.isfile(path):
        shutil.copy(path, destination)
        print(f"copied {path} to {destination}")
    else:
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                shutil.copy(os.path.join(path, item), destination)
                print(f"copied {item} to {destination}")
            else:
                os.mkdir(os.path.join(destination, item))
                copy_to_static(
                    os.path.join(path, item), os.path.join(destination, item)
                )
