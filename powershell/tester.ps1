Import-Module ActiveDirectory

function Lazy_Ou_Selector{
    $i = 0
    $ou_table = @{}
    Read-Host 'Please enter full or partial OU name...' | ForEach-Object {
        Get-ADOrganizationalUnit -Filter "Name -like '*$_*'" | ForEach-Object {
            $distinguishedName = $_.DistinguishedName
            $ou_table["$i"] = "$distinguishedName"
            $i = $i + 1
            }
    }
    Write-Output $ou_table
    
    Read-Host 'Please enter the index for the correct OU' | ForEach-Object{  
       if([int]$_ -le $ou_table.Count) {
            return $ou_table["$_"]
       }
    }
    #|Format-Table Name, DistinguishedName -A}
}

#Get-ADOrganizationalUnit -Filter "Name -like '*superou*'" | Format-Table Name, DistinguishedName -A