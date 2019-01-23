# FSND Item Cataloge

# description

Item Catalog is a project from udacity full stack web development nano degree program which aims to develope an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

# tools used in the project
1- vagrant tool (https://www.vagrantup.com/downloads.html) .
2-virtual box  (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
3-git bash (https://git-scm.com/downloads)
4-python 3.x.x
5-Flask 1.0.2
6-flask-httpauth 3.2.4
7-flask-sqlalchemy 2.3.3
8-SQLAlchemy 1.2.16

# How to install
1-download and install vagrant
2-download and install virtual box
3-download get bash
4-clone this machine configuration file from  repository [ FSND-Virtual-Machine ].(https://github.com/udacity/fullstack-nanodegree-vm) and unzip it.

# Set Up your environment
1-open git bash inside the FSND-Virtual-Machine and do the following commands
```
cd vagrant/
vagrant up
winpty vagrant ssh 
```
2-go to the workspace directory
```cd /vagrant/catalog```
3-put all the file inside this zip file into that directory
```
python database-setup.by
python lotsofitems.py
python application.py
```

# Explore the application
1-go to your website and type localhost:5000
2-navigate between diffrent category
3-if you want to add edit delete your own items sign in first to be able to do so
