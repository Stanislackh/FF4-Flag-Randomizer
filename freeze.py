from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['Tk_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = "Win32GUI"  # Pour application graphique sous Windows

includefiles = [
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
    "images"]

options = {
    'build_exe': {
        'include_files': includefiles
    },
}

# options d'inclusion/exclusion des modules
includes = ['PIL']  # nommer les modules non trouves par cx_freeze
excludes = []
packages = []  # nommer les packages utilises

# copier les fichiers non-Python et/ou repertoires et leur contenu:

# Paramètres de l'exécutable
target = Executable(
    script="Main.pyw",
    copyright="Slackh",
    base=base)

setup(name="FF4",
      version="1.0",
      options=options,
      description="Ayano Best Waifu",
      executables=[target]
      )
