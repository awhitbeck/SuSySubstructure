import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

process = cms.Process("analysis")

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.options   = cms.untracked.PSet(
    SkipEvent   = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
    )

## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

###############
# tree maker
###############

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
makeTreeFromMiniAOD(process,
                    outFileName="ReducedSelection",
                    reportEveryEvt=options.reportEvery,
                    testFileName="",
                    Global_Tag="PHYS14_25_V2::All",
                    lostlepton=False,
                    gammajets=False,
                    numProcessedEvt=options.numEvents
                    )

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
process.TreeMaker2.VectorTLorentzVector.append("goodElectrons4Vec(Electrons)")


##################################
# DEFINE MODULES FOR ANALYSIS
##################################

###############
# gen stuff
###############

process.genParticles = cms.EDProducer("genParticlesProducer",
                                      genCollection = cms.untracked.InputTag("prunedGenParticles"),
                                      debug = cms.untracked.bool(False)
                                      )

process.TreeMaker2.VectorTLorentzVector.append("genParticles(genParticles)")
process.TreeMaker2.VectorInt.append("genParticles:PDGid(genParticles_PDGid)")
#process.TreeMaker2.VectorInt.append("genParticles:parent(genParticles_parent)")

###############
# photon stuff
###############

from AWhitbeck.SuSySubstructure.photonStudies_cff import * 
photonSetup(process) ## define relevant modules and a sequence to be used, process.photonSeq

# ==================
# fat jet stuff 
# ==================

from AWhitbeck.SuSySubstructure.fatJetStudies_cff import *
fatJetSetup(process) ## define relevant modules and a sequence to be used, process.SumJetMass

# ==================
# ak4 jets
# ==================

process.ak4Jets = cms.EDProducer("fourVectorProducer",
                                   particleCollection = cms.untracked.InputTag("GoodJets"),
                                   debug = cms.untracked.bool(False)
                                   )

process.ak4JetsRaw = cms.EDProducer("fourVectorProducer",
                                    particleCollection = cms.untracked.InputTag("slimmedJets"),
                                    debug = cms.untracked.bool(False)
                                    )

from AllHadronicSUSY.Utils.jetproperties_cfi import jetproperties
process.JetsPropertiesRaw = jetproperties.clone(JetTag  = cms.InputTag('slimmedJets'),
                                                BTagInputTag	        = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
                                                METTag  = cms.InputTag("slimmedMETs"),
                                                )


process.TreeMaker2.VectorTLorentzVector.append("ak4Jets")
process.TreeMaker2.VectorTLorentzVector.append("ak4JetsRaw")
#process.TreeMaker2.VectorInt.append("GoodJets:passJetID(ak4Jets_passedJetID)")

process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminator(ak4Jets_CSVdisc)")
process.TreeMaker2.VectorDouble.append("JetsProperties:chargedHadronEnergyFraction(ak4Jets_chargeHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:neutralHadronEnergyFraction(ak4Jets_neutralHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:photonEnergyFraction(ak4Jets_photonEfrac)")
process.TreeMaker2.VectorInt.append("JetsProperties:chargedHadronMultiplicity(ak4Jets_chargedHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:neutralHadronMultiplicity(ak4Jets_neutralHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:photonMultiplicity(ak4Jets_photonMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:flavor(ak4Jets_flavor)")

process.TreeMaker2.VectorDouble.append("JetsPropertiesRaw:bDiscriminator(ak4JetsRaw_CSVdisc)")
process.TreeMaker2.VectorDouble.append("JetsPropertiesRaw:chargedHadronEnergyFraction(ak4JetsRaw_chargeHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsPropertiesRaw:neutralHadronEnergyFraction(ak4JetsRaw_neutralHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsPropertiesRaw:photonEnergyFraction(ak4JetsRaw_photonEfrac)")
process.TreeMaker2.VectorInt.append("JetsPropertiesRaw:chargedHadronMultiplicity(ak4JetsRaw_chargedHadMult)")
process.TreeMaker2.VectorInt.append("JetsPropertiesRaw:neutralHadronMultiplicity(ak4JetsRaw_neutralHadMult)")
process.TreeMaker2.VectorInt.append("JetsPropertiesRaw:photonMultiplicity(ak4JetsRaw_photonMult)")
process.TreeMaker2.VectorInt.append("JetsPropertiesRaw:flavor(ak4JetsRaw_flavor)")


### ak4 gen jets
process.ak4GenJets = cms.EDProducer("fourVectorProducer",
                                   particleCollection = cms.untracked.InputTag("slimmedGenJets"),
                                   debug = cms.untracked.bool(False)
                                   )

process.TreeMaker2.VectorTLorentzVector.append("ak4GenJets")

######################
# event filters
######################

process.RA2eventFilter = cms.EDFilter("RA2eventFilter",
                                      HTCollection = cms.untracked.InputTag("htNoPhotons"),
                                      minHT = cms.untracked.double(500.),
                                      MHTCollection = cms.untracked.InputTag("mhtNoPhotons"),
                                      minMHT = cms.untracked.double(200.),
                                      NJetsCollection = cms.untracked.InputTag("nJetsNoPhotons"),
#                                      minNJets = cms.untracked.int(4),
                                      BTagsCollection = cms.untracked.InputTag("BTags"),
#                                      minBTags = cms.untracked.int(0),
                                      minDeltaPhiNCollection = cms.untracked.InputTag("metNoPhotons","minDeltaPhiN"),
                                      debug = cms.untracked.bool(False)
                                      )

## CONFIGURE TFILESERVICE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile+"_RA2AnalysisTree.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

##  LOAD DATAFILES
if options.inputFilesConfig!="" :
    process.load("AWhitbeck.SuSySubstructure."+options.inputFilesConfig+"_cff")

if options.files!=[] :   
    readFiles = cms.untracked.vstring()
    readFiles.extend( options.files )
    process.source = cms.Source("PoolSource",
                                fileNames = readFiles )

##  DEFINE SCHEDULE

process.WriteTree = cms.Path( process.Baseline * 
                              process.goodElectrons4Vec * 
                              process.goodMuons4Vec *  

                              process.photonSeq *
                              
                              #process.RA2eventFilter *

                              process.genParticles * 

                              process.JetsPropertiesRaw *
                              process.ak4Jets *
                              process.ak4JetsRaw *
                              process.ak4GenJets *
                              process.HTJetsFourVec *

                              process.SumJetMass * 

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
