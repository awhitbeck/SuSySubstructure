from ROOT import TChain, TFile, TTree
from time import sleep
from array import array
import sys
import os
import math 
import glob

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sample", dest="sample", default = "ALL",
		                      help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")
parser.add_option('--run',action="store_true",dest="run",default=False,help='do training')
parser.add_option('--add',action="store_true",dest="add",default=False,help='do training')

(options, args) = parser.parse_args()

########################################################################################################################
########################################################################################################################
def fillSampleIndex(tSI):
	weight = -1;
	
	# tSI.append( ["QCD_Pt-30to50_Tune4C_13TeV_pythia8",(161500000.*1000.)] );
	# tSI.append( ["QCD_Pt-50to80_Tune4C_13TeV_pythia8",(22110000.*1000.)] );
	# tSI.append( ["QCD_Pt-80to120_Tune4C_13TeV_pythia8",(3000114.*1000.)] );
	# tSI.append( ["QCD_Pt-120to170_Tune4C_13TeV_pythia8",(493200.*1000.)] );
	# tSI.append( ["QCD_Pt-170to300_Tune4C_13TeV_pythia8",(120300.*1000.)] );
	# tSI.append( ["QCD_Pt-300to470_Tune4C_13TeV_pythia8",(7475.*1000.)] );
	# tSI.append( ["QCD_Pt-470to600_Tune4C_13TeV_pythia8",(587.1*1000.)] );
	# tSI.append( ["QCD_Pt-600to800_Tune4C_13TeV_pythia8",(167.*1000.)] );
	# tSI.append( ["QCD_Pt-800to1000_Tune4C_13TeV_pythia8",(28.25*1000.)] );
	# tSI.append( ["QCD_Pt-1000to1400_Tune4C_13TeV_pythia8",(8.195*1000.] );
	# tSI.append( ["QCD_Pt-1400to1800_Tune4C_13TeV_pythia8",(0.7346*1000.)] );
	# tSI.append( ["QCD_Pt-1800to2400_Tune4C_13TeV_pythia8",(0.102*1000.)] );
	
	tSI.append( ["QCD_HT-500To1000_13TeV-madgraph",(26740*1000.)] );
	tSI.append( ["QCD_HT_1000ToInf_13TeV-madgraph",(769.7*1000.)] );

	tSI.append( ["TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola",(818.0*1000.)] );
	tSI.append( ["WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola",(55.61*1000.)] );
	tSI.append( ["WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola",(18.81*1000.)] );
	tSI.append( ["ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola",(11.99*1000.)] );
	tSI.append( ["ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola",(4.113*1000.)] );

	tSI.append( ["SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola",(0.325388*1000.)] );
	tSI.append( ["SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola",(0.0141903*1000.)] );
	tSI.append( ["SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola",(0.325388*1000.)] );
	tSI.append( ["SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola",(0.025977*1000.)] );
	tSI.append( ["SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola",(0.0856418*1000.)] );
	tSI.append( ["SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola",(0.0141903*1000.)] );

	return weight;

def ProcessSample(remotedir,sampleNames,odir,lheweight):

	print "--------------------"
	print "Processing sample..."

	#change to a tmp dir
	os.chdir("tmp");
	curdir = os.getcwd();

	# make the relevant scripts
	for i in range(len(sampleNames)):
		# print "sample file name =",sampleNames[i]
		fileName, fileExtension = os.path.splitext(sampleNames[i])

		f1n = "tmp_%s_%i.sh" %(fileName,i);
		f1=open(f1n, 'w')
		f1.write("#!/bin/sh \n");
		f1.write("source /cvmfs/cms.cern.ch/cmsset_default.csh \n");
		f1.write("set SCRAM_ARCH=slc6_amd64_gcc481\n")
		f1.write("cd %s \n" % (curdir))
		f1.write("cd .. \n")
		f1.write("eval `scramv1 runtime -sh`\n")
		f1.write("python SlimAndSkim.py --filename %s --outputdir %s --lheWeight %s \n" % (remotedir+sampleNames[i], odir, lheweight))
		#f.write("cd Sens3/ \n")
		#f1.write("cd %s \n" % (workDir))
		#f1.write("%s %s %s -s %d -n %sSig%dCombine%d  \n" %(basecommand, datacard, options, r,testname,j,i))
		f1.close()

		f2n = "tmp_%s_%i.condor" %(fileName,i);
		f2=open(f2n, 'w')
		f2.write("universe = vanilla \n");
		f2.write("Executable = %s \n" % (f1n) );
		f2.write("Requirements = Memory >= 199 &&OpSys == \"LINUX\"&& (Arch != \"DUMMY\" )&& Disk > 1000000 \n");
		f2.write("Should_Transfer_Files = YES \n");
		f2.write("WhenToTransferOutput  = ON_EXIT_OR_EVICT \n");
		f2.write("Output = out_$(Cluster).stdout \n");
		f2.write("Error = out_$(Cluster).stderr \n");
		f2.write("Log = out_$(Cluster).log \n");
		f2.write("Notification    = Error \n");
		f2.write("Queue 1 \n");
		f2.close();

		os.system("condor_submit %s" % (f2n));

	os.chdir("../.");

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
	
if __name__ == '__main__':

	# this is where all of the condor config files go
	if not os.path.isdir("tmp"): os.mkdir("tmp");

	# parameters
	RemoteDir = "/eos/uscms/store/user/awhitbe1/PHYS14productionV3/";
	# SampleName  = "SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola";
	SampleName  = options.sample;
	OutputDir = "/eos/uscms/store/user/ntran/SUSY/ReducedTrees/Phys14-v3";

	TheSampleIndex = [];
	fillSampleIndex( TheSampleIndex );

	# run on one or all
	samplesToRunOn = [];
	if SampleName == "ALL":
		for i in range(len(TheSampleIndex)): samplesToRunOn.append(TheSampleIndex[i][0]);
	else: 
		samplesToRunOn.append( SampleName );

	for BaseName in samplesToRunOn:

		# find files of a particular sample name
		filelist = os.listdir(RemoteDir)
		filenames = [];
		lheWeight = -1;
		for fn in filelist:
			if BaseName in fn: filenames.append(fn);
		for i in range(len(TheSampleIndex)):
			if BaseName == TheSampleIndex[i][0]: lheWeight = TheSampleIndex[i][1];

		print "Sample Name = ",BaseName, "and number of files = ",len(filenames);

		# process that file (slim and skim), include LHE weight, Condor stylez
		if options.run: ProcessSample(RemoteDir,filenames,OutputDir,lheWeight);

		# hadd those guys
		if options.add: 
			haddCmmd = "hadd -f ";
			haddCmmd += OutputDir+"/"+BaseName+".all.root";
			for fn in filenames: 
				curFN = OutputDir+"/"+fn;
				if os.path.isfile(curFN): haddCmmd += " " + OutputDir+"/"+fn
			#print haddCmmd;
			os.system(haddCmmd);		




