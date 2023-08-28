import streamlit as st

def main():
    
    st.image("lifecycle.gif", use_column_width=True)

    topics = [
        "RoadMap",
        "Understanding DevOps",
        "Version Control (e.g., Git)",
        "Scripting and Automation (e.g., Python, Bash)",
        "Linux Fundamentals (Command Line)",
        "Networking and Security",
        "Cloud Platforms (e.g., AWS, Azure, Google Cloud)",
        "Configuration Management (e.g., Ansible, Puppet, Chef)",
        "Containerization (Docker)",
        "Container Orchestration (Kubernetes)",
        "CI/CD",
        "Infrastructure as Code (IaC) (e.g., Terraform)",
        "Monitoring and Logging",
        "Learn Software Engineering Practices",
        "Security Best Practices (DevSecOps)",
        "DevOps Guide",
        "Additional resources"
    ]

    selected_topic = st.sidebar.radio("Select a topic", topics)

    if selected_topic:
        md_content = read_md_content("devops.md")
        selected_content = extract_content(md_content, selected_topic)
        
        if selected_topic == "RoadMap":
            st.image("roadmap.png", use_column_width=True)
        else:
            st.markdown(selected_content, unsafe_allow_html=True)

def read_md_content(filename):
    with open(filename, "r") as md_file:
        md_content = md_file.read()
    return md_content

def extract_content(md_content, selected_topic):
    lines = md_content.split('\n')
    content = []
    capturing = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line == f"# {selected_topic}":
            capturing = True
        elif stripped_line.startswith("# "):
            capturing = False

        if capturing:
            content.append(line)

    return '\n'.join(content)

if __name__ == "__main__":
    main()
