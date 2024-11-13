# Install Azure PowerShell module (if not already installed)
Install-Module -Name Az -AllowClobber -Scope CurrentUser

# Authenticate with Azure
Connect-AzAccount

# Variables
$resourceGroupName = "example-resources"
$location = "East US"
$storageAccountName = "examplestorageacct"

# Create Resource Group
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create Storage Account
New-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccountName -Location $location -SkuName Standard_LRS -Kind StorageV2 -Tags @{environment="staging"}