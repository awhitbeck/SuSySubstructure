import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/12284DB9-4227-E511-A438-02163E013674.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/164/00000/402F0995-A326-E511-86BB-02163E013948.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/167/00000/70C4A781-A826-E511-95B4-02163E013414.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/168/00000/627E9C65-DD26-E511-87FB-02163E013576.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/244/00000/E42FEF61-6E27-E511-B93A-02163E0143C0.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/251/00000/0292F6F9-8A27-E511-9074-02163E012213.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/252/00000/9ADEE140-9C27-E511-919A-02163E011D23.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/493/00000/323EBCB2-D428-E511-86E5-02163E01463E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/497/00000/826586F3-FC28-E511-89EE-02163E01340A.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/498/00000/20B6D9C3-FE28-E511-BD2D-02163E0117FF.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/499/00000/EA52602B-0929-E511-AB5B-02163E011955.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/500/00000/4897C658-4129-E511-AA73-02163E0135F3.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/521/00000/B4B3A942-6429-E511-8A0C-02163E01413E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/PromptReco-v1/000/251/522/00000/E817E288-5C29-E511-9EDC-02163E011A5A.root' ] );


secFiles.extend( [
               ] )
