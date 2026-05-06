from nicegui import ui


def apply_app_theme() -> None:
    ui.colors(
        primary="#2f6fed",
        secondary="#1f9d8b",
        accent="#c97a10",
        positive="#1e9e63",
        negative="#d94f4f",
        warning="#d78a1d",
        dark="#18324a",
    )

    ui.add_css("""
    body {
        background:
            radial-gradient(circle at top left, rgba(47, 111, 237, 0.10), transparent 28%),
            radial-gradient(circle at top right, rgba(31, 157, 139, 0.10), transparent 30%),
            linear-gradient(180deg, #f7fafc 0%, #eef4f8 100%);
        color: #16324a;
    }
    .nicegui-content {
        background: transparent;
    }
    .page {
        width: 100%;
        max-width: 1500px;
        margin-left: auto;
        margin-right: auto;
        min-height: calc(100vh - 76px);
        box-sizing: border-box;
        padding: 10px;
    }
    .card_title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #15324a;
    }
    .q-table__card {
        box-shadow: none !important;
    }
    .q-card {
        background: rgba(255, 255, 255, 0.88) !important;
        border: 1px solid rgba(21, 50, 74, 0.08);
        border-radius: 18px !important;
        box-shadow: 0 4px 16px rgba(21, 50, 74, 0.08) !important;
        backdrop-filter: blur(10px);
    }
    .q-dialog .q-card {
        background: #ffffff !important;
        backdrop-filter: none;
    }
    .q-btn {
        border-radius: 14px !important;
        font-weight: 700;
        letter-spacing: 0.01em;
        box-shadow: 0 8px 18px rgba(21, 50, 74, 0.10);
    }
    .q-btn:before {
        border-radius: 14px !important;
    }
    .q-badge {
        border-radius: 999px;
        font-weight: 700;
        letter-spacing: 0.01em;
    }
    .q-tabs {
        gap: 6px;
    }
    .q-tab {
        color: #557187;
        border-radius: 14px;
        min-height: 52px;
    }
    .q-tab--active {
        color: #15324a !important;
        background: rgba(255, 255, 255, 0.82);
    }
    .q-tab__indicator {
        background: #2f6fed !important;
        height: 3px !important;
        border-radius: 999px;
    }
    .q-separator--vertical {
        background: rgba(21, 50, 74, 0.10);
    }
    .text-grey-7,
    .text-grey-8 {
        color: #5f788c !important;
    }
    .q-tab-panels {
        background: transparent !important;
    }
    .main-tab-panels,
    .main-tab-panels .q-panel,
    .main-tab-panels .q-tab-panel {
        width: 100%;
        background: transparent !important;
    }
    .target-setup-panels .q-tab-panel {
        padding-top: 0 !important;
    }
    .q-page-container {
        padding-bottom: 0 !important;
    }
    """)
