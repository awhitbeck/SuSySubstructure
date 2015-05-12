import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

def photonSetup( process ) :

    process.TreeMaker2.VectorDouble.append("goodPhotons:isEB(photon_isEB)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:genMatched(photon_genMatched)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hadTowOverEM(photon_hadTowOverEM)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:hasPixelSeed(photon_hasPixelSeed)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIso(photon_pfChargedIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(photon_pfChargedIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIso(photon_pfGammaIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(photon_pfGammaIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIso(photon_pfNeutralIso)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(photon_pfNeutralIsoRhoCorr)")
    process.TreeMaker2.VectorDouble.append("goodPhotons:sigmaIetaIeta(photon_sigmaIetaIeta)")

    # ==========================
    # jets post photon cleaning
    # ==========================

    process.HTJetsNoPhotons = cms.EDProducer("CleanPATJetProducer",
                                             photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                             jetCollection = cms.untracked.string("HTJets"), 
                                             debug = cms.untracked.bool(False)
                                             )
    
    process.MHTJetsNoPhotons = cms.EDProducer("CleanPATJetProducer",
                                              photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                              jetCollection = cms.untracked.string("MHTJets"), 
                                              debug = cms.untracked.bool(False)
                                              )
    
    process.slimmedPhotons4Vec = cms.EDProducer("fourVectorProducer",
                                                particleCollection = cms.untracked.InputTag("slimmedPhotons"),
                                                debug = cms.untracked.bool(False)
                                                )

    process.TreeMaker2.VectorTLorentzVector.append("slimmedPhotons4Vec(photonCands)")

    process.bestPhoton4Vec = cms.EDProducer("fourVectorProducer",
                                        particleCollection = cms.untracked.InputTag("goodPhotons","bestPhoton"),
                                        debug = cms.untracked.bool(False)
                                        )
    
    process.TreeMaker2.VectorTLorentzVector.append("bestPhoton4Vec(bestPhoton)")
    process.TreeMaker2.VarsInt.append("goodPhotons:NumPhotons(NumPhotons)")
    
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
                                          cleanTag = cms.untracked.InputTag("goodPhotons","bestPhoton")
                                          )
    
    process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN1(DeltaPhiN1noPhotons)")
    process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN2(DeltaPhiN2noPhotons)")
    process.TreeMaker2.VarsDouble.append("metNoPhotons:DeltaPhiN3(DeltaPhiN3noPhotons)")
    process.TreeMaker2.VarsDouble.append("metNoPhotons:minDeltaPhiN(minDeltaPhiNnoPhotons)")
    process.TreeMaker2.VarsDouble.append("metNoPhotons:Pt(METnoPhotonsPt)")
    process.TreeMaker2.VarsDouble.append("metNoPhotons:Phi(METnoPhotonsPhi)")

    ##  DEFINE SEQUENCE

    process.photonSeq = cms.Sequence( process.slimmedPhotons4Vec *
                                      process.bestPhoton4Vec *
                                      process.HTJetsNoPhotons * 
                                      process.MHTJetsNoPhotons * 
                                      process.htNoPhotons * 
                                      process.mhtNoPhotons * 
                                      process.deltaPhiNoPhotons * 
                                      process.nJetsNoPhotons * 
                                      process.metNoPhotons 
                                      )
