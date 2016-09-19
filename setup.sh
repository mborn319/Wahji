# TODO: have the $PWD variable get sent to the wahji.py module
#       so that we always know where Wahji is installed.
#       This will be useful when copying themes folders, default content folders, etc.
echo python $PWD/wahji.py \$@ >> wahji.sh
mv wahji.sh wahji #rename script file
chmod +x wahji #make script file executable
mv wahji /bin #move file to /bin
