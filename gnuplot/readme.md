plot "1.dat" # assumes col1=x, col2=y; shows '+' at data point
plot '2col.dat' using 1:2                      # 1=x, 2=y (this is the default)
plot '2col.dat' using 2:1                      # 2=x, 1=y (reverse the graph)


set terminal png = (to save graph as png)   
set output "1.png" (saves graph as png)    
set grid = grid tiles   
set title "title" = main title   
set yrange [20:160] = sets lowest y to 20 and highest y to 160  
u 1:2 = using 1:2   
w lp = with linepoints    
t "title" = title of the line    
lw 2 = line width  

```
plot "1.dat" u 1:2 w l , "1.dat" u 1:3 w l , "1.dat" u 1:4 w l     
 ```
 
 
 
 ![ey](https://i.stack.imgur.com/QpFsh.png)   



 
[SCRIPT Process Memory/CPU Usage](https://dzone.com/articles/monitoring-process-memorycpu-usage-with-top-and-pl)     

[Guide](http://lowrank.net/gnuplot/index-e.html)   
[Lines,Colors...](http://gnuplot.sourceforge.net/docs_4.2/node62.html)   
[Guide1](https://alvinalexander.com/technology/gnuplot-charts-graphs-examples/)   
[Guide2 Demo](http://gnuplot.sourceforge.net/demo/)  
