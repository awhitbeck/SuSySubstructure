import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/096/00000/EAC7605D-5526-E511-A895-02163E011FAB.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/161/00000/6E54E224-9C26-E511-B468-02163E0121BD.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/162/00000/D83F99AD-4227-E511-8960-02163E0133B5.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/163/00000/728A4697-9F26-E511-ADAD-02163E0119C9.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/164/00000/80F01937-A426-E511-B2D7-02163E01182A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/167/00000/A6972749-A826-E511-B7C5-02163E013414.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/168/00000/3CBFC5DE-BB26-E511-A5C2-02163E0135B4.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/244/00000/D8D780D0-7727-E511-A2C5-02163E0137FC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/251/00000/6EED993F-9927-E511-A6A9-02163E01259F.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/252/00000/289A42F1-9627-E511-8A00-02163E011C7F.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/491/00000/9C464F2A-C628-E511-8923-02163E01463E.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/493/00000/6819E5CA-C828-E511-AD4E-02163E0135F3.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/497/00000/D43AFD8F-E028-E511-8467-02163E01414A.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/498/00000/969A3EAE-EB28-E511-B91A-02163E012601.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/499/00000/5EEEB744-F728-E511-8E47-02163E013440.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/500/00000/1838372C-2329-E511-8E7B-02163E011BD1.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/521/00000/9A3A76CA-6629-E511-8B2E-02163E011EE9.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/PromptReco-v1/000/251/522/00000/9297A416-5B29-E511-8956-02163E014543.root' ] );


secFiles.extend( [
               ] )
