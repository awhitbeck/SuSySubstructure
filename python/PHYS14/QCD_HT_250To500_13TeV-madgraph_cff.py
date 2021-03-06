import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/344677E1-3B6F-E411-8F29-0025905A6082.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/407299DC-3B6F-E411-8BB7-003048FFD760.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4C7BFAD9-3B6F-E411-8D2A-002618943939.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/668FA4DE-3B6F-E411-999B-0025905A6090.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/685711DF-3B6F-E411-A91F-003048FF9AC6.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9874CEDE-3B6F-E411-B601-003048FFCB84.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9A2FF7DA-3B6F-E411-84A3-002618943910.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9ADC70DC-3B6F-E411-8AF7-002618943981.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/9ED1B3DC-3B6F-E411-B2A9-003048FFD752.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CAD14ADD-3B6F-E411-915E-003048FFCB9E.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/D81A62DD-3B6F-E411-A317-0025905A6090.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/E480D0D9-3B6F-E411-B57A-0026189438EF.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F01ED9E0-3B6F-E411-A15B-0025905B8598.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F81885DD-3B6F-E411-A135-002618943910.root',
       '/store/mc/Phys14DR/QCD_HT_250To500_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F84786DA-3B6F-E411-B404-00261894390A.root' ] );


secFiles.extend( [
               ] )

