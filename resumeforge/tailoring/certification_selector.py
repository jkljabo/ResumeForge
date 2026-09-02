class CertificationSelector:

    def select(
        self,
        profile,
        match,
    ):

        if match is None:
            return profile.certifications

        matched = {
            keyword.lower()
            for keyword in match.matched
        }

        selected = []

        for certification in profile.certifications:

            text = certification.lower()

            if any(keyword in text for keyword in matched):
                selected.append(certification)

        return selected