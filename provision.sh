cd /vagrant
sudo apt-get install -y python-dev python-virtualenv libxml2-dev libxslt1-dev libffi-dev postgresql-server-dev-9.4 git
make init
make update
make data
