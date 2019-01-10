# Logs Analysis Project

this is Logs Analysis Project, part of the Udacity

## goal of project
 write SQL queries to answer the following questions about a PostgreSQL
database.

 * What are the most popular three articles of all time? *
 * Who are the most popular article authors of all time? *
 * On which days did more than 1% of requests lead to errors? *

## Required Libraries
this project code requires the following:

* Python 3.5.2
* psycopg2 2.7.3.2
* PostgreSQL 9.5.10

You can run the project in a Vagrant managed virtual machine (VM) .
(see below for how to run the VM). For this you
will need to downlods first VM [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on
your system.

## Project contents
This project consists of the following files:

* `log-analysis-project_pr.py` - The Python program that connects to the PostgreSQL
  database, executes the SQL queries and displays the results.
* `README.md` - This read me file.
* `Output` - The output of code.


### Bringing the VM up
Bring up the VM with the following run the command:

```bash
vagrant up
```

The first time you run this command, it will take awhile, as Vagrant needs to
download the VM image.

You can then log into the VM with the following command:

```bash
vagrant ssh
```
if you want  More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant
```

### Load the logs into the database

Then run the following command to load the logs into the database:

```bash
psql -d news -f newsdata.sql
```

### Running the reporting tool
The logs reporting tool is executed with the following command:

```bash
python3 logs_analysis_pr.py
```

The answers to the three questions should now be displayed.

### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to log out of it and shut it
down with this command:

```bash
vagrant halt
```
