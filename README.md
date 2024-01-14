# ime_cursor_tkinter
This program is a simple utility to check the input state of Korean and English characters using Tkinter and PyStray.
## Description
The program displays a small window with a character label ('가' or 'a') that reflects the current input state. It also provides a system tray icon for easy access to control the program.
## Features
- Real-time monitoring of input language and Caps Lock status.
- Minimalistic interface with a small window and system tray icon.
## Usage
1. Run the executable or the script.
2. The program window will show the current input state with the displayed character.
3. Use the system tray icon for additional options:
   - **Show**: Bring the program window to the front.
   - **Stop**: Minimize the program to the system tray.
   - **Quit**: Close the program.
## Build Instructions
To build an executable using PyInstaller, you can use the following command:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
2. Navigate to the directory containing your script (IME_cursor_kor_eng.py) and icon file (image.ico).
3. Run the following command to create a standalone executable:
   ```bash
   pyinstaller -w --icon=image.ico --add-data "image.ico;." IME_cursor_kor_eng.py
   - The -w flag is used for a windowed application (no console window).
   - "--icon=image.ico" specifies the icon file for the executable.
   - "--add-data "image.ico;." includes the icon file in the executable.
4. After the process completes, the dist directory will contain the standalone executable.
### Notes
- Ensure to replace "image.ico" with the actual path to your icon file.
## Dependencies
- python3.x
- pystray
- pillow
## Additional Information
- This program was tested on a Windows environment.
- The system tray functionality is implemented using PyStray.
- Feel free to customize and enhance the program according to your needs.
## License
This program is released under the MIT License.
