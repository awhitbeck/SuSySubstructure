from ROOT import TChain, TFile, TTree
from time import sleep
from array import array
import sys
import os
import math 
import glob

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", default = "T1tttt", help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")
parser.add_option("-o", "--outputdir", dest="outputdir", default = "T1tttt", help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")
parser.add_option("-w", "--lheWeight", dest="lheWeight", default = "T1tttt", help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")

(options, args) = parser.parse_args()

if __name__ == '__main__':


	print "filename = ", options.filename
	print "outputdir = ", options.outputdir
	print "lheWeight = ", options.lheWeight
	basename = os.path.basename( options.filename );
	# #accessProtocol = "root://cmsxrootd-site.fnal.gov//store/user/"
	# #bkgDir = "awhitbe1/RA2Tree_13TeV_25ns20PU_V1/"

	# accessProtocol = "";
	# #bkgDir = "/eos/uscms/store/user/awhitbe1/RA2Tree_13TeV_25ns20PU_V1/"
	# bkgDir = "/uscmst1b_scratch/lpc1/3DayLifetime/ntran/SUSY/fromAndrew/RA2Tree_13TeV_25ns20PU_V1/"

	# ### background trees
	# #tree = TChain("RA2TreeMaker2/RA2PreSelection")
	# fullpath = accessProtocol + bkgDir + sampleName;
	# # print fullpath
	# # tree.Add( fullpath ) 

	#print fullpath
	f1 = TFile(options.filename,'read');
	#f1.ls()
	tree = f1.Get("TreeMaker2/PreSelection");


	tree.SetBranchStatus("*",0);
	tree.SetBranchStatus("HT",1);
	tree.SetBranchStatus("MHT",1);
	tree.SetBranchStatus("NJets",1);
	tree.SetBranchStatus("sumJetMass",1); 
	tree.SetBranchStatus("BTags",1);              
	tree.SetBranchStatus("Leptons",1);
	# tree.SetBranchStatus("Jet1Pt",1);
	# tree.SetBranchStatus("Jet2Pt",1);
	# tree.SetBranchStatus("Jet3Pt",1);
	# tree.SetBranchStatus("DeltaPhi1",1);  
	# tree.SetBranchStatus("DeltaPhi2",1);  
	# tree.SetBranchStatus("DeltaPhi3",1);  

	# tree.SetBranchStatus("ak4Num",1);     
	# tree.SetBranchStatus("ak4Pt",1);      
	# tree.SetBranchStatus("ak4Eta",1);     

	ofile = TFile(options.outputdir+"/"+basename,'RECREATE');
	ofile.cd();
	otree = tree.CloneTree(0);

	lheWeight = array( 'f', [ 0. ] );  
	b_lheWeight = otree.Branch("lheWeight",lheWeight,"lheWeight/F"); #xs*lumi/nev, take lumi as 1fb-1


	nent = tree.GetEntriesFast();
	for i in range(nent):

		if(i % (1 * nent/100) == 0):
			sys.stdout.write("\r[" + "="*int(20*i/nent) + " " + str(round(100.*i/nent,0)) + "% done");
			sys.stdout.flush();

		tree.GetEntry(i);
		lheWeight[0] = float(options.lheWeight);

		if tree.HT > 500 and tree.NJets > 2 and tree.MHT > 0:
			otree.Fill();   

	print "\n"
	#otree.Print();
	otree.AutoSave();
	ofile.cd();
	otree.Write();
	ofile.Close();
