# Perceptron
Code examples:
 - [Multi-layer percetron implemented in numpy](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/MLP.ipynb)

# FFNN

Sources:
 - [Neural Networks and Deep Learning book](http://neuralnetworksanddeeplearning.com/)
 - [Introduction to Deep Learning by Eugene Charniak](https://cs.brown.edu/courses/csci1460/assets/files/deep-learning.pdf)

Code examples:
 - [Playing with different simple datasets in TF](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/FFNN.ipynb)

# RNN

Sources:
 - The Unreasonable effectiveness of RNN: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
 
Code examples:
 - [Minimal char-rnn in Numpy by Karpathy](https://gist.github.com/karpathy/d4dee566867f8291f086)
 - [Minimal char-rnn in Keras](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
 - [Minimal char-rnn in Keras by me with more comments :)](https://github.com/BartyzalRadek/neuroinformatics-course/blob/master/LSTM.ipynb)
 
## LSTM 

**Sources:**
 - Great blog by Distill founder: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ = source of the diagrams!
 - LSTM variants, hyperparam tuning etc.: [LSTM: A Search Space Odyssey](https://arxiv.org/pdf/1503.04069.pdf)
 
**Explanation:**

 - 1 LSTM layer = 1 LSTM cell = 1 box on the diagram
 - 1 LSTM cell processes a sequences of vectors **x_t** and returns a sequence of vectors **h_t**

<img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/LSTM-chain.png" alt="LSTM cell unrolled in time" width="600"/> 

<img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/LSTM-notation.png" alt="LSTM notation" width="300"/>

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
   
## Sequence-to-Sequence architectures: (mainly from machine translation POV)

**Sources:**

Attention seq2seq models from translation: 
 - [Blogpost with visualizations](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
 
seq2seq learning:
 - [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
 - [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078v3)
 - [TensorFlow Neural Machine Translation (seq2seq) Tutorial](https://github.com/tensorflow/nmt)
 - [Blogpost - source for seq2seq image](https://medium.com/@devnag/seq2seq-the-clown-car-of-deep-learning-f88e1204dac3)

**Sequence Modeling:**
 - = predict after each time step: x_t -> y_t
 - predictions based only on the previous elements in the sequence
 - Dilated Convolutions (TCN = Temporal Convolutional Nets) VS RNN: 
   - Paper: https://arxiv.org/abs/1803.01271
   - Code by authors: https://github.com/locuslab/TCN
   - My talk + handout: https://github.com/BartyzalRadek/lets-talk-ml/blob/master/talks/CNN_vs_RNN
 
**Sequence-to-Sequence:**
 - process whole input sequence and then generate the new sequence
 - e.g. machine translation


### Encoder-Decoder architecture
  - <img src="https://cdn-images-1.medium.com/max/1250/1*yG2htcHJF9h0sohcZbBEkg.png" alt="Encoder-Decoder with fixed-size contex vector." width="600"/>
  - Encoder = RNN: processes whole input sequence and outputs a single fixed-size contex vector C representing it
  - Decoder = RNN: at each time step t:
    - input: C and h_{t-1}
    - output: h_t = hidden representation at time t that is then passed through a FFNN to get distribution over classes (characters, words, etc..)   
  - Encoder and Decoder can but usually don't share their weights
  - input does not have to be a sequence: generate text descriptions for images:
    - Encoder = CNN outputting context vector
    - Decoder = RNN generating text from the context vector
    - [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555)
    
### Encoder-Decoder with Attention
  - containing all information about a long input sequence in one fixed-size vector is hard => attention
  - save all the hidden states of the encoder not just the last one (previously called C)
  - context is now a list of hidden states (or RNN outputs) with same length as the input sequence = input_seq_len * RNN_output_dim matrix
  - Decoder = RNN: at each time step t:
    - process the context list into a single fixed-size vector by attention
    - = weighted sum over the hidden states - the weights are generated at each step = focus on different parts of the input
    - input: 
      - processed context = single RNN_output_dim sized vector
      - h_{t-1}
    - output: h_t = hidden representation at time t that is then passed through a FFNN to get distribution over classes (characters, words, etc..)
  - Attention calculation at time step = 4 = input sequence has length 3 = we have 3 hidden states from encoder and now we are decoding:
  - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/attention_vec.png" alt="Attention calculation" width="600"/>

### Transformer
  - [Orig paper: Attention Is All You Need](https://arxiv.org/abs/1706.03762)
  - [pytorch impl. with a blogpost](https://medium.com/@kolloldas/building-the-mighty-transformer-for-sequence-tagging-in-pytorch-part-ii-c85bf8fd145)
  - [tensor2tensor library with official implementation of Transformer in TF](https://github.com/tensorflow/tensor2tensor/tree/master/tensor2tensor/models)
  - [Illustrated Transformer = source for used imgs](http://jalammar.github.io/illustrated-transformer/)
  - [Transformer talk by author - source for motivation](https://www.youtube.com/watch?v=rBCqOTEfxvg)
  - **Motivation:**
    - RNNs: 
      - not parallelizable
      - number of time steps = input sequence length
      - possibly a lot of words between words relevant to each other
      - O(n * d^2) - n = input seq length, d = hidden representation dimension 
    - Dilated Convolutions CNNs: 
      - parallelizable
      - log(n) number of time steps with input sequence length n 
      - still too focused at the position of the words
      - O(n * d^2) - n = input seq length, d = hidden representation dimension
    - Transformer:
      - Encoder calculates word embeddings in constant number of time steps
      - Decoder outputs one element of output sequence at a time = its sequential? 
      - O(n^2 * d) - worse in theory but in machine translation: d =~1000, n=~100 => 10x faster than RNN
  - **Whole architecture:**
  - Feed Forward layers at the same level share weights = it just one layer depicted as 2 to show that the comp. can be parallelized there
  - Add + Normalize = LayerNorm(layer_output + residual_connection)
  - <img src="http://jalammar.github.io/images/t/transformer_resideual_layer_norm_3.png" alt="Encoder+Decoder" width="700"/>
  - **Encoder:**
    - Self attention: 
    - Q, K, V = input embeddings * W_Q, W_K, W_V = Linear layer
    - Q, K, V can all be identical! 
    - <img src="http://jalammar.github.io/images/t/self-attention-output.png" alt="Self attention" width="400"/>
    - In matrix form: 
    - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/transformer_self_attention.png" alt="Attention calculation" width="350"/>
    - Multi-head attention = do the self attention 8 times -> concat outputs -> multiply by W_O to get output of correct shape = Linear layer:
    - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/transformer_multi_head.png" alt="Multi-head attention" width="500"/>

# CNN

**Sources:** 
 - http://cs231n.github.io/convolutional-networks/

**Notes:** 
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
   - My talk explaining dilated convs vs RNN: https://github.com/BartyzalRadek/lets-talk-ml/blob/master/talks/CNN_vs_RNN
 
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
