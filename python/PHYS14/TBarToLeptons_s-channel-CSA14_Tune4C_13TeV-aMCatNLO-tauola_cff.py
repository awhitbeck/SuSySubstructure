import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/02520655-8B70-E411-8E0A-485B39800BFB.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04864D4B-8B70-E411-8219-002590D0AF66.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/20A3F07E-8A70-E411-88DD-485B39800B62.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/6E5E955C-AE70-E411-BFF8-E0CB4E19F9BC.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/74073559-AE70-E411-A8B1-485B39800BFB.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F8624749-8B70-E411-A424-E0CB4E29C4F6.root',
       '/store/mc/Phys14DR/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FA0E1127-8B70-E411-A626-E0CB4E553642.root' ] );


secFiles.extend( [
               ] )

