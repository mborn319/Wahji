echo python $PWD/wahji.py "$@" > wahji.sh #Create script file
mv wahji.sh wahji #rename script file
chmod +x wahji #make script file executable
mv wahji /bin #move file to /bin
