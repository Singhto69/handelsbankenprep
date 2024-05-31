function Test-AdminPrivilege{
    $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Prompt-AdminPrivilege{
    param(
        [string]$origin_path = $PSCommandPath 
    )


    $admin_check = Test-AdminPrivilege
    if (-not $admin_check){
        Write-Warning "Administrator privileges are required. Please run this script as an Administrator."
        #Expected format example:  -File "C:\path\to\your\script.ps1"
        #$script = '-File "' + $myInvocation.MyCommand.Definition + '"'
        $script = '-File "' + $origin_path + '"'
        Write-Host "Script Command: $script"
        #  Start-Process Powershell = start another instance of powershell
        # -ArgumentList passes $script as argument to the new instance
        # -Verb RunAs builtin windows feature to prompt for admin privilege
        Start-Process PowerShell -ArgumentList $script -Verb RunAs
        exit
    }
}