# experiments

###Resources:
*The folder contains deploy.txt which defines the cnn net,consolidation.csv which is the metadata and the mean image file

###Data:
*The folder contains train.txt and test.txt file which lists the name of images(named by imagehash) used for training
 and testing the model

###Approach1:
*Approach 1 is the method where we extract the feature vectors from the last second layer(fc7) and use these feature
 vectors to train a linear classifier.
*Each ipynb file is jupyter notebook referring to a particular experiment
*Other file which is required is the caffemodel weights of the pretrained cnn which can be downloaded from
 [http://dl.caffe.berkeleyvision.org/bvlc_reference_caffenet.caffemodel]
