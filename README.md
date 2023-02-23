### initialize

    terraform init

### preview terraform actions

    terraform plan

### apply configuration with variables

    terraform apply -var-file terraform.tfvars

### destroy a single resource

    terraform destroy -target resource.name

### destroy everything from tf files

    terraform destroy

### show resources and components from current state

    terraform state list

### show current state of a specific resource/data

    terraform state show resource.name    
    
### download required packages for the python script 
    
    pip install -r requirements.txt 
