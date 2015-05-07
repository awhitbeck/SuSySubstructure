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

process.TreeMaker2.RecoCandVector = cms.vstring()

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

######################
#   edit weight stuff
######################

#from configureWeightProducer import *
#process.WeightProducer2 = configureWeightProducer(options.inputFilesConfig)
#process.WeightProducer2.Lumi                       = cms.double(4000)
#process.WeightProducer2.PU                         = cms.int32(0) # PU S10 3 for S10 2 for S7
#process.WeightProducer2.FileNamePUDataDistribution = cms.string("NONE")

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
process.TreeMaker2.VectorInt.append("genParticles:parent(genParticles_parent)")

###############
# minDeltaPhi
###############

process.minDeltaPhi = cms.EDProducer("minDeltaPhiProducer",
                                     jetCollection = cms.untracked.string("MHTJets"),
                                     metCollection = cms.untracked.string("slimmedMETs"),
                                     debug         = cms.untracked.bool(False)
                                     )

process.TreeMaker2.VarsDouble.append("minDeltaPhi(minDeltaPhi)")
process.TreeMaker2.VectorDouble.append("minDeltaPhi:deltaPhiN(deltaPhiN)")

###############
# photon stuff
###############

process.photonProd = cms.EDProducer("PhotonIDisoProducer",
                                    photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                    rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                    debug = cms.untracked.bool(False)
                                    )

process.TreeMaker2.VectorTLorentzVector.append("photonProd")
process.TreeMaker2.VectorDouble.append("photonProd:isEB(photon_isEB)")
process.TreeMaker2.VectorDouble.append("photonProd:genMatched(photon_genMatched)")
process.TreeMaker2.VectorDouble.append("photonProd:hadTowOverEM(photon_hadTowOverEM)")
process.TreeMaker2.VectorDouble.append("photonProd:hasPixelSeed(photon_hasPixelSeed)")
process.TreeMaker2.VectorDouble.append("photonProd:pfChargedIso(photon_pfChargedIso)")
process.TreeMaker2.VectorDouble.append("photonProd:pfChargedIsoRhoCorr(photon_pfChargedIsoRhoCorr)")
process.TreeMaker2.VectorDouble.append("photonProd:pfGammaIso(photon_pfGammaIso)")
process.TreeMaker2.VectorDouble.append("photonProd:pfGammaIsoRhoCorr(photon_pfGammaIsoRhoCorr)")
process.TreeMaker2.VectorDouble.append("photonProd:pfNeutralIso(photon_pfNeutralIso)")
process.TreeMaker2.VectorDouble.append("photonProd:pfNeutralIsoRhoCorr(photon_pfNeutralIsoRhoCorr)")
process.TreeMaker2.VectorDouble.append("photonProd:sigmaIetaIeta(photon_sigmaIetaIeta)")

####################
# sum jet mass 
####################

#ak12 jets
from RecoJets.JetProducers.ak5PFJets_cfi import *

process.chsPFCandidates = cms.EDFilter("CandPtrSelector", 
                                       src = cms.InputTag("packedPFCandidates"), 
                                       cut = cms.string("fromPV")
                                       )

process.ak1p2Jets = ak5PFJets.clone(src = cms.InputTag("chsPFCandidates"),
                                    rParam = cms.double(1.2),
                                    useTrimming = cms.bool(True),
                                    rFilt = cms.double(0.2),
                                    trimPtFracMin = cms.double(0.05),
                                    useExplicitGhosts = cms.bool(False)
                                    )

process.ak1p2sumJetMass = cms.EDProducer("sumJetMassProducer",
                                         jetCollection = cms.untracked.string("ak1p2Jets"),
                                         ptCut = cms.untracked.double(50.0),
                                         debug = cms.untracked.bool(False)
                                         )

process.ak1p2Jets4Vec = cms.EDProducer("fourVectorProducer",
                                       particleCollection = cms.untracked.InputTag("ak1p2Jets"),
                                       debug = cms.untracked.bool(False)
                                       )

process.TreeMaker2.VectorTLorentzVector.append("ak1p2Jets4Vec(ak1p2Jets)")
process.TreeMaker2.VarsDouble.append("ak1p2sumJetMass(ak1p2Jets_sumJetMass)")

# nsubjettiness stuff
process.nSubjettiness = cms.EDProducer("NsubjettinessProducer",
                                       jetCollection = cms.untracked.string("ak1p2Jets"),
                                       particleCollection = cms.untracked.string("chsPFCandidates"),
                                       clusterRadius = cms.untracked.double(1.2),
                                       trimPtFracMin = cms.untracked.double(0.05),
                                       trimJets = cms.untracked.bool(True),
                                       subjetPtCut = cms.untracked.double(30.),
                                       subjetMassCut = cms.untracked.double(30.),
                                       subjetRcut = cms.untracked.double(0.15),
                                       subjetPtImbalance = cms.untracked.double(0.15),
                                       debug = cms.untracked.bool(False)
                                       )

process.TreeMaker2.VectorDouble.append("nSubjettiness:tau1(ak1p2Jets_tau1)")
process.TreeMaker2.VectorDouble.append("nSubjettiness:tau2(ak1p2Jets_tau2)")
process.TreeMaker2.VectorDouble.append("nSubjettiness:tau3(ak1p2Jets_tau3)")
process.TreeMaker2.VectorDouble.append("nSubjettiness:tau4(ak1p2Jets_tau4)")
process.TreeMaker2.VectorInt.append("nSubjettiness:NumSubjets(ak1p2Jets_nSubjets)")

process.ak1p2JetsNoTrim = ak5PFJets.clone(src = cms.InputTag("chsPFCandidates"),
                                          rParam = cms.double(1.2),
                                          useTrimming = cms.bool(False),
                                          rFilt = cms.double(0.2),
                                          trimPtFracMin = cms.double(0.05),
                                          useExplicitGhosts = cms.bool(False)
                                          )

process.ak1p2NoTrimSumJetMass = cms.EDProducer("sumJetMassProducer",
                                         jetCollection = cms.untracked.string("ak1p2JetsNoTrim"),
                                         ptCut = cms.untracked.double(50.0),
                                         debug = cms.untracked.bool(False)
                                         )

process.ak1p2JetsNoTrim4Vec = cms.EDProducer("fourVectorProducer",
                                       particleCollection = cms.untracked.InputTag("ak1p2JetsNoTrim"),
                                       debug = cms.untracked.bool(False)
                                       )

#process.TreeMaker2.VectorTLorentzVector.append("ak1p2JetsNoTrim4Vec(ak1p2JetsNoTrim)")
#process.TreeMaker2.VarsDouble.append("ak1p2NoTrimSumJetMass(ak1p2JetsNoTrim_sumJetMass)")

#reclustered ak12 jets

#process.slimmedJetsPt30 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
#                                          cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -5.0'),
#                                          src = cms.InputTag("slimmedJetsLooseID")
#                                          )
from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
process.slimmedJetsPt15 = SubJetSelection.clone(
    JetTag  = cms.InputTag('slimmedJets'),
    MinPt                                                                 = cms.double(15),
    MaxEta                                                                = cms.double(5.0),
    )

process.fattenedJetsPt15 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt15"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          ptCut         = cms.untracked.double(15.),
                                          etaCut        = cms.untracked.double(5.0),
                                          debug         = cms.untracked.bool(False)
                                          )

process.fattenedJetsPt20 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt15"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          ptCut         = cms.untracked.double(20.),
                                          etaCut        = cms.untracked.double(5.0),
                                          debug         = cms.untracked.bool(False)
                                          )

process.fattenedJetsPt30 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt15"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          ptCut         = cms.untracked.double(30.),
                                          etaCut        = cms.untracked.double(5.0),
                                          debug         = cms.untracked.bool(False)
                                          )

process.TreeMaker2.VectorTLorentzVector.append("fattenedJetsPt15(ak1p2JetsPt15Reclust)")
process.TreeMaker2.VarsDouble.append("fattenedJetsPt15:sumJetMass(ak1p2JetsPt15Reclust_sumJetMass)")
process.TreeMaker2.VectorTLorentzVector.append("fattenedJetsPt20(ak1p2JetsPt20Reclust)")
process.TreeMaker2.VarsDouble.append("fattenedJetsPt20:sumJetMass(ak1p2JetsPt20Reclust_sumJetMass)")
process.TreeMaker2.VectorTLorentzVector.append("fattenedJetsPt30(ak1p2JetsPt30Reclust)")
process.TreeMaker2.VarsDouble.append("fattenedJetsPt30:sumJetMass(ak1p2JetsPt30Reclust_sumJetMass)")

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

# ==========================
# jets post photon cleaning
# ==========================

process.HTJetsNoPhotons = cms.EDProducer("CleanPATJetProducer",
                                         photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                         jetCollection = cms.untracked.string("HTJets"), 
                                         rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                         debug = cms.untracked.bool(False)
                                         )

process.MHTJetsNoPhotons = cms.EDProducer("CleanPATJetProducer",
                                          photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                          jetCollection = cms.untracked.string("MHTJets"), 
                                          rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                          debug = cms.untracked.bool(False)
                                          )

process.bestPhoton = cms.EDProducer("fourVectorProducer",
                                    particleCollection = cms.untracked.InputTag("HTJetsNoPhotons","bestPhoton"),
                                    debug = cms.untracked.bool(False)
                                    )

process.TreeMaker2.VectorTLorentzVector.append("bestPhoton(bestPhoton)")
process.TreeMaker2.VarsInt.append("HTJetsNoPhotons:NumPhotons(Photons)")

process.HTJetsFourVec = cms.EDProducer("fourVectorProducer",
                                       particleCollection = cms.untracked.InputTag("HTJetsNoPhotons"),
                                       debug = cms.untracked.bool(False)
                                       )

process.TreeMaker2.VectorTLorentzVector.append("HTJetsFourVec(ak4JetsNoPhotons)")

process.htNoPhotons = cms.EDProducer("HTDouble",
                                     JetTag = cms.InputTag("HTJetsNoPhotons")
                                     )

process.TreeMaker2.VarsDouble.append("htNoPhotons(HTnoPhotons)")

process.mhtNoPhotons = cms.EDProducer("MhtDouble",
                                      JetTag = cms.InputTag("MHTJetsNoPhotons")
                                      )

process.TreeMaker2.VarsDouble.append("mhtNoPhotons(MHTnoPhotons)")

process.deltaPhiNoPhotons = cms.EDProducer("DeltaPhiDouble",
                                      MHTJets = cms.InputTag("MHTJetsNoPhotons"),
                                      DeltaPhiJets = cms.InputTag("MHTJetsNoPhotons")
                                      )

process.TreeMaker2.VarsDouble.append("deltaPhiNoPhotons:DeltaPhi1(DeltaPhi1noPhotons)")
process.TreeMaker2.VarsDouble.append("deltaPhiNoPhotons:DeltaPhi2(DeltaPhi2noPhotons)")
process.TreeMaker2.VarsDouble.append("deltaPhiNoPhotons:DeltaPhi3(DeltaPhi3noPhotons)")

process.nJetsNoPhotons = cms.EDProducer("NJetInt",
                                      JetTag = cms.InputTag("HTJetsNoPhotons")
                                      )

process.TreeMaker2.VarsInt.append("nJetsNoPhotons(NJetsNoPhotons)")

process.metNoPhotons = cms.EDProducer("METDouble",
                                      METTag   = cms.InputTag("slimmedMETs"),
                                      JetTag   = cms.InputTag("MHTJetsNoPhotons"),
                                      cleanTag = cms.untracked.InputTag("HTJetsNoPhotons","bestPhoton")
                                      )

process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN1(DeltaPhiN1noPhotons)")
process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN2(DeltaPhiN2noPhotons)")
process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN3(DeltaPhiN3noPhotons)")
process.TreeMaker2.VarsDouble.append("metNoPhotons:minDeltaPhiN(minDeltaPhiNnoPhotons)")
process.TreeMaker2.VarsDouble.append("metNoPhotons:Pt(METnoPhotonsPt)")
process.TreeMaker2.VarsDouble.append("metNoPhotons:Phi(METnoPhotonsPhi)")

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
                              #process.LostLepton *
                              process.goodElectrons4Vec * 
                              process.goodMuons4Vec *  
                              process.minDeltaPhi *
                              process.JetsPropertiesRaw *
                              process.HTJetsNoPhotons * 
                              process.MHTJetsNoPhotons * 
                              process.htNoPhotons * 
                              process.mhtNoPhotons * 
                              process.deltaPhiNoPhotons * 
                              process.nJetsNoPhotons * 
                              process.metNoPhotons *
                              process.bestPhoton *
                              
                              #process.RA2eventFilter *

                              process.genParticles * 
                              process.photonProd *
                              process.chsPFCandidates *
                              process.ak4Jets *
                              process.ak4JetsRaw *
                              process.ak1p2Jets * 
                              process.ak1p2sumJetMass * 
                              process.nSubjettiness *
                              process.ak1p2Jets4Vec *
                              #process.ak1p2JetsNoTrim *
                              #process.ak1p2NoTrimSumJetMass * 
                              #process.ak1p2JetsNoTrim4Vec *
                              process.slimmedJetsPt15 * 
                              process.fattenedJetsPt30 * 
                              process.fattenedJetsPt20 * 
                              process.fattenedJetsPt15 *
                              process.ak4GenJets *
                              process.HTJetsFourVec *

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
