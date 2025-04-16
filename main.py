import streamlit as st
from PIL import Image
import webbrowser

# Configurando a pagina
st.set_page_config(
    page_title="Portfolio - Kitharo Nunes Almeida",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded",
)

SOCIAL_LINKS = {
    "LinkedIn": {"url": "https://www.linkedin.com/in/kitharo-nunes/", "icon": "fab fa-linkedin"},
    "Github": {"url": "https://github.com/KitharoNA", "icon": "fab fa-github"},
}

SKILLS = {
    "Front-end": ["HTML", "CSS", "JavaScript", "Node.js", "Tailwind CSS"],
    "Back-end": ["Python", "Pandas", "SQL", "MongoDB"]
}

PROJECTS = [
    {
        "title": "Modelo Preditivo de Dados (Python, SQL, Pandas, Numpy)",  
        "description": "Manipulação e análise de grandes volumes de dados, utilizando ferramentas de ciência de dados e IA para gerar insights práticos."
    },
    {
        "title": "Plataforma de Comunicação (Node.js, MongoDB, HTML/CSS/JavaScript)", 
        "description": "Uma plataforma de comunicação que permite agendamento de envio de comunicação, consulta de status de envio de comunicação e cancelamento de envio de comunicação."
    },
    {
        "title": "Página de login ( NodeJs, Angular CLI, TypeScript)",
        "description": "Um simples aplicativo desenvolvido de login e cadastro."
    },
]

EDUCATION = [
    {
    "course": "Graduação - Análise e Desenvolvimento de Sistemas (Anhanguera)",
    "time": "Março de 2022 - Dezembro de 2023"
    },
    {
    "course": "Pós Graduação - Inteligência Artificial (Uniceub)",
    "time": "Janeiro de 2024 - Agosto de 2024"
    }
]

CERTIFICATIONS = [
    "MTA: Introduction to Programming Using Python - <b>Universidade Presbiteriana Mackenzie",
    "Technical Support Fundamentals - Google",
    "Google Cloud Computing Foundations - Google",
    "Introduction to Software Engineering - IBM",
    "Collaborate Effectively for Professional Success - IBM",
    "Pacote Office - Universitat Autònoma de Barcelona"
]

EXPERIENCE = [
    {
        "title": "Estágio em TI (Suporte Técnico)",
        "company": "NN Assessoria - Outubro de 2022 - Dezembro de 2023",
        "description": "Auxiliava na instalação, configuração e manutenção de computadores, identificando e solucionando problemas; realizava verificação e análise de dados utilizando o Excel, garantindo a integridade das informações; ajustava e oferecia suporte a sistemas organizacionais, auxiliando na otimização e no funcionamento eficiente dos processos; auxiliava no suporte a usuários"
    }
]

def load_css():
    """Carrega todos os estilos CSS"""
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary-color: #38bdf8;  /* Azul para destacar links */
                --secondary-color: #1e293b;  /* Cinza escuro */
                --text-light: #f8fafc;  /* Branco quase puro */
                --shadow: 0 4px 6px -1px rgba(255, 255, 255, 0.1);
            }

            .project-card, .experience-item {
                background: #12151c;  /* Cor mais clara para destaque */
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            .project-card:hover, .experience-item:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(255, 255, 255, 0.1);
            }
        </style>          
    """, unsafe_allow_html=True)

def social_links():
    links_html = "".join(
        f'<a href="{info["url"]}" target="_blank" style="margin: 0 10px; font-size: 1.5rem; color: var(--primary-color);">'
        f'<i class="{info["icon"]}"></i></a>'
        for name, info in SOCIAL_LINKS.items()
    )
    st.markdown(f'<div style="text-align: center; margin: 2rem 0;">{links_html}</div>', unsafe_allow_html=True)

def show_projects():
    st.markdown("## 📦 Projetos recentes")
    cols = st.columns(3)
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="project-card">
                    <h3>{project['title']}</a></h3>
                    <p>{project['description']}</p>
                </div>
            """, unsafe_allow_html=True)


def show_experience():
    st.markdown("## 💼 Experiência Profissional")
    cols = st.columns(3)
    for exp in EXPERIENCE:
            st.markdown(f"""
                <div class="experience-item">
                    <h3>{exp['title']}</h3>
                    <p><strong>{exp['company']}</strong></p>
                    <p>{exp['description']}</p>
                </div>
            """, unsafe_allow_html=True)


def main():
    load_css()

    #Sidebar
    with st.sidebar:
        st.markdown("""
                    <div style ="text-align: center;">
                    <img src="https://scontent.fbsb8-2.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=dst-png_s200x200&_nc_cat=110&ccb=1-7&_nc_sid=136b72&_nc_ohc=a1K6_KaoqeEQ7kNvgEW9coO&_nc_oc=AdniezzpFe480_z6-TiUQX7Dx3IxR21w-td0mF6iUHAukV-knC44f2GyMsVc4clQfAm-sNRco4sTRCOwBpAiGWLI&_nc_zt=24&_nc_ht=scontent.fbsb8-2.fna&oh=00_AYEdnHEG8XQXEqMqNC_r7vSxAOLu3-y2xMUWzjfO781CDw&oe=6813DF7A" style="border-radius: 50%; width: 160px; height: 160px; object-fit: cover; margin-bottom: 1rem;">
                        <h2>Kitharo Nunes Almeida</h2>
                        <p>Programador Python e Cientista de Dados</p>
                    </div>
                    
        """, unsafe_allow_html=True)
        # Contato
        with st.expander("✉️ Contato", expanded=True):
            st.markdown("""
                    <p><i class="fas fa-map-marker-alt"></i> Brasília, Brasil</p> 
                    <p><i class="fas fa-envelope"></i> kitharonn@gmail.com</p>
                    <p><i class="fas fa-mobile"></i> 61 99265-5124</p>

            """, unsafe_allow_html=True)

        social_links()

    #Conteudo principal
    st.title("Kitharo Nunes Almeida")
    st.markdown("### Desenvolvedor Full-stack | HTML | CSS | JavaScript | SQL | Java | Python")

    #Sobre mim
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
                ## 💻 Sobre mim
                Desenvolvedor de software com formação em Análise e Desenvolvimento de Sistemas e pós-graduação em Inteligência Artificial. Possuo experiência em programação com Python, SQL, Java, Front-end, além de conhecimentos em Segurança da Informação. Busco oportunidades para ingressar na carreira de T.I para aplicar o meu conhecimento de Hard skills e Soft Skills. Tenho um Inglês (B1) e espanhol (B1) que me permite comunicar em diferentes contextos.
            """, unsafe_allow_html=True)
        with col2:
            st.image("https://cdni.iconscout.com/illustration/premium/thumb/cientista-de-dados-10929747-8779582.png", width=250)

        # Habilidades tecnicas
        st.markdown("## 🛠️ Habilidades Técnicas")
        cols = st.columns(2)
        for idx, (title, items) in enumerate(SKILLS.items()):
            with cols[idx]:
                items_html = "".join(f"<li>{item}</li>" for item in items)
                st.markdown(f"""
                    <div style="background: #12151c; border-radius: 10px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: var(--shadow); transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.1);">
                        <h3>{title}</h3>
                        <ul>{items_html}</ul>
                    </div>
                """, unsafe_allow_html=True)

        # Projetos em 3 colunas
        show_projects()

        # Educação
        st.markdown("## 📚 Educação")
        for edu in EDUCATION:
            st.markdown(f"""
                <div style="background: #12151c; border-radius: 10px; padding: 1rem; margin-bottom: 0.6rem; box-shadow: var(--shadow); transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.1); border-left: 4px solid var(--text-light); color: var(--text-light)">
                    <h3 style="margin: 0">{edu["course"]}</h3>
                    <p style="color: #bbb;"><strong>{edu["time"]}</strong></p>
                </div>
            """, unsafe_allow_html=True)

        # Certificacoes
        st.markdown("## 📜 Certificações")
        for cert in CERTIFICATIONS:
            st.markdown(f"""
                <div style="background: #12151c; border-radius: 10px; padding: 1rem; margin-bottom: 0.6rem; box-shadow: var(--shadow); transition: all 0.3s ease; border: 1px solid rgba(255, 255, 255, 0.1); border-left: 4px solid var(--text-light)">
                   📌 {cert}
                </div>
            """, unsafe_allow_html=True)

        # Experiencia profissional
        show_experience()

        # Rodape
        st.markdown(f"""
                <div style="text-align: center; padding:2 rem; color: #64748b; margin-top: 4rem">
                   © 2025 Kitharo Nunes Almeida • Desenvolvido com ❤️ usando Streamlit
                </div>
        """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()