# Overview of the SuSySubstructure Package

This package is intended to study various substructure techniques for gluino searches.  For ease 
of use, it is used in conjuction with the [TreeMaker](https://github.com/TreeMaker/TreeMaker/) package employed by the RA2/b analysis.  


## Setup Instruction

```
setenv SCRAM_ARCH slc6_amd64_gcc491
cmsrel CMSSW_7_2_3_patch1
cd CMSSW_7_2_3_patch1/src
cmsenv
git clone git@github.com:awhitbeck/TreeMaker.git -b CMSSW_7_2_X .
git clone git@github.com:awhitbeck/SuSySubstructure.git -b synch_June26_2015 AWhitbeck/SuSySubstructure
cd AWhitbeck/SuSySubstructure
./retrieveFastJetTools.sh
cd ../../
scram b -j 8
wget http://people.physics.tamu.edu/aperloff/CMS_JEC/PHYS14_V4/PHYS14_V4_MC.db -P AWhitbeck/SuSySubstructure/test/
```

## Input files

A number of config fragments
are stored in the python directory for files list for entire samples.  For PHYS14 samples, see list of config files [here](./python/PHYS14/).
There are also some private samples that have been produced for more detailed studies.  The corresponding
config files are [here](./python/privateSamples/).

## Relevant Code

For producing analysis trees, the config file, PHYS14production.py, should be used.  This config file also also
for command line arguments to be passed along.  The relevant command line arguments are:

| argument name     | default       | usage example        | comments        |
| ----------------- |:-------------:| --------------------:| ---------------:| 
| inputFilesConfig  | ""            | intputFilesConfig=PHYS14.SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola | config file for inputs, automatically appended with _cff.py |
| outputFile        | "T1tttt"      | outputFile=T1tttt    | root file for outputs, automatically appended with _RA2AnalysisTree.root |
| files             | ""            | files=file:myMINIAODfile.root | This can be used for comma separated lists of files. |

So, an example of how to run the code would be:

<pre>
cmsRun PHYS14production.py inputFilesConfig=PHYS14.SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola outputFile=T1tttt_mGl-1200_mLSP-800
</pre>

## Submit Production to Condor (@ LPC)

There are also utilities set up to run over all of the PHYS14 samples and save the output tree to your specified area (eos is required!).
The [test/condorSub](./test/condorSub) directory contains all of the relevant scripts.
If you copy this to another directory and run the [looper.sh](./test/condorSub/looper.sh) script, it will submit one job per file to condor for all of the relevant PHYS14 samples. Example:

<pre>
cp -r condorSub myProduction
cd myProduction
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction/
</pre>

The jobs open the files over xrootd, so [looper.sh](./test/condorSub/looper.sh) will check that you have a valid grid proxy.
It will also make a tarball of the current CMSSW working directory to send to the worker node.
If you want to reuse an existing CMSSW tarball (no important changes have been made since the last time you submitted jobs),
there is an extra argument:
```
./looper.sh root://cmseos.fnal.gov//store/user/YOURUSERNAME/myProduction/ keep
```

Things to do for batch submission:

1. get code working for check for and resubmitting failed jobs

## Calculating integrated luminosity

Scripts are available to calculate the integrated luminosity from data ntuples (produced with TreeMaker):

<pre>
python lumiSummary.py
./calcLumi.sh
</pre>

The first script [lumiSummary.py](./lumiSummary.py) loops over a list of data samples and creates a JSON
file for each sample consisting of the lumisections which were actually processed. (This script is based on
the CRAB3 client job report scripts.)

The second script [calcLumi.sh](./calcLumi.sh) runs [lcr2](https://twiki.cern.ch/twiki/bin/view/CMS/Lcr2) on the
JSON files created by the first script. It will automatically copy `lcr2.py` and the `runcsv` directory from AFS.
