import os
import sys
import numpy as np
import struct
import caffe

def printUsageAndExit():
    print("Usage: feature-vectors image-directory caffe-deploy caffe-model mean-image-npy layer-name output-directory")
    sys.exit(1)

if len(sys.argv) != 7:
    printUsageAndExit()

imageDirectory = sys.argv[1]
imageMeanFile = sys.argv[4]
layerName = sys.argv[5]
outputDirectory=sys.argv[6]

print("Loading model")
cnn = caffe.Net(sys.argv[2], caffe.TEST, weights=sys.argv[3])
print("Done loading")

if layerName not in cnn.blobs:
    print("Invalid layer name: %s" % layerName)
    printUsageAndExit()

# reshape to accept one image at a time.
(_, c, w, h) = cnn.blobs['data'].data.shape
cnn.blobs['data'].reshape(1, c, w, h)
transformer = caffe.io.Transformer({'data': cnn.blobs['data'].data.shape})
transformer.set_mean('data', np.load(imageMeanFile).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_raw_scale('data', 255.0)




def uploadFeatureVector(imageFile, layerName, d):
        fullImagePath=os.path.join(imageDirectory,imageFile)
        cnn.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(fullImagePath))
        cnn.forward()
        featureVector = cnn.blobs[layerName].data[0]
        assert(len(featureVector) == d)
        fullOutputPath=os.path.join(outputDirectory,imageFile)
        if os.path.isfile(fullOutputPath)==False: 
           fout=open(fullOutputPath,'wb')
           fout.write(struct.pack('f'*d, *featureVector))
           fout.close()




allImageFiles = os.listdir(imageDirectory)
d = len(cnn.blobs[layerName].data[0])

for imageFile in allImageFiles:
    fullOutputPath=os.path.join(outputDirectory,imageFile)
    if os.path.isfile(fullOutputPath)==False:
        print imageFile
        uploadFeatureVector( imageFile, layerName, d)



