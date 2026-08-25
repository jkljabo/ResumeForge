from resumeforge.models import Header


def test_header_model():

    header = Header(
        name="Jason Little",
        headline="Senior Software Engineer",
        tagline="Enterprise Modernization",
        location="Marietta, GA",
        phone="404-783-3480",
        email="jason.k.little@comcast.net",
        linkedin="https://linkedin.com/in/jason",
        github="https://github.com/jkljabo",
        portfolio="https://jasonlittle-dev.netlify.app"
    )

    assert header.name == "Jason Little"
    assert header.headline == "Senior Software Engineer"