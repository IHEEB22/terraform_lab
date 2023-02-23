# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import random
import string
import schedule
import time
import DateTime
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient


def deploy_b1s_vm():

    SUBSCRIPTION_ID = "6a94b8ef-60d8-4825-8249-e29f86430566"
    GROUP_NAME = "rg-cool-spider"
    VIRTUAL_MACHINE_NAME = "myVM"
    DISK="myOsDisk"

    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )
    compute_client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
        )

    # Get virtual machine
    vm = compute_client.virtual_machines.get(
        GROUP_NAME,
        VIRTUAL_MACHINE_NAME
    )
    # Get Disck
    disk = compute_client.disks.get(
        GROUP_NAME,
        DISK,
    )
 
    print(f"{vm.name} details  \n")
    print(f"The Vmid = {vm.vm_id}  \n")
    print(f"Provisioning state= {vm.provisioning_state}  \n")
    print(f"Extensions time budget = {vm.extensions_time_budget}  \n")
    print(f"envirement = {vm.tags['env']}  \n")
    print(f"Location = {vm.location}  \n")
    print(f"Vm disk size =  {disk.disk_size_gb} Gb \n")
    print(f"Vm os type =  {disk.os_type} \n")
    print(f"Disk time created = {disk.time_created.strftime('%m/%d/%Y at %I:%M:%S')} \n")
    print('---------------------------------------------------------------------')
    print('                        wait for 5 seconds  ...                      ')
    print('---------------------------------------------------------------------')

    
schedule.every(5).seconds.do(deploy_b1s_vm)
try :
    while 1 :
                schedule.run_pending()
                time.sleep(1)    
except:
    print("vm is still pending")
# # to do :
# monotor the hole setup for this vm seatch for other attributes and scarp nic,nsg and virtual network
# push the project to git 
 
 






if __name__ == "__deploy_b1s_vm__":
    deploy_b1s_vm()
