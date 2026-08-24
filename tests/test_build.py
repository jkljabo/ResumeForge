from pathlib import Path

from resume.loader import load_resume
from resume.builder import ResumeBuilder
from resume.sections import header, summary

def test_build_resume():
    resume = load_resume()

    builder = ResumeBuilder()

    header.render(builder.document, resume)
    summary.render(builder.document, resume)

    output = Path("output") / "test_resume.docx"

    builder.save(output)

    assert output.exists()
    
Write-Host ""
Write-Host "Build Verification"
Write-Host "------------------"

python build_resume.py

if ($LASTEXITCODE -eq 0)
{
    Write-Host "Resume build succeeded." -ForegroundColor Green
}
else
{
    Write-Host "Resume build FAILED." -ForegroundColor Red
}