import streamlit as st

st.set_page_config(
    page_title="DupeGen",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# GLOBAL CSS
# ---------------------------------------------------------

st.html("""
<style>

:root {
    --bg: #080b14;
    --sidebar: #0d1220;
    --card: #111827;
    --border: #263247;
    --text: #f8fafc;
    --muted: #94a3b8;
    --purple: #8b5cf6;
    --cyan: #22d3ee;
    --green: #22c55e;
}

.stApp {
    background: var(--bg);
    color: var(--text);
}

header {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    background: var(--sidebar);
    border-right: 1px solid var(--border);
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
}

.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 24px;
}

.metric-value {
    font-size: 2rem;
    font-weight: 800;
    color: white;
}

.metric-label {
    color: var(--muted);
    font-size: .8rem;
    margin-bottom: 10px;
}

.metric-desc {
    color: var(--muted);
    font-size: .75rem;
    margin-top: 12px;
}

.hero {
    background:
        radial-gradient(circle at top right,
        rgba(139,92,246,.2), transparent 35%),
        #101827;

    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 38px;
}

.status {
    display:inline-block;
    background:rgba(34,197,94,.1);
    border:1px solid rgba(34,197,94,.3);
    color:#86efac;
    border-radius:999px;
    padding:8px 15px;
}

.section-title {
    color:white;
    font-size:1.35rem;
    font-weight:700;
    margin-top:30px;
    margin-bottom:15px;
}

</style>
""")

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.html("""
    <div style="padding:10px 5px 25px 5px">

        <div style="
            color:white;
            font-size:1.6rem;
            font-weight:800">
            ◈ DUPEGEN
        </div>

        <div style="
            color:#94a3b8;
            font-size:.78rem;
            margin-top:4px">
            Synthetic Image Intelligence
        </div>

    </div>
    """)

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Generate",
            "Dataset",
            "Quality",
            "Trust & Diversity",
            "Export"
        ]
    )

    st.divider()

    st.caption("WORKSPACE")
    st.write("**DupeGen Research**")
    st.caption("Image Generation Workspace")

    st.divider()

    st.html("""
    <div class="status">
        ● Pipeline Online
    </div>
    """)

# ---------------------------------------------------------
# OVERVIEW
# ---------------------------------------------------------

if page == "Overview":

    st.html("""
    <div class="hero">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:flex-start">

            <div>

                <div style="
                    font-size:2.5rem;
                    font-weight:800;
                    color:white">
                    Synthetic Image Intelligence
                </div>

                <div style="
                    color:#94a3b8;
                    font-size:1.05rem;
                    margin-top:12px">
                    Generate realistic synthetic image datasets
                    for rare and underrepresented visual scenarios.
                </div>

            </div>

            <div class="status">
                ● System Operational
            </div>

        </div>

    </div>
    """)

    st.html("""
    <div class="section-title">
        Platform Overview
    </div>
    """)

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("SOURCE IMAGES", "2,480", "Reference images"),
        ("GENERATED", "10,000", "Synthetic images"),
        ("QUALITY", "94.6", "Overall score"),
        ("DIVERSITY", "91.8", "Visual variation")
    ]

    for col, (label, value, desc) in zip([c1,c2,c3,c4], cards):

        with col:

            st.html(f"""
            <div class="card">

                <div class="metric-label">
                    {label}
                </div>

                <div class="metric-value">
                    {value}
                </div>

                <div class="metric-desc">
                    {desc}
                </div>

            </div>
            """)

    st.html("""
    <div class="section-title">
        Current Edge Case
    </div>
    """)

    left, right = st.columns([2,1])

    with left:

        st.html("""
        <div class="card">

            <div style="
                color:white;
                font-size:1.2rem;
                font-weight:700">
                Night-time pedestrians in heavy rain
            </div>

            <div style="
                color:#94a3b8;
                margin-top:10px">
                Rare visual conditions selected for
                synthetic image generation.
            </div>

            <div style="
                display:flex;
                gap:60px;
                margin-top:25px">

                <div>

                    <div class="metric-label">
                        RARE COVERAGE
                    </div>

                    <div class="metric-value">
                        6.2%
                    </div>

                </div>

                <div>

                    <div class="metric-label">
                        TARGET
                    </div>

                    <div class="metric-value">
                        10,000
                    </div>

                </div>

            </div>

        </div>
        """)

    with right:

        st.html("""
        <div class="card">

            <div style="
                color:white;
                font-size:1.1rem;
                font-weight:700">
                Pipeline Status
            </div>

            <div style="
                color:#86efac;
                margin-top:18px">
                ✓ Image Processing
            </div>

            <div style="
                color:#86efac;
                margin-top:10px">
                ✓ Generation Pipeline
            </div>

            <div style="
                color:#86efac;
                margin-top:10px">
                ✓ Quality Evaluation
            </div>

        </div>
        """)

    st.html("""
    <div class="section-title">
        DupeGen Workflow
    </div>
    """)

    w1, w2, w3 = st.columns(3)

    workflow = [
        ("01", "Define", "Describe the rare visual scenario."),
        ("02", "Generate", "Create synthetic images."),
        ("03", "Validate", "Evaluate quality and diversity.")
    ]

    for col, (num, title, text) in zip([w1,w2,w3], workflow):

        with col:

            st.html(f"""
            <div class="card">

                <div style="
                    color:#8b5cf6;
                    font-size:1.4rem;
                    font-weight:800">
                    {num}
                </div>

                <div style="
                    color:white;
                    font-weight:700;
                    margin-top:10px">
                    {title}
                </div>

                <div style="
                    color:#94a3b8;
                    margin-top:8px">
                    {text}
                </div>

            </div>
            """)

# ---------------------------------------------------------
# GENERATE PAGE
# ---------------------------------------------------------

elif page == "Generate":

    st.html("""
    <div class="hero">

        <div style="
            font-size:2.3rem;
            font-weight:800;
            color:white;">
            Create Synthetic Dataset
        </div>

        <div style="
            color:#94a3b8;
            font-size:1rem;
            margin-top:10px;">
            Turn rare visual scenarios into high-quality
            synthetic image datasets.
        </div>

    </div>
    """)

    st.html("""
    <div class="section-title">
        Dataset Definition
    </div>
    """)

    left, right = st.columns([1.25, 0.75], gap="large")

    # -----------------------------------------------------
    # LEFT SIDE
    # -----------------------------------------------------

    with left:

        st.html("""
        <div class="card">

            <div style="
                font-size:1.25rem;
                font-weight:700;
                color:white;">
                Define Your Edge Case
            </div>

            <div style="
                color:#94a3b8;
                margin-top:7px;
                margin-bottom:20px;">
                Describe the visual scenario your model
                currently lacks sufficient training data for.
            </div>

        </div>
        """)

        scenario = st.text_area(
            "Scenario Description",
            value="Night-time pedestrians in heavy rain",
            height=130,
            placeholder=(
                "Example: Night-time pedestrians in heavy rain "
                "near urban intersections..."
            )
        )

        st.caption(
            "Be specific about objects, environment, lighting, "
            "weather and visual conditions."
        )

        st.html("""
        <div style="
            margin-top:25px;
            color:white;
            font-size:1.05rem;
            font-weight:700;">
            Reference Images
        </div>

        <div style="
            color:#94a3b8;
            margin-top:5px;
            margin-bottom:12px;">
            Optional — upload real images to guide generation.
        </div>
        """)

        uploaded_files = st.file_uploader(
            "Upload reference images",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

        if uploaded_files:

            st.success(
                f"{len(uploaded_files)} reference image(s) uploaded."
            )

    # -----------------------------------------------------
    # RIGHT SIDE
    # -----------------------------------------------------

    with right:

        st.html("""
        <div class="card">

            <div style="
                font-size:1.25rem;
                font-weight:700;
                color:white;">
                Dataset Configuration
            </div>

            <div style="
                color:#94a3b8;
                margin-top:7px;
                margin-bottom:25px;">
                Configure the synthetic dataset.
            </div>

        </div>
        """)

        image_count = st.slider(
            "Number of Images",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100
        )

        resolution = st.selectbox(
            "Resolution",
            [
                "512 × 512",
                "768 × 768",
                "1024 × 1024",
                "1536 × 1536"
            ],
            index=2
        )

        variation = st.slider(
            "Visual Variation",
            min_value=0,
            max_value=100,
            value=70
        )

        realism = st.slider(
            "Realism",
            min_value=0,
            max_value=100,
            value=85
        )

        st.html(f"""
        <div style="
            margin-top:25px;
            padding:15px;
            background:#0b1220;
            border:1px solid #263247;
            border-radius:12px;">

            <div style="
                color:#94a3b8;
                font-size:.75rem;">
                ESTIMATED DATASET
            </div>

            <div style="
                color:white;
                font-size:1.5rem;
                font-weight:800;
                margin-top:5px;">
                {image_count:,} images
            </div>

            <div style="
                color:#64748b;
                font-size:.75rem;
                margin-top:4px;">
                {resolution} · Synthetic Image Dataset
            </div>

        </div>
        """)

# ---------------------------------------------------------
# DATASET PAGE
# ---------------------------------------------------------

elif page == "Dataset":

    st.html("""
    <div class="hero">

        <div style="
            font-size:2.3rem;
            font-weight:800;
            color:white;">
            Synthetic Dataset
        </div>

        <div style="
            color:#94a3b8;
            margin-top:10px;">
            Explore, inspect and manage your generated
            synthetic image dataset.
        </div>

    </div>
    """)

    # -----------------------------------------------------
    # DATASET HEADER
    # -----------------------------------------------------

    st.html("""
    <div class="section-title">
        Night-time Pedestrians · Heavy Rain
    </div>
    """)

    c1, c2, c3, c4 = st.columns(4)

    dataset_metrics = [
        ("IMAGES", "2,300"),
        ("RESOLUTION", "1024 × 1024"),
        ("QUALITY", "94.6"),
        ("DIVERSITY", "91.8")
    ]

    for col, (label, value) in zip(
        [c1, c2, c3, c4],
        dataset_metrics
    ):

        with col:

            st.html(f"""
            <div class="card">

                <div class="metric-label">
                    {label}
                </div>

                <div class="metric-value"
                     style="font-size:1.45rem;">
                    {value}
                </div>

            </div>
            """)

    # -----------------------------------------------------
    # FILTER BAR
    # -----------------------------------------------------

    st.html("""
    <div style="height:20px;"></div>
    """)

    search_col, filter_col, sort_col = st.columns(
        [2, 1, 1]
    )

    with search_col:

        search = st.text_input(
            "Search",
            placeholder="Search generated images...",
            label_visibility="collapsed"
        )

    with filter_col:

        quality_filter = st.selectbox(
            "Quality",
            [
                "All Images",
                "High Quality",
                "Needs Review"
            ],
            label_visibility="collapsed"
        )

    with sort_col:

        sort_by = st.selectbox(
            "Sort",
            [
                "Newest",
                "Quality",
                "Similarity"
            ],
            label_visibility="collapsed"
        )

    # -----------------------------------------------------
    # IMAGE GALLERY
    # -----------------------------------------------------

    st.html("""
    <div class="section-title">
        Generated Images
    </div>
    """)

    import os

    image_folder = "data/generated"

    if os.path.exists(image_folder):

        image_files = [
            f for f in os.listdir(image_folder)
            if f.lower().endswith(
                (".png", ".jpg", ".jpeg", ".webp")
            )
        ]

    else:

        image_files = []

    if search:

        image_files = [
            f for f in image_files
            if search.lower() in f.lower()
        ]

    if not image_files:

        st.info(
            "No generated images found. "
            "Add images to data/generated/"
        )

    else:

        # Display four images per row

        for i in range(0, len(image_files), 4):

            row_files = image_files[i:i + 4]

            cols = st.columns(4)

            for col, filename in zip(cols, row_files):

                with col:

                    image_path = os.path.join(
                        image_folder,
                        filename
                    )

                    st.image(
                        image_path,
                        use_container_width=True
                    )

                    st.caption(
                        filename
                    )


# ---------------------------------------------------------
# QUALITY PAGE
# ---------------------------------------------------------

elif page == "Quality":

    st.html("""
    <div class="hero">

        <div style="
            font-size:2.3rem;
            font-weight:800;
            color:white;">
            Quality Intelligence
        </div>

        <div style="
            color:#94a3b8;
            margin-top:10px;">
            Evaluate the quality of generated synthetic images.
        </div>

    </div>
    """)

    c1, c2, c3 = st.columns(3)

    metrics = [
        ("OVERALL QUALITY", "94.6"),
        ("REALISM", "96.2"),
        ("CONSISTENCY", "94.1")
    ]

    for col, (label, value) in zip([c1, c2, c3], metrics):

        with col:

            st.html(f"""
            <div class="card">

                <div class="metric-label">
                    {label}
                </div>

                <div class="metric-value">
                    {value}
                </div>

            </div>
            """)

    st.html("""
    <div class="section-title">
        Evaluation Pipeline
    </div>
    """)

    st.info(
        "Member 2's quality-scoring module will be connected here."
    )


# ---------------------------------------------------------
# TRUST & DIVERSITY PAGE
# ---------------------------------------------------------

elif page == "Trust & Diversity":

    st.html("""
    <div class="hero">

        <div style="
            font-size:2.3rem;
            font-weight:800;
            color:white;">
            Trust & Diversity
        </div>

        <div style="
            color:#94a3b8;
            margin-top:10px;">
            Understand how diverse and trustworthy your
            synthetic image dataset is.
        </div>

    </div>
    """)

    c1, c2 = st.columns(2)

    with c1:

        st.html("""
        <div class="card">

            <div class="metric-label">
                DIVERSITY SCORE
            </div>

            <div class="metric-value">
                91.8
            </div>

            <div class="metric-desc">
                Visual variation across generated samples
            </div>

        </div>
        """)

    with c2:

        st.html("""
        <div class="card">

            <div class="metric-label">
                COVERAGE
            </div>

            <div class="metric-value">
                88.4%
            </div>

            <div class="metric-desc">
                Coverage of target visual conditions
            </div>

        </div>
        """)


# ---------------------------------------------------------
# EXPORT PAGE
# ---------------------------------------------------------

elif page == "Export":

    st.html("""
    <div class="hero">

        <div style="
            font-size:2.3rem;
            font-weight:800;
            color:white;">
            Export Dataset
        </div>

        <div style="
            color:#94a3b8;
            margin-top:10px;">
            Prepare your synthetic image dataset for
            downstream machine learning workflows.
        </div>

    </div>
    """)

    st.html("""
    <div class="section-title">
        Export Configuration
    </div>
    """)

    format_type = st.selectbox(
        "Dataset Format",
        [
            "ZIP — Image Files",
            "COCO",
            "YOLO",
            "ImageFolder"
        ]
    )

    st.info(
        f"Selected export format: {format_type}"
    )

    st.button(
        "↓  Prepare Dataset",
        type="primary"
    )