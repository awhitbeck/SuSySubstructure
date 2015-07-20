#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#python generateSubmission.py -n 1 -s -f PHYS14.GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.DYJetsToLL_M-50_13TeV-madgraph-pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-1400to1800_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-1800to2400_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-2400to3200_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-3200_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-1000to1400_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-800to1000_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-600to800_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-470to600_Tune4C_13TeV_pythia8 -o $outputDir
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_Pt-300to470_Tune4C_13TeV_pythia8 -o $outputDir

#### gluino
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola 
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola 
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola 
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola 
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola 
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola 

#### sqaurk
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-600_mLSP-580_Tune4C_13TeV-madgraph-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-900_mLSP-100_Tune4C_13TeV-madgraph-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-1200_mLSP-100_Tune4C_13TeV-madgraph-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-600_mLSP-550_Tune4C_13TeV-madgraph-tauola

#### rare backgrounds
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.TTWJets_Tune4C_13TeV-madgraph-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.TTZJets_Tune4C_13TeV-madgraph-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.TTbarH_M-125_13TeV_amcatnlo-pythia8-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.WH_HToBB_WToLNu_M-125_13TeV_powheg-herwigpp
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.ZH_HToBB_ZToNuNu_M-125_13TeV_powheg-herwigpp
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola
python generateSubmission.py -o $outputDir -n 1 -s -f PHYS14.TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola

#python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT-100To250_13TeV-madgraph -o $outputDir        
python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT_1000ToInf_13TeV-madgraph -o $outputDir       
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT_250To500_13TeV-madgraph_ext1 -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT-500To1000_13TeV-madgraph -o $outputDir       
python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT_1000ToInf_13TeV-madgraph_ext1 -o $outputDir
python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT-500To1000_13TeV-madgraph_ext1 -o $outputDir  
#python generateSubmission.py -n 1 -s -f PHYS14.QCD_HT_250To500_13TeV-madgraph -o $outputDir

#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.DoubleEG -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.DoubleMuon -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.EGamma -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.HTMHT -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.MET -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.SingleElectron -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.SingleMu -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.SingleMuon -o $outputDir
#python generateSubmission.py -n 1 -s -f Run2015B-PromptReco-v1.SinglePhoton -o $outputDir
