Write-Output "Checking for Active Directory..."
$AD_module_status = Get-Module -ListAvailable -Name ActiveDirectory

if (-not $AD_module_status) {
    Write-Output "RSAT module not installed, installing..."
    Get-WindowsCapability -Name RSAT.ActiveDirectory.DS-LDS.Tools* -Online | Add-WindowsCapability -Online
    Import-Module ActiveDirectory
}

$AD_module_status = Get-Module -ListAvailable -Name ActiveDirectory
if ($AD_module_status){
    Write-Output "RSAT module installed."
} else{
    Write-Output "Failed installing RSAT module."
}



