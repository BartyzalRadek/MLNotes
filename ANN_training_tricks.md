# General tricks to improve ANN models

## Single-model ensembling
 - [nice blogpost](https://towardsdatascience.com/stochastic-weight-averaging-a-new-way-to-get-state-of-the-art-results-in-deep-learning-c639ccf36a)

### Snapshot Ensembling
 - [Snapshot Ensembles: Train 1, get M for free](https://arxiv.org/abs/1704.00109)
 - save weights = snapshot models during whole training duration
 - have ensemble of N models at the end of training - can average their predictions or create meta-model
 - cyclical (cosine = `\_|\_|\_`) LR
 - 1 cycle = 20-40 epochs - save weights at the end of cycle before increasing the LR 
 - use this schedule for the whole training duration
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/snapshot_ensembling.png" width="600"/>
 
### Fast Geometric Ensembling (FGE)      
 - [Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs](https://arxiv.org/abs/1802.10026)
 - also snapshots model, ends up with N models after training
 - cyclical linear LR = `/\/\/\/\`
 - 1 cycle = 2-4 epochs - save weights at the end of cycle before increasing the LR 
 - use this LR schedule in the last stage of the training
 - <img src="https://github.com/BartyzalRadek/MLNotes/blob/master/img/FGE.png" width="600"/> 
 
### Stochastic Weight Averaging
 - [Averaging Weights Leads to Wider Optima and Better Generalization](https://arxiv.org/abs/1803.05407)
 - approximates the FGE approach with a single model
 - averaging of multiple points along the trajectory of SGD, with a cyclical or constant learning rate
 - if using cyclical LR - save weight at minimal LR points
 - if using constant LR - save weights each epoch
 - store running average of the saved weights of the model that is being trained
 - have to only store 2 sets of weights during training
 - inference is done on the model with averaged weights = single model
 
## ULMFit: Universal Language Model Fine-tuning for Text Classification 

[Paper](https://arxiv.org/abs/1801.06146)
         
[Blogpost](http://nlp.fast.ai/classification/2018/05/15/introducting-ulmfit.html)

[Model ZOO](http://forums.fast.ai/t/language-model-zoo-gorilla/14623)

Lets say our task is sentiment classification of twitter messages:
 - Pre-train LM on large text collection from the language - e.g. WikiText
 - Fine-tune LM on the training texts of our task = twitter messages
 - Create classification network:
   - Input: Concat last hidden state of fine-tuned LM, max-pooled hidden state and average-pooled hidden state = max hidden state and average of all hidden states of the fine-tuned model during processing the input text
   - Append 2 feed-forward layer followed by sigmoid classification layer
 - Train the classification network from scratch = only params trained from scratch

Fine-tuning of LM is done by:
- **discriminative fine-tuning:** different LR for each layer
- **Slanted triangular learning rates:** /\ LR with quicker early rise and slower descent = slanted to the left

Training classification network:
- same as fine-tuning unfreezing
- **Gradual unfreezing:** Train only last layer for 1 epoch, then unfreeze the L-1 layer and trai both of them for 1 epoch ...