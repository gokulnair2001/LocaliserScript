# 📃 PP Localiser Script
Adding localisations from the sheet is a mess so here is a small helper for you. Localiser Script helps to fetch translations from Master sheet for the desired keys

## Usage

### Step 1️⃣
* Since its a python script you need python installed on your locals
* In case you do not know how to install Python
  ```
  brew install pyenv
  ```
* The script consists of few libraries which are used to fetch values from google sheet and manipulate raw data. Thus download the folowing libraries:
  
  ```
  pip install google-api-python-client
  ```
  ```
  pip install google-auth
  ```
  ```
  pip install google-auth-oauthlib
  ```
  ```
  pip install google-auth-httplib2
  ```
  ```
  pip install pandas
  ```

* Ik a lot of libraries, but yeah its what it is🫡.

### Step 2️⃣
* Download the [script](https://github.com/gokulnair2001/LocaliserScript) and `SSToken.json` file 

### Step 3️⃣
* Open the script on any IDE and modify the following values as per need
```py
# File Paths
CREDENTIAL_FILE_LOCATION = "/Users/gokulnair/Desktop/SSToken.json"
LOCALIZED_FILE_LOCATION = "/Users/gokulnair/Desktop/Localisation.odt"
STRING_NAME_KEYS = ['create_site', 'next_add_team', 'calculate_payables'] // Add keys here
SUCCESS_RANGE_NAME = "Project modules" // This is the desired sub sheet in which your keys are added
```
### Step 4️⃣
* Run your script using Terminal or IDE

## ⚠️ Important
* Localised file will be stored at the above specified location
* Initially the script wil create a new `Localisation.odt` file on your local, later if you are not deleting the file then it will start apending the content on the same file

### 👀 Vision 
* Hope this finds helpful to you
* I tried creating a GUI using swift by injecting Python script into it, but local injecting won't allow importing third party libraries, thus distributing the Script itself

