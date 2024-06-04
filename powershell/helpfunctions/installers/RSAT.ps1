#Note , RSAT is only available on enterprise and pro editions...
Write-Output "Checking for Active Directory..."
$AD_module_status = Get-Module -ListAvailable -Name ActiveDirectory

if (-not $AD_module_status) {
    Write-Output "RSAT module not installed, installing..."
    Get-WindowsCapability -Name "RSAT.ActiveDirectory.DS-LDS.Tools*" -Online | Add-WindowsCapability -Online
    $installStatus = Get-WindowsCapability -Name RSAT.ActiveDirectory.DS-LDS.Tools* -Online | Select Name, State
    Import-Module ActiveDirectory
}
$AD_module_status = Get-Module -ListAvailable -Name ActiveDirectory
if ($AD_module_status){
    Write-Output "RSAT module sucessfully installed."
    return $true
} else{
    Write-Output "Failed installing RSAT module."
    return $false
}



