import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.topMonitoring_cfi import topMonitoring

hltSUSmonitoring = topMonitoring.clone(
  FolderName = 'HLT/SUS/default/',
  histoPSet = dict(
      lsPSet = dict(
            nbins =  2500,
            xmin  =    0.,
            xmax  =  2500.),

      metPSet = dict(
            nbins =   30 ,
            xmin  =   0 ,
            xmax  =  300),

      ptPSet = dict(
            nbins =  60 ,
            xmin  =  0 ,
            xmax  = 300 ),

      phiPSet = dict(
            nbins =  32 ,
            xmin  =  -3.2 ,
            xmax  =  3.2 ),
     
      etaPSet = dict(
            nbins =  24  ,
            xmin  =  -2.4 ,
            xmax  =  2.4 ),

      htPSet = dict(
            nbins =  60 ,
            xmin  =   0 ,
            xmax  =  600),

      # Marina
      csvPSet = dict(
            nbins = 50 ,
            xmin  =  0.0 ,
            xmax  = 1.0 ),

      #BTV
        DRPSet = dict(
             nbins = 60 ,
             xmin  = 0.0 ,
             xmax  =  6.0),


        invMassPSet = dict(
              nbins = 40 ,
              xmin  =  0.0 ,
              xmax  = 80.0 ),

        MHTPSet = dict(
              nbins =  80,
              xmin  =   60,
              xmax  =   300),
   
    #MET and HT binning
    metBinning = [0,20,40,60,80,100,125,150,175,200],
    HTBinning  = [0,20,40,60,80,100,125,150,175,200,300,400,500,700],
    #Eta binning
    eleEtaBinning = [-2.4,-2.1,-1.5,-0.9,-0.3,0.,0.3,0.9,1.5,2.1,2.4],
    jetEtaBinning = [-2.4,-2.1,-1.5,-0.9,-0.3,0.,0.3,0.9,1.5,2.1,2.4],
    muEtaBinning  = [-2.4,-2.1,-1.5,-0.9,-0.3,0.,0.3,0.9,1.5,2.1,2.4],
    #pt binning
    elePtBinning = [0,5,10,20,30,40,50,70,100,200,400],
    jetPtBinning = [0,5,10,20,30,40,50,70,100,200,400],
    muPtBinning  = [0,5,10,20,30,40,50,70,100,200,400],
    #Eta binning 2D
    eleEtaBinning2D = [-2.5,-1.5,-0.6,0.,0.6,1.5,2.5],
    jetEtaBinning2D = [-2.5,-1.5,-0.6,0.,0.6,1.5,2.5],
    muEtaBinning2D  = [-2.5,-1.5,-0.6,0.,0.6,1.5,2.5],
    #pt binning 2D
    elePtBinning2D = [0,20,30,50,100,200,400],
    jetPtBinning2D = [0,20,30,50,100,200,400],
    muPtBinning2D  = [0,20,30,50,100,200,400],
    #HT and phi binning 2D
    HTBinning2D  = [0,20,40,70,100,150,200,400,700],
    phiBinning2D = [-3.1416,-1.8849,-0.6283,0.6283,1.8849,3.1416],
  ),
  #Suvankar
  applyLeptonPVcuts = False,
  leptonPVcuts = dict(
        dxy =   9999.,
        dz  =   9999.),
  met       = "pfMet", # pfMet
  jets      = "ak4PFJetsCHS", # ak4PFJets, ak4PFJetsCHS, pfJetsEI
  electrons = "gedGsfElectrons", # while pfIsolatedElectronsEI are reco::PFCandidate !
  muons     = "muons", # while pfIsolatedMuonsEI are reco::PFCandidate !


  #Suvankar
  vertices  = "offlinePrimaryVertices",

  # Marina
  btagAlgos = ["pfCombinedSecondaryVertexV2BJetTags"],
  workingpoint = 0.8484, # Medium

  HTdefinition = 'pt>30 & abs(eta)<2.5',
  leptJetDeltaRmin = 0.4,

  numGenericTriggerEventPSet = dict(
    andOr         =  False,
    andOrHlt      = True,# True:=OR; False:=AND
    hltInputTag   = "TriggerResults::HLT",
    errorReplyHlt =  False,
    verbosityLevel = 0),

  denGenericTriggerEventPSet = dict(
    andOr         =  False,
    andOrHlt      = True,# True:=OR; False:=AND
    hltInputTag   =  "TriggerResults::HLT",
    errorReplyHlt =  False,
    dcsInputTag   =  "scalersRawToDigi",
    dcsRecordInputTag = "onlineMetaDataDigis",
    dcsPartitions = [ 24, 25, 26, 27, 28, 29], # 24-27: strip, 28-29: pixel, we should add all other detectors !
    andOrDcs      = False,
    errorReplyDcs = True,
    verbosityLevel = 0)
)
