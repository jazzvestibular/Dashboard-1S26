import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from presenca_aulas import mostrar_presenca_aulas
from gamificacao import mostrar_gamificacao
from resultados_simulados import mostrar_resultados_simulados
import datetime
import pytz
from logs import escrever_planilha

def dia_hora():

    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    data_e_hora_brasilia = datetime.datetime.now(fuso_horario_brasilia)
    data_hoje_brasilia = str(data_e_hora_brasilia.date())
    hora_atual_brasilia = str(data_e_hora_brasilia.strftime('%H:%M:%S'))
    return data_hoje_brasilia, hora_atual_brasilia

def define_estado():
    return {
        'pagina_atual': 'Alunos'
    }

def get_estado():
    if 'estado' not in st.session_state:
        st.session_state.estado = define_estado()
    return st.session_state.estado

def mostrar_alunos(nome, permissao, email, turma):
    estado = get_estado()

    def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
        htmlstr = f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText == '{widget_label}') {{ 
                        elements[i].style.color ='{font_color}';
                        elements[i].style.background = '{background_color}';
                        elements[i].style.width = '600px';  // Adiciona a largura desejada
                        elements[i].style.height = '50px';  // Adiciona a altura desejada
                    }}
                }}
            </script>
            """
        components.html(f"{htmlstr}", height=0, width=0)

    if permissao == 'Administrador':

        with st.container():
                col1, col2= st.columns([1,1])
                with col1:
                    botao_clicado12 = col1.button('Gamificação', key='b12')
                    ChangeButtonColour('Gamificação', 'white', '#ff80e6')
                with col2:
                    botao_clicado13 = col2.button('Resultado nos simulados', key='b13')
                    ChangeButtonColour('Resultado nos simulados', 'white', '#ff80e6')


        st.markdown(
        """
        <hr style="border: 1px solid #ff80e6; margin-top: -30px;">
        """,
        unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado12, botao_clicado13]

        if all(not botao for botao in botoes_menu) and estado['pagina_atual'] != 'Alunos - Resultados nos simulados' and estado['pagina_atual'] != 'Alunos - Presença nas aulas':
            estado['pagina_atual'] = 'Alunos - Gamificação'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_gamificacao(nome, permissao, email, turma)

        elif botao_clicado12:
            estado['pagina_atual'] = 'Alunos - Gamificação'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_gamificacao(nome, permissao, email, turma)

        if botao_clicado13 or estado['pagina_atual'] == 'Alunos - Resultados nos simulados':
            estado['pagina_atual'] = 'Alunos - Resultados nos simulados'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_resultados_simulados(nome, permissao, email, turma)

    elif (permissao == 'Aluno' or permissao == 'Mentor' or permissao == 'Responsável'):

        with st.container():
                col1, col2 = st.columns([1,1])
                with col1:
                    botao_clicado12 = col1.button('Gamificação', key='b12')
                    ChangeButtonColour('Gamificação', 'white', '#ff80e6')
                with col2:
                    botao_clicado13 = col2.button('Resultado nos simulados', key='b13')
                    ChangeButtonColour('Resultado nos simulados', 'white', '#ff80e6')

        #with st.container():
        #        col2, col3, col4, col5 = st.columns([1,1,1,1])
        #        with col2:
        #            botao_clicado13 = col2.button('Resultado nos simulados', key='b13')
        #            ChangeButtonColour('Resultado nos simulados', 'white', '#ff80e6')

        st.markdown(
        """
        <hr style="border: 1px solid #ff80e6; margin-top: -30px;">
        """,
        unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado12, botao_clicado13]
        #botoes_menu = [botao_clicado13]

        #estado['pagina_atual'] = 'Alunos - Resultados nos simulados'
        #data_hoje_brasilia, hora_atual_brasilia = dia_hora()
        #data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
        #escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
        #mostrar_resultados_simulados(nome, permissao, email, turma)

        if all(not botao for botao in botoes_menu) and estado['pagina_atual'] != 'Alunos - Resultados nos simulados' and estado['pagina_atual'] != 'Alunos - Presença nas aulas':
            
            estado['pagina_atual'] = 'Alunos - Gamificação'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_gamificacao(nome, permissao, email, turma)

        elif botao_clicado12:
            estado['pagina_atual'] = 'Alunos - Gamificação'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_gamificacao(nome, permissao, email, turma)

        elif botao_clicado13 or estado['pagina_atual'] == 'Alunos - Resultados nos simulados':
            estado['pagina_atual'] = 'Alunos - Resultados nos simulados'
            data_hoje_brasilia, hora_atual_brasilia = dia_hora()
            data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
            escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
            mostrar_resultados_simulados(nome, permissao, email, turma)

    elif permissao == 'Inscrito Simulado Nacional':

        with st.container():
                col1, col2 = st.columns([1,1])
                with col1:
                    botao_clicado14 = col1.button('Resultado Simulado Nacional', key='b14')
                    ChangeButtonColour('Resultado Simulado Nacional', 'white', '#ff80e6')

        st.markdown(
        """
        <hr style="border: 1px solid #ff80e6; margin-top: -30px;">
        """,
        unsafe_allow_html=True
        )

        botoes_menu = [botao_clicado14]
            
        estado['pagina_atual'] = 'Alunos - Resultados nos simulados'
        data_hoje_brasilia, hora_atual_brasilia = dia_hora()
        data_to_write = [[nome, permissao, data_hoje_brasilia, hora_atual_brasilia, get_estado()['pagina_atual'], "", "", email]]
        escrever_planilha("17KVukpAvTZmYEh2fbbeqIrJjDSww1KJe8JWKUmHOv9k", data_to_write, "Logs | 26")
        mostrar_resultados_simulados(nome, permissao, email, turma)


    

    



    