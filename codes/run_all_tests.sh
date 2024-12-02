#!/bin/bash

for f in $(find . -name 'ideal_gas*.py' -o -name 'nvt_harmonic.py'); do
  echo -e "********************\nRunning $f\n********************"
  python $f
done
