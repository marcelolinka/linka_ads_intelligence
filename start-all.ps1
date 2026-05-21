# Linka Ads Intelligence — sobe frontend + API em janelas independentes
# Execute: .\start-all.ps1

$root = $PSScriptRoot

# --- Frontend (porta 8080) ---
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-File", "$root\server.ps1" `
  -WindowStyle Normal

# --- FastAPI (porta 8000) ---
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy", "Bypass", "-Command", `
  "cd '$root\api'; .\.venv\Scripts\uvicorn main:app --reload --port 8000" `
  -WindowStyle Normal

Write-Host ""
Write-Host "Servidores iniciados em janelas independentes:" -ForegroundColor Green
Write-Host "  Frontend  -> http://localhost:8080" -ForegroundColor Cyan
Write-Host "  API       -> http://localhost:8000" -ForegroundColor Cyan
Write-Host "  API Docs  -> http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para parar: feche as janelas do PowerShell abertas." -ForegroundColor Gray
