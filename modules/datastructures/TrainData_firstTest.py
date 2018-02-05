'''
Created on 21 Feb 2017

@author: jkiesele
'''
from TrainDataDeepJetDomAda import TrainDataDeepJetDomAda, fileTimeOut



class TrainData_firstTest(TrainDataDeepJetDomAda):
    '''
    same as TrainData_deepCSV but with 4 truth labels: B BB C UDSG
    '''


    def __init__(self):
        '''
        Constructor
        '''
        TrainDataDeepJetDomAda.__init__(self)
        
        self.addBranches(['jet_pt', 'jet_eta'])
       
        #self.addBranches(['track_pt'], 6)
        
        

    def readFromRootFile(self,filename,TupleMeanStd, weighter):
        
        weights,x_all,alltruth, _ =self.getFlavourClassificationData(filename,TupleMeanStd, weighter)
        
        self.w=[weights]
        self.x=[x_all]
        self.y=[alltruth]


