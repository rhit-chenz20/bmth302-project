#!/bin/bash
declare date="May12"
mkdir "result"
mkdir "result/${date}"
mkdir "result/${date}/CSV"
mkdir "result/${date}/Fig"

declare c=0
declare count=0
declare max=10
declare V=1
declare T=0.25

# learning model
for MS in 1 5 10
do
    for FIT in 0 1 
    do
        for ML in 3 5 10
        do
            for SZ in 500
            do
                let "count+=1"
                echo "running $count"

                python3 run.py -fs $SZ -ml $ML -ms $MS -fit $FIT -fn "result/${date}/CSV/ml_${ML}_ms_${MS}_fit_${FIT}_${V}" &
                if ((count>$max))
                then
                    wait
                    let "count=0"
                fi
            done
        done
    done
done              
echo "finished simulation"

for MS in 1 5 10
do
    for FIT in 0 1 
    do
        for ML in 3
        do
            for SZ in 100
            do
                let "count+=1"
                echo "running $count"

                python3 bar_plot.py -fn result/${date}/CSV/ml_*_ms_${MS}_fit_${FIT}_${V}_models.csv -o result/${date}/Fig/ms_${MS}_fit_${FIT}_t_${T}_sort_sumfit.png -t $T &
                if ((count>$max))
                then
                    wait
                    let "count=0"
                fi
            done
        done
    done
done          
