rm -r folder = (deletes this folder and all the folders there )              

mkdir -p folder/{1..3}/{1..3} = (makes folders inside a folder )                        
ls -l * = (shows folders and stuff within folders)                           

```
!#/bin/bash     
mkdir DEF   
cd DEF    
touch test.txt    
cd ..   
cp DEF/test.txt ./text1.txt   


how to launch : ./first_script.sh   
PATH=$PATH:./     
```




change permissions for read, write, execute :   
           rwx rwx rwx  
chmod 744 (111 100 100)   
