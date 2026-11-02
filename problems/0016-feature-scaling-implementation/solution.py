import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	mean=np.mean(data,axis=0,keepdims=True)
	std=np.std(data,axis=0,keepdims=True)
	standardized_data=(data-mean)/std

	min_val=np.min(data,axis=0,keepdims=True)
	max_val=np.max(data,axis=0,keepdims=True)
	normalized_data=(data-min_val)/(max_val-min_val)





	return np.round(standardized_data,4), np.round(normalized_data,4)