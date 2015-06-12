# Overview of the SuSySubstructure Package

This package is intended to study various substructure techniques for gluino searches.  For ease 
of use, it is used in conjuction with the [TreeMaker](https://github.com/TreeMaker/TreeMaker/) package employed by the RA2/b analysis.  


## Setup Instruction

<pre>
setenv SCRAM_ARCH slc6_amd64_gcc491
cmsrel CMSSW_7_4_1
cd CMSSW_7_4_1/src
cmsenv
git clone https://github.com/awhitbeck/TreeMaker.git -b CMSSW_7_4_X .
mkdir AWhitbeck
cd AWhitbeck
git clone https://github.com/awhitbeck/SuSySubstructure.git
cd SuSySubstructure
bash retrieveFastJetTools.sh
cd ../../
scram b -j8
wget http://people.physics.tamu.edu/aperloff/CMS_JEC/PHYS14_V4/PHYS14_V4_MC.db AWhitbeck/SuSySubstructure/test/.
</pre>

## Input files

A number of config fragments
are stored in the python directory for files list for entire samples.  For PHYS14 samples, see list of config files [here](https://github.com/awhitbeck/SuSySubstructure/tree/master/python/PHYS14).
There are also some private samples that have been produced for more detailed studies.  The corresonding
config files are [here](https://github.com/awhitbeck/SuSySubstructure/tree/June4_2015/python/privateSamples).

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

There are also utilities set up to run over all of the PHYS14 samples and save the output tree to your some specified area (eos is strongly recommended!).  The test/condor_sub directory contains all of the relevant scripts. If you copy this to another directory and run the [looper.sh](https://github.com/awhitbeck/SuSySubstructure/blob/June4_2015/test/condorSub/looper.sh) script, it will submit one job per file to condor for all of the relevant PHYS14 samples. Example:

<pre>
cp -r condor_sub myProduction
cd myProduction
bash looper.sh /eos/uscms/store/user/YOURUSERNAME/myProduction/
</pre>

The job open the files over xrootd, so be sure that the output directory already exists and that you have a valid grid proxy:

<pre>
voms-proxy-init -voms cms
</pre>

Things to do for batch submission:

1. get code working for check for and resubmitting failed jobs
