from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"

# --- GENERAL SETTINGS ---

PAGE_TITLE = "Digital CV | Nikola Miljkovic"
PAGE_ICON = ":wave:"
NAME = "Nikola Miljkovic"
DESCRIPTION = """
Software Engineer
"""

EMAIL = "sdnikola72@gmail.com"

SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/nikola-miljkovi%C4%87-9361481a5/",
    "GitHub": "https://github.com/nikolaaa98?tab=repositories",
}

PROJECTS = {
    "🏆 WPF application for status monitoring",
    "🏆 Guessing game of two components server and an indefinite number of players using C/C++",
    "🏆 Web Application using ASP.NET MVC",
    "🏆 Web Application using Flask in python 3 with database",
    "🏆 Space invaders game using Python PyQT5",
    "🏆 Create DST Tool application for reading diagnostics files, compare and generate requirements in excel using PyQT5",
    "🏆 Create panel in Vector CANoe for calculate CRC and Clock and export results using CAPL Code"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- ABOUT ME ---

st.write('\n')
st.subheader("About me")
st.write("---")
st.write("""
    My objective is to develop my technical skills in the field of computer science, from web development where I worked with AngularJS, Flask, Django, Laravel to application development where I worked with .NET WPF, PyQt5, and many more.

Also, I have experience with databases (SQL), cloud computing, and networking protocols (TCP, UDP, IP)

I am currently working in the automotive industry where I'm trying to gain knowledge about AUTOSAR architecture, requirements coverage, test automation, programming in Embedded C language, developing GUI applications for customers, CAN/LIN protocols, hardware, and many more.

Interested in the fields of Artificial Intelligence, Machine Learning, Docker and Big Data, which I am currently studying in my master's program.

Always trying to learn new things to improve my skills and knowledge. 
Open-minded and very communicative person.
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ 2.5+ years expereince in automotive industry
- ✔️ University degree in software engineering
- ✔️ Very good knowledge in overall systems engineering
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Experience with test devices such as Vector for CAN/LIN testing
- ✔️ Knowledge in Embedded Software development, ASPICE, UDS, OBD and ISO26262
- ✔️ Experience in developing and supporting automated testing frameworks
- ✔️ Experience in handling tools such as IBM Rhapsody, Enterprise Architect, MATLAB Simulink, DOORS
- ✔️ Proven experience in designing, implementing, and validating tests 
- ✔️ Proficient in debugging embedded system issues (hardware and software)
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: C (SWATT), C++, Python (PyQt5, Flask, Django, PyTest, Jenkins, Robot Framework), .NET (MVC, WPF, ASP. NET) SQL, Angular,
JavaScript, Microcontrollers (Arduino), Agile, Networking (UDP/TCP), SCADA (Modbus protocol), VHDL
- 📊 Data Visulization: PowerBi, MS Excel, UML, IBM Rhapsody,  IBM DOORS, DOORS DXL, Enterprise Architect, Jira, Git
- 📚 Testing: Vector CANoe, CAPL Code, AUTOSAR, CAN/LIN bus, CANoe DiVa, CANdelaStudio, UDS protocol, Test Automation Framework (TAF), Selenium, V-Model, Electrical measurements, Soldering 
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

#--- JOB 1
st.write("🚧", "**System Test Engineer | Continental Automotive**")
st.write("10/2021 - Present")
st.write("Novi Sad, Serbia")
st.write(
    """
► Responsible for designing and automating System level
tests in order to ensure that the software delivered by the
development team meet all specific customer
requirements
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**.NET/Web Software Engineer | DEVPRO Solutions**")
st.write("09/2020 - 10/2020")
st.write("Belgrade, Serbia")
st.write(
    """
► Student Internship, integration testing of the application
and identifying, troubleshooting, and solving application
code-related issues
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
st.write("""
    🏆 WPF application for status monitoring - https://github.com/nikolaaa98/WPFApplication\n
    🏆 Guessing game of two components server and an indefinite number of players using C/C++ - https://github.com/nikolaaa98/IKP\n
    🏆 Web Application using ASP.NET MVC - https://gitlab.com/pr54-2017-webprojekat/pr54-2017nikolamiljkovicvebprogramiranje\n
    🏆 Web Application using Flask in python 3 with database - https://github.com/nikolaaa98/PUSGS_ProjekatNikolaMiljkovic\n
    🏆 Space invaders game using Python PyQT5 - https://github.com/nikolaaa98/space_invaders    
    """
)

st.write('\n')
st.subheader("Licenses & Certifications")
st.write("---")
st.write("""
    🏆 Certified Tester Foundation Level (CTFL) ISTQB® - International Software Testing Qualifications Board\n
    - Issued Jun 2023     
         """
)

st.write('\n')
st.subheader("Contact")
st.write("---")
st.write("""
Date of birth : 29.05.1998\n
Mobile phone : +381 649747 247\n
Location : Novi Sad, Serbia 
    """
)