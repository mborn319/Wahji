# TODO: have the $PWD variable get sent to the wahji.py module
#       so that we always know the current working directory.
echo python $PWD/wahji.py \$@ >> wahji.sh
mv wahji.sh wahji #rename script file
chmod +x wahji #make script file executable
mv wahji /bin #move file to /bin
