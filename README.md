# Codes on Finding the Closest Border Checkpoint


## About this code

The code aims to allow Ukrainians to find the closest western border checkpoint from their location by entering the location name (can be English, Ukrainian or any other languages). It also shows the path to get to the checkpoint from the location on the map. Since Ukraine map data is too large to process, we use the data from Hong Kong instead.


## Requirements needed

1. Visual Studio Code is used.
2. Python 3.7+ interpreter with osmnx environment is used.
3. There is numpy with version 1.21.2 or higher in the python interpreter.
4. There is pandas with version 1.3.3 or higher in the python interpreter.
5. Openpyxl is downloaded.
6. Geopy is downloaded.
7. Anaconda3 is installed on the computer.


## How to create environment with osmnx

1. Open Anaconda Prompt while right-clicking to run as administrator.
2. Type in the following command without outer quotations: "conda config --prepend channels conda-forge"
3. Type in the following command without outer quotations: "conda create -n ox --strict-channel-priority osmnx jupyterlab"
4. When asking if change should be implemented, enter y and continue.
5. Wait until "(base) PS C:\Window\system32" is shown again (Applies to other command as well).
6. Type in the following command: "conda activate ox". Then "(base)PS..." should be changed to "(ox) PS...".
7. Type in the following command without outer quotations: "python -m ipykernel install --user --name ox --display-name "Python (ox)"".

## How to download packages

1. Open Anaconda Prompt while right-clicking to run as administrator.
2. Type in the following command: "conda activate ox". Then "(base)PS..." should be changed to "(ox) PS...".
3. Type in the following command where you replace geopy with the actual package name: "pip install geopy"
4. When asking if change should be implemented, enter y and continue.
5. Wait until "(ox) PS C:\Window\system32" is shown again.
6. Repeat step 3 to step 5 if you want to install more packages.


## How to run the app

1. Upzip the folder with all codes.
2. Open Visual Studio Code. Make sure all requirements above are met. If not, install all of the necessary packages into the python interpreter.
3. Click "File" at the top left corner and then click "Open Folder" and select the upzip folder. After that, click "Select Folder" so that all files are opened in VS Code.
4. Select the python interpreter with name "ox".
5. On the left side of VS Code, an explorer should be found with all file names inside the folder.Open ukraine_app folder and then open data.py to modify the directory to your own version.
6. Save data.py and close it off. 
7. Click "app.py" and open it.
8. Change the value of location_name to the one of your interest.
9. Click the triangle button at the top right corner of the VS code to run the app.
10. The result is shown in terminal at the bottom.
11. In case you want to rerun the code, kill the terminal by clicking trash bin logo near bottom and run the code again.
