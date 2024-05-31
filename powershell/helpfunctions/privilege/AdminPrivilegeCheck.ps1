# WindowsIdentity::GetCurrent() = Retrieve current windows user associated with this process
# Windowsprincipal = security context of user account associated with current running process or thread.
function Test-AdminPrivilege{
    $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

#  Start-Process Powershell = start another instance of powershell
# -ArgumentList passes $script as argument to the new instance
# -Verb RunAs builtin windows feature to prompt for admin privilege
function Prompt-AdminPrivilege{
    param(
        [string]$origin_path = $PSCommandPath 
    )


    $admin_check = Test-AdminPrivilege
    if (-not $admin_check){
        Write-Warning "Process $PID Does not have admin privileges. Please approve running as an Administrator."
        #Expected format: -File "C:\path\to\your\script.ps1"
        #$script = '-File "' + $myInvocation.MyCommand.Definition + '"'
        $script = '-File "' + $origin_path + '"'
        #Write-Host "Script Command: $script"
        Start-Process PowerShell -ArgumentList $script -Verb RunAs
        exit
    }
    return $true
}