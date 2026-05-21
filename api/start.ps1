# Inicia a API Linka Ads Intelligence
# Execute: .\api\start.ps1

Set-Location $PSScriptRoot

if (-not (Test-Path ".venv")) {
    Write-Host "Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv .venv
}

Write-Host "Ativando ambiente virtual..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1

if (-not (Test-Path ".venv\Lib\site-packages\fastapi")) {
    Write-Host "Instalando dependencias..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host "API rodando em http://localhost:8000" -ForegroundColor Green
Write-Host "Docs em http://localhost:8000/docs" -ForegroundColor Cyan
uvicorn main:app --reload --port 8000
