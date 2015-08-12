import FWCore.ParameterSet.Config as cms
from commandLineParameters import *
import sys,os

process = cms.Process("analysis")

## configure geometry & conditions
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")

##  LOAD DATAFILES
readFiles = cms.untracked.vstring()

if options.inputFilesConfig!="" :
    process.load("AWhitbeck.SuSySubstructure."+options.inputFilesConfig+"_cff")
    readFiles.extend( process.source.fileNames )

if options.files!=[] :    
    readFiles.extend( options.files )

## auto configuration for different scenarios
if options.scenario == "Phys14":
    Global_Tag="PHYS14_25_V2"
    tagname="PAT"
    geninfo=True
    jsonfile=""
    jecfile=""
    residual=False
elif options.scenario == "Spring15":
    Global_Tag="MCRUN2_74_V9"
    tagname="PAT"
    geninfo=True
    jsonfile=""
    jecfile="Summer15_25nsV2_MC"
    residual=False
elif options.scenario == "2015B":
    Global_Tag="74X_dataRun2_Prompt_v1"
    tagname="RECO"
    geninfo=False
    jsonfile="Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt"
    jecfile="Summer15_50nsV2_DATA"
    residual=False
elif options.scenario == "re2015B":
    Global_Tag="74X_dataRun2_Prompt_v1"
    tagname="PAT"
    geninfo=False
    jsonfile="Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt"
    jecfile="Summer15_50nsV2_DATA"
    residual=False

###############
# tree maker
###############

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
                    outFileName=options.outputFile+"_RA2AnalysisTree",
                    reportEveryEvt=options.reportEvery,
                    testFileName=readFiles,
                    Global_Tag=Global_Tag,
                    lostlepton=False,
                    tagandprobe=False,
                    numProcessedEvt=options.numEvents,
                    doZinv=True,
                    debugtracks=False,
                    geninfo=geninfo,
                    tagname=tagname,
                    jsonfile=jsonfile,
                    jecfile=jecfile,
                    residual=residual
                    )

process.options.SkipEvent   = cms.untracked.vstring('ProductNotFound')

# drop all recoCand stuff and replace with 4-vectors
# --------------------------------------------------
process.TreeMaker2.VarsRecoCand = []

process.goodElectrons4Vec = cms.EDProducer("fourVectorProducer",
                                           particleCollection = cms.untracked.InputTag("LeptonsNew","IdIsoElectron"),
                                           debug = cms.untracked.bool(False)
                                           )

process.goodMuons4Vec = cms.EDProducer("fourVectorProducer",
                                           particleCollection = cms.untracked.InputTag("LeptonsNew","IdIsoMuon"),
                                           debug = cms.untracked.bool(False)
                                           )

process.TreeMaker2.VectorTLorentzVector.append("goodMuons4Vec(Muons)")
process.TreeMaker2.VectorInt.append("LeptonsNew:MuonCharge(MuonCharge)")
process.TreeMaker2.VectorTLorentzVector.append("goodElectrons4Vec(Electrons)")
process.TreeMaker2.VectorInt.append("LeptonsNew:ElectronCharge(ElectronCharge)")

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

###############
# rho stuff
###############

process.TreeMaker2.VarsDouble.append("fixedGridRhoFastjetAll(rho)")

# ==================
# fat jet stuff 
# ==================

#from AWhitbeck.SuSySubstructure.fatJetStudies_cff import *
#fatJetSetup(process) ## define relevant modules and a sequence to be used, process.SumJetMass

# ==================
# ak4 jets
# ==================

process.ak4Jets = cms.EDProducer("fourVectorProducer",
                                   particleCollection = cms.untracked.InputTag("GoodJets"),
                                   debug = cms.untracked.bool(False)
                                   )

#process.ak4JetsRaw = cms.EDProducer("fourVectorProducer",
#                                    particleCollection = cms.untracked.InputTag("slimmedJets"),
#                                    debug = cms.untracked.bool(False)
#                                    )

process.TreeMaker2.VectorTLorentzVector.append("ak4Jets")
#process.TreeMaker2.VectorTLorentzVector.append("ak4JetsRaw")
#process.TreeMaker2.VectorInt.append("GoodJets:passJetID(ak4Jets_passedJetID)")

process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorUser(ak4Jets_CSVdisc)")
process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorMVA(ak4Jets_MVAdisc)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorSimpleCSV(ak4Jets_SimpleCSVdisc)")

#process.TreeMaker2.VectorInt.append("JetsProperties:NumBhadrons(ak4Jets_NumBhadrons)")
#process.TreeMaker2.VectorInt.append("JetsProperties:NumChadrons(ak4Jets_NumChadrons)")

process.TreeMaker2.VectorDouble.append("JetsProperties:chargedHadronEnergyFraction(ak4Jets_chargeHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:neutralHadronEnergyFraction(ak4Jets_neutralHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:photonEnergyFraction(ak4Jets_photonEfrac)")
process.TreeMaker2.VectorInt.append("JetsProperties:chargedHadronMultiplicity(ak4Jets_chargedHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:neutralHadronMultiplicity(ak4Jets_neutralHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:photonMultiplicity(ak4Jets_photonMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:flavor(ak4Jets_flavor)")

### ak4 gen jets
#process.ak4GenJets = cms.EDProducer("fourVectorProducer",
#                                   particleCollection = cms.untracked.InputTag("slimmedGenJets"),
#                                   debug = cms.untracked.bool(False)
#                                   )

#process.TreeMaker2.VectorTLorentzVector.append("ak4GenJets")

## CONFIGURE TFILESERVICE

process.TFileService.closeFileFast = cms.untracked.bool(True)

##  DEFINE SCHEDULE

process.WriteTree = cms.Path( process.Baseline * 
                              process.AdditionalSequence *
                              process.goodElectrons4Vec * 
                              process.goodMuons4Vec *  

                              process.ak4Jets *
                              #process.ak4JetsRaw *
                              #process.ak4GenJets *

                              #process.SumJetMass * 
                              
                              process.TreeMaker2 
                              )

#OUPUT CONFIGURATION
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('test.root'),
#                               #save only events passing the full path
#                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
#                               outputCommands = cms.untracked.vstring('drop *','keep *_*photon*_*_*','keep *_*Jets*_*_*'
#                                                                      )
#                               )

#process.outpath = cms.EndPath(process.out)
