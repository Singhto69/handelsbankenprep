$baseDirectory = Split-Path -Parent $PSCommandPath
. $baseDirectory\helpfunctions\privilege\AdminPrivilegeCheck.ps1

#$Host.UI.RawUI.BackgroundColor = 'Black'
#$Host.UI.RawUI.ForegroundColor = 'Green'
# Clear screen to apply color changes immediately
#Clear-Host
Write-Output "Checking admin privileges for process $PID ..."
$admin_privilege = Prompt-AdminPrivilege -origin_path $PSCommandPath

if (-not $admin_privilege){
    Write-Host "Process $PID Failed to elevate admin privileges for main script , exiting..."
    exit
}
Write-Output "Process $PID has admin privileges. Proceeding..."
& $baseDirectory\helpfunctions\installers\DISM.ps1
& $baseDirectory\helpfunctions\installers\RSAT.ps1