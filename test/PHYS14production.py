import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

process = cms.Process("analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

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

###############
# tree maker
###############

from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
process = makeTreeFromMiniAOD(process,
                    outfile=options.outputFile+"_RA2AnalysisTree",
                    reportfreq=options.reportEvery,
                    dataset=readFiles,
                    globaltag="PHYS14_25_V2::All",
                    lostlepton=True,
                    hadtau=True,
                    tagandprobe=False,
                    numevents=options.numEvents,
                    doZinv=True,
                    debugtracks=False,
                    geninfo=True,
                    tagname="PAT",
                    jsonfile="",
                    applyjec=False
                    )

process.options   = cms.untracked.PSet(
    SkipEvent   = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
    )

## CONFIGURE TFILESERVICE

process.TFileService.closeFileFast = cms.untracked.bool(True)

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

# ==================
# rho stuff
# ==================

process.TreeMaker2.VarsDouble.append("fixedGridRhoFastjetAll(rho)")

# ==================
# fat jet stuff 
# ==================

#from AWhitbeck.SuSySubstructure.fatJetStudies_cff import *
#process = fatJetSetup(process) ## define relevant modules and a sequence to be used, process.SumJetMass
#process.AdditionalSequence += process.SumJetMass ## add process.SumJetMass to sequence

# ==================
# ak4 jets
# ==================

#process.TreeMaker2.VectorRecoCand.append("GoodJets(ak4Jets)")
#process.TreeMaker2.VectorRecoCand.append("slimmedJets(ak4JetsRaw)")
#process.TreeMaker2.VectorInt.append("GoodJets:passJetID(ak4Jets_passedJetID)")

#process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorUser(ak4Jets_CSVdisc)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorMVA(ak4Jets_MVAdisc)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:bDiscriminatorSimpleCSV(ak4Jets_SimpleCSVdisc)")

#process.TreeMaker2.VectorInt.append("JetsProperties:NumBhadrons(ak4Jets_NumBhadrons)")
#process.TreeMaker2.VectorInt.append("JetsProperties:NumChadrons(ak4Jets_NumChadrons)")

#process.TreeMaker2.VectorDouble.append("JetsProperties:chargedHadronEnergyFraction(ak4Jets_chargeHadEfrac)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:neutralHadronEnergyFraction(ak4Jets_neutralHadEfrac)")
#process.TreeMaker2.VectorDouble.append("JetsProperties:photonEnergyFraction(ak4Jets_photonEfrac)")
#process.TreeMaker2.VectorInt.append("JetsProperties:chargedHadronMultiplicity(ak4Jets_chargedHadMult)")
#process.TreeMaker2.VectorInt.append("JetsProperties:neutralHadronMultiplicity(ak4Jets_neutralHadMult)")
#process.TreeMaker2.VectorInt.append("JetsProperties:photonMultiplicity(ak4Jets_photonMult)")
#process.TreeMaker2.VectorInt.append("JetsProperties:flavor(ak4Jets_flavor)")

### ak4 gen jets
#process.TreeMaker2.VectorRecoCand.append("slimmedGenJets(ak4GenJets)")
