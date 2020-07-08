tput setaf 1 = (output colour changes to RED)

[Stuff](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_01.html)   

[for/while...](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html)   



bc = opens base conversion(convert decimal numbers to binary)   
ibase=10    
obase=2     
[Decimal to Binary conversion](https://www.thecrowned.org/base-conversion-ubuntu-decimal-binary)    




. filename or bash filename (execute a file/script in bash)   

ps -a (shows bash things running (kill -9 12345 to stop it running))
rm gg.txt (deletes a file)
time ./ filename (shows how long you script loads)    
echo $0 - ar kādu termināli strādā    
[PS1=$ (customise bash prompt)](https://help.ubuntu.com/community/CustomizingBashPrompt)    
ctrl + alt + t - open terminal      
ctrl + shift + t - new tab in terminal  
nano - text redactor    
chmod 777 filename (give all permissions to a file)  (chmod +x filename : makes it executable)      
ls -lt ...c/l/a...(list/show directory/files sorted by date(t))          
TAB - autofill            
sh - different shell (uses less resources(no colours and stuff..))      
absolūtā adrese vienmēr ir (/ aka (root)  
hexdump -C(or -c) abc.txt  (hex code or ASCII symbol)   
[Hexdump](http://manpages.ubuntu.com/manpages/xenial/en/man1/hexdump.1.html)  
[Hexdump / xxd](http://manpages.ubuntu.com/manpages/trusty/man1/xxd.1.html)
xxd - binary code   
?1 byte = 8 bits (0/1 - 2 states) => unique codes 2^8 = 256?    
[ASCII table](http://www.ecowin.org/ascii.htm)   


![Screenshot from 2020-07-03 14-35-24](https://user-images.githubusercontent.com/58115541/86465573-95f78180-bd3a-11ea-83ec-36650731cc8d.png)    
drwxrwxr....        
d - directory(folders)
rw - read write     
x - execute(to make things executable : chmod +x filename)      
1,2,3,4,5 - apakšdirektorijas faili(more stuff in there)    

![Screenshot from 2020-07-03 14-43-50](https://user-images.githubusercontent.com/58115541/86466089-b1af5780-bd3b-11ea-8f33-27f9b5c111c8.png)        
cd - aiziet home/user (or default directory)    
cd . - aiziet uz to pašu vietu kur esi tagad        
cd .. - aiziet no jeb kuras citas direktorijas tur kur vajag (piem cd ../Desktop or cd ../Documents)  (vai vienkārši cd .. jump the tree(similar so cd / (goes to root)))   

cp ../abc.txt ../ABC/abc2.txt (kopē abc.txt un ieliek viņu /ABC/abc2.txt)   
cat ../ABC/abc2.txt - read this file (jābūt pareizajā direktorijā(mapē))         

adresses - absolute (/ - root directory), relative (. , .. , ~)   
lshw - list everything in the computer (processor,drive,usb ports...)   
whereis $PATH (wh)      
git clone https://github.com/Drumich/EDIBO         

```
for i in {1..5} ; do echo $i $((i*i)) ; done
```

