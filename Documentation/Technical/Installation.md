# Installation Guide

Requirements:

	- Linux based on Red Hat - development on Oracle Linux 7.8 (APP+DB)
	- PostgreSQL Server
	- Python3
	- Django
	- pip
	
1 - Database Installation
	- Install PostgreSQL server with all dependencies
	- Initialize PostgreSQL Cluster
	- Configure PostgreSQL as wanted
	- Create user
		create user iem with login password '....';
	- Create database
		create database iemdb with owner=iem encoding='UTF-8';
	- Grant connect on database
		grant connect on database iemdb to iem;
	- Connect to IEMDB
		\c iemdb
	- Create schema
		create schema authorization iem;
	- Allow user IEM to connect in pg_hba.conf
	- Reload PostgreSQL Cluster
		pg_ctl reload
	- Perform any additional settings
		
Database Service
	- Create any service to control IEMDB PostgreSQL server
	
Application Installation
	- Copy files to desired server
	- Copy IEM/sample.env to db.env
		- Edit variable values in db.env
	- Start server
		python $PATH/manage.py runserver IPADDR:PORT

Application Service
	- Create any service to control IEM application server