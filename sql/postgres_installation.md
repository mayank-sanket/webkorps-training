
# installation steps (latest version of postgres via terminal)



# 1. add postgres repository 


sudo apt update
sudo apt install -y wget gnupg
wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list


# 2. update package list

sudo apt update


# 3. install postgresql

sudo apt install -y postgresql postgresql-contrib 
    
- postgresql (installs the postgresql database server)
- postgresql-contrib (provides the additional extensions, like pg_stat_statements, hstore)

# 4. verify installation

psql --version




# 5. start and enable postgresql service


sudo systemctl start postgresql
sudo systemctl enable postgresql


# 6. switch to the postgresql user

sudo -i -u postgres


##  accessing postgresql shell

psql



# ----------------------------------------------------------------

# checking default postgresql user

- by default, PostgreSQL creates postgres superuser during installation. 


# 2. list postgresql user via psql

- first switch to postgres user:
 sudo -i -u postgres
 
- open psql shell: 
    psql

- list all users(roles):
 \du


# 3. check environment variables

echo $USER (works when the user is postgres)

# 4. use psql to test users (guess)

psql -U username -d database_name


# 5. check the postgresql config files

sudo nano /etc/postgresql/<version>/main/pg_hba.conf (replace version with your installed version)




## ____________________________________________________________-


## NOTE: 
- if you want to use pgadmin4 as well as psql shell then ensure that the default user (ie, postgres) has a password set and use this password to configure servers and databases with pgadmin4

# to set password

sudo -u postgres psql

ALTER USER POSTGRES PASSWORD 'your_new_password'