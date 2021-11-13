function ver-perfilredactual{
$perfilRed = Get-NetConnectionProfile
Write-Host "Nombre de red: " $perfilRed.name
Write-Host "Perfil de red: " $perfilRed.NetworkCategory
}
ver-perfilredactual
function Ver-reglasBloqueo{
if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){
Get-NetFirewallRule -Action Block -Enabled True
} else {
Write-Host "No hay reglas definidas aun"
}
}
Ver-reglasBloqueo