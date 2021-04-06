# Scraping Tested Comic Episodes on Webtoons using Python and Selenium
### The scripts output will contain the following columns:
* Episode Name
* Date
* Loves
* Episode Number
* Comments Count
* Comment Username
* Comment Description
* Comment Likes
* Comment Dislikes
* Reply Username
* Reply Description
* Reply Likes
* Reply Dislikes

## How to Run the Script on Windows

### Clone the repository to your system as a ZIP File
![Screenshot 2021-04-05 133004](https://user-images.githubusercontent.com/60167177/113604302-140eee80-9613-11eb-9ef5-6f3fb86d3fb1.png)

### Click the arrow on the folder and click "Show in folder"
![Screenshot 2021-04-05 132235](https://user-images.githubusercontent.com/60167177/113604465-55070300-9613-11eb-935c-96bd5be38caf.png)

### Right click the ZIP file and click "Extract All..."
![Screenshot 2021-04-05 133642](https://user-images.githubusercontent.com/60167177/113605143-3a815980-9614-11eb-8ca7-520e0e33dfbf.png)

### Input your desired directory to save the folder (you will need this later)
### Click "Extract"
![Screenshot 2021-04-05 134152](https://user-images.githubusercontent.com/60167177/113605490-b9769200-9614-11eb-9296-0a3f232b5091.png)

### Install Python
#### [Click Here](https://www.python.org/ftp/python/3.7.8/python-3.7.8-amd64.exe) to download Python3.8 (requires Python3.8 or lower)

### Click to open the installer
![Screenshot 2021-04-05 131101](https://user-images.githubusercontent.com/60167177/113602280-6c90bc80-9610-11eb-9e5e-45bb39c61864.png)

### Check the "Add Python 3.8 to PATH" box then click "Install Now"
![Screenshot 2021-04-05 131239](https://user-images.githubusercontent.com/60167177/113602706-ed4fb880-9610-11eb-9bc7-931e2f732b6b.png)

### Once the installation is complete, press the "Windows" key and search for Command Prompt by typing "CMD"
### Click "Open" to open the Command Prompt
![Screenshot 2021-04-05 135248](https://user-images.githubusercontent.com/60167177/113606643-49690b80-9616-11eb-858d-2ef353dae016.png)

### Type "python --version" and press enter to verify python is installed and in PATH
![Screenshot 2021-04-05 135515](https://user-images.githubusercontent.com/60167177/113606970-afee2980-9616-11eb-8441-03be8d3c40a5.png)

### Navigate to the extracted folder using the "cd" command: Type "cd C:\YOUR\DIRECTORY\HERE\webtoons-comments-in-python-main" and press enter
### Use the "dir" command to veridy you're in the correct folder
![Screenshot 2021-04-05 141214](https://user-images.githubusercontent.com/60167177/113608757-f47ac480-9618-11eb-9889-b37d218bde43.png)

### Run the command "py -m pip install -r requirements.txt" to install all of the required dependencies
![Screenshot 2021-04-05 141640](https://user-images.githubusercontent.com/60167177/113609314-969aac80-9619-11eb-85b9-89ed2ce3fd1b.png)

### Wait for the installations to complete, then run the command "python webtoons_scraping.py" to execute the script
![Screenshot 2021-04-05 142001](https://user-images.githubusercontent.com/60167177/113609639-0ad55000-961a-11eb-9661-a733c5d6c63b.png)

### The script will display data being actively scraped until the eventual message "EXECUTION COMPLETE"

### After execution, 2 output files will appear in the directory, one in CSV and one in XLSX format

### Disclaimer
We checked robots.txt file of the URL: https://www.webtoons.com/en/challenge/tested/list?title_no=231173&page=1 and learned that we are allowed to scrape comic data.
