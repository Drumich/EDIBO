%history -f a.txt   (saves ipythons current sessions history)

[!!!Python problem solutions!!!](https://www.sanfoundry.com/python-problems-solutions/)     

[python challenges](https://www.hackerrank.com/)        


dir(a)  what you can do with this variable      
a.reverse() (reverses the list)   
a.sort() (sorts list by numerical values)   
a.sort(reverse=True) (sorts the list in reverse(from highest to lowest))  




a = {"ābols":"apple"} ({} dictionary)       
a["ābols"] (shows apple)   
a.update({"bumbieris":"pear"})    
a.pop("ābols")    



python -m http.server = launches python so you can view you directories (127.0.0.1:8000 or localhost:8000 - firefox) or (curl 127.0.0.1:8000 - bash)       
vars() = shows all variables available      
type(a) (shows what type is a (for example a = 1 is integer or a = 1.2 is float))     



a.__ doc__     
a.pop.__ doc__ (shows documentation about pop)   
print(a.__ doc__)      
a[0] (index shows first number)   
idle & (opens python prompt or smthing)   



a"aA".hex() = 41    
hex(ord("A")) = 0x41    
  
s = set()     
s.add(11) = can add strings and stuff     
s2 = set()  
s2.add(11)  
s - s2    
s.difference(s2)    


for i in range(9):print(i) = (or i* i or i,i or i,i* i)   
for i in range(-4,5) : print("Number") ; print(i)  = show numbers from -4 to 4   
print(i, " " , end="") (print everything in a row NOT a column!)   
print("\t" , "\n" , end="") (tab , new row ...)



[%s and %d](https://matthew-brett.github.io/teaching/string_formatting.html)   
```
Vārds = "Jānis"
summa = 420
nr = 6969696969




s = """
Godājamais %s
Jums ir pienācis naudas pārvedums
ar vērtību %d EUR
Lai saņemtu naudu atsūtiet
īsziņu uz telefona nr. %d

Cieņā,
         Atraitne.
"""  %(Vārds,summa,nr)

print(s)


# %s = string
# %d = int

```

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)









[Python stuff](https://www.w3schools.com/python/python_variables.asp)            
[Python math and stuff](https://en.wikibooks.org/wiki/Python_Programming/Basic_Math)        
[More Python stuff](https://www.py4e.com/lessons)     
[complex numbers](https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/)     
