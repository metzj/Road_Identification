import numpy as np

#this function takes in two thresholds and extracts what is inbetween those. The default threshold values were found in the segmentation notebook.
def image_threshold_segmentation(img, thresholds=[0.3, 0.4]):
    output = np.zeros(img.shape)
    
    output = (np.sign(img - thresholds[0]*np.ones(img.shape)) + 1)/2
    output -= (np.sign(img - thresholds[1]*np.ones(img.shape)) + 1)/2
        
    return output