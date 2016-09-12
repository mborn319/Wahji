echo python $PWD/wahji.py \$@ >> wahji.sh
mv wahji.sh wahji #rename script file
chmod +x wahji #make script file executable
mv wahji /usr/local/bin #move file to /usr/local/bin
