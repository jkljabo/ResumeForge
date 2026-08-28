from abc import ABC, abstractmethod


class BaseTheme:

    def apply(self, document):
        raise NotImplementedError

    def style_heading(self, paragraph, level):
        """Called after a heading is created."""
        return paragraph

    def style_paragraph(self, paragraph):
        """Called after a paragraph is created."""
        return paragraph

    def style_bullet(self, paragraph):
        """Called after a bullet is created."""
        return paragraph