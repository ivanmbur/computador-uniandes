#!/bin/sh

rm 01_notas.tsv*
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv
awk '{if(($3 == "MATEMA") && (($4 + $5 + $6)/3 >= 3)) print $1,$2,($4 + $5 + $6)/3}' 01_notas.tsv > nombre.txt  
