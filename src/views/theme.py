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
        max-width: 1760px;
        margin-left: auto;
        margin-right: auto;
        min-height: calc(100vh - 76px);
        box-sizing: border-box;
        padding: 10px 14px 54px;
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
    .cargo-capacity-card {
        border-radius: 8px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: stretch !important;
    }
    .cargo-capacity-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 18px;
        padding: 14px 16px;
        border-bottom: 1px solid rgba(21, 50, 74, 0.08);
    }
    .cargo-capacity-metrics {
        display: grid;
        grid-template-columns: repeat(2, minmax(94px, 1fr));
        gap: 8px;
        min-width: min(100%, 250px);
    }
    .cargo-metric {
        padding: 8px 10px;
        border-radius: 8px;
        background: #f4f8fb;
        border: 1px solid rgba(21, 50, 74, 0.08);
    }
    .cargo-metric-label {
        color: #5f788c;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    .cargo-metric-value {
        color: #15324a;
        font-size: 1.28rem;
        font-weight: 800;
        line-height: 1.1;
    }
    .cargo-metric-caption {
        color: #5f788c;
        font-size: 0.78rem;
        white-space: nowrap;
    }
    .cargo-visual {
        padding: 12px 16px 10px;
    }
    .cargo-workspace-grid {
        display: grid;
        grid-template-columns: minmax(520px, 1.05fr) minmax(480px, 0.95fr);
        gap: 12px;
        padding: 0 16px 10px;
        align-items: start;
    }
    .cargo-plane-column,
    .cargo-cg-column {
        min-width: 0;
    }
    .aircraft-shell {
        display: grid;
        grid-template-columns: 9% 1fr 12%;
        align-items: center;
        width: 100%;
        min-height: 112px;
    }
    .aircraft-nose {
        height: 72px;
        border-radius: 999px 0 0 999px;
        background: linear-gradient(90deg, #dce7ef, #f7fbfd);
        border: 1px solid rgba(21, 50, 74, 0.12);
        border-right: 0;
    }
    .aircraft-tail {
        height: 72px;
        clip-path: polygon(0 0, 58% 0, 100% 50%, 58% 100%, 0 100%);
        background: linear-gradient(90deg, #f7fbfd, #dce7ef);
        border: 1px solid rgba(21, 50, 74, 0.12);
        border-left: 0;
    }
    .cargo-deck {
        position: relative;
        display: flex;
        align-items: center;
        min-height: 90px;
        padding: 20px 14px 30px;
        background: #ffffff;
        border-block: 1px solid rgba(21, 50, 74, 0.12);
        box-shadow: inset 0 0 0 1px rgba(47, 111, 237, 0.08);
    }
    .cargo-slot-strip {
        display: flex;
        width: 100%;
        height: 42px;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(21, 50, 74, 0.16);
        background: #edf4f9;
    }
    .cargo-slot {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 11px;
        color: transparent;
        font-size: 0.65rem;
        font-weight: 700;
        border-right: 1px solid rgba(21, 50, 74, 0.14);
        background: linear-gradient(180deg, #f8fbfd 0%, #eaf2f7 100%);
    }
    .cargo-slot:nth-child(5n) {
        background: linear-gradient(180deg, #eef8f6 0%, #dcefeb 100%);
    }
    .cargo-load-slot {
        position: relative;
        padding: 4px 3px;
        color: #557187;
    }
    .cargo-slot-number {
        position: absolute;
        top: 2px;
        left: 50%;
        transform: translateX(-50%);
        color: #6f8799;
        font-size: 0.54rem;
        font-weight: 800;
    }
    .cargo-slot-load {
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 2px;
        width: 100%;
        height: 100%;
        padding-top: 9px;
    }
    .cargo-empty-slot {
        color: #8ba0af;
        font-size: 0.5rem;
        font-weight: 700;
        text-transform: uppercase;
        writing-mode: vertical-rl;
        margin-inline: auto;
    }
    .loaded-cargo {
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        color: #ffffff;
        font-size: 0.58rem;
        font-weight: 900;
        line-height: 1;
        min-height: 14px;
        box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.12);
    }
    .loaded-cargo-standard {
        flex: 1;
        background: #2f6fed;
    }
    .loaded-cargo-half {
        flex: 1;
        background: #1f9d8b;
    }
    .cargo-slot:last-child {
        border-right: 0;
    }
    .selected-cargo-length {
        position: absolute;
        left: 14px;
        right: 14px;
        bottom: 12px;
        height: 22px;
        color: #15324a;
        border-inline: 2px solid #2f6fed;
    }
    .selected-cargo-length::before {
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        top: 10px;
        border-top: 2px solid #2f6fed;
    }
    .selected-cargo-length span {
        position: absolute;
        left: 50%;
        top: -8px;
        transform: translateX(-50%);
        padding: 0 5px;
        background: #ffffff;
        color: #15324a;
        font-size: 0.78rem;
        font-weight: 800;
        line-height: 1;
    }
    .cargo-samples {
        display: grid;
        grid-template-columns: auto 1fr;
        align-items: center;
        gap: 12px;
        margin-top: 8px;
    }
    .cargo-samples-label {
        color: #446276;
        font-size: 0.82rem;
        font-weight: 800;
        white-space: nowrap;
    }
    .cargo-samples-strip {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
    }
    .cargo-sample {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 25px;
        height: 17px;
        border-radius: 4px;
        background: #dfeaf2;
        color: #33566f;
        font-size: 0.62rem;
        font-weight: 800;
        border: 1px solid rgba(21, 50, 74, 0.12);
    }
    .cargo-sample-overflow {
        background: #fff3df;
        color: #935a09;
        border-color: rgba(201, 122, 16, 0.28);
    }
    .cargo-sample-half {
        background: #dff3ef;
        color: #146f63;
    }
    .cargo-sample-loaded {
        background: #2f6fed;
        color: #ffffff;
        border-color: #2f6fed;
    }
    .cargo-note {
        margin-top: 0;
        padding: 8px 10px;
        border-left: 4px solid #1f9d8b;
        border-radius: 8px;
        background: #f5faf9;
        color: #446276;
        font-size: 0.92rem;
    }
    .cargo-loading-visual {
        padding: 0;
    }
    .cargo-load-controls {
        margin-top: 8px;
        padding: 9px;
        border-top: 1px solid rgba(21, 50, 74, 0.08);
        border-radius: 8px;
        background: #f8fbfd;
        border: 1px solid rgba(21, 50, 74, 0.08);
    }
    .cg-shear-section {
        margin: 0;
        padding: 12px;
        border-radius: 8px;
        background: #f8fbfd;
        border: 1px solid rgba(21, 50, 74, 0.10);
    }
    .cg-shear-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 14px;
        margin-bottom: 10px;
    }
    .cg-shear-subtitle,
    .shear-caption {
        color: #5f788c;
        font-size: 0.86rem;
    }
    .cg-status {
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 900;
        white-space: nowrap;
    }
    .cg-status-ok {
        color: #116943;
        background: #dcf5e9;
    }
    .cg-status-bad {
        color: #9a2525;
        background: #fde4e4;
    }
    .cg-axis-panel {
        position: relative;
        height: 88px;
        border-radius: 8px;
        background:
            linear-gradient(90deg, rgba(47, 111, 237, 0.05), transparent 50%, rgba(201, 122, 16, 0.06)),
            #ffffff;
        border: 1px solid rgba(21, 50, 74, 0.08);
        overflow: hidden;
    }
    .cg-axis-line {
        position: absolute;
        left: 24px;
        right: 24px;
        top: 48px;
        height: 2px;
        background: #8da4b6;
    }
    .cg-limit-zone {
        position: absolute;
        top: 22px;
        bottom: 18px;
        background: rgba(31, 157, 139, 0.14);
        border-inline: 1px solid rgba(31, 157, 139, 0.48);
    }
    .cg-axis-label {
        position: absolute;
        top: 10px;
        color: #6a8295;
        font-size: 0.75rem;
        font-weight: 800;
    }
    .cg-axis-forward {
        left: 14px;
    }
    .cg-axis-aft {
        right: 14px;
    }
    .cg-marker {
        position: absolute;
        top: 46px;
        transform: translateX(-50%);
        padding-top: 12px;
        color: #446276;
        font-size: 0.68rem;
        font-weight: 900;
        white-space: nowrap;
    }
    .cg-marker::before {
        content: "";
        position: absolute;
        left: 50%;
        top: -12px;
        width: 3px;
        height: 26px;
        transform: translateX(-50%);
        border-radius: 999px;
        background: #446276;
    }
    .cg-min::before,
    .cg-max::before {
        background: #d78a1d;
    }
    .cg-target::before {
        background: #1f9d8b;
    }
    .cg-empty {
        top: 14px;
    }
    .cg-empty::before {
        background: #557187;
    }
    .cg-loaded {
        top: 62px;
        color: #15324a;
        font-size: 0.78rem;
    }
    .cg-loaded::before {
        height: 34px;
        top: -24px;
        background: #2f6fed;
        box-shadow: 0 0 0 4px rgba(47, 111, 237, 0.14);
    }
    .cg-metrics {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 8px;
        margin-top: 10px;
    }
    .cg-metrics div {
        padding: 8px 9px;
        border-radius: 8px;
        background: #ffffff;
        border: 1px solid rgba(21, 50, 74, 0.08);
    }
    .cg-metrics span {
        display: block;
        color: #6a8295;
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
    }
    .cg-metrics strong {
        color: #15324a;
        font-size: 0.9rem;
    }
    .cg-metrics .cg-metric-over-limit {
        background: #fde4e4;
        border-color: rgba(217, 79, 79, 0.38);
    }
    .cg-metrics .cg-metric-over-limit span,
    .cg-metrics .cg-metric-over-limit strong {
        color: #9a2525;
    }
    .cg-left-mass {
        background: #eef5ff !important;
        border-color: rgba(47, 111, 237, 0.22) !important;
    }
    .cg-left-mass span,
    .cg-left-mass strong {
        color: #2457b8 !important;
    }
    .cg-right-mass {
        background: #fff6e8 !important;
        border-color: rgba(201, 122, 16, 0.24) !important;
    }
    .cg-right-mass span,
    .cg-right-mass strong {
        color: #935a09 !important;
    }
    .cg-left-mass.cg-side-over-limit,
    .cg-right-mass.cg-side-over-limit {
        background: #fde4e4 !important;
        border-color: rgba(217, 79, 79, 0.38) !important;
    }
    .cg-left-mass.cg-side-over-limit span,
    .cg-left-mass.cg-side-over-limit strong,
    .cg-right-mass.cg-side-over-limit span,
    .cg-right-mass.cg-side-over-limit strong {
        color: #9a2525 !important;
    }
    .shear-panel {
        margin-top: 10px;
        padding: 10px;
        border-radius: 8px;
        background: #ffffff;
        border: 1px solid rgba(21, 50, 74, 0.08);
    }
    .shear-title {
        color: #15324a;
        font-size: 0.92rem;
        font-weight: 900;
        margin-bottom: 6px;
    }
    .shear-svg {
        display: block;
        width: 100%;
        height: 74px;
        border-radius: 6px;
        background:
            linear-gradient(90deg, transparent 49.8%, rgba(21, 50, 74, 0.08) 50%, transparent 50.2%),
            linear-gradient(180deg, #f8fbfd, #eef5f9);
    }
    .shear-axis,
    .shear-midline {
        stroke: rgba(21, 50, 74, 0.28);
        stroke-width: 0.7;
    }
    .shear-midline {
        stroke-dasharray: 2 2;
    }
    .shear-line {
        fill: none;
        stroke: #2f6fed;
        stroke-width: 2.2;
        stroke-linecap: round;
        stroke-linejoin: round;
    }
    .cargo-load-header {
        width: 100%;
        align-items: baseline;
        justify-content: space-between;
        gap: 12px;
        padding-top: 0;
        margin-bottom: 8px;
    }
    .cargo-load-actions {
        width: 100%;
        align-items: center;
        gap: 8px;
    }
    .cargo-load-select {
        min-width: min(100%, 280px);
        flex: 1;
    }
    .cargo-position-select {
        width: 132px;
    }
    .cargo-table-section {
        padding: 0 16px 16px;
        display: block;
        width: 100%;
        box-sizing: border-box;
        clear: both;
    }
    .cargo-table-header {
        width: 100%;
        align-items: center;
        justify-content: flex-start;
        gap: 12px;
        margin-bottom: 10px;
    }
    .cargo-table-badge {
        padding: 5px 10px;
    }
    .cargo-data-table {
        width: 100% !important;
        min-width: 100% !important;
        border-radius: 8px;
        overflow: hidden;
        border-color: rgba(21, 50, 74, 0.10) !important;
    }
    .cargo-data-table .q-table__container,
    .cargo-data-table .q-table__middle,
    .cargo-data-table table {
        width: 100% !important;
    }
    .cargo-data-table table {
        table-layout: fixed;
    }
    .cargo-data-table th:nth-child(1),
    .cargo-data-table td:nth-child(1) {
        width: 12%;
    }
    .cargo-data-table th:nth-child(2),
    .cargo-data-table td:nth-child(2) {
        width: 22%;
    }
    .cargo-data-table th:nth-child(3),
    .cargo-data-table td:nth-child(3) {
        width: 18%;
    }
    .cargo-data-table th:nth-child(4),
    .cargo-data-table td:nth-child(4) {
        width: 48%;
    }
    .cargo-data-table thead tr {
        background: #f4f8fb;
    }
    .cargo-data-table th {
        color: #446276;
        font-weight: 800 !important;
        font-size: 0.78rem;
        text-transform: uppercase;
    }
    .cargo-data-table td {
        color: #15324a;
        font-weight: 600;
    }
    .cargo-data-table tbody tr:nth-child(even) {
        background: #fbfdfe;
    }
    @media (max-width: 1180px) {
        .cargo-workspace-grid {
            grid-template-columns: 1fr;
            padding-inline: 14px;
        }
        .cg-metrics {
            grid-template-columns: repeat(3, minmax(0, 1fr));
        }
    }
    @media (max-width: 760px) {
        .page {
            padding-inline: 10px;
        }
        .cargo-capacity-header {
            display: block;
        }
        .cargo-capacity-metrics {
            grid-template-columns: repeat(3, minmax(0, 1fr));
            min-width: 0;
            margin-top: 14px;
        }
        .cargo-metric {
            padding: 8px;
        }
        .cargo-metric-value {
            font-size: 1.15rem;
        }
        .cargo-metric-caption {
            white-space: normal;
        }
        .cargo-workspace-grid {
            gap: 10px;
            padding: 0 10px 12px;
        }
        .aircraft-shell {
            grid-template-columns: 8% 1fr 10%;
            min-height: 150px;
        }
        .aircraft-nose,
        .aircraft-tail {
            height: 84px;
        }
        .cargo-deck {
            min-height: 112px;
            padding: 26px 10px 36px;
        }
        .cargo-slot-strip {
            height: 46px;
        }
        .cargo-slot {
            min-width: 5px;
            font-size: 0;
        }
        .cargo-slot-load {
            padding-top: 7px;
        }
        .cargo-slot-number,
        .cargo-empty-slot {
            display: none;
        }
        .loaded-cargo {
            font-size: 0;
            min-height: 11px;
        }
        .selected-cargo-length {
            left: 10px;
            right: 10px;
        }
        .cargo-samples {
            grid-template-columns: 1fr;
            gap: 8px;
        }
        .cargo-samples-label {
            white-space: normal;
        }
        .cargo-loading-visual,
        .cargo-load-controls {
            padding-inline: 10px;
        }
        .cargo-load-controls {
            margin-top: 8px;
        }
        .cg-shear-section {
            margin-inline: 0;
            padding: 12px;
        }
        .cg-shear-header {
            display: block;
        }
        .cg-status {
            display: inline-block;
            margin-top: 8px;
        }
        .cg-metrics {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .cg-marker {
            font-size: 0.58rem;
        }
        .shear-svg {
            height: 96px;
        }
        .cargo-load-actions {
            align-items: stretch;
        }
        .cargo-load-select,
        .cargo-position-select {
            width: 100%;
        }
        .cargo-table-section {
            padding: 0 10px 14px;
        }
    }
    """)
