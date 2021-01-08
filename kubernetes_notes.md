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


