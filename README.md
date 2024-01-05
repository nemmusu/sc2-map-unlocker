# Readme
[README: Italian](./README_IT.md)

[README: English](./README.md)
# Stronghold Crusader 2 Map Unlocker

This is a simple program that allows you to unlock the original maps of Stronghold Crusader 2 so that they can be edited in the map editor.

The program was created using the Python programming language and the PyQt5 library for the graphical interface.

To use the program, you need to run the unlocker.exe file included in the stronghold_map_unlocker.zip archive. To create this .exe file, the command `python compile.py build` was used (the compile.py file is present in the repository).

Once the program is launched, to unlock a map, click on the "Unlock Maps" button. You will be prompted to select the .shmap file to unlock. Once the file is selected, a new file with the extension "-unlocked.shmap" will be created, containing the unlocked map. You will be asked where to save the file. The map will be named after the file and you will be able to modify the description from the map editor.

Once the operation is completed, a confirmation message will be displayed.

## To use the script, install PyQt5 using pip

You can run the following command in your terminal:

```
pip install pyqt5
```

To start the map_unlocker.pyw script, follow these steps:

1. Make sure you have installed PyQt5 as described above.

2. Open your terminal and navigate to the directory where the map_unlocker.pyw file is located.

3. Run the following command to start the script:

```
python map_unlocker.pyw
```

The script will open a window with the graphical interface of the Stronghold Crusader 2 Editor Unlocker program. You can then use the program to unlock maps as described in the description above.

# Compilation
To create the executable of the Stronghold Crusader 2 Editor Unlocker program, you need to use cx_Freeze, a Python module that allows you to create executable packages from Python scripts.

First, you need to install cx_Freeze using pip. You can run the following command in your terminal:

```
pip install cx_Freeze
```

Once cx_Freeze is installed, you can proceed with creating the program's executable.
Run the following command to create the executable:

```
python compile.py build
```

This command will use cx_Freeze to create the program's executable. The executable will be created in the `build` directory inside the current directory.

Once the executable creation is complete, you can run it simply by double-clicking the unlocker.exe file.

# Executable

In the `build` folder, there is a zip file that contains an executable version of the program (already compiled and ready to use).

# Screenshot

![SC2 Map Unlocker](https://github.com/nemmusu/sc2-map-unlocker/blob/main/screenshots/interface_example.png)