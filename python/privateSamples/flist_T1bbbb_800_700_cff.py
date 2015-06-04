import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

for i in xrange(0,100):
    readFiles.extend(['/store/user/pedrok/SUSY2015/T1bbbb/step5/step5_T1bbbb_800_700_n1000_part%s.root'%(i+1)])

secFiles.extend( [
               ] )
