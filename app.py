import streamlit as st
from modules.scraper import get_instagram_data
from modules.scoring import calculate_engagement_rate, overall_score
from modules.ai_engine import generate_growth_plan
from modules.pdf_report import generate_pdf

st.set_page_config(page_title="AI Social Media Auditor", layout="wide")

st.title("AI Agency-Level Social Media Auditor")

username = st.text_input("Enter Instagram Username")

if st.button("Generate Audit"):

    with st.spinner("Analyzing profile..."):
        data = get_instagram_data(username)
        engagement_rate = calculate_engagement_rate(data["followers"], data["post_data"])
        score = overall_score(engagement_rate, data["posts"])
        report = generate_growth_plan(data, engagement_rate)

        st.subheader("Audit Results")
        st.write(f"Followers: {data['followers']}")
        st.write(f"Engagement Rate: {engagement_rate}%")
        st.write(f"Overall Score: {score}/100")

        st.text_area("Growth Plan", report, height=400)

        pdf_file = generate_pdf(report)
        with open(pdf_file, "rb") as f:
            st.download_button("Download PDF Report", f, file_name="audit_report.pdf")
