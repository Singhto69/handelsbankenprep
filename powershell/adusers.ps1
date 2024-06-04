$basedir = Split-Path -Parent $PSCommandPath
. $basedir\helpfunctions\privilege\AdminPrivilegeCheck.ps1
$admin_privilege = Prompt-AdminPrivilege -origin_path $PSCommandPath
$dependency0 = & $basedir\helpfunctions\installers\DISM.ps1
$dependency1 = & $basedir\helpfunctions\installers\RSAT.ps1
if ($admin_privilege -and $dependency0 -and $dependency1){Write-Host 'Dependency check completed... proceeding...'}
Import-Module ActiveDirectory

$tar_ou = Read-Host 'Where shall the users be added? use normal text'
$tar_domain = Get-ADDomain
& $basedir\helpfunctions\formatters\string_to_ou.ps1 -target_ou $tar_ou -base_domain $tar_domain



#Debug statement
#Write-Output $basedir
#Read-Host