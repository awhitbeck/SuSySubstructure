import sys,os

flist = [
'/DoubleEG/Run2015B-PromptReco-v1/MINIAOD',
'/DoubleMuon/Run2015B-PromptReco-v1/MINIAOD', 
'/EGamma/Run2015B-PromptReco-v1/MINIAOD',
'/SingleElectron/Run2015B-PromptReco-v1/MINIAOD',
'/SingleMu/Run2015B-PromptReco-v1/MINIAOD',
'/SingleMuon/Run2015B-PromptReco-v1/MINIAOD',
'/SinglePhoton/Run2015B-PromptReco-v1/MINIAOD',
'/HTMHT/Run2015B-PromptReco-v1/MINIAOD'
]

for f in flist:
    cmd="wget --no-check-certificate --output-document="+f.split('/')[1]+"_cff.py \"https://cmsweb.cern.ch/das/makepy?dataset="+f+"&instance=prod/global\""
    print cmd
    os.system(cmd)
