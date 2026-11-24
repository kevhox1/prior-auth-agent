"""Shared look for every page: the CSS from ui/styles.css, the icon set and the HTML block helper."""

from __future__ import annotations

import html
import re
from pathlib import Path

import streamlit as st

CSS = (Path(__file__).parent / "styles.css").read_text()
FONTS = ("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700"
         "&family=Space+Grotesk:wght@500;600;700&display=swap")
DISCLAIMER = "Synthetic data only. Not clinically validated. Not medical advice."
REPO = "https://github.com/kevhox1/prior-auth-agent"

# Icons from the design (24px grid, stroke = currentColor).
_ICONS = {
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6z"/><path d="M12 8.5v4.5"/><path d="M12 16v.01"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5"/><path d="M12 7.5v.01"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16 9.5"/>',
    "x": '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    "pending": '<circle cx="12" cy="12" r="9" stroke-dasharray="3.2 3"/><path d="M12 8v5"/><path d="M12 16.5v.01"/>',
    "swap": '<path d="M4 8h13l-3-3"/><path d="M20 16H7l3 3"/>',
    "warn": '<path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4.5"/><path d="M12 17.5v.01"/>',
    "arrow": '<path d="M4 12h15"/><path d="M14 7l5 5-5 5"/>',
    "chevron": '<path d="M9 6l6 6-6 6"/>',
    "tick": '<path d="M7 12.5l3.3 3.3L17.5 8"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.5l3.5 2"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.2-4 4-6 7.5-6s6.3 2 7.5 6"/>',
    "list": '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><path d="M4.5 6.5v.01M4.5 12v.01M4.5 17.5v.01"/>',
    "lock": '<rect x="5" y="11" width="14" height="9.5" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "code": '<path d="M8.5 7l-5 5 5 5"/><path d="M15.5 7l5 5-5 5"/>',
}
STATUS_ICON = {"met": "check", "notmet": "x", "insuf": "pending", "conf": "swap"}


def icon(name: str, size: int = 15, width: float = 2.2) -> str:
    return (f'<svg class="pa-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{_ICONS[name]}</svg>')


def e(s) -> str:
    return html.escape(str(s))


_BLOCK_TAGS = re.compile(r"<(/?)(h1|h2|h3|p|ul|li)\b")


def block(markup: str) -> None:
    """Render an HTML fragment. st.markdown keeps inline SVG and <details>, which st.html strips.
    Headings, paragraphs and lists become divs so Streamlit's markdown styles don't override the design,
    and newlines become entities so a blank line in chart text can't end the HTML block."""
    markup = _BLOCK_TAGS.sub(lambda m: f"<{m.group(1)}div", markup).replace("\n", "&#10;")
    st.markdown(f'<div class="pa-x">{markup}</div>', unsafe_allow_html=True)


def inject_css() -> None:
    css = "\n".join(line for line in CSS.splitlines() if line.strip())  # no blank lines inside markdown HTML
    st.markdown(f"<style>@import url('{FONTS}');\n{css}</style>", unsafe_allow_html=True)


def brand(sub: str) -> None:
    block(f'<div class="pa-brand"><div class="pa-brand-mark">{icon("shield", 22, 2)}</div><div>'
          f'<div class="pa-brand-name">Prior Auth Agent</div><div class="pa-brand-sub">{e(sub)}</div></div></div>')
