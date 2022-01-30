#! /bin/bash

for (( c=1; c<=3; c++ ))
do

    python ./src/approvals.py >> log
    python ./src/automatizacion_boton.py >> log
    python ./src/automatizacion_reglas.py >> log
    python ./src/calendario.py >> log
    python ./src/countdown.py >> log

done
