$baseDirectory = Split-Path -Parent $PSCommandPath
Write-Output $baseDirectory
. $baseDirectory\helpfunctions\privilege\AdminPrivilegeCheck.ps1

$admin_privilege = Prompt-AdminPrivilege -origin_path $PSCommandPath
if (-not $admin_privilege){
    Write-Host "Failed to elevate admin privileges for main script , exiting..."
} 
Read-Host
& $baseDirectory\helpfunctions\installers\DISM.ps1
Read-Host
& $baseDirectory\helpfunctions\installers\RSAT.ps1
Read-Host