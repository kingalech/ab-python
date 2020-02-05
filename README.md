![featured-image](https://raw.githubusercontent.com/andela-mnzomo/project-dream-team-one/master/flask-crud-part-one.jpg)
Dream Team Project, *Build a CRUD Web App With Python and Flask*.

- [ShellScript to install](https://gitlab.com/cloudhedge/pro-serv-demo/-/blob/dev/CHDemoAppsSetups-Scripts-Centos-7/dreamteam/dreamteam-app/installation.sh)

Following are the commands to make this application run:

```
#!/bin/bash

setenforce 0
iptables -F

MYSQL_PASSWORD=Admin@12345
MY_PUBLIC_IP=$1

yum install epel-release

yum install -y mysql-devel gcc python-pip python-devel

type -P wget &>/dev/null && echo "wget is already installed." || yum install wget -y
type -p rpm &>/dev/null && echo "rpm is already installed." || yum install rpm -y
type -p git &>/dev/null && echo "git is already installed." || yum install git -y

echo "Verifying mysql-server using wget"
[ -f "mysql57-community-release-el7-7.noarch.rpm" ] && echo "mysql-server rpm file exists" || wget http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm

echo "Verifying if mysql server is installed or not"

if rpm -q mysql57-community-release-el7-7.noarch > /dev/null 
then 
	echo "MYSQL installed"
else
	echo "MYSQL is not installed, we are installing it using rpm"
	rpm -ivh mysql57-community-release-el7-7.noarch.rpm
fi

echo "Verifying if the mysql-server is installed"
type -p mysql &>/dev/null && echo "MySQL server is installed." || yum install mysql-community-server -y

echo "Starting the mysqld service using systemctl"

systemctl enable mysqld
systemctl start mysqld

TEMP_PASSWORD=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $(NF)}')
echo "MYSQL_PASSWORD is $TEMP_PASSWORD"

echo "Changing the root password for mysql-server"
echo "ALTER USER 'root'@'localhost' IDENTIFIED BY 'Admin@12345'; flush privileges;" > reset_pass.sql
# Log in to the server with the temporary password, and pass the SQL file to it.
mysql -u root --password="$TEMP_PASSWORD" --connect-expired-password < reset_pass.sql

rm -rf reset_pass.sql

mysql -u root --password="$MYSQL_PASSWORD" -e 'select user, host from mysql.user;'

mysql -u root --password="$MYSQL_PASSWORD" -e "CREATE USER 'admin'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
mysql -u root --password="$MYSQL_PASSWORD" -e "GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'admin'@'%' with grant option;"
mysql -u root --password="$MYSQL_PASSWORD" -e "FLUSH PRIVILEGES;"

mysql -u admin --password="$MYSQL_PASSWORD" -e "CREATE DATABASE dreamteam_db;"

current_path=$(pwd)
db_server=$1

pip install -r requirements.txt

export FLASK_CONFIG=development
export FLASK_APP=run.py
export FLASK_DB_HOST=$db_server

flask db init
flask db migrate
flask db upgrade

sed -i "10s/.*/WorkingDirectory=$(echo $current_path | sed 's_/_\\/_g')/" dreamTeam.service
sed -i "5s/.*/export FLASK_DB_HOST=$db_server/" python_app.sh

cp dreamTeam.service /etc/systemd/system/
systemctl daemon-reload
systemctl start dreamTeam.service

echo 'Done'
```
