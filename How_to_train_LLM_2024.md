# How to train LLM 

 - Youtube: https://www.youtube.com/watch?v=2-SPH9hIKT8
 - Slides: https://docs.google.com/presentation/d/1IkzESdOwdmwvPxIELYJi8--K3EZ98_cL6c5ZcLKSyVg/edit#slide=id.p

**Overview with Tools:**
I – Training:
 - data preparation – [datatrove](https://github.com/huggingface/datatrove)
   - [text clustering](https://github.com/huggingface/text-clustering)
 - efficient training techniques – [nanotron](https://github.com/huggingface/nanotron)
 - evaluation – [lighteval](https://github.com/huggingface/lighteval)

II – Fine-tuning:
 - RLHF – [TRL](https://github.com/huggingface/trl)

III – Inference:
 - quantization – [bitsandbytes](https://github.com/TimDettmers/bitsandbytes)
 - deployment – [Text Generation Inference](https://github.com/huggingface/text-generation-inference)

## Training

Data is everything.

### Data Preparation

Different stages of training need different data.
 => Each training stage has different goals

Assume no generalizitaion capability.

Latest resources
 - A Survey on Data Selection for Language Models
   - https://arxiv.org/abs/2402.16827
 - Yi: Open Foundation Models by 01.AI
   - https://arxiv.org/abs/2403.04652


Recent dataset reports
 - Dolma (AllenAI): an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research
   - https://arxiv.org/abs/2402.00159
 - RefinedWeb (Falcon): Outperforming Curated Corpora with Web Data, and Web Data Only
   - https://arxiv.org/abs/2306.01116



#### Pretraining
 - maximum coverage, diversity, robustness
 - 1T tokens, ideally 10T tokens
 - show the model what we want it to know = e.g. Physics knowledge
 - show the model what it can come in contact with 
   - e.g. toxic behavior etc., so we can later train the model to avoid this
 - how do you measure data quality?
   - rules written by humans
   - ML models identifying quality text
   - topic filters to ensure all you desired topics are in

Start with Common Crawl = Internet 10 years ago.
 - everyone uses it, only large enough Internet dataset
 - remove other langs. than English = 50%
 - remove duplicates
   - fuzzy = use hashes, BLOOM filters (very good), MinHash
   - exact = substrings or sentences = requires a lot of memory to store all those substrings
   - good data is duplicated a lot, so deduplication can increase the share of bad data
 - get left with ~10%
 - prepared dataset 'FineWeb' coming from HuggingFace

Other sources of data:
 - Code = Github, Software Heritage
   - [StarCoder2 and StackV2](https://arxiv.org/abs/2402.19173) = largest code dataset
 - Curated = Wikipedia, Books
 - Synthetic = other LLM generates data for you
   - "Rephrase the Web" = let LLM rewite a webpage cleanly and use that for training => faster training
   - [Cosmopedia](https://huggingface.co/blog/cosmopedia)
     - generated samples by giving the LLM different seed phrases = write about this in this style for this audience
     - ![The distribution of seed data, generation format and target audiences in Cosmopedia dataset.](https://huggingface.co/datasets/HuggingFaceTB/images/resolve/main/cosmopedia/histograms.png)

Tools:
 - Language filtering: https://fasttext.cc/
 - Cleaning with heuristics: statistics = word counts, repeating characters, etc.
   - sample it, keep some noise
 - Cleaning with ML: classifier with good examples and bad examples
   - fastText classifier with n-gram size=2
   - 5-gram perplexity Kneser-Ney model on Wikipedia 
     - introducing bias, Wikipedia is written 90% by men
 - Manually go through a sample of data you keep and remove!

Preparing data for training:
 - shuffle
 - Tokenize:
   - numbers, 2 ways to split them into tokens:
     - 1 - 10 = split all digits = LAMMA
     - 1 - 1000 = one token per number up to 1000, split the rest = GPT
   - scaling tokenization is not easy, parallelize well
     - possible to tokenize during training, but restartin training is trickier
     - or tokenize up front but that is expensive

Evaluate Data Quality:
 - train small model = 1-2B params on 30G tokens
 - choose good benchmark:
   - metric monotone increase as training goes, no oscillation
   - low variance with seeds and parts of datasets
   - want to tell datasets apart
   - C4 = good dataset
   - and then some difficult one
 - https://github.com/huggingface/text-clustering
 - look at tokenizer output = longest tokens
 - ALL of these steps can be done in:
   - https://github.com/huggingface/datatrove

#### Modeling

size/efficiency
 - 4D Parallelism:
   - Data Parallelism
     - duplicate model on N GPUs, split the batch and then merge the gradient updates = all-reduce, can be bottleneck
   - Tensor Parallelism
     - when you are limited in data parall. = cannot replicate model on GPUs
     - re-write model code to divide all matrix multiplications to 8x parts of the matrices and put them on separate GPUs
   - Pipeline Parallelism
   - Sequence Parallelism


#### instruction-tuning
 - alignment
 - in-context learning
 - task-specific fine-tuning
