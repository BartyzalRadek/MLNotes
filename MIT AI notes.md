## MIT AGI talks by Lex Fridman
https://agi.mit.edu/


### Brains, Minds, and Machines (Tomaso Poggio)
https://www.youtube.com/watch?v=aSyZvBrPAyk

 - humans don't have more genes than fruit flies
 - fruit flies are hard coded, we are not
 - guess: we are born with parts of the brain that are plastic and prepared to 
   learn some specific task very easily but the command from the gene is not 
   the detailed circuit (that would require many bits) instead its smth like: 
   imprint things you see in first weeks in life connected to food
 - brain = parts of modules VS mush of the same thing
   - different parts have specific functions but the brain is redundant
   - cortex is from the same hardware but learns different modules
   
 - to understand powerpoint you don't need to understand transistors
  = bad analogy for brain because computer were built that way with different levels
  of abstraction. Brain is more intertwined - high level function with low level design.
  
 - its easire to grow short range connectivity => grow deep networks combining results
   of these locally connected neurons = solving compositional problems = maybe thats the reson that 
   the world around us looks compositional - we are wired to see it as compositional
   
 - overparametrization = a lot of global optima = a lot of solutions for 
   models with more unknown aprameters than equations


### Statistical Learning (Vladimir Vapnik)
https://www.youtube.com/watch?v=STFcvzoxVw4&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4

**Instrumentalism** = science is useful for prediction = just laws for prediction

**Realism** = science describes objective truth = find God's laws = true everywhere

 - for understanding I need conditional probability, for prediction I need a model
 - math is the language used by God
 - math shows the truth VS human intuition = misleading fantasy
 - intuition used to create new axioms = integral wisdom of humanity
 - imagination = only our **interpretation** of reality which can be wrong

#### Great teacher = what makes a great teacher?
 - teacher know reality = chooses what information to give you to help you solve the task
 - good teacher introduces a good invariant (predicate) which greatly reduces the number of admissible functions = reduces the VC dimension = diversity of admissible functions
 - "looks like a duck, swims like a duck, quacks like a duck" - saying jumps like a duck does not add information - it is a legal predicate but it is useless
 - now in ML we use a lot of data = we do not choose good predicates - but "good" relies on what we already know - "jumps like a duck" does not help, because we know that birds don't jump
 - ML = take space of possible function - I reduce it to an admissible set of function by using training data
 - admissible set of functions has VC dimension = small = still infinite number of functions but not that diverse = I am able to pick up the best function using only small amount of predicates = training examples
 - intelligence = finding the special predicates that help us reduce the set of possible functions the most = reduce the VC dimension of the admissible set of functions
 - VC dimension: https://www.cs.cmu.edu/~bapoczos/Classes/ML10715_2015Fall/slides/VCdimension.pdf

Notes:
 - How to find the good predicates? How to reduce the training data? - Interesting connection to Dataset Distillation: https://arxiv.org/abs/1811.10959v1
 - The Unreasonable Effectiveness of Mathematics in the Natural Sciences: http://www.hep.upenn.edu/~johnda/Papers/wignerUnreasonableEffectiveness.pdf
 - Invariance = the rule is true under all condition = it is invariant

### How the brain creates emotions (Lisa Feldman Barrett)
https://www.youtube.com/watch?v=qwsft6tmvBA&t=0s&index=17&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4

 - faces alone do not show emotion
 - affect = simple VS emotion = more complex
 - simple feelings = un/pleasant = body tells us something is wrong != emotion
 - what we call emotion can be considered illness (nostalgia VS depression)
 - machines do not need emotions but simple feelings because the emotions differ in different cultures, some do not feel sad
 - affects = simple feelings = properties of consciousness = feeling good/bad/calm/hungry = regulation of body = keeping it alive
 - infants can't regulate their bodies = cannot predict needs of the body and fulfill them = somebody else does it for them = they learn
 - words teach infants abstract concepts = same word implies same concept even if the objects are different
 - reward = getting the system (body) to normal => simple feelings arise => from them complex feelings
 - = everything arises from the brain trying to regulate the body
 - can't make brains bigger => allow other brains to regulate our nervous system = thats why we are social animals = we need other people, loneliness = die 7 years sooner
 - need for balance VS need for novelty = exploration VS exploitation = expend energy to get reward
 - depression = we expended too much energy without reward = the brain decides it does not want to expend more energy

### Deep Reinforcement Learning (Pieter Abbeel)
https://www.youtube.com/watch?v=l-mYLq6eZPY&index=3&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4

 - problem is both HW and SW
 - easy to psychol. connect to the robot
 - its a RL problem - optimize for likability of the robot by people - how to give it feedback?
 - numeric rewards are hard to come by - its easier for people to compare = say this is better/worse
 - reward is delayed + sparse -> what actions were present when I get high reward = make them more probable
 - simple control architecture can effectively control complex systems - linear feedback control can stabilise a helicopter
 - linear feedback control is very good, but not good enough
 - Neural net tiles the space = layers the linear controllers => it works even better
 - we need **hierarchical reasoning** to make higher level decision like doing a PHD vs contracting specific muscles
 - limitation of old reasoning systems: they weren't grounded in real world, that connection had to be hand coded
 - DL -> can see/understand world around us = connect itself to the real world
 - hierarchy gives us better credit assignment = faster learning
 - lets just end-to-end optimize for faster learning = get hierarchy

#### Transfer learning
 - levels of generalization
 - **learning to master** = motion of planets now VS **learning to generalize** = motion of planets after new planet enters the system
 - neocortex is fairly modular (same parts can be used for different things) = can we design smth similarly modular?

#### Imitation learning VS Self play
 - Imitation learning = copy teacher
 - Self play = 
 - challenge of RL is getting signal = self play = I always get a signal = can naturally learn much quickly
 - = turn as much problems to self play as possible = faster learning
 - cannot use self play -> give partial rewards for completing sub tasks -> a lot of partial rewards -> why not just show the robot what to do?
 - how to show what to do?
   - guide the robot - high signal to noise ratio = fast learning
   - show the robot through 3rd party = robot sees us, but doesn't experience it = has to map your hand to its hand = like machine translation for demonstration 

#### Simulators
 - ensemble of simulators, none of them are perfect, but if I train in all of them the real world is just another simulation for the robot   
 
#### Representative tests of complex ability
 - drivers licence = short test but representative of human's skill to drive - how to do that for a machine?
                                                                                                     

### Godel Machines, Meta-Learning, and LSTMs (Juergen Schmidhuber)
https://www.youtube.com/watch?v=3FIo6evmweo&list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4&index=2

 - General solver = improves itself = true Meta learning - limits = Goedel, physics
 - Goedel machines = programs that rewrite themselves, http://people.idsia.ch/~juergen/goedelmachine.html
 - good theory of problem solving - should be practical = optimal with regard to available resources
 
#### Simplicity is beauty
 - code running the universe is really simple = few lines of code = builds on layers of abstraction produced by the scientists (calculus, matrices ...)
 - no physiscal evidence for non-deterministic universe - maybe it's all a pseudo-random algorithm
 - look for a short program able to backtrack to the creation of universe = we don't need extra bits of information to describe each measurement of spin
 - simplicity is beatiful, elegant - laws of reality = short programs predicting what happens 
 - **predictive coding** = don't have to store the observations, just the law predicting them
 - history of science = history of compression = progress = insight
 - measure the depth of the insight = maximize it = try to see data that allows us to learns something new = exploration
 - **power play** = lets search for pairs of (problem, solver able to solve the problem) = pose your own questions
 - space of all the possible problems - next problem = the simplest problem that the current solver cannot solve and does not forget previous solutions

#### Curiosity 
 - evolution - exploration is good - built into us
 - some people are extremely explorative - they die, but the rest survives 

#### Creativity 
 1. find a solution for a problem = applied creativity
 2. pure creativity = find your own problems
 
#### Consciousness
 - compression is a side effect of prediction
 - compression of the world around us => we appear in our world = compress the properties of the agent (of our body/actions) = thinking about self
 - = necessary side effect
 
#### RNN, value of depth, past + future 
 - we need memory of the past to predict the future, classify whats happening now
 - each timestep = virtual layer of RNN
 - most problem currently do not require to look very far back
 - learn to put important stuff into the memory = clever mechanism for forggetting, keeping info = LSTMs
 - credit assignment problem millions of steps into the past = possible with LSTMs 
 - there is 1 past but many possible futures - which one to choose = how do you plan next action sequence = Reinforcement learning = thats a problem LSTM cannot solve
 - Model = LSTM = predictive model of the world
 - Controller = selects the future actions
 - Controller can learn by itself how to use the Model - maybe ignore it or use some subprograms of the Models
 - next wave of AI = RL = machines shaping data through their actions - self-driving cars etc.
 - babies build predictive models of the world = build machines like babies
 
#### Symbolic, logic programming
 - proof search = logic programming = asymptotically optimal = best theorem provers
 - sub-optimal stuff = gradient descent = practical
 
#### Future outlook
 - near term: easy to say which jobs are going to disappear but hard to say which are going to be invented
 - new jobs are constantly created
 - countries with high level of automation have very low unemployment rates
