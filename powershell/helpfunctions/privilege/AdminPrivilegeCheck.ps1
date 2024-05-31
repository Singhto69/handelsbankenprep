function Test-AdminPrivilege{
    $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    Write-Host $currentUser
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    Write-Host $principal
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}


function Prompt-AdminPrivilege{
    $admin_check = Test-AdminPrivilege
    Write-Output $admin_check
    if (-not $admin_check){
        Write-Warning "Administrator privileges are required. Please run this script as an Administrator."
        $script = "-File `"" + $myInvocation.MyCommand.Definition + "`""
        Start-Process PowerShell -ArgumentList $script -Verb RunAs
        exit
    }
}

#Prompt-AdminPrivilege