from resumeforge.domain import Education


def test_education_model():

    education = Education(
        school="Georgia State University",
        degree="Bachelor of Science",
        field="Computer Science",
        graduation_year="2003"
    )

    assert education.school == "Georgia State University"
    assert education.degree == "Bachelor of Science"