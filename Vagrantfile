# -*- mode: ruby -*-
# vi: set ft=ruby :

## Set Variables
$VM_BASE_BOX = "ubuntu/bionic64"     ## defines vm base box/image: Ubuntu 18.04.6 LTS (Bionic Beaver);
$VM_NAME = "ubuntu1804-pgsql84-app"  ## defines vm names of: gui display name, vagrant vm name, hostname
$VM_CPUS = 2                         ## defines vm number of CPUs/Cores;
$VM_RAMS = 2048                      ## defines vm number of RAM in MB;
$VM_LAN_IP = "192.168.0.71"          ## defines vm ip-address in your local network;
##


## Begin of Vagrantfile configuration (syntax version is v2)
Vagrant.configure("2") do |config|

  config.vm.box = $VM_BASE_BOX                              ## base box/image of vm;

  config.vm.box_check_update = false                        ## disable box updates from Vagrant Cloud;
  config.vm.define $VM_NAME                                 ## vm name (default name is "default");
  config.vm.hostname = $VM_NAME                             ## network hostname;

  ## Network configuration
  config.vm.network "public_network", ip: $VM_LAN_IP        ## public accessible ip-address of VM interface (from internal LAN address range);

  ## Provider-specific configuration (Oracle VirtualBox)
  config.vm.provider "virtualbox" do |vb|
    vb.name = $VM_NAME                                      ## vm display name in VirtualBox GUI;
    vb.gui = false                                          ## disable VM console in VirtualBox GUI when VM is creating;
    vb.check_guest_additions=false                          ## disabled is "Guest Additions Tools" is installed on VM (this tools is not required on servers);
    vb.cpus = $VM_CPUS                                      ## number of CPUs/Cores;
    vb.memory = $VM_RAMS                                    ## number of RAM in MB;
  end


  ## Provisioning0: Copy webapp sources from Host to Guest home directory (/home/vagrant)
  #config.vm.provision "file", source: "/home/devops/src/webapp-postgres-django", destination: "/home/vagrant/webapp-postgres-django"           ## не хватает прав для запист в /opt
  #config.vm.provision "file", source: "/home/devops/src/webapp-postgres-django", destination: "/opt/webapp-postgres-django", privileged: true  ## нет sudo режима
  #
  config.vm.provision "file", source: "/home/devops/src/webapp-postgres-django", destination: "/tmp/webapp-postgres-django"
  config.vm.provision "shell", inline: "mv /tmp/webapp-postgres-django /opt/webapp-postgres-django"


  ## Provisioning1: Installing PostgreSQL 8.4 client and Python3 Base packages on Guest host
  config.vm.provision "DeployPython3Django", type: "shell", inline:<<-SHELL

    ## STEP - Create new user "devops" and configure ssh access with key authentication (1)
    echo
    echo "--STEP10: Creating special sudo user.."
    useradd -p '$6$y8aQ4FxWTNrDzVSa$sG1j1s7dfTu3PlKwrmv7NLDuH7ADnY6rB26aZ9HJPpE3ucqwbeLAQiHj81xE3Z8BoDlzfWm1LhNktYsL07/E7.' -G sudo --create-home --shell /bin/bash devops
    touch /etc/sudoers.d/devops
    echo "devops  ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/devops
    id devops
    echo

    ## STEP - Create new user "devops" and configure ssh access with key authentication (2)
    echo "--STEP11: Generating ssh key pair and configuring ssh service for user connection.."
    sudo -u devops /bin/bash -c "mkdir -p /home/devops/.ssh"
    chmod u=rwx,g=,o= /home/devops/.ssh
    sudo -u devops /bin/bash -c "echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBfGokGoaKzkCofNwwTPVko198HhAuwHeD+F6xO5Khk5 devops@userver1804' >> /home/devops/.ssh/authorized_keys"    
    chmod u=rw,g=,o= /home/devops/.ssh/authorized_keys
    echo

    ## STEP - Update and upgrade OS (only current Ubuntu18 release)
    echo "--STEP20: Updating package list nad upgrade current packages.."
    apt update -y 2>/dev/null
    apt upgrade -y 2>/dev/null
   
    ## STEP - Install PostgreSQL client (lates for current os release)
    echo "--STEP30: Installing PostgreSQL v8.4 client (webapp).."
    apt install -y wget ca-certificates 2>/dev/null
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
    tail -n1 /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    apt update -y 2>/dev/null
    apt upgrade -y 2>/dev/null    
    #DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical apt-get --option Dpkg::Options::=--force-confold -q -y install postgresql-contrib-8.4
    apt install -y postgresql-client 2>/dev/null
    psql --version

    ## STEP - Check PostgreSQL on remote host with SQL Queries
    echo "--STEP31: Executing select query (show PostgreSQL version and sample data).."
    #PGPASSWORD=vagrant@pass psql -c "select version()::varchar(100);" | grep PostgreSQL | awk '{print $1" "$2}'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT version()::varchar(100);" | grep PostgreSQL | awk '{print $1" "$2}'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT word FROM greetings WHERE lang = 'ENG';" -t | cut -d ' ' -f 2 | sed '/^$/d'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT word FROM greetings WHERE lang = 'FRA';" -t | cut -d ' ' -f 2 | sed '/^$/d'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT word FROM greetings WHERE lang = 'DEU';" -t | cut -d ' ' -f 2 | sed '/^$/d'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT word FROM greetings WHERE lang = 'ITA';" -t | cut -d ' ' -f 2 | sed '/^$/d'
    PGPASSWORD=vagrant@pass psql -t postgres://192.168.0.70:5432/vagrant?sslmode=disable -U vagrant -c "SELECT word FROM greetings WHERE lang = 'RUS';" -t | cut -d ' ' -f 2 | sed '/^$/d'
    echo

    ## STEP - Install Python3 and PopstgreSQL modules
    echo "--STEP40: Installing Python3 and modules.."
    apt install -y tree
    apt install -y python3 python3-pip 2>/dev/null
    apt install -y libpq-dev python3-psycopg2
    apt install -y build-essential libssl-dev libffi-dev python3-dev
    apt install -y python3-venv
    pip3 install --upgrade pip
    python3 --version
    pip --version
    echo


    ## STEP - Create project folder, activate vnev, install Python3 packages and run Django webapp
    #sudo mkdir /opt/webapp-postgres-django
    #sudo cp -R /home/vagrant/webapp-postgres-django/* /opt/webapp-postgres-django
    sudo chown -R vagrant:vagrant /opt/webapp-postgres-django
    cd /opt/webapp-postgres-django
    #pwd
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py runserver 0.0.0.0:8000
    #deactivate

    echo "--FINISHED;"

  SHELL

end
