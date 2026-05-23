# =============================================================================
# app.py — Small Business Dashboard
#          Public demo entry point.
# -----------------------------------------------------------------------------

from components.core import (
    ensure_directories,
    load_styles,
    load_data,
    build_filters,
    get_page,
    render_page,
)

# ── Setup ──
ensure_directories()
load_styles()

# ── Data ──
df = load_data()
filtered_df = build_filters(df)

# ── Navigation & Routing ──
page = get_page()
render_page(page, filtered_df, df)


