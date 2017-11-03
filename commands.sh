#!/bin/bash

#Perform following yum installtion

yum install wget -y
cd /usr/src
rm -fv csf.tgz
wget https://download.configserver.com/csf.tgz
tar -xzf csf.tgz
cd csf
sh install.sh
yum install perl-libwww-perl -y
yum install unzip -y 

sleep_period=20
################
echo "waiting for $sleep_period seconds to perform manual transfer of file /etc/csf/csf.conf from remote PC"
sleep $sleep_period
file=$(ls -td /etc/csf/* | head -1)
echo "$file"
if [ $file ==  "/etc/csf/csf.conf" ]; then
  echo "$file is uploading and its latest file "
else 
  echo "please transfer of file /etc/csf/csf.conf from remote PC"	
fi

echo "check Manually it is  uploaded 100% or not "

while true; do
    read -p "want to continue press Y or else N to wait " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done

################

csf -a 23.250.9.96; 
service iptables stop
csf -r
yum install httpd -y

################
#NANO Command: Need to do changes in file, location is /etc/php.ini


echo "waiting for $sleep_period seconds to perform manual transfer of file /etc/php.ini from remote PC"
sleep $sleep_period
file=$(ls -td /etc/* | head -1)
if [ $file == '/etc/php.ini' ]; then
  echo "latest File $file is uploading "
fi

echo "check Manually it upload 100% or not "

while true; do
    read -p "uploaded is fine  and want to continue press Y or else N to wait " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done





################

service httpd start
yum install mysql-server -y
service mysqld start
/usr/bin/mysql_secure_installation

################
#at this point script will ask to do some manual intruption, like Enter, press y or n (exit) and enter
################
while true; do
    read -p "PRESS Y or else N to exit " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.  ";;
    esac
done



yum install php php-mysql -y
service httpd restart
yum install php php-mysql httpd
service httpd restart
echo "=============================================================\n"

################
echo "At this point we need to press enter manually"
################
echo "Please enter below mysql comamnds"
echo "CREATE DATABASE script_123 "
echo "CREATE USER 'script_123'@'localhost' IDENTIFIED BY '12345678' "
echo "GRANT ALL PRIVILEGES ON * . * TO 'script_123'@'localhost'"

echo "=================================================================\n"

mysql -u root -p


################
#ctrl+c for exit
################

yum install epel-release -y
yum install phpmyadmin -y

################
#need to make changes in cron file, Location is /etc/httpd/conf.d/phpMyAdmin.conf
################

echo "waiting for $sleep_period seconds to perform manual transfer of file /etc/httpd/conf.d/phpMyAdmin.conf from remote PC"
sleep $sleep_period
file=$(ls -td /etc/httpd/conf.d/* | head -1)
if [ $file == '/etc/httpd/conf.d/phpMyAdmin.conf' ]; then
  echo "latest File is uploading "
fi

echo "check Manually it upload or not "

while true; do
    read -p "uploaded is fine  and want to continue press Y or else N to wait " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done





service httpd restart
yum install cronie -y
crontab /etc/crontab
service crond restart

################
# make changes in cron file, Location is /var/spool/cron/root

echo "waiting for $sleep_period seconds to perform manual transfer of file /var/spool/cron/root  from remote PC"
sleep $sleep_period

file=$(ls -td /var/spool/cron/ | head -1)
if [ $file == '/var/spool/cron/root' ]; then
  echo "$file File is uploading "
fi

echo "check Manually it upload or not "

while true; do
    read -p "uploaded is fine  and want to continue press Y or else N to wait " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done




################

wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm && rpm -Uvh epel-release-latest-6.noarch.rpm
wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && rpm -Uvh remi-release-6*.rpm

################
# need to make changes in remi.repo file, Location is /etc/yum.repos.d/remi.repo
################
echo "waiting for $sleep_period seconds to perform manual transfer of file /etc/yum.repos.d/remi.repo from remote PC"
sleep $sleep_period

file=$(ls -td /etc/yum.repos.d/ | head -1)
if [ $file == '/etc/yum.repos.d/remi.repo' ]; then
  echo "$file File is uploading "
fi

echo "check Manually it is uploaded or not"

while true; do
    read -p "uploaded is fine  and want to continue press Y or else N to wait " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo "sleep #for $sleep_period" 
		sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done




yum -y update mysql*

################
#at this point we need to press enter manually
################
service mysqld restart

################
#for exit, need to use ctrl+c
################

sleep 2

cd /var/www/html/
sleep 1
wget http://interspireaddon.com/files/file.zip
wget http://interspireaddon.com/files/data.zip

unzip /var/www/html/file.zip
unzip /var/www/html/data.zip


mysql -D script_123 < data.sql
chmod -R 777 /var/www/html/admin/addons/spins/install/backup
chmod -R 777 /var/www/html/admin/addons/installer/install/backup
chmod -R 777 /var/www/html/admin/com/storage
chmod -R 777 /var/www/html/admin/temp
chmod 777 /var/www/html/admin/includes/js/javascript.js
chmod 777 /var/www/html/admin/com/ext/interspire_email/email.php
chmod 777 /var/www/html/admin/functions/api/send.php
chmod 777 /var/www/html/admin/functions/api/ss_email.php
chmod 777 /var/www/html/admin/includes/config.php
service crond restart

################
#need to make changes in config file, Location is /var/www/html/admin/includes/config.php
#This change I can do manually because this change will change in every installtion so we can't make a fix file for it.
################

file=$(ls -td /var/www/html/admin/includes/* | head -1)
if [ $file == '/var/www/html/admin/includes/config.php' ]; then
  echo "$file File is uploading "
fi

echo "check Manually it is uploaded or not"

while true; do
    read -p "if file is uploaded is fine  and want to continue press Y or else N to EXIT " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo "sleep #for $sleep_period" 
                sleep $sleep_period;;
        * ) echo "Please answer yes or no.  ";;
    esac
done

