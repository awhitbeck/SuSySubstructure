import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/08158E31-1023-E411-924C-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/1201034C-0823-E411-9894-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/12C4B6C4-FF22-E411-9361-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/12EB20B2-1223-E411-9BA3-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/14AF4FD7-0723-E411-9C70-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/167E39CC-1123-E411-B88C-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/24E754DE-1223-E411-9969-002590DE6E30.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/26E845F1-0623-E411-9477-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/28340BB8-FF22-E411-BF90-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/3070A929-0623-E411-ACAD-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/329FD1D3-1623-E411-94EC-002590DE6E3C.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/34C33729-0323-E411-91A6-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/3A5BCB3D-1223-E411-8A1C-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/4ACFC81D-0623-E411-91DB-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/5E217FA0-1123-E411-B8FE-00266CF3E174.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/74E798A6-0623-E411-A8DD-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/7C942D98-1123-E411-A2E6-002590DE6E30.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/80C281BD-0123-E411-A00B-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/86910399-0B23-E411-B4D5-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/92E1BA8A-0B23-E411-8407-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/94CE13E7-0723-E411-BDA9-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/A03E42E8-1023-E411-B7A9-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/A413483F-FE22-E411-BBC2-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/AEC84B39-0023-E411-87C1-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B0FD2216-1F23-E411-9F47-003048C3E7F7.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B6176824-0623-E411-A207-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/B848EA14-0623-E411-BAAB-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/BE024839-0023-E411-9A8E-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/C231B638-0023-E411-84FD-002590DD61E0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/C27CE6C6-0523-E411-B2BE-003048C3E7ED.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/C89D991C-1223-E411-972D-D8D385FF35F1.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D063834B-0823-E411-9D45-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D0C23E39-0023-E411-8175-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/D403AA72-0C23-E411-A86A-002590DE6E3C.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/DCAA3C16-1323-E411-8BF2-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E248F683-0623-E411-8A0B-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/E4531095-0023-E411-A18B-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/EAB1AAD6-1A23-E411-BA96-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/F032EAD7-0723-E411-AE35-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/F0462967-1123-E411-8700-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/F49877B4-0123-E411-9D12-002590DD61E0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/F811CEF3-0723-E411-8BB8-003048C3E7ED.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/20000/44EC56B3-5624-E411-AB47-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/20000/6E6B5899-5724-E411-A7A3-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/20000/D8415A92-5824-E411-8EA5-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/0453C030-2723-E411-B368-D8D385FF35F1.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/06C88039-0F23-E411-8AE6-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/0EE37402-0C23-E411-86DB-002590DE6E3C.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/10C40305-1023-E411-AFA8-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/10C71DFB-0B23-E411-9D00-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/10D96FF1-0623-E411-B3C9-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/123F3BC6-0823-E411-9533-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/1E1C0229-0A23-E411-8670-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/1E7E9241-0923-E411-9DA3-003048C3E7ED.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/1EB4E5D2-FD22-E411-9673-D8D385FF35F1.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/1EE145AE-0D23-E411-825D-002590DE6E30.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/2634764D-1023-E411-A31C-D8D385FF35F1.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/2AC48ED0-0823-E411-A683-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/3005C39B-2623-E411-A68C-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/36113799-1623-E411-821A-002590DE6E3C.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/3668CE1A-1523-E411-BC84-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/4E99323C-0F23-E411-BCE0-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/50C5883D-0C23-E411-83B1-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/56FB3444-0923-E411-8E11-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/5A2BA6D6-0823-E411-891E-002590DE6E3C.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/62134BC9-0823-E411-87BE-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/6AA4F840-0923-E411-BF60-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/6C6633D9-0823-E411-8EC0-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/6E5EB040-0C23-E411-97FB-002590DE6E30.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/6EAFD2FD-0D23-E411-B097-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/702C78D5-1123-E411-A7C5-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/724DA071-2023-E411-ACBB-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/7A032343-0923-E411-B12D-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/7E51ACB8-0D23-E411-A889-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/7E66ED2E-0F23-E411-A2F1-002590DE6E30.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/7E958294-0D23-E411-826C-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/80073540-0923-E411-AD4F-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/8272F341-1323-E411-BFDF-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/84914F59-1023-E411-BC64-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/9C03CCB0-2023-E411-A5E1-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/9E4EF55D-2023-E411-924B-D8D385FF35F1.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/9EB10FDB-1123-E411-9C84-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/A2B818AF-1023-E411-A2DE-002590DE38C8.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/A4BA26C8-0823-E411-B1D7-002590DE6E8A.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/AE703440-0923-E411-92BE-002590DE6C56.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/AEC12469-0D23-E411-9498-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/B68BD5E6-0723-E411-8F2A-002590DD7CD4.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/B8294EE9-0F23-E411-ADB2-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/B841A765-0923-E411-AEB9-002590DD7CD4.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/BC22C7FD-2023-E411-8623-003048C3E7F7.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/BC550CFC-0923-E411-A8F7-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/C66DEC40-0923-E411-8C1D-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/C6E90487-0B23-E411-8E05-D8D385FF344D.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/C8F8B88A-0B23-E411-8997-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/CC450A55-0823-E411-84F7-002590DE39F0.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/CC7A926D-0F23-E411-AC7E-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/CE97CB6B-1323-E411-B477-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/D2862F94-1623-E411-A888-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/D8179D3D-0923-E411-BE2A-002590DD7C9E.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/D84A8AF7-1F23-E411-A3FC-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/DA465DC1-1B23-E411-B5B7-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/DCCC80CF-1123-E411-A62A-D8D385AE9F79.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/DE5E6F3C-0923-E411-8A51-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/E4352DAB-0E23-E411-BA07-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/EC3963B8-1423-E411-AAB5-002590DE3A92.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/EC3B0486-0823-E411-9B37-002590DE6E28.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/F65C720A-0923-E411-A448-002590DE6E8A.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/FC85165F-0E23-E411-B095-00266CF3E0FC.root',
       '/store/mc/Spring14miniaod/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/30000/FEAEED0C-0E23-E411-952B-D8D385AE9F79.root' ] );


secFiles.extend( [
               ] )
