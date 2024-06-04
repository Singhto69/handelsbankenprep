$basedir = Split-Path -Parent $PSCommandPath
. $basedir\helpfunctions\privilege\AdminPrivilegeCheck.ps1
$admin_privilege = Prompt-AdminPrivilege -origin_path $PSCommandPath
$dependency0 = & $basedir\helpfunctions\installers\DISM.ps1
$dependency1 = & $basedir\helpfunctions\installers\RSAT.ps1
if ($admin_privilege -and $dependency0 -and $dependency1){Write-Host 'Dependency check completed... proceeding...'}
Import-Module ActiveDirectory

$target_ou = & $basedir\helpfunctions\ad\ou_input_dn_output_selector_raw.ps1
Write-Host $target_ou
#Read-Host




#Debug statement
#Write-Output $basedir
#Read-Host