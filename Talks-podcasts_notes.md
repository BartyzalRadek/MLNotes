## Talks, Podcasts, Interview notes


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


### Eric Weinstein: Revolutionary Ideas in Science, Math, and Society

 - theoretical physicist = source of the whole economy: biology, chemistry, peace through the invention of nuclear weapons, Web

 - social networks: 
  - how much of disagreeable things do you want to see? See only things that I disagree with but are actualy true.
    See the reason why I should see them.

 - social control
   - why cannot we physically disable cameras, microphones on devices, why is the camera indicator light sw controlled
   - 2D: emergence VS intention - profit is only a part of the intentions, political/social control, 
     changing the discussion about things that are not benefitial to the platform = what are they bending to in "Pakistan", etc..
     
### Autonomous Weapons Systems Policy (Richard Moyes)

https://www.youtube.com/watch?v=U6lJI-NSfBY

 - Landmine = static autonomous weapon, input from outside world = pressure on plate -> function of input -> explosion
 - International Law:
   - International Human Rights Law = right to live, dignity
   - International Humanitarian Law = rules of behavior during the war = do not kill too many civilians
   - Treaties of specific weapons
   - these are negotiated by countries
   - requires social function from all states = no world police
 - AW discussed in UN:
   - how the targets are selected
   - what is a target, when and where is force applied to a target
   
 - Advantages of autonomy:
   - speed of decision making
   - speed in coordination of large numbers in swarms
   - reach = not rely on communication infrastructure
   
 - Disandvatages:
   - moral
   - legal arguments: machine doing legal decision - law is addressed to humans not machines
     treat AW as machines or agents?
   - easier to go to war, arms races, etc.
   
 - What is the human element that we want to preserve?
   - "human control"
   - nobody wants AW without any human control = rogue drones etc.
   - OTH person clicks to shoot when there is a red light with no idea what is happening = not enough control
 
 - Requirements = Context to talk about AW:
   - predictive, reliable, transparent
   - accurate information:
     - outcome we want to achieve = what is a target, what weapon to use
     - how does the technology works
     - context = are there civilians, other objects similar to targets, urban area
   - timely human intervention = able to turn it off
   - accountability
   
 - Example with missiles over an area:
   - tanks in an area the commander cannot see - fires missiles into the area, 
     the missiles locate the tanks (heat signatures) and destroy them
   - if the area is small we have context = its a desert, city etc.
   - if the area is large = e.g. whole country and we just send missiles to destroy the "tanks" in the area, 
     the **context** of applied force is unknown to the commander = problem
 - How to encode the classification of humans as targets vs non-targets
 
### Jeff Hawkins: Thousand Brains Theory of Intelligence

https://www.youtube.com/watch?v=-EVqrDlAqYo

 - neocortex has similar structure everywhere, in all mammals
 - Hierarchical Temporal Memory (HTM) theory of intelligence = On Intelligence
   - temporal:
     - brain processes information through time
     - not instant like CNN
   - memory:
     - we build a model of the world
   - hierarchical
     - hierarchy of neurons
   - not wrong but too simple for the current knowledge
   
 - neocortex is big evolutionary jump
   - initially it had straightforward positive impact on survivability
   - from single purpose neural HW = heartbeat ...
   - to general purpose neural HW = understanding abstract concepts
   
 - Thousand Brain Theory = all ideas, everything we know is stored in reference frames
   - we know that brains predict what will happen
     - what does it need for it?
     - everything is stored in reference frames - location of finger in reference to a cup
   - everything is in reference frames
   - consequences:
     - every  tiny square of neocortex can learn a complete model of an object
     - all columns are building a model of something
       - visual models of a cup, sensual model, auditorial model
       - all of them are coming together
     - sensory fusion problem - when does it all come together?
       - all models of a cup (thousands of them) are voting 
       - guessing what are we touching/sensing
       - each model produces its probability of a what they think is the object we are touching
       - associative memory mechanism - they all vote for the single best answer
       - the layer that does the voting converges on one answer - it thinks its a cup
   - memory palace = mentally moving through the reference frames = walk through the house
     - brain uses grid cells for everything = reference frames even when we think about concepts
     - thinking about concepts = moving in reference frames
     - solving problems = finding a path through a reference frames
   - reference frame
     - x,y,z cartesian coords = reference frame
     - you have a point in space, given a movement, you can say what will the next point be
       - its spatial = how can we move from one point to other
       - grid cells can implement N dims space
   - attention
     - attend to room -> table -> cup -> logo -> letter -> pop back up room reference
 - neurons
   - thousands of synapses
   - time based prediction engines
   - "Neurons have thousands of synapses" paper
   - forming new synapses to detect a presence a tens of activated synapses at the same time = some prediction
   -  
   
### Harry Cliff: Particle Physics and the Large Hadron Collider

https://www.youtube.com/watch?v=8A-5gIW0-eI

 - LHC
   - large microscope
   
 - particles = ripples in a quantum field, the fields are everywhere, like electr-magnetic fields
   - atom consists of 3 types of particles:
     - electrons = ripple in a an electron field
     - up-quarks = ripple in a an up-quark field
     - down-quarks = ripple in a down-quark field
   - photon is a ripple in a electro-magnetic field  
    
 - how to discover new particle = create a ripple in a new field = the important thing is the existence of the field
   - Higgs field = everywhere like other field, but to confirm it - create a ripple in it to create an observable particle
   - creating a ripple in this field required a lot of energy
 - particle accelerators:
   - circular 
     - particles go fast = to make them go round you need strong magnets to curve them around the bend
       - LHC used the strongest magnets known = to increase forces = increase size
   - linear
   
 - 1 beam of particles in LHC consists of cca 40 bunches = 30cm long and couple microns thick
   - 2 of them cross in front of a detector
   
 - 4 forces in the universe:
   - electro-magnetic = interaction between charged particles, infinite range 
   - strong force = holds quarks together
   - weak
   - gravity
   
 - protons, neutrons etc. consist of quarks
 - strong force holding quarks together is too strong to knock them out
   - if we try to pull 2 quarks apart, we keep adding energy till the strong force snaps 
     and the energy released creates 2 new quarks = we get 4 quarks
     
   - gluons are the particles of strong force = strong force field = gluon field
   
 - the field is warped by the charge of the particles (ripples) which causes the force
 
 - weak force - bosons are particles - 70x mass of protons
   - manifests only at short distances, why?
     - the particle of the field has a very large mass = the force dies of very quickly (spatially)

 - quantum field theory was not compatible with particles having large mass
  - solution = they have no mass by themselves, they get it by another process
  - = new quantum field = Higgs field, particles get mass through interaction with it
  - what we observe as mass of the particle = Higgs field is drawn to a particle = the energy of the Higgs field packed around the particle = mass
  - if we "turn off" Higgs field => all particles would be massless and fly around with speed of light
  
 - electro-magnetic force + weak force = manifestation of 1 underlining force
 
 - Higgs field is fundamentally different from all other fields:
   - other field are ~0 in empty space, except for quantum fluctuations
   - Higgs field has a non-zero default value everywhere = energy stored everywhere in the universe
   - this energy is what gives mass to the particles
   - the level of energy has to be very precise:
     - 2 likely scenarios for the level of energy =:
       - 0 everywhere = all particles massless = cannot form atoms = no stuff
       - or it explodes to extreme values that even electron would be so massive it would collapse into a blackhole = universe made of blackholes
     - you need an exact setup for atoms to exist
     - possible explanation except God and infinite multiverses:
      - supersymmetry = all fields have symmetric super-fields that cancel each other out and tune the Higgs field to the needed value
       - but tough luck - we should have found the super-fields by LHC but none were found so who knows 

### Stephen Wolfram: ChatGPT, Dark Matter, & AI

https://www.youtube.com/watch?v=xHPQ_oSsJgg

 - How to describe the Universe?
   1. "what's stuff made of"
     - is everything from atoms, are the atoms the same etc.
     - => time is not considered, just what is the world made of at this moment
   2. mathematical description of reality = 16th century+
     - time is a parameter
     - we set time to a specific number and we get the state of the universe at that time
   3. How to describe complex systems?
     - solving differential equation to get a snowflake shape does not work (scale?)
     - if there are rules how the world works, how to make these rules as simple as possible? (so we can write them down and use them)
     - => set of rules = program (we talk about rules as programs because that's what we are familiar with)
     - => describe the world by a program = set of rules
     - time is not a parameter anymore, to advance in time, you have to run the program step by step (from given conditions, the intial state)
     - so what programs are there in the computational space of all programs? (his famous cellular automata diagram)
       - a lot of them have simple rules => simple output
       - but some programs with simple rules have a very complex output: https://www.wolframalpha.com/input/?i=cellular+automaton+rule+30
       - TODO finish
