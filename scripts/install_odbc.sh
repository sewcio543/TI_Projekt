apt-get update

apt-get install -y \
        curl \
        gnupg \
        apt-transport-https \
        unixodbc \
        unixodbc-dev \
        lsb-release

apt-get clean

# if ! [[ "16.04 18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
# then
#     echo "Ubuntu $(lsb_release -rs) is not currently supported.";
#     exit;
# fi

curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc

curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

apt-get update

ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev unixodbc
# optional: for bcp and sqlcmd
ACCEPT_EULA=Y apt-get install -y mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
