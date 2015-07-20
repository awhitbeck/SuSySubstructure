import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/ZH_HToBB_ZToNuNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/32ABFE4A-916B-E411-B2FA-00266CFFBC60.root',
       '/store/mc/Phys14DR/ZH_HToBB_ZToNuNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/DA048446-916B-E411-9DEE-C4346BC8C310.root',
       '/store/mc/Phys14DR/ZH_HToBB_ZToNuNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/54CBC5EF-EC6B-E411-87BB-008CFA051DA8.root' ] );


secFiles.extend( [
               ] )

