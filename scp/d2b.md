```
#!/bin/bash

function num()
{
    CONV=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})

    n=""
    for byte in `echo ${1} | tr "." " "`; do
        n="${n}.${CONV[${byte}]}"
    done
    echo ${n:1}
}

echo "Enter the number"
read n

a=`num "${n}"`


echo "${a}"

```
