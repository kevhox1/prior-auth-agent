"""Entry point: a start-here tour and the reviewer console.

    .venv/bin/streamlit run ui/app.py

The pages are ui/tour.py and ui/console.py. Shared styling is in ui/theme.py and ui/styles.css.
"""

import streamlit as st

st.set_page_config(page_title="Prior Auth Agent", page_icon=":material/shield:", layout="wide")
page = st.navigation([
    st.Page("tour.py", title="Start here", icon=":material/explore:", default=True),
    st.Page("console.py", title="Reviewer console", icon=":material/fact_check:"),
], position="top")
page.run()
