## Notes on Kubernetes course
 - https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/20914618#overview
 - also see the notes on Docker that describes the project structure: 

### Why Kubernetes
 - to scale up our app we want to scale up only the worker container not the e.g. NGINX container
 - Elastic Beanstalk would scale up by multiplying the whole app = all containers including NGINX
 -  = if we have an app that needs to run multiple different containers

### What is Kubernetes
 - cluster = Master + Nodes
 - Node = Virtual machine or physical computer
   - can run anything = multiple different types of docker containers
 - Master = controls what runs on each Node
 - Load Balancer = outside of cluster and redirects traffic to the Nodes

### Working with Kubernetes
 - `minikube` = sets up local env tiny cluster = for dev purposes
   - just to create and run a single Virtual Machine = Node
 - for production = e.g. Amazon EKS, Google GKE
 - `kubectl` = used for managing containers in the node
   - used both for dev and in production

### Docker Compose vs Kubernetes
 - Docker compose:
   - builds the containers
   - 1 config for multiple containers
   - sets up networking = port mapping etc.
 - Kubernetes
   - needs already built containers, e.g. on DockerHub
   - 1 config file per object
   - networking has to be set up manually
   - => config file to set up the networking
   
### Kubernetes Configs
 - configs are for creating `objects` not `containers`
 - object = a thing that exists in Kubernetes cluster
 - multiple objects can run on a single Node 
 - object types:
   - `Pod`
     - runs 1 or more docker containers
     - a grouping of containers with a very similar purpose
     - = contaners that absolutely have to be ran together = e.g. a DB and a container monitoring the DB
     - smallest thing to deploy to run a single container
   - `Service` = setup networking inside the cluster
     - 4 subtypes: = under key `spec`: `type` in the config
       - ClusterIP
       - NodePort = expose a container to the outside worls, only good for dev purposes!
       - LoadBalancer
       - Ingress
   - ...
 - `apiVersion`: specifies the set of objects that we can use
   - e.g. `v1` gives us access to objects `Pod` and `Service` and others
 - `kind` = type of the object = e.g. Pod, Service
 
 
#### Pod config
```
apiVersion: v1
kind: Pod
metadata:
  name: client-pod
  labels:
    component: web            = this key-value pair can be anything its just a label that can be used by other objects to select this object
spec:
  containers:
    - name: client
      image: stephengrider/multi-client
      ports:
        - containerPort: 3000
```
#### Service config
```
apiVersion: v1
kind: Service
metadata:
  name: client-node-port
spec:
  type: NodePort             = sub-type of Service object
  ports:
    - port: 3050             = port that other object can use to acccess the target Pod
      targetPort: 3000       = same as the containerPort of the target Pod
      nodePort: 31515        = port that we type into browser to access the target Pod, thats why this is useful mainly for dev work
  selector:
    component: web           = looks for all object = target objects (e.g. Pods) with this key-value pair and applies this port mapping to it
```

#### Networking on a Node
 - `kubeproxy` = at the beginning at each Node
   - look for Services = networking objects
 - each Node has an IP address - we need that to access the Node = it's not on localhost!
 - get the IP by `minikube ip`
 
#### kubectl commands
 - `kubectl apply -f <config>`
 - `kubectl get <object type>` = e.g. pods, services
 

#### Master 
 - kube-apiserver runs on it:
   - it monitors what object it runs and how many copies of the objects are running
   - it tells the Nodes what to run

#### Imperative vs Declarative management of the cluster
 - **imperative** = do exactly these steps
   - Kubernetes supports this also = but we don't want to use this!
   - we would have to check the current state ourself
 - **declarative** = I want the end result look like this
   - = edit the deployment file and pass it to master, it will find out the current state of the cluster and make the needed changes to reach the desired end state 
   
