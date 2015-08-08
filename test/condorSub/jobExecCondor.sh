#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

CMSSWVER=$1
OUTDIR=$2
SAMPLE=$3
FILELIST=$4
SCENARIO=$5

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "OUTDIR:     $OUTDIR"
echo "SAMPLE:     $SAMPLE"
echo "FILELIST:   $FILELIST"
echo "SCENARIO:   $SCENARIO"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
source /cvmfs/cms.cern.ch/cmsset_default.sh
# cmsenv
eval `scramv1 runtime -sh`
cd -

# copy data files to current dir
cp $CMSSW_BASE/src/AWhitbeck/SuSySubstructure/data/* .

# run CMSSW
cmsRun PHYS14production.py outputFile=${SAMPLE} files=${FILELIST} scenario=${SCENARIO} 2>&1

# copy output to eos
echo "xrdcp output for condor"
for FILE in *.root
  do
    xrdcp -f ${FILE} ${OUTDIR}/
    rm ${FILE}
  done



