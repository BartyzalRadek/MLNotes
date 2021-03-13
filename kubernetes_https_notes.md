## How to get HTTPS support for Kubernetes cluster app

 - Taken from Udemy course on Docker and Kubernetes: https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11628340#overview
 
### Setup

1. buy a domain
2. point the domain to our application = IP address of the Ingress controller in our Kubernetes cluster
   - @ `A record` -> IP address of our app
   - www `CNAME record` -> mydomain.com 
     - this redirects users coming to www.mydomain.com to A record of mydomain.com
3. setup `Cert Manager`
 - will automatically ask for certificates and store them 
 - install using Helm

 - sets up communication:
   1. can you give me certificate that says I own mydomain.com
   2. LetsEncrypt sends request to mydomain.com
   3. if we reply, LetsEncrypt will give us a certificate for 90 days

 - consists of 2 objects:
   - `Issuer` = telling Cert Manager where to ask for certificates = e.g. `LetsEncrypt`
   - `Certificate` = describes details about the certificate that should be obtained
     - this object also defines a `Secret` object where the Cert Manager will store the received certificate
     
4. tell NGINX Ingress to use HTTPS and use the certificate in the Secret object
 - also tell it to redirect HTTP to HTTPS

### Kubernetes setup
 - `kubectl get certificates`
 - `kubectl describe certificates`

**Issuer object configuration file example**
```
apiVersion: cert-manager.io/v1alpha2
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: "myemail@gmail.com"
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01: {}             # use HTTP mode of getting certificates insted of DNS mode
```

**Certificate object configuration file example**
```
apiVersion: cert-manager.io/v1alpha2
kind: Certificate
metadata:
  name: k8s-multi-com-tls
spec:
  secretName: k8s-multi-com
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: mydomain.com
  dnsNames:
    - mydomain.com
    - www.mydomain.com
  acme:
    config:
      - http01:
          ingressClass: nginx
        domains:
          - mydomain.com
          - www.mydomain.com
```


