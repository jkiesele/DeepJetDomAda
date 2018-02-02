from keras import backend as K



def exampleLoss(y_true, x_pred):
    
    
    dxrel=(x_pred - y_true)
    dxsq=K.square(dxrel)
    #K.clip(lossval,-1e6,1e6)
    
    return K.mean( dxsq , axis=-1)
    


global_loss_list['exampleLoss']=exampleLoss

