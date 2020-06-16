
if [ "$(whoami)" == "root" ] ; then
    echo "Setting up your server"
    sudo DEBIAN_FRONTEND=noninteractive sudo apt-get update && sudo apt-get upgrade -qq < /dev/null > /dev/null
    echo "updated server apt cache"
 
    sudo DEBIAN_FRONTEND=noninteractive sudo apt-get install python3-pip < /dev/null > /dev/null
    echo "Installed Python pip"

    sudo DEBIAN_FRONTEND=noninteractive pip3 install -r Tooling/requirements.txt < /dev/null > /dev/null
    echo "Installed pip dependencies"
    sudo DEBIAN_FRONTEND=noninteractive sudo apt-get install unzip -qq < /dev/null > /dev/null
    echo "Installed unzip"
    sudo DEBIAN_FRONTEND=noninteractive sudo apt-get install chromium-browser -qq < /dev/null > /dev/null
    echo "Installed chromium browser"
    sudo DEBIAN_FRONTEND=noninteractive wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip < /dev/null > /dev/null
    unzip chromedriver_linux64.zip 
    echo "Downloaded and unzipped ChromeDriver for Selenium"
else
    echo "Please run as root"
    exit 1
fi