import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.SusMonitor_cfi import hltSUSmonitoring

#This is added by Pablo in order to monitor the auxiliary paths for electron fake rate calculation
susEle8CaloJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle8CaloJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>10 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,10,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,10,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle8CaloJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>10 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,10,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,10,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdL_TrackIdL_IsoVL_PFJet30_v*'])
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susEle8CaloIdMJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloIdMJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle8CaloIdMJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloIdMJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>10 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,10,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,10,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle8CaloIdMJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele8CaloIdMJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>10 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,10,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,10,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v*'])
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susEle12CaloJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele12CaloJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle12CaloJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele12CaloJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>14 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,12,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,12,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle12CaloJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele12CaloJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>14 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,12,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,12,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v*'])
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susEle17CaloIdMJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele17CaloIdMJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle17CaloIdMJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele17CaloIdMJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>19 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,19,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,19,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle17CaloIdMJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele17CaloIdMJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>19 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,19,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,19,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele17_CaloIdM_TrackIdM_PFJet30_v*']),
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susEle23CaloJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle23CaloJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>25 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle23CaloJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>14 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,12,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,12,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v*']),
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susEle23CaloIdMJet30_jet = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloIdMJet30/JetMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>50 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,50,60,80,120,200,400],
                     elePtBinning2D = [0,50,70,120,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele35_WPTight_Gsf_v*', 'HLT_Ele38_WPTight_Gsf_v*', 'HLT_Ele40_WPTight_Gsf_v*'])
)
susEle23CaloIdMJet30_ele = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloIdMJet30/ElectronMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>25 & abs(eta)<2.4',
    jetSelection = 'pt>80 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,50,60,80,120,200,400],
                     jetPtBinning2D = [0,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*']),
    denGenericTriggerEventPSet = dict(hltPaths = ['HLT_PFJet60_v*'])
)
susEle23CaloIdMJet30_all = hltSUSmonitoring.clone(
    FolderName = 'HLT/SUS/Ele23CaloIdMJet30/GlobalMonitor',
    nmuons = 0,
    nelectrons = 1,
    njets = 1,
    eleSelection = 'pt>14 & abs(eta)<2.4',
    jetSelection = 'pt>35 & abs(eta)<2.4',
    histoPSet = dict(eleEtaBinning = [-2.1,-1.5,-0.9,-0.6,-0.3,-0.1,0,0.1,0.3,0.6,0.9,1.5,2.1],
                     eleEtaBinning2D = [-2.1,-1.5,-0.6,0,0.6,1.5,2.1],
                     elePtBinning = [0,12,25,30,32.5,35,40,45,50,60,80,120,200,400],
                     elePtBinning2D = [0,12,25,30,40,50,60,80,100,200,400],
                     jetPtBinning = [0,30,35,37.5,40,50,60,80,120,200,400],
                     jetPtBinning2D = [0,30,35,40,50,60,80,100,200,400]),
    numGenericTriggerEventPSet = dict(hltPaths = ['HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*']),
    #denGenericTriggerEventPSet = dict(hltPaths = ['HLT_IsoMu24_v*'])
)
susHLTEleCaloJets = cms.Sequence(
    susEle8CaloJet30_ele
  + susEle8CaloJet30_jet
  + susEle8CaloJet30_all
  + susEle12CaloJet30_ele
  + susEle12CaloJet30_jet
  + susEle12CaloJet30_all
  + susEle23CaloJet30_ele
  + susEle23CaloJet30_jet
  + susEle23CaloJet30_all
  + susEle8CaloIdMJet30_ele
  + susEle8CaloIdMJet30_jet
  + susEle8CaloIdMJet30_all
  + susEle17CaloIdMJet30_ele
  + susEle17CaloIdMJet30_jet
  + susEle17CaloIdMJet30_all
  + susEle23CaloIdMJet30_ele
  + susEle23CaloIdMJet30_jet
  + susEle23CaloIdMJet30_all
)
