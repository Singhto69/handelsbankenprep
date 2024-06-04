Import-Module ActiveDirectory

$module_status = Get-Module -ListAvailable -Name ActiveDirectory
if ($module_status){
    Write-Host "AD successfully loaded..."
}else{
    Write-Host "AD failed to load..."
}

$domain = Get-ADDomain
Write-Host $domain

$curuser = Get-ADUser -Filter * -SearchBase 'OU=superou,DC=testdomain,DC=tony,DC=com' | Write-Output $_