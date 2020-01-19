#!/bin/sh                   

#BSUB -q normal       

#BSUB -o %J.out

#BSUB -e %J.err

#BSUB -n 1 

#BSUB -J JOBNAME

#BSUB  -R span[ptile=1]   

#BSUB -m "node03"         

#BSUB  -gpu  num=1         


python demo.py
