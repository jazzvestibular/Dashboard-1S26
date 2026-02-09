import streamlit as st

st.set_page_config(page_title="Jazz Vestibular", page_icon="./logo_jazz_menor.png", layout="wide")

import streamlit.components.v1 as components
from alunos import mostrar_alunos
from professores import mostrar_professores
from logs import escrever_planilha
import datetime
import pytz

def dia_hora():

    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    data_e_hora_brasilia = datetime.datetime.now(fuso_horario_brasilia)
    data_hoje_brasilia = str(data_e_hora_brasilia.date())
    hora_atual_brasilia = str(data_e_hora_brasilia.strftime('%H:%M:%S'))
    return data_hoje_brasilia, hora_atual_brasilia

def define_estado():
    return {
        'pagina_atual': 'Página Inicial'
    }

def get_estado():
    if 'estado' not in st.session_state:
        st.session_state.estado = define_estado()
    return st.session_state.estado

def mostrar_botoes(permissao, nome, email, turma):

    estado = get_estado()

    html_br="""
        <br>
        """

    with st.container():
            col1, col2, col3 = st.columns([3,4,3])
            with col1:
                st.markdown(html_br, unsafe_allow_html=True)
            with col2:
                st.image("./logo_jazz.png")
            with col3:
                st.markdown(html_br, unsafe_allow_html=True)

    def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
        htmlstr = f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText == '{widget_label}') {{ 
                        elements[i].style.color ='{font_color}';
                        elements[i].style.background = '{background_color}';
                        elements[i].style.width = '120px';  // Adiciona a largura desejada
                        elements[i].style.height = '50px';  // Adiciona a altura desejada
                    }}
                }}
            </script>
            """
        components.html(f"{htmlstr}", height=0, width=0)

    if permissao == "Administrador":

        with st.container():
                col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1,1,1,1,1,1,1,1,1])
                with col1:
                    botao_clicado1 = col1.button('Alunos', key='b1')
                    ChangeButtonColour('Alunos', 'white', '#9E089E')

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado1]

        if all(not botao for botao in botoes_menu) and estado['pagina_atual'][:6] == 'Alunos':
            estado = get_estado()
            mostrar_alunos(nome, permissao, email, turma)

        elif botao_clicado1 or estado['pagina_atual'][:6] == 'Alunos':
            estado = get_estado()
            mostrar_alunos(nome, permissao, email, turma)

    elif permissao == "Time":

        with st.container():
                col1, col2, col3, col4, col5, col6, col8, col9 = st.columns([1,1,1,1,1,1,1,1])
                with col1:
                    botao_clicado1 = col1.button('Alunos', key='b1')
                    ChangeButtonColour('Alunos', 'white', '#9E089E')

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado1]

        if all(not botao for botao in botoes_menu):
            estado = get_estado()
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao, email, turma)

        if botao_clicado1:
            estado = get_estado()
            estado['pagina_atual'] = 'Alunos'
            mostrar_alunos(nome, permissao, email, turma)

        if botao_clicado2:
            estado = get_estado()
            estado['pagina_atual'] = 'Professores'
            mostrar_professores(nome, permissao, email, turma)
        
        if botao_clicado9:
            estado = get_estado()
            estado['pagina_atual'] = 'Mentoria'

    elif (permissao == 'Aluno' or permissao == 'Mentor' or permissao == 'Responsável' or permissao == 'Inscrito Simulado Nacional'):

        container = st.container()
        with container:
            cols = st.columns([1])  
            col1 = cols[0]  
            botao_clicado1 = col1.button('Alunos', key='b1')
            ChangeButtonColour('Alunos', 'white', '#9E089E')

        st.markdown(
            """
            <hr style="border: 1px solid #9E089E; margin-top: -30px;">
            """,
            unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado1]

        if all(not botao for botao in botoes_menu):
            estado = get_estado()
            mostrar_alunos(nome, permissao, email, turma)

        if botao_clicado1:
            estado = get_estado()

            mostrar_alunos(nome, permissao, email, turma)


from tela_login import mostrar_tela_login

if __name__ == "__main__":
    
    login, permissao, nome, email, turma = mostrar_tela_login()
    if login:
        mostrar_botoes(permissao, nome, email, turma)
        if get_estado()['pagina_atual'] == 'Página Inicial':
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")


    

    


