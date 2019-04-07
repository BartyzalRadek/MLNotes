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