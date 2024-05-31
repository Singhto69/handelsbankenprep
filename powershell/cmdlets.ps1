.\helpfunctions\installers\DISM.ps1
$AD_module_status = Get-Module -ListAvailable -Name ActiveDirectory
$windowsVersion = [System.Environment]::OSVersion.Version
#Write-Output $windowsVersion.Major
#Write-Output $windowsVersion.toString()


if ( -not $AD_module_status ) { 
    Write-Output "ActiveDirectory missing, installing... " 
    if($windowsVersion.Major -ge 10){
    
    }


}