$machine_execution_status = Get-ExecutionPolicy
if ( $machine_execution_status -eq 'Restricted' ){
    Set-ExecutionPolicy RemoteSigned
}