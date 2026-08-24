Write-Host ""
Write-Host "ResumeForge Project Verification"
Write-Host "================================="
Write-Host ""

Write-Host "Current Directory:"
Get-Location

Write-Host ""
Write-Host "Directory Structure"
Write-Host "-------------------"
tree /F

Write-Host ""
Write-Host "Python Version"
Write-Host "--------------"
python --version

Write-Host ""
Write-Host "Python Executable"
Write-Host "-----------------"
python -c "import sys; print(sys.executable)"

Write-Host ""
Write-Host "Pip Version"
Write-Host "-----------"
python -m pip --version

Write-Host ""
Write-Host "Pytest Version"
Write-Host "--------------"
python -m pytest --version

Write-Host ""
Write-Host "Installed Packages"
Write-Host "------------------"
python -m pip show python-docx
python -m pip show reportlab
python -m pip show pytest

Write-Host ""
Write-Host "Project Files"
Write-Host "-------------"

Get-ChildItem -Recurse -File |
    Select-Object FullName, Length |
    Sort-Object FullName

Write-Host ""
Write-Host "Done."