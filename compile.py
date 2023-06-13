import PyInstaller.__main__


def compile_script():
    """A Script to compile the code to exe"""
    PyInstaller.__main__.run([
        "app.py",
        "--onefile",
        "--windowed",
        "--console",
        "--name",
        "Chat To Chat",
        "--specpath",
        "./build",
    ])


if __name__ == "__main__":
    compile_script()
