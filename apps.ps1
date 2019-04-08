#powershell -ExecutionPolicy ByPass -File apps.ps1
#Set-ExecutionPolicy RemoteSigned
#https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6
param([string]$arg1,[string]$arg2)
function runas(){
$user = [string]$arg1
$pass = [string]$arg2
$username = $user
$password = $pass
$credentials = New-Object System.Management.Automation.PSCredential -ArgumentList @($username,(ConvertTo-SecureString -String $password -AsPlainText -Force))

Start-Process "c:\windows\system32\notepad.exe" -Credential($credentials)
}
runas($user,$pass)