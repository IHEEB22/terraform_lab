### start the minikube cluster before applying the configuration 

    minikube start

### make sure minikube is running you should get the host,apiserver and kubelet running 

    minikube status  
 
### preview terraform actions

    terraform plan 

### auto approve the configuration 

    terraform apply --auto-approve

### inspect the Deployments in your cluster

    kubectl get deployment $(terraform output -raw deployment_name)

### show k8s pods state

    kubectl get pods 

### open the nginx server using your browser
    
    minikube service $(terraform output -raw service_name)

    
