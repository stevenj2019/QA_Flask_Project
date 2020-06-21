sudo apt-get update -y 
sudo apt-get upgrade -y
sudo apt-get install python3-pip unzip chromium-browser python3-venv -y
python3 -m venv venv

. venv/bin/activate
pip3 install -r Tooling/requirements.txt

export TEST_DB_URI=
export TEST_SECRET_KEY=

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
pytest --cov-report term-missing --cov=./application

python3 Tooling/generate_service.py
mv Tooling/Flask.service /etc/systemd/system

sudo systemctl deamon-reload
sudo sysemctl start Flask

rm -rf Tooling
rm -rf Documentation_rss
rm -rf Testing
rm create.py
rm README.md