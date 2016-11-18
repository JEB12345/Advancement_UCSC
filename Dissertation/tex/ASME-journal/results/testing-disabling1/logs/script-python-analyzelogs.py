import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import prettyplotlib as ppl




data = np.loadtxt("muscleRestLengths.csv", delimiter=",")[200:,1:] #discard first 2 seconds and time column

data_normalized = data-data.mean(0)
data_normalized /= data_normalized.std(0)

#plot box data
plt.figure()
plt.boxplot(data,0,'')

#from matplotlib.mlab import PCA
#r = PCA(data_normalized)
#plt.plot(r.fracs,'+-') #only four "principal" components!
#because there are only four steps in the signal!
#plt.figure()
#plt.title("PCA first 4 principal components")
#plt.plot(r.project(data_normalized)[:,:4]+8*np.arange(4))

#now do something useful
#signal periodicity is 400 BTW

#plt.figure()
#plt.plot(data_normalized+np.arange(24)*4,'blue')
#plt.plot(data_normalized[:,11]+11*4,'red',linewidth=4)
#plt.title('Actuator 11 is different!')
#plt.ylabel("muscleRestLengths")


#slow
ncc = np.zeros((data_normalized.shape[1],data_normalized.shape[1]))
for i in xrange(data_normalized.shape[1]):
    for j in xrange(data_normalized.shape[1]):
        ncc[i,j] = np.abs(np.correlate(data_normalized[:,i],data_normalized[:,j],mode='full')/(data_normalized.shape[0]-1)).max()
#most signals are highly correlated!!! 


#let's look at the delays
ncc_delay = np.zeros((data_normalized.shape[1],data_normalized.shape[1]))
for i in xrange(data_normalized.shape[1]):
    for j in xrange(data_normalized.shape[1]):
        ncc_delay[i,j] = (np.correlate(data_normalized[:,i],data_normalized[:,j],mode='full')).argmax()-5800+1

#time for something simple: the average equilibrium length of each motor
#plt.figure()
#plt.plot(np.sort(data.mean(0)),'+-')
#they all seem different, so the algorithm hasn't learned a symmetric gait

#combine results
#plt.figure()
#plt.subplot(1,2,1)
#plt.imshow(ncc,interpolation='nearest',cmap=plt.cm.gray_r)
#plt.title("Normalized Cross-Correlation")
#plt.colorbar()
#plt.subplot(1,2,2)
#plt.imshow(np.where(np.abs(ncc_delay)%400>=200,400-np.abs(ncc_delay)%400,np.abs(ncc_delay)%400),interpolation='nearest',cmap=plt.cm.gray_r)
#plt.title("Optimal time delay")
#plt.colorbar()

#Let's time shift all the signals to align with signal 0
data_normalized_aligned = np.zeros(data.shape)
for i in xrange(24):
   data_normalized_aligned[:,i] = (np.roll(data_normalized[:,i],int(ncc_delay[0,i])))

#THIS LOOKS FUNNY
#plt.figure()
#plt.plot(data_normalized_aligned)
#plt.title("time aligned normalized signals")

#plt.figure()
#for i in xrange(24):
#    plt.plot(data_normalized[:,np.argsort(ncc_delay[0])[i]]+2*i)
#plt.title("signals ordered by time diff wrt signal 0, black = delay")
#for i in xrange(10):
#    plt.plot(-np.sort(ncc_delay[0])+400*i,np.arange(24)*2,'black',linewidth=4)


#if we look at the PCA of this, then 98% of the variance is explained by the first 2 components!
#plt.figure()
#r2 = PCA(data_normalized_aligned)
#plt.plot(r2.project(data_normalized_aligned)[:,:2]+8*np.arange(2))
#you need a sign wave and a double frequency sign wave

#td = np.zeros(ncc.shape)
#for i in xrange(24):
#	td[i,:] = np.sort((ncc_delay[i]+400+int(ncc_delay[0,i]))%800)
#plt.figure()
#plt.title("sequential activation of motors")
#plt.plot(td.T)

##Atil
import scipy.cluster.hierarchy as hclus

#do clustering using the correlation matrix # (1-ncc) or ncc doesn't matter
plt.figure()
linkage_matrix=hclus.linkage(1-ncc,method='ward');
dend = hclus.dendrogram(linkage_matrix,
           color_threshold=0.3,
           show_leaf_counts=True)

#order the correlation matrix according to the clustering
ncc_ordered = np.zeros((data_normalized.shape[1],data_normalized.shape[1]))
for i in xrange(data_normalized.shape[1]):
        for j in xrange(data_normalized.shape[1]):
                ncc_ordered[i,j]=ncc[dend['leaves'][i],j]

#show normalized cross correlation coeff
f, axarr = plt.subplots(1,2)
im1 = axarr[0].imshow(ncc,interpolation='nearest',cmap=plt.cm.gray_r)
im2 = axarr[1].imshow(ncc_ordered,interpolation='nearest',cmap=plt.cm.gray_r)
f.colorbar(im2)

#order signals according to the clustering
data_normalized_aligned_ordered = np.zeros(data.shape)
for i in xrange(24):
    ii=dend['leaves'][i];
    data_normalized_aligned_ordered[:,i] = data_normalized_aligned[:,ii]

f, axarr = plt.subplots(2,1)
im2 = axarr[0].plot(data_normalized+np.arange(24)*4,'blue')
im1 = axarr[1].plot(data_normalized_aligned_ordered+np.arange(24)*4,'blue')
f.axes[0].get_xaxis().set_visible(False)
f.axes[0].get_yaxis().set_visible(False)
f.axes[1].get_yaxis().set_visible(False)
#f.axes[1].text(0.3,0.3,'s\nd\nf\ng',fontsize=10)

for i in xrange(24):
	axarr[0].annotate(i,xy=(5800,4*i),xytext=(0,0),textcoords='offset points',fontsize=10)
	rect1 = matplotlib.patches.Rectangle((2350-ncc_delay[0,i],4*i-2), 1200, 4, color='red',alpha=0.2)
	axarr[0].add_patch(rect1)
	rect1 = matplotlib.patches.Rectangle((2750-ncc_delay[0,i],4*i-2), 400, 4, color='yellow')
	axarr[0].add_patch(rect1)
	
	axarr[1].annotate(dend['leaves'][i],xy=(5800,4*i),xytext=((i%1),0),textcoords='offset points',fontsize=10)

axarr[1].axvspan(2350,3550,color='red',alpha=0.2)
axarr[1].axvspan(2750,3150,color='yellow')
