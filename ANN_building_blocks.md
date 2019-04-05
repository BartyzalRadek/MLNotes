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

### BatchNorm
 - [Coursera Andrew Ng](https://www.coursera.org/lecture/deep-neural-network/why-does-batch-norm-work-81oTm)
 - for each feature: calculate mean and variance over the mini-batch