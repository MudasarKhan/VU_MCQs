import streamlit as st
import streamlit as st
from PIL import Image
file_path = r"Logo.PNG"
try:
    logo = Image.open(file_path)
    st.sidebar.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error(f"File '{file_path}' Path Dont Find.")

videos = {
    "Python": [
        {"link": "https://www.youtube.com/embed/-HRmvXsmF7E", "caption": "Python Introduction",
         "feedback": "Great for beginners."},
        {"link": "https://www.youtube.com/embed/pLGbRH2eT_s", "caption": "Python Advance",
         "feedback": "Informative and detailed."},
        {"link": "https://www.youtube.com/embed/UoaQKARwtSo", "caption": "Python Operators",
         "feedback": "Covers advanced topics."},
        {"link": "https://www.youtube.com/embed/G9SMgE2RHBo", "caption": "Python Library",
         "feedback": "Covers advanced topics."},
        {"link": "https://www.youtube.com/embed/k5wLGNzd7PQ-", "caption": "Python Database",
         "feedback": "Covers advanced topics."},
        {"link": "https://www.youtube.com/embed/G9SMgE2RHBo", "caption": "Python Video 3",
         "feedback": "Covers advanced topics."},
    ],
    "Java Object Oriented Programming": [
        {"link": "https://www.youtube.com/embed/tiwbbImZLYM", "caption": "Java Introduction",
         "feedback": "Comprehensive overview."},
        {"link": "https://www.youtube.com/embed/iv5mzOEH7-8", "caption": "Order of Operations",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/PVXztEwMSbI", "caption": "Operators",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/J1Ft2cPK2Ws", "caption": "Object Oriented Programming UsingJava",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/WWiK8XLRU0w", "caption": "Data Types, Variable & Operators",
         "feedback": "Hands-on tutorial."},
        # Add more videos here...
    ],
    "Machine Learning": [
        {"link": "https://www.youtube.com/embed/tiwbbImZLYM", "caption": "Machine Learning Introduction",
         "feedback": "Comprehensive overview."},
        {"link": "https://www.youtube.com/embed/iv5mzOEH7-8", "caption": "Order of Operations",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/PVXztEwMSbI", "caption": "Operators",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/J1Ft2cPK2Ws", "caption": "Object Oriented Programming UsingJava",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/WWiK8XLRU0w", "caption": "Data Types, Variable & Operators",
         "feedback": "Hands-on tutorial."},
        # Add more videos here...
    ],
"Artificial Intelligence": [
        {"link": "https://www.youtube.com/embed/tiwbbImZLYM", "caption": "Artificial Intelligance Introduction",
         "feedback": "Comprehensive overview."},
        {"link": "https://www.youtube.com/embed/iv5mzOEH7-8", "caption": "Order of Operations",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/PVXztEwMSbI", "caption": "Operators",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/J1Ft2cPK2Ws", "caption": "Object Oriented Programming UsingJava",
         "feedback": "Hands-on tutorial."},
        {"link": "https://www.youtube.com/embed/WWiK8XLRU0w", "caption": "Data Types, Variable & Operators",
         "feedback": "Hands-on tutorial."},
        # Add more videos here...
    ],

    # Add more subjects and videos here...
}
# Videos information


def main():
    st.title("Video Recommendation System")

    # Selectbox for subjects
    subject = st.selectbox("Select a Subject",
                           ["Python", "Java Object Oriented Programming", "Machine Learning", "Artificial Intelligence"])

    st.write(f"Videos for {subject}:")
    subject_videos = videos.get(subject, [])

    # Display videos in a grid
    for i in range(0, len(subject_videos), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(subject_videos):
                video = subject_videos[i + j]
                with cols[j]:
                    st.markdown(f"<div style='border:1px solid #ccc; padding:10px; margin:5px; height:370px;'>"
                                f"<iframe width='100%' height='200' src='{video['link']}' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"
                                f"<h4>{video['caption']}</h4>"
                                f"<p>{video['feedback']}</p>"
                                f"</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
