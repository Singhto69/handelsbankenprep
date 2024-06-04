Import-Module ActiveDirectory

Get-ADOrganizationalUnit -Filter 'Name -like "superou"' | Format-Table Name, DistinguishedName -A

# For ou in list assign number , let user click number to decide?