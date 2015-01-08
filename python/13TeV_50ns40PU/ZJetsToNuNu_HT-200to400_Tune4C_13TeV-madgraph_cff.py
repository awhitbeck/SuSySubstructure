import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0067608D-4C1E-E411-9CBE-0025905A60F8.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/006FC287-4C1E-E411-8957-0025905A6136.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/00D9C4D9-4C1E-E411-9690-002618943870.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0604C0E0-4B1E-E411-8041-0025905A6092.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0614A7E9-4B1E-E411-966F-0025905A60BE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/06CC6667-4C1E-E411-A411-0025905A612A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/084C28C9-4C1E-E411-9247-002590593878.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0862FA95-4C1E-E411-A561-0025905A6122.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0AA40EEE-4B1E-E411-8022-0025905B8598.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0AFBD9D9-4C1E-E411-AA93-0025905A60CE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0CD2BE85-4C1E-E411-9534-0025905A612A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1079CE01-4D1E-E411-B2AD-0025905A608C.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1ED0B5D3-4C1E-E411-BD53-0025905A607A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/28C20A79-4C1E-E411-B8E6-0025905B8592.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2A165A24-4C1E-E411-BA8A-0025905A608A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2A42367B-4C1E-E411-AE1E-0026189438D5.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2A8C2D85-4C1E-E411-AF27-0025905A612A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2AFC3E2B-4D1E-E411-9F76-00259059391E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2C3E88E0-4B1E-E411-B50E-0026189438D5.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2EC0A637-4D1E-E411-A684-0025905B8590.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/30411335-4C1E-E411-AE81-0025905964CC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/307EF088-4C1E-E411-8818-0025905A60FE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/326910FA-4B1E-E411-8C31-0026189438E2.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/328DBDD8-4B1E-E411-83EC-00261894396D.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3409A0D1-4C1E-E411-8F61-0025905A608C.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/347C63C8-4C1E-E411-8BF0-0025905964BE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/34F0F52A-4D1E-E411-B2B6-0025905A60AA.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/38C3CBE8-4B1E-E411-BB5E-0026189438C4.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4016A1DB-4B1E-E411-8DF9-0025905A60E0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4247B209-4D1E-E411-832E-0025905A48BA.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/42736BF7-4C1E-E411-A30A-003048FFCB74.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4A2B3C85-4C1E-E411-8B5B-0025905B8582.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4C776C2F-4C1E-E411-B1A7-0025905A60F4.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4CBD2723-4D1E-E411-BDF8-002590596468.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4EC2E388-4C1E-E411-A3D4-0025905A60FE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5016A02A-4D1E-E411-9F3D-0025905A60F4.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/50398040-4D1E-E411-843A-002590593872.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/52042700-4C1E-E411-AF6D-0025905938AA.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5406AC2A-4D1E-E411-A252-0025905A60F4.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5602B448-4C1E-E411-81BE-0025905B85D6.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/56093F2A-4C1E-E411-9502-0025905B8582.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5615870C-4D1E-E411-81B4-0025905A612E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5A58932C-4D1E-E411-8033-0025905A48C0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5C924AE0-4B1E-E411-861C-0025905A607E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/606B4F8F-4C1E-E411-AA55-0025905A60F2.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/60CD798A-4C1E-E411-8C4D-00248C55CC40.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6260A286-4C1E-E411-B350-003048D15D48.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/64481C2C-4D1E-E411-908B-003048FFCB96.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6619C4F8-4B1E-E411-A281-0025905A6056.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/661F647F-4C1E-E411-89F1-0025905A612E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/66591F85-4C1E-E411-9448-0025905A612A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6ED0D400-4C1E-E411-AD71-0025905A48BA.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/722A708E-4C1E-E411-906B-0025905A605E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7404338B-4C1E-E411-AC18-0025905A60BE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/74183920-4D1E-E411-B01D-0025905B8592.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7432C3A9-4C1E-E411-AFE1-003048FFD7BE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/745AF6D5-4C1E-E411-9B0F-0025905A6122.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/74686D51-4C1E-E411-A52B-00261894398C.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/766D788A-4C1E-E411-BCFE-00248C55CC40.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/78349121-4C1E-E411-AA6C-00261894391B.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/78A561E4-4C1E-E411-B7BF-0025905A60CE.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7A90DC81-4C1E-E411-B204-0026189437EC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7C661085-4C1E-E411-859D-0025905A612A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/822F362B-4D1E-E411-B81D-0025905A60F4.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8427EAFB-4B1E-E411-B4F4-00259059391E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/84E6C038-4C1E-E411-B39B-0025905A6080.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8C96E1A0-4C1E-E411-86ED-00259059642A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9000A4D5-4B1E-E411-9E6F-003048D25BA6.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/90E8A18A-4C1E-E411-BCA8-00248C55CC40.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9C6273F6-4C1E-E411-B3FD-002618943874.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9EBD46FE-4B1E-E411-A3D6-0025905A6136.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9EEC4642-4C1E-E411-9653-003048FFD7A2.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A07AF9E1-4B1E-E411-96E1-0026189437F0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A6C6164A-4C1E-E411-89B1-0025905A6088.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A6F47B43-4C1E-E411-A37F-0025905964CC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A8941809-4D1E-E411-9136-003048D15DF0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AADC01FA-4B1E-E411-895C-0025905A607A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AE50284C-4C1E-E411-A876-0025905B8592.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B01502E7-4C1E-E411-801B-002590596484.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B0F689CE-4C1E-E411-A068-002618943894.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B23B788A-4C1E-E411-96D0-00248C55CC40.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B6AADD89-4C1E-E411-8A70-00261894386A.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B6B07FA0-4C1E-E411-9AA4-0025905A60A6.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BAF590D7-4C1E-E411-A07D-002590596498.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BCBD1BBF-4C1E-E411-9C23-003048FFD744.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BEA80C73-4C1E-E411-BBAB-0025905A6084.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BED27002-4D1E-E411-9A2C-0026189437F0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C003584D-4C1E-E411-BEC1-0025905A60E0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C415E5FF-4B1E-E411-8E63-00248C0BE005.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C48D670E-4D1E-E411-9DAD-0025905A6080.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C4E258DD-4B1E-E411-9129-002618943870.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C4FBC867-4C1E-E411-B175-0025905964CC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C8FEE458-4C1E-E411-AA44-0025905A6060.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CA7F7D28-4D1E-E411-8B80-0025905A6118.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CE69B233-4C1E-E411-B229-0025905A4964.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CE6CC9FA-4C1E-E411-A513-0025905A6126.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CEED1079-4C1E-E411-8CFE-0025905B8592.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D0692AE2-4B1E-E411-9F45-0025905A6136.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D659CDD9-4C1E-E411-983C-0025905964A6.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D87DDF6F-4C1E-E411-ACE8-0025905A6136.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DAF5114B-4C1E-E411-8224-003048FFD728.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DCE46349-4C1E-E411-BE2B-002590596498.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DCEC30A1-4C1E-E411-AA8C-0025905A6092.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DE1550CF-4C1E-E411-ABA5-0025905A6118.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DECA4C91-4C1E-E411-A80D-003048FFCC2C.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E0C582D7-4B1E-E411-B589-002618943874.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E0F60370-4C1E-E411-A485-0026189438D5.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E2B719F2-4B1E-E411-A01D-0025905A60BC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E4922392-4C1E-E411-9CF1-0025905A611C.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E4AFCF23-4C1E-E411-8706-002354EF3BDC.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E4B3EF9A-4C1E-E411-A484-00259059642E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/EA265B34-4C1E-E411-A8D8-003048FFCB74.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F08FBB55-4C1E-E411-952C-003048FFD744.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F205FEF4-4C1E-E411-A72C-0025905A6094.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F4D4652F-4D1E-E411-9572-0025905A608E.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F64D932C-4D1E-E411-94AA-0025905A48C0.root',
       '/store/results/susy/StoreResults/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FA029883-4C1E-E411-BA2B-0026189438A9.root' ] );


secFiles.extend( [
               ] )
