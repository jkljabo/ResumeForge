def main():

    from pathlib import Path

    from resume.builder import ResumeBuilder
    from resume.loader import load_resume

    from resume.sections import header
    from resume.sections import summary

    resume = load_resume()

    builder = ResumeBuilder()

    header.render(builder.document, resume)
    summary.render(builder.document, resume)

    output = Path("output") / "Executive_Master_Resume_v8.docx"

    builder.save(output)

    print("Resume generated.")

if __name__ == "__main__":
    main()