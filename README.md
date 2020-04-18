# final-selenuim-edu
Final selenium test project 

### Prerequisites

It's only for MacOS X

install Python3, follow this guide https://installpython3.com/mac/

create virtual environment 
```
mkdir environments
cd environments
python3 -m venv selenium_env
```
### Install packages
#####1. Install packages using  requirements.txt 
 ```
pip install -r requirements.txt
 ```
download selenium webdriver for Chrome
find actual link here https://sites.google.com/a/chromium.org/chromedriver/downloads
then:
 ```
wget http://actual_link
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
 ```

#####2. Install everything manually

you have to activate environment
it's your sandbox there you will install and use python package to avoid mixing them with system packages   
```
source selenium_env/bin/activate
pip install selenium
```

download selenium webdriver for Chrome
find actual link here https://sites.google.com/a/chromium.org/chromedriver/downloads
then:
 ```
wget http://actual_link
unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
 ```

Install PyTest
(be sure your are in selenium_env, 
otherwise activate it ```source selenium_env/bin/activate ```)
```
pip install pytest
pip install pytest-rerunfailures
 ```

### Run

To Run test execute
```
pytest -v --tb=line --language=en
```
