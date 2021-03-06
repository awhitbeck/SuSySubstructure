import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/WH_HToBB_WToLNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/12328AE8-796B-E411-9D32-002590A831B4.root',
       '/store/mc/Phys14DR/WH_HToBB_WToLNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/6826B3A7-796B-E411-805C-002481E150C2.root',
       '/store/mc/Phys14DR/WH_HToBB_WToLNu_M-125_13TeV_powheg-herwigpp/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/72ABD9A1-796B-E411-A212-002590200B3C.root' ] );


secFiles.extend( [
               ] )

