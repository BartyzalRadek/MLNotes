### Perceptron
Code examples:
 - [Multi-layer percetron implemented in numpy](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/MLP.ipynb)

### FFNN

Sources:
 - [Neural Networks and Deep Learning book](http://neuralnetworksanddeeplearning.com/)

Code examples:
 - [Playing with different simple datasets in TF](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/FFNN.ipynb)

### RNN

Sources:
 - The Unreasonable effectiveness of RNN: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
 
Code examples:
 - [Minimal char-rnn in Numpy by Karpathy](https://gist.github.com/karpathy/d4dee566867f8291f086)
 - [Minimal char-rnn in Keras](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
 - [Minimal char-rnn in Keras by me with more comments :)](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/LSTM.ipynb)
 
### LSTM 

**Sources:**
 - Great blog by Distill founder: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ = source of the diagrams!
 - LSTM variants, hyperparam tuning etc.: [LSTM: A Search Space Odyssey](https://arxiv.org/pdf/1503.04069.pdf)
 
**Explanation:**

 - 1 LSTM layer = 1 LSTM cell = 1 box on the diagram
 - 1 LSTM cell processes a sequences of vectors **x_t** and returns a sequence of vectors **h_t**

![LSTM cell unrolled in time](https://github.com/BartyzalRadek/MLNotes/blob/master/img/LSTM-chain.png) 

![LSTM notation](https://github.com/BartyzalRadek/MLNotes/blob/master/img/LSTM-notation.png)

 - Sigmoid/Tanh Neural Network Layer = densely connected feed-forward layer with Sigmoid/Tanh activation
 - Sigmoid returns [0,1]
 - Tanh returns [-1, 1] - used as normalization + has better gradients than Sigmoid
 
### Stacked LSTM

```
model = Sequential()
model.add(LSTM(layer_size, return_sequences=True, input_shape=(3,1)))
model.add(LSTM(layer_size, return_sequences=True))
model.add(LSTM(layer_size, return_sequences=True))
model.compile(optimizer='adam', loss='mse')
```

 - The first LSTM layer LSTM_0 gets input sequence **X** and return a sequence **S_1**
 - The second LSTM layer LSTM_1 gets input **S_1** and outputs a sequence **S_2** etc.
 - It can be imagined as the LSTM cell unrolled in time with another one on top of it with **x_t** replaced by **h_t** of the first LSTM layer:
   - **x_0** -> LSTM_0 -> **h_0_0** -> LSTM_1 -> **h_0_1** -> ... -> first element of output sequence
   - **x_1** -> LSTM_0 -> **h_1_0** -> LSTM_1 -> **h_1_1** -> ... -> second element of output sequence

### CNN

Sources: 
 - http://cs231n.github.io/convolutional-networks/

Notes: 
 - For example, suppose that the input volume has size [32x32x3], (e.g. an RGB CIFAR-10 image). 
 If the receptive field (or the filter size) is 5x5, 
 then each neuron in the Conv Layer will have weights to a [5x5x3] region in the input volume, 
 for a total of 5x5x3 = 75 weights (and +1 bias parameter). 
 Notice that the extent of the connectivity along the depth axis must be 3, since this is the depth of the input volume.
  = **The connectivity is local in space (e.g. 5x5), but full along the input depth (3).**
  
 - **Parameter sharing:** We are going to constrain the neurons in each depth slice to use the same weights and bias.
 
    - WxHxD = size of input
    - F = filter size
    - K = number of filters
  
   With parameter sharing, it introduces F⋅F⋅D weights per filter, for a total of (F⋅F⋅D)⋅K weights and K biases for the whole network.
   
 - **1x1 convolution:** If the input is [32x32x3] then doing 1x1 convolutions would effectively be doing 
 3-dimensional dot products (since the input depth is 3 channels).
 
 - **Dilated convolutions:** Dilation of 0: `w[0]*x[0] + w[1]*x[1] + w[2]*x[2]`. 
 For dilation 1 the filter would compute `w[0]*x[0] + w[1]*x[2] + w[2]*x[4]`.
 If you stack two 3x3 CONV layers on top of each other then you can convince yourself that 
 the neurons on the 2nd layer are a function of a 5x5 patch of the input 
 (we would say that the effective receptive field of these neurons is 5x5). 
 If we use dilated convolutions then this effective receptive field would grow much quicker.
 
 - **Pooling:** Pooling layer with filters of size 2x2 applied with a stride of 2 downsamples every depth slice
 in the input by 2 along both width and height, discarding 75% of the activations. 
 
 - **Getting rid of pooling:** Discarding pooling layers has also been found to be important in 
 training good generative models, such as variational autoencoders (VAEs) or generative adversarial networks (GANs).
 
 - **Simple layer pattern:** `INPUT -> [[CONV -> RELU]*N -> POOL?]*M -> [FC -> RELU]*K -> FC`
 
 - Prefer a stack of small filter CONV to one large receptive field CONV layer. 
 
   The neurons would be computing a linear function over the input, while the three stacks of CONV layers 
   contain non-linearities that make their features more expressive. 
   
   Intuitively, stacking CONV layers with tiny filters as opposed to having one CONV layer with big filters allows us 
   to express more powerful features of the input, and with fewer parameters. As a practical disadvantage, we might 
   need more memory to hold all the intermediate CONV layer results if we plan to do backpropagation.
   
 - Why are smaller filters better than larger ones?
 
   ![7x7 vs 3x3](https://github.com/BartyzalRadek/MLNotes/blob/master/img/7x7_vs_3x3.png)
   ![bottleneck vs 3x3](https://github.com/BartyzalRadek/MLNotes/blob/master/img/bottleneck_vs_3x3.png)
   ![1x3 + 3x1 = 3x3](https://github.com/BartyzalRadek/MLNotes/blob/master/img/1x3-3x1.png)
