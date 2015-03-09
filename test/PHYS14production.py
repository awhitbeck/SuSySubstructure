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

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeTreeFromMiniADO
makeTreeTreeFromMiniADO(process,
                        outFileName="ReducedSelection",
                        reportEveryEvt=options.reportEvery,
                        testFileName="",
                        Global_Tag="PHYS14_25_V2::All",
                        lostlepton=False,
                        gammajets=False,
                        numProcessedEvt=options.numEvents
                        )

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

process.TreeMaker2.VectorTLorentzVector.append("ak1p2JetsNoTrim4Vec(ak1p2JetsNoTrim)")
process.TreeMaker2.VarsDouble.append("ak1p2NoTrimSumJetMass(ak1p2JetsNoTrim_sumJetMass)")

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
                                   particleCollection = cms.untracked.InputTag("slimmedJets"),
                                   debug = cms.untracked.bool(False)
                                   )

process.TreeMaker2.VectorTLorentzVector.append("ak4Jets")

process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminator(ak4Jets_CSVdisc)")
process.TreeMaker2.VectorDouble.append("JetsProperties:chargedHadronEnergyFraction(ak4Jets_chargeHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:neutralHadronEnergyFraction(ak4Jets_neutralHadEfrac)")
process.TreeMaker2.VectorDouble.append("JetsProperties:photonEnergyFraction(ak4Jets_photonEfrac)")
process.TreeMaker2.VectorInt.append("JetsProperties:chargedHadronMultiplicity(ak4Jets_chargedHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:neutralHadronMultiplicity(ak4Jets_neutralHadMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:photonMultiplicity(ak4Jets_photonMult)")
process.TreeMaker2.VectorInt.append("JetsProperties:flavor(ak4Jets_flavor)")

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
                              process.minDeltaPhi *
                              process.genParticles * 
                              process.photonProd *
                              process.chsPFCandidates *
                              process.ak4Jets *
                              process.ak1p2Jets * 
                              process.ak1p2sumJetMass * 
                              process.nSubjettiness *
                              process.ak1p2Jets4Vec *
                              process.ak1p2JetsNoTrim *
                              process.ak1p2NoTrimSumJetMass * 
                              process.ak1p2JetsNoTrim4Vec *
                              process.slimmedJetsPt15 * 
                              process.fattenedJetsPt30 * 
                              process.fattenedJetsPt20 * 
                              process.fattenedJetsPt15 *
                              process.ak4GenJets *
                              #process.JetsProperties *
                              process.HTJetsNoPhotons * 
                              process.MHTJetsNoPhotons * 
                              process.htNoPhotons * 
                              process.mhtNoPhotons * 
                              process.deltaPhiNoPhotons * 
                              process.nJetsNoPhotons * 
                              process.metNoPhotons *
                              process.bestPhoton *

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
