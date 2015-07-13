import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/096/00000/8A2D533C-5626-E511-AF3C-02163E011FAB.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/161/00000/AC857A3B-9C26-E511-B32E-02163E012704.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/162/00000/BE906A2C-4327-E511-8014-02163E0121CC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/163/00000/9CB965BF-9F26-E511-8FB1-02163E012040.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/164/00000/2CA2349A-A526-E511-A371-02163E0138D0.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/167/00000/C446EC67-A726-E511-81C1-02163E0119E7.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/168/00000/747F782A-BB26-E511-BA24-02163E011EE9.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/6A0A8868-4B27-E511-B3F8-02163E011BD1.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/7E66D014-D628-E511-9D1E-02163E012603.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/84B7599F-4E27-E511-9DEC-02163E014509.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/C47A9CF9-6227-E511-908E-02163E014509.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/E8FEB382-3228-E511-8B4D-02163E0133E3.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/244/00000/F2D83438-6927-E511-A22B-02163E01182A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/251/00000/4AA28544-9027-E511-AEF5-02163E01472B.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/251/00000/E6F7FA3F-7E27-E511-B271-02163E014181.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/2672D59D-B827-E511-BB31-02163E01358B.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/3866DC22-8627-E511-8700-02163E01463E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/4A3B62E0-8D27-E511-9EC6-02163E0140E1.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/8A8CCAA5-8827-E511-A64E-02163E014558.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/8CE81C36-8427-E511-9817-02163E0127D3.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/252/00000/F0686F9B-BA27-E511-82C7-02163E0142FD.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/491/00000/EAD8F705-C628-E511-A141-02163E0133B6.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/493/00000/324A1F04-C928-E511-AE77-02163E011ABC.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/497/00000/66FC7B3B-E028-E511-AB85-02163E01463E.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/498/00000/6A6EB96C-EC28-E511-8B71-02163E01340C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/499/00000/D89CF3FD-F728-E511-AC0C-02163E0136CF.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/500/00000/3E3DEF56-2429-E511-8E40-02163E0128FE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/521/00000/7CA3211F-8F29-E511-BE9E-02163E0133E3.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/522/00000/7853D0B3-8B29-E511-8B13-02163E012073.root' ] );


secFiles.extend( [
               ] )
