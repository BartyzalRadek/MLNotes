# Building blocks for ANN

## Combining inputs

### Add = ResNet
 - https://arxiv.org/abs/1512.03385
 - `y = activation(f(x) + x)`
 - add the inputs
 -  = residual conection
 - **skip connection** = add result of a distant past layer
 - **parametrized skip connection** = `y = f(y_prev_1 + y_prev_2 + ...)` = add past outputs and then run them through a layer with activation
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

### Weight channels with extra params = SE Net
 - [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507v3)
 - HxWxC input -> Global Average Pooling -> 1x1xC -> ReLU -> Sigmoid = weights of channels -> multiply input channels by them
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/se_net.png" width="400"/>

### Convolve
 - 

## Dropout

### Spatial Dropout
 - zeroes out whole channels = feature maps
 - each channel has prob p to be zeroed out
 - 1D example: seq len=4, num channels=3, [source](https://stats.stackexchange.com/questions/282282/how-is-spatial-dropout-in-2d-implemented):
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/spatial_dropout.png" width="600"/>

## Normalization
 - overview: http://mlexplained.com/2018/11/30/an-overview-of-normalization-methods-in-deep-learning/
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/norm_methods.png" width="800"/>

### BatchNorm
 - [How Does Batch Normalization Help Optimization?](https://arxiv.org/abs/1805.11604)
 - [Coursera Andrew Ng](https://www.coursera.org/lecture/deep-neural-network/why-does-batch-norm-work-81oTm)
 - [Explanation of how normalization of inputs makes hessian better conditioned](http://mlexplained.com/2018/01/10/an-intuitive-explanation-of-why-batch-normalization-really-works-normalization-in-deep-learning-part-1/)
 - [Exaplanation of Hessian](http://mlexplained.com/2018/02/02/an-introduction-to-second-order-optimization-for-deep-learning-practitioners-basic-math-for-deep-learning-part-1/)
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
     - Hessian is better conditioned if we normalize the inputs: 
       - eigen vectors = directions of change
       - eigen values = how large is the curvature
       - larger eigen value = larger curvature = need smaller step size = max limit on my learning rate if its same for all dimensions
       - small eigen value = small curvature = slow convergence = could use bigger step size
       - difference in largest - smallest eigen val = **conditioning** of matrix
       - **ill-conditioned** = large difference in largest and smallest = have to use small step size not to diverge in the directions of eigen vectors with large eigen vals 
         which leads to slow convergence in directions of eigenvectors with small eigen vals = solved by adaptive learning rate for each direction = ADAM = use momentum
       
 - pitfalls:
   - different computation at train and test time
   - small batches = a lot of noise
   - not suitable for RNN - we would have to store the statistics for each time step = for unrolled network
   - fine-tuning pre-trained net with frozen BN layer = do not update the BN mean/var with new mini-batch statistics if using small dataset to fine tune. See [J. Howard comment](https://forums.fast.ai/t/freezing-batch-norm/8377/5)
   - optimizations is dependent on batch size = in distributed training the batch size must be same for all machines

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
 - combination of **layer normalization** and **instance normalization**:
   - all the channels in a single group = layer normalization
   - one channel = one separate group = instance norm
 - GN's computation is independent of batch sizes
 - can be naturally transferred from pre-training to fine-tuning
 - can outperform BN in object detection and segmentation in COCO, video classification
 - LayerNorm treats all channels with same weight = group norm allows for flexibility
 - but image channels are also correlated = thats why grouping works better than instance norm
 
### Batch Renormalization
 - https://arxiv.org/abs/1702.03275
 - use moving average of mean/std over batches
 
### Batch-Instance Normalization
 - [Batch-Instance Normalization for Adaptively Style-Invariant Neural Networks](https://arxiv.org/abs/1805.07925) 
 - interpolation between batch normalization and instance normalization - the balancing param is learned by SGD
 - instance normalization completely erases style information = for some tasks we want to keep some style information
 
### Switchable Normalization
 - [Differentiable Learning-to-Normalize via Switchable Normalization](https://arxiv.org/abs/1806.10779)
 - weighted average of different mean and var statistics from Batch Norm, Layer Norm, Instance Norm
 - the weights of the normalizers are trained
 - select different normalizers for different layers
 
### Spectral Normalization
 - [Spectral Normalization for Generative Adversarial Networks](https://arxiv.org/abs/1802.05957)
 - stabilize the training of the discriminator
 - limiting the Lipschitz constant of the discriminator
   - Lipschitz constant L = L for a function f where for any x and y: `|| f(x) - f(y) || <= L || x - y ||`
 - restrict the Lipschitz constant by normalizing the weight matrices by their largest eigenvalue (or their spectral norm – hence the name) 