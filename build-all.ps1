# URL to App - Build Script
# Run this script to build for all platforms
# Usage: .\build-all.ps1

$ErrorActionPreference = "Stop"

Write-Host "=== URL to App - Multi-Platform Builder ===" -ForegroundColor Cyan
Write-Host ""

$PROJECT_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $PROJECT_ROOT

Write-Host "[1/4] Installing dependencies..." -ForegroundColor Yellow
npm install
Write-Host ""

Write-Host "[2/4] Building frontend..." -ForegroundColor Yellow
npm run build
Write-Host ""

Write-Host "[3/4] Building Tauri app for current platform..." -ForegroundColor Yellow
npm run tauri build
Write-Host ""

Write-Host "[4/4] Build complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Output location: src-tauri\target\release\bundle\" -ForegroundColor Cyan
Write-Host ""
Write-Host "Note: Cross-compilation requires additional setup:" -ForegroundColor Yellow
Write-Host "  - Windows: Already configured" -ForegroundColor Gray
Write-Host "  - macOS: Requires macOS host or cross-compilation toolchain" -ForegroundColor Gray
Write-Host "  - Linux: Requires Linux host or Docker cross-compilation" -ForegroundColor Gray
Write-Host ""
Write-Host "For true cross-platform builds, consider using:" -ForegroundColor Yellow
Write-Host "  - GitHub Actions (recommended)" -ForegroundColor Gray
Write-Host "  - Docker with multi-platform targets" -ForegroundColor Gray
Write-Host "  - CI/CD services like Cirrus CI or Azure Pipelines" -ForegroundColor Gray
