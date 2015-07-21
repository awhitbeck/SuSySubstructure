#!/bin/bash

#check for necessary lcr2 ingredients

if [ ! -f lcr2.py ]; then
  echo "Copying lcr2.py from AFS"
  cp /afs/cern.ch/user/m/marlow/public/lcr2/lcr2.py .
fi

if [ ! -d runcsv ]; then
  echo "Copying runcsv from AFS"
  cp -r /afs/cern.ch/user/m/marlow/public/lcr2/runcsv/ .
fi

for i in json/lumiSummary_*.json
  do
    echo $i
    python lcr2.py -i $i -p 0
  done
