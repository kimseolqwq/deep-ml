import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    x=np.sum((y_pred==1) & (y_true==1))
    y=np.sum(y_true==1)
    if y==0 :
        return 0.0
    return x/y
    pass
