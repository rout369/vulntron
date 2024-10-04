from library.libraries import *

def open_new_command_line():
    current_os = platform.system()
    current_dir = os.getcwd()  # Get the current working directory

    if current_os == "Windows":
        # Open new cmd in the current directory
        subprocess.Popen(f'start cmd /K "cd {current_dir}"', shell=True)
    elif current_os == "Linux":
        # Open gnome-terminal in the current directory
        subprocess.Popen(['gnome-terminal', '--working-directory', current_dir])
    elif current_os == "Darwin":  # macOS
        # Open Terminal in the current directory
        subprocess.Popen(['open', '-a', 'Terminal', current_dir]) 
