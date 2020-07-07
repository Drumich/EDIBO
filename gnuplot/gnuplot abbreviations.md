 ![ey](https://i.stack.imgur.com/QpFsh.png)   
 [More Abbreviations](https://superuser.com/questions/508644/looking-up-gnuplot-abbreviations)  
 ```
 set grid
set title 'BP and Heartrate'
set yrange [50:160]
set xlabel 'time (military)'
set label 'finished walk' at 15, 140
unset label
set label 'finished walk' at 15, 105
plot 'bp-hr.dat' u 1:2 w lp t 'systolic', 'bp-hr.dat' u 1:3 w lp t 'diastolic', 'bp-hr.dat' u 1:4 w lp t 'heartrate'
```  

set grid = grid tiles   
set title = main title   
set yrange [20:160] = sets lowest y to 20 and highest to 160  
u 1:2 = using 1:2   
w lp = with linepoints    
t = title of the line   

 
 
 
 
 
 
