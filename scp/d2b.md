```
#!/bin/bash
  
clear #notīra ekrānu
function num()  #ispildāmā funkcija
{
    CONV=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})

    n=""        #not defined numurs
    for byte in `echo ${1}` ; do        #
        n="${n}.${CONV[${byte}]}"
    done
    echo ${n:1}
}

echo "Enter the number"
read n

a=`num "${n}"`


echo "${a}"


```
