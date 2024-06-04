#Follow the DRY ( Dont Repeat Yourself) principle!
Write-Output "Checking for DISM Module..."
$dism_module = Get-Module -ListAvailable -Name DISM
if (-not $dism_module) {
    Write-Output "DISM module is not available. Enabling the feature..."
    Enable-WindowsOptionalFeature -Online -FeatureName "Microsoft-Windows-Deployment-Tools-Feature" -All
    Write-Output "DISM module is not available. Importing Module..."
    Import-Module DISM
}

$dism_module = Get-Module -ListAvailable -Name DISM
if ($dism_module) {
    Write-Output "DISM module is available."
    return $true
} else {
    Write-Output "Failed to enable and import the DISM module."
    return $false
}