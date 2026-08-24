def main():

    from pathlib import Path

    from resumeforge.builder import ResumeBuilder
    from resumeforge.loader import load_resume

    from resumeforge.sections import header
    from resumeforge.sections import summary

    resume = load_resume()

    builder = ResumeBuilder()

    header.render(builder.document, resume)
    summary.render(builder.document, resume)

    output = Path("output") / "Executive_Master_Resume_v8.docx"

    builder.save(output)

    print("Resume generated.")

if __name__ == "__main__":
    main()