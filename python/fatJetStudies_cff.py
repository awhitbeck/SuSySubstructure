import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

#process = cms.Process("analysis")

def fatJetSetup( process ):

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
    
    process.TreeMaker2.VectorRecoCand.append("ak1p2Jets")
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
    
    #process.TreeMaker2.VectorRecoCand.append("ak1p2JetsNoTrim")
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
    
    ##  DEFINE SEQUENCE
    process.SumJetMass = cms.Sequence(process.chsPFCandidates *
                                      process.ak1p2Jets * 
                                      process.ak1p2sumJetMass * 
                                      process.nSubjettiness *
                                      #process.ak1p2JetsNoTrim *
                                      #process.ak1p2NoTrimSumJetMass * 
                                      process.slimmedJetsPt15 * 
                                      process.fattenedJetsPt30 * 
                                      process.fattenedJetsPt20 * 
                                      process.fattenedJetsPt15 
                                      )

    return process
    