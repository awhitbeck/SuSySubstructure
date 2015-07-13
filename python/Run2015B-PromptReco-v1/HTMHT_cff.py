import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/161/00000/8412AF15-9C26-E511-93AD-02163E014254.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/162/00000/CA6877F1-4127-E511-99FE-02163E0133F0.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/163/00000/8EA8A101-A026-E511-95FD-02163E0146EB.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/164/00000/589EF4FA-A226-E511-9E8E-02163E014437.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/167/00000/D6B0973F-A826-E511-A7D8-02163E0125E8.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/168/00000/FEB9B9F8-D226-E511-974B-02163E01412F.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/244/00000/D224B8E7-6427-E511-B922-02163E012284.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/251/00000/E6BA5ADA-9327-E511-8936-02163E012213.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/252/00000/9AB824FB-A627-E511-92B3-02163E012AA4.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/493/00000/682CF925-C928-E511-9B6A-02163E012603.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/497/00000/8C68CAD7-E028-E511-B0F8-02163E012283.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/498/00000/7C1AFB0F-EF28-E511-B264-02163E01445F.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/499/00000/F8B56DF1-F628-E511-8862-02163E014729.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/500/00000/A4639A5E-2629-E511-B564-02163E011C7F.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/521/00000/7C9781A0-5F29-E511-9877-02163E013432.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/522/00000/BCFCA4F1-5929-E511-B6CC-02163E0133A4.root' ] );


secFiles.extend( [
               ] )
