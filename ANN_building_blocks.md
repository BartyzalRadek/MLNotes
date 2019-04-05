# Building blocks for ANN

## Combining inputs

### Add = ResNet
 - https://arxiv.org/abs/1512.03385
 - `y = f(x) + x`
 - add the inputs
 - residual conection = skip connection
 - learn only what to add not the whole transformation
 - subsequent layers are dependent on each other
 
### Concat = DenseNet
 - https://arxiv.org/abs/1608.06993
 - `y = f(x) || x`
 - concatenate the inputs
 - allows for diverse features - the features from first layers are carried unchanged
 
### Interpolate = HighwayNet
 - https://arxiv.org/abs/1505.00387
 - `y = f(x)*g(x) + x*(1-g(x))`, both g(x) are identical = share weights
 - g(x) = sigmoid(Wx + b)
 - addition with extra layer outputting alpha for each dimension: `y_i = alpha*f(x_i) + (1-alpha)*x_i`

### LSTM style
 - `y = f(x)*sigmoid_1(x) + tanh(x)*sigmoid_2(x)`
 - both sigmoid and tanh represent a FF layer: sigmoid(Wx + b)
 - no weight sharing

### Convolve
 - 


## Normalization
 - overview: http://mlexplained.com/2018/11/30/an-overview-of-normalization-methods-in-deep-learning/
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/norm_methods.png" width="800"/>

### BatchNorm
 - 
 - [Coursera Andrew Ng](https://www.coursera.org/lecture/deep-neural-network/why-does-batch-norm-work-81oTm)
 - [How Does Batch Normalization Help Optimization?](https://arxiv.org/abs/1805.11604)
 - for each feature: 
   - calculate mean and variance over the mini-batch
   - normalize each feature to mean=0, var=1
   - rescale to mean=beta, var=gamma - why rescale? the network might need a certain range to be effective e.g. for ReLU
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/batch_norm.png" width="400"/>
 - old, probably wrong explanation:
   - covariate shift = input distribution changed
   - internal covariate shift = distribution of inputs to a certain layer changes by changing weights of the prev layer
   - reducing internal covariate shift is probably not even happening - see [1](https://arxiv.org/abs/1805.11604)
 - how does it help then?
   - high-order interactions = changing one weight affects subsequent layers
   -  = changing one weight can make the activations fly all over the place in complex ways
   - With BN, we can control the magnitude and mean of the activations **independently** of all other layers
   - BN makes the loss surface easier to optimize, smoother = we can use higher LR
 - pitfalls:
   - different computation at train and test time
   - small batches = a lot of noise
   - not suitable for RNN - we would have to store the statistics for each time step = for unrolled network
   - fine-tuning pre-trained net with frozen BN layer = do not update the BN mean/var with new mini-batch statistics if using small dataset to fine tune. See [J. Howard comment](https://forums.fast.ai/t/freezing-batch-norm/8377/5)

### WeightNorm
 - https://arxiv.org/abs/1602.07868
 - replace each k-dimensional weight vector w by: `w = (g / ||v||) * v`
   - g = scalar
   - v = k-dimensional vector
   - ||v|| = euclidean norm of v
   - g, v are now updated by SGD during training
 - each w now has `||w|| = g`
 - speed up convergence by decoupling the norm of the weight from its direction = net can optimize them separately with separate gradient flows
 - combine with `mean-only BN` = BN but only with the mean normalization, no division by var
 - can be used with smaller batch sizes because the mean-only BN is not so drastic
 
### LayerNorm
 - https://arxiv.org/abs/1607.06450
 - transpose of batch norm: 
   - BatchNorm normalizes the inputs across the batch dim = statistics same for all mini-batch examples
   - LayerNorm normalizes the inputs across the features = statistics independent of other mini-batch examples
 - compute the mean and variance used for normalization from all of the summed inputs to the neurons in a layer on a single training case
 - exactly the same computation at training and test times
 - applicable to RNN: computes the normalization statistics separately at each time step
 - stabilizes hidden states in RNNs
 
### Instance Normalization
 - [Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022)
 - similar to layer normalization but goes one step further: 
   - computes the mean/std and normalize across each **channel** in each training example
 - makes net agnostic to the contrast of the original image
 - = specific to images = not for RNNs
 - works well for style transfer, also used on GANs
 
### Group Normalization
 - https://arxiv.org/abs/1803.08494
 - GN divides the channels into groups and computes within each group the mean and variance for normalization
 - combination of layer normalization and instance normalization:
   - all the channels in a single group = layer normalization
   - one channel = one separate group = instance norm
 - GN's computation is independent of batch sizes
 - can be naturally transferred from pre-training to fine-tuning
 - can outperform BN in object detection and segmentation in COCO, video classification   