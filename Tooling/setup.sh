sudo apt-get update -y 
sudo apt-get upgrade -y
sudo apt-get install python3-pip unzip chromium-browser python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install -r Tooling/requirements.txt
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
pytest