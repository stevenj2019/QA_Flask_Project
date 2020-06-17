echo "Preparing Server"
sudo apt-get update -y 
sudo apt-get upgrade -y
sudo apt-get install python3-pip unzip chromium-browser python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install -r Tooling/requirements.txt

echo "Testing Software"
export TEST_DB_URI=''
export TEST_SECRET_KEY=''
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
pytest -> This Fails right now 


echo "Deploying"
export PROD_DB_URI=''
export PROD_SECRET_KEY=''
python3 Tooling/generate_service.py
cd Tooling
mv Flask.Service /etc/systemd/system/
cd ../
sudo systemctl deamon-reload
sudo systemctl start Flask