---

## Clean Desktop Python Script

This Python script is designed to automatically clean your desktop by deleting all files and folders located on it. It can be called from the command prompt (cmd) and is intended to help you keep your desktop organized.

### Instructions:

1. Create a folder named `utils` at the root of your C drive (C://).

2. Save the Python script `clean_desktop.py` inside the `utils` folder.

3. Open the Python script `clean_desktop.py` using a text editor of your choice.

4. Locate the line that looks like the following:
   ```python
   desktop_path = f"C:/Users/your_user/Desktop"
   ```
   
5. Replace `'your_user'` with your actual username. For example, if your username is `john_doe`, the line should be changed to:
   ```python
   desktop_path = f"C:/Users/john_doe/Desktop"
   ```

6. Save the changes to the `clean_desktop.py` file.

7. Open the command prompt (cmd) on your system.

8. Navigate to the `utils` folder using the `cd` command. For example:
   ```
   cd C:\utils
   ```

9. Run the script using the following command:
   ```
   python clean_desktop.py
   ```

10. The script will start cleaning your desktop by deleting all files and folders. Be cautious and ensure that you have backed up any important data before executing the script.

### Important Notes:

- This script will delete all files and folders on your desktop, including shortcuts. Make sure you have a backup of any important files before running the script.

- The `clean_desktop.py` script will only delete the files and folders in the user's desktop folder. Ensure you are running the script with appropriate permissions and that the desktop folder is accessible.

- Use this script at your own risk. The developer is not responsible for any data loss or damage caused by the usage of this script.

- For support or issues related to the script, please create an issue on the GitHub repository.

### License:

This project is licensed under the [MIT License](LICENSE).

---
