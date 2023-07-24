import os
import shutil

def clean_desktop(path):
    try:
        if not os.path.exists(path):
            print("Desktop folder not found.")
            return

        desktop_content = os.listdir(path)

        for item in desktop_content:
            item_path = os.path.join(path, item)

            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"File deleted: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Folder deleted: {item_path}")

        print("Desktop has been cleaned successfully!")
    except Exception as e:
        print(f"An error occurred while cleaning the desktop: {e}")


if __name__ == "__main__":
    # Replace 'your_user' with your username
    desktop_path = f"C:/Users/your_user/Desktop"

    clean_desktop(desktop_path)
