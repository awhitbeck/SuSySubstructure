#!/bin/bash

date

source /uscmst1/prod/sw/cms/bashrc prod
workerNodeDir=`pwd`
echo $workerNodeDir
cd <CMSSW_BASE>
eval `scram runtime -sh`
cd -

cmsRun PHYS14production.py outputFile=<OUTPUTDIR>/<SAMPLE>_<INDEX> files=<FILELIST>

