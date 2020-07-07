
#! /bin/bash
#Comment
cd
echo "Hello World"
a=3 b=4
echo $a+$b=$((a+b))
echo `date`



[loop script](https://stackoverflow.com/questions/11176284/time-condition-loop-in-shell)   


60 second loop
```
#!/bin/bash
secs=10
SECONDS=0
while (( SECONDS < secs )) ; 
do
df --output=pcent /dev/sda2 | tail -1
sleep 1
done
```   

Forever loop
```
#!/bin/bash
for (( ; ; ))
do
df --output=pcent /dev/sda2 | tail -1
sleep 1
done
```    



https://tsugi.sakai.lv/portal - must register here for projects and sharing...  




man command(opens manual( /[Oo]ption searches for word option ( n for next search)))        
ls -l       
whereis vim         
df -h (check disk space and stuff)      
df --output=pcent /dev/sda2 (shows only percentage of the disk usage)    
df -B 1 /dev/sda2 (shows disk storage in Bits)      
[FIELD_LIST is a comma-separated list of columns to be included. Valid field names are: 'source', 'fstype', 'itotal', 'iused', 'iavail', 'ipcent', 'size', 'used', 'avail', 'pcent' and 'target' (see info page).]      

```
#! /bin/bash
 
kopa="`df | grep sda2 | awk '{print $2}'`"
lietots="`df | grep sda2 | awk '{print $3}'`"
pieejams="`df | grep sda2 | awk '{print $4}'`"

echo $kopa $lietots $pieejams

echo Tiek izmantoti $((lietots*100/kopa)) %
echo Ir pieejams $((pieejams*100/kopa)) %
```
```
$echo awk -v n=1000 'BEGIN{print(n*0.8)}'
```






[%](https://unix.stackexchange.com/questions/421083/bash-how-to-calculate-percentage-from-number)   
https://www.geeksforgeeks.org/du-command-linux-examples/        
https://help.ubuntu.com/community/grep  
https://www.tldp.org/LDP/abs/html/textproc.html         
https://askubuntu.com/questions/847752/how-to-capture-disk-usage-percentage-of-a-partition-as-an-integer        
https://www.tutorialspoint.com/sed/sed_overview.htm     
https://askubuntu.com/questions/20752/how-can-i-search-within-a-manpage         
https://www.gnu.org/software/bash/manual/bash.pdf       



Git upload  

#!/bin/bash
git config --global user.email eee@eeee.lv
git add .
git commit -m "02072020_16_20"
git pull
git push origin master
