import os
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.containerservice import ContainerServiceClient 
from azure.identity import DefaultAzureCredential
# set the Azure credentials

resource_group="iheb"
aks_cluster_name="aks-demo-aks"
SUBSCRIPTION_ID="x-x-x-x"
credentials=DefaultAzureCredential()


# initialize the AKS client
aks_client = ContainerServiceClient(
        credential=credentials,
        subscription_id=SUBSCRIPTION_ID)

# get the list of nodes in the AKS cluster
aks_client_functions = dir(aks_client.container_services.get("MC_iheb_aks-demo-aks_francecentral","aks-pool1-26527595-vmss000000"))
# print(aks_client.container_services)
agent_pools=aks_client.agent_pools.list(resource_group, aks_cluster_name)
# get the aks object the AKS cluster
aks_cluster_info = aks_client.managed_clusters.get(resource_group, aks_cluster_name)


# print the aks infos 
print("aks infos :\n")
print("1 ." ,aks_cluster_info.agent_pool_profiles[0].count,'\n')
print("2 ." ,aks_cluster_info.api_server_access_profile,"\n")
print("3 ." ,aks_cluster_info.kubernetes_version ,"\n")
print("5 ." ,aks_cluster_info.node_resource_group ,"\n")
print("6 ." ,aks_cluster_info.sku.tier ,"\n")
print("7 ." ,aks_cluster_info.provisioning_state ,"\n")
print("8." ,aks_cluster_info.aad_profile ,"\n")
print("9." ,aks_cluster_info.api_server_access_profile ,"\n")
print("--------------------------------\n-----------------------------------")

# print the aks pools info in this example i have just one pool
for agent_pool in agent_pools:
    print('Agent pool name:', agent_pool.name)
    print('Number of agents:', agent_pool.count)
    print('Agent VM size:', agent_pool.vm_size)
    print('Agent pool type:', agent_pool.type)
    print('OS disk size:', agent_pool.os_disk_size_gb)
    print('VNET subnet ID:', agent_pool.vnet_subnet_id)
    print('VMs state:', agent_pool.power_state.code)
    print('Tags:', agent_pool.tags)
    print('-----------------------------')



