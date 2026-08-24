from resume.loader import load_resume

def test_resume_loads():
    resume = load_resume()

    assert resume is not None