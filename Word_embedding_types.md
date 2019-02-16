## Differences between word embedding types

#### Fixed vs contextual:

 - **fixed word representation:**
   - Word2Vec, Glove, FastText 
   - word 'bank' will have one embedding regardless of the sentence it is in. 
   - Embedding = f(word)
   - easy to explore relationships between words
   
 - **contextual word embeddings:**
   - ELMo, BERT 
   - word *bank* in *Finance bank.* will have different embedding than in *River bank.* 
   - Embedding = f(word, context)
   - improves performance notably on downstream tasks
   - harder to explore things like analogies, nearest words, or word meaning changes between corpses 
     as one needs to sample in context to really take advantage of the embeddings as intended.
 
#### Tokenization

 - **per word:** 
   - handles whole words = can't easily handle words they haven't seen before
   - Word2Vec, Glove
    
 - **per word-fragment:**
   - FastText, BERT
    
 - **per character:**
   - ELMo


#### Sources of embeddings:
 - **Word2Vec:** 
   - attempts to predict context given a word or a word given its context (depending on the model)
   - handles whole words
   
 - **Glove:** 
   - starts with a co-occurrence matrix and attempts to "compress" it, while preserving the words co-occurrence probabilities
   - handles whole words
   
 - **FastText:** 
   - based on Word2Vec
   - word-fragment based 
   - can usually handle unseen words
   - generates one vector per word
   
 - **ELMo:**
   - contextual
   - character-based, providing vectors for each character that can combined through a deep learning model or simply averaged to get a word vector 
   - official implementation uses character level convolutions to produce word-level embeddings, followed by BiLSTMs to make them contextual
   
   
 - **BERT:**
   - contextual 
   - chunking unrecognized words into ngrams it recognizes (e.g. circumlocution might be broken into "circum", "locu" and "tion"), and these ngrams can be averaged into whole-word vectors
   - uses [wordpiece]{https://arxiv.org/pdf/1609.08144.pdf} tokenization of input words
   - designed to be fine-tuned easily, and is designed so you can drop it into a classifier without having to do much network building or customization. 
   - fine-tuning of these vectors can potentially hurt generalization, especially if your data set is small.  
 
 
#### Wordpiece

**Layman terms description:**

More sophisticated version of the BPE tokenization method. 
In BPE you start with a character vocabulary, and repeatedly add the most frequently occurring combination of existing tokens to your vocabulary. 
In wordpiece, rather than using on frequency, you combine the two tokens in your vocabulary that will minimize the likelihood over the corpora given the vocabulary.

**Extract from original publication:** https://arxiv.org/pdf/1609.08144.pdf

4.1 Wordpiece Model

= Split text into sub-word units.
Completely data-driven and guaranteed to generate
a deterministic segmentation for any possible sequence of characters. It is similar to the method used in [38]
to deal with rare words in Neural Machine Translation.
For processing arbitrary words, we first break words into wordpieces given a trained wordpiece model.
Special word boundary symbols are added before training of the model such that the original word sequence
can be recovered from the wordpiece sequence without ambiguity. At decoding time, the model first produces
a wordpiece sequence, which is then converted into the corresponding word sequence.
Here is an example of a word sequence and the corresponding wordpiece sequence:

 - Word: Jet makers feud over seat width with big orders at stake
 - wordpieces: _J et _makers _fe ud _over _seat _width _with _big _orders _at _stake
 
In the above example, the word “Jet” is broken into two wordpieces “_J” and “et”, and the word “feud”
is broken into two wordpieces “_fe” and “ud”. The other words remain as single wordpieces. “_” is a special
character added to mark the beginning of a word.

  