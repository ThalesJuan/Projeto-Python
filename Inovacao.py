import flet as ft
import mysql.connector
import datetime as dt

def main(pagina):
    texto = ft.Text("Qual você escolhe ?", size=20)
    pagina.vertical_alignment = "center"
    pagina.horizontal_alignment = "center"

    def Entrada(evento):
        pagina.remove(texto)
        pagina.remove(btn_entrada)
        pagina.remove(btn_saida)
        pagina.remove(btn_pesquisar)
        pagina.update()

        data_atual = dt.datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y")
        
        dt_entrada = ft.TextField(data_formatada)
        marca = ft.TextField(label="Marca")
        modelo = ft.TextField(label="Modelo")
        ano = ft.TextField(label="Ano")
        renavam = ft.TextField(label="Renavam")
        placa = ft.TextField(label="Placa")
        cor = ft.TextField(label="Cor")
        comprado = ft.TextField(label="Comprado do Sr.", width=925)
        rua = ft.TextField(label="Rua", width=600)
        N = ft.TextField(label="Número")
        bairro = ft.TextField(label="Bairro", width=600)
        cidade = ft.TextField(label="Cidade")
        tel = ft.TextField(label="Tel", width=300)
        obsc = ft.TextField(label="OBS", width=600)

        col0 = [dt_entrada]
        col1 = [marca, modelo, ano]
        col2 = [renavam, placa, cor]
        col3 = [comprado]
        col4 = [rua, N]
        col5 = [bairro, cidade]
        col6 = [tel, obsc]

        row0 = ft.Row(spacing=20, controls=col0, alignment="center")
        row1 = ft.Row(spacing=20, controls=col1, alignment="center")
        row2 = ft.Row(spacing=20, controls=col2, alignment="center")
        row3 = ft.Row(spacing=20, controls=col3, alignment="center")
        row4 = ft.Row(spacing=20, controls=col4, alignment="center")
        row5 = ft.Row(spacing=20, controls=col5, alignment="center")
        row6 = ft.Row(spacing=20, controls=col6, alignment="center")
        row0 = ft.Row(spacing=20, controls=col0, alignment="center")

        pagina.add(row0)
        pagina.add(row1)
        pagina.add(row2)
        pagina.add(row3)
        pagina.add(row4)
        pagina.add(row5)
        pagina.add(row6)

        pagina.update()

        # Criando a mensagem de retorno
        resp_widget = ft.Text("Adicionado com sucesso !", size=20)

        # Defina uma variável para controlar se o formulário foi preenchido ou não
        form_preenchido = False

        def inserir(evento):

            campos_vazios = []

            if dt_entrada.value == "":
                campos_vazios.append("Data de Entrada")
            if marca.value == "":
                campos_vazios.append("Marca")
            if modelo.value == "":
                campos_vazios.append("Modelo")
            if ano.value == "":
                campos_vazios.append("Ano")
            if renavam.value == "":
                campos_vazios.append("Renavam")
            if placa.value == "":
                campos_vazios.append("Placa")
            if cor.value == "":
                campos_vazios.append("Cor")
            if comprado.value == "":
                campos_vazios.append("Comprado")
            if rua.value == "":
                campos_vazios.append("Rua")
            if N.value == "":
                campos_vazios.append("Número")
            if bairro.value == "":
                campos_vazios.append("Bairro")
            if cidade.value == "":
                campos_vazios.append("Cidade")
            if tel.value == "":
                campos_vazios.append("Telefone")

            mensagemFaltou = None

            if campos_vazios:
                mensagemFaltou = ft.Text("Faltou preencher os seguintes campos: {}".format(", ".join(campos_vazios)), text_align="center", size=20)
                pagina.add(mensagemFaltou)

            else:

                mensagemErro = ft.Text("Deu erro", size=20)

                try:
                    # Conectando ao banco de dados
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="inovacao"
                    )
                    cursor = conn.cursor()

                    if obsc.value != "":
                        cursor.execute("insert into entrada(DATA_ENTRADA,COMPRADO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM,PLACA,MARCA,MODELO,ANO,COR,OBSC) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_entrada.value, comprado.value, rua.value, N.value, bairro.value, cidade.value, tel.value, renavam.value, placa.value, marca.value, modelo.value, ano.value, cor.value, obsc.value))
                    else:
                        cursor.execute("insert into entrada(DATA_ENTRADA,COMPRADO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM,PLACA,MARCA,MODELO,ANO,COR) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_entrada.value, comprado.value, rua.value, N.value, bairro.value, cidade.value, tel.value, renavam.value, placa.value, marca.value, modelo.value, ano.value, cor.value))

                    conn.commit()
                    conn.close()

                    marca.value = ""
                    modelo.value = ""
                    ano.value = ""
                    renavam.value = ""
                    placa.value = ""
                    cor.value = ""
                    comprado.value = ""
                    rua.value = ""
                    N.value = ""
                    bairro.value = ""
                    cidade.value = ""
                    tel.value = ""
                    obsc.value = ""
                    mensagemFaltou = ""
                    mensagemErro = ""

                    pagina.add(resp_widget)

                except mysql.connector.Error as e:
                    pagina.add(mensagemErro)

        def limpar(evento):
            if tel.value == "" or obsc.value == "" or cidade.value == "" or bairro.value == "" or rua.value == "" or N.value == "" or comprado.value == "" or cor.value == "" or placa.value == "" or marca.value == "" or modelo.value == "" or ano.value == "" or renavam.value == "" or resp_widget == "" or mensagemFaltou == "":
                marca.value = ""
                modelo.value = ""
                ano.value = ""
                renavam.value = ""
                placa.value = ""
                cor.value = ""
                comprado.value = ""
                rua.value = ""
                N.value = ""
                bairro.value = ""
                cidade.value = ""
                tel.value = ""
                obsc.value = ""
                resp_widget.value = ""
                mensagemFaltou = ""

                pagina.update()

        def voltar(evento):
            # Limpar a página completamente
            pagina.clean()

            # Adicionar widgets padrão de volta à página
            pagina.add(texto)
            pagina.add(btn_pesquisar)
            pagina.add(btn_entrada)
            pagina.add(btn_saida)

            pagina.update()

        btn_salvar = ft.ElevatedButton("Salvar", on_click=inserir, width=100, scale=1.3)
        espaco1 = ft.Text("")
        btn_limpar = ft.ElevatedButton("Limpar", on_click=limpar, width=100, scale=1.3)
        espaco2 = ft.Text("")
        btn_voltar = ft.ElevatedButton("Voltar", on_click=voltar, width=100, scale=1.3)

        linha_vazia = ft.Text("\n", size=5)
        pagina.add(linha_vazia)

        col_btn = [btn_salvar, espaco1, btn_limpar, espaco2, btn_voltar]

        row_btn = ft.Row(spacing=20, controls=col_btn, alignment="center")

        pagina.add(row_btn)


    def Saida(evento):
        pagina.clean()

        # Criando a mensagem de retorno
        resp_widget = ft.Text("Salvo com sucesso !", size=20)

        def placa(evento):
            try:
                pagina.clean()

                placa = ft.TextField(label="Digite a placa")

                pagina.add(placa)

                # Defina uma variável para controlar se o formulário foi preenchido ou não
                form_preenchido = False

                mensagemNEncontrado = ft.Text("Não encontrado", size=20)

                def ok(evento):

                    try:
                        # Conectando ao banco de dados
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="root",
                            database="inovacao"
                        )
                        cursor = conn.cursor()

                        # Verificar se o valor existe no banco de dados
                        cursor.execute("SELECT * FROM entrada WHERE placa = %s", (placa.value,))
                        resultado = cursor.fetchone()

                        if resultado:
                            pagina.clean()

                            data_entrada = ft.Text(f"Data de Entrada: {resultado[0]}", size=20)
                            comprado = ft.Text(f"Comprado: {resultado[1]}", size=20)
                            rua = ft.Text(f"Rua: {resultado[2]}", size=20)
                            numero = ft.Text(f"Número: {resultado[3]}", size=20)
                            bairro = ft.Text(f"Bairro: {resultado[4]}", size=20)
                            cidade = ft.Text(f"Cidade: {resultado[5]}", size=20)
                            telefone = ft.Text(f"Telefone: {resultado[6]}", size=20)
                            renavam = ft.Text(f"Renavam: {resultado[7]}", size=20)
                            #placa = ft.Text(f"Placa: {resultado[8]}", size=20)
                            marca = ft.Text(f"Marca: {resultado[9]}", size=20)
                            modelo = ft.Text(f"Modelo: {resultado[10]}", size=20)
                            ano = ft.Text(f"Ano: {resultado[11]}", size=20)
                            cor = ft.Text(f"Cor: {resultado[12]}", size=20)
                            obsc = ft.Text(f"OBS: {resultado[13]}", size=20)

                            col10 = [data_entrada, comprado, telefone]
                            col11 = [rua, numero, bairro, cidade]
                            col12 = [renavam, marca, modelo, ano, cor]

                            row10 = ft.Row(spacing=20, controls=col10, alignment="center")
                            row11 = ft.Row(spacing=20, controls=col11, alignment="center")
                            row12 = ft.Row(spacing=20, controls=col12, alignment="center")

                            #pagina.add(placa)

                            pagina.add(row10)
                            pagina.add(row11)
                            pagina.add(row12)
                            pagina.add(obsc)

                            data_atual = dt.datetime.now()
                            data_formatada = data_atual.strftime("%d/%m/%Y")

                            dt_saida = ft.TextField(data_formatada)
                            vendido = ft.TextField(label="Vendido ao Sr.")
                            rua_saida_widget = ft.TextField(label="Rua")
                            numero_saida_widget = ft.TextField(label="Nº", width=100)
                            bairro_saida_widget = ft.TextField(label="Bairro")
                            cidade_saida_widget = ft.TextField(label="Cidade")
                            telefone_saida_widget = ft.TextField(label="Telefone")
                            obs_saida_widget = ft.TextField(label="OBS", width=600)

                            col20 = [dt_saida, vendido, telefone_saida_widget]
                            col21 = [rua_saida_widget, numero_saida_widget, bairro_saida_widget, cidade_saida_widget]
                            col22 = [obs_saida_widget]

                            row20 = ft.Row(spacing=20, controls=col20, alignment="center")
                            row21 = ft.Row(spacing=20, controls=col21, alignment="center")
                            row22 = ft.Row(spacing=20, controls=col22, alignment="center")

                            linha_vazia = ft.Text("\n", size=5)
                            pagina.add(linha_vazia)

                            pagina.add(row20)
                            pagina.add(row21)
                            pagina.add(row22)
                                    
                            pagina.update()

                            resp_widget = ft.Text("Adicionado com sucesso", size=20)

                            mensagemErro = ft.Text("Deu erro", size=20)
                                    
                            def salvar_renavam(evento):
                                campos_vazios = []

                                if dt_saida.value == "":
                                    campos_vazios.append("Data de Saída")
                                if vendido.value == "":
                                    campos_vazios.append("Vendido")
                                if rua_saida_widget.value == "":
                                    campos_vazios.append("Rua")
                                if numero_saida_widget.value == "":
                                    campos_vazios.append("Número")
                                if bairro_saida_widget.value == "":
                                    campos_vazios.append("Bairro")
                                if cidade_saida_widget.value == "":
                                    campos_vazios.append("Cidade")
                                if telefone_saida_widget.value == "":
                                    campos_vazios.append("Telefone")
                                
                                mensagemFaltou = None

                                if campos_vazios:
                                    mensagemFaltou = ft.Text("Faltou preencher os seguintes campos: {}".format(", ".join(campos_vazios)), text_align="center", size=20)
                                    pagina.add(mensagemFaltou)

                                else:

                                    try:
                                        # Conectando ao banco de dados
                                        conn = mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="root",
                                            database="inovacao"
                                        )
                                        cursor = conn.cursor()

                                        data_entrada = resultado[0]
                                        comprado = resultado[1]
                                        rua = resultado[2]
                                        numero = resultado[3]
                                        bairro = resultado[4]
                                        cidade = resultado[5]
                                        telefone = resultado[6]
                                        renavam = resultado[7]
                                        placa = resultado[8]
                                        marca = resultado[9]
                                        modelo = resultado[10]
                                        ano = resultado[11]
                                        cor = resultado[12]
                                        obsc = resultado[13]

                                        if obs_saida_widget.value != "":
                                            cursor.execute("insert into saida(DATA_SAIDA,VENDIDO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM_ENTRADA, PLACA_ENTRADA,MARCA_ENTRADA,MODELO_ENTRADA,ANO_ENTRADA,COR_ENTRADA,OBSV) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_saida.value, vendido.value, rua_saida_widget.value, numero_saida_widget.value, bairro_saida_widget.value, cidade_saida_widget.value, telefone_saida_widget.value, int(renavam), placa, marca, modelo, ano, cor, obs_saida_widget.value))

                                        else:
                                            cursor.execute("insert into saida(DATA_SAIDA,VENDIDO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM_ENTRADA, PLACA_ENTRADA,MARCA_ENTRADA,MODELO_ENTRADA,ANO_ENTRADA,COR_ENTRADA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_saida.value, vendido.value, rua_saida_widget.value, numero_saida_widget.value, bairro_saida_widget.value, cidade_saida_widget.value, telefone_saida_widget.value, int(renavam), placa, marca, modelo, ano, cor))

                                        conn.commit()
                                        conn.close()

                                        vendido.value = ""
                                        rua_saida_widget.value = ""
                                        numero_saida_widget.value = ""
                                        bairro_saida_widget.value = ""
                                        cidade_saida_widget.value = ""
                                        telefone_saida_widget.value = ""
                                        obs_saida_widget.value = ""

                                        pagina.add(resp_widget)

                                    except Exception as e:
                                        # Lidar com a exceção
                                        erro = ft.Text(f"Deu o erro: {e}")
                                        print(erro)

                            linha_vazia = ft.Text("\n", size=5)
                            pagina.add(linha_vazia)

                            btn_salvar = ft.ElevatedButton("Salvar", on_click=salvar_renavam, width=110, scale=1.3)
                            espaco = ft.Text("")
                            btn_voltar = ft.ElevatedButton("Voltar", on_click=voltar, width=110, scale=1.3)

                            col_btn = [btn_salvar, espaco, espaco2, btn_voltar]

                            row_btn = ft.Row(spacing=20, controls=col_btn, alignment="center")

                            pagina.add(row_btn)

                            # Fechando a conexão
                            conn.close()
                                    
                        else:
                            pagina.add(mensagemNEncontrado)
                            
                    except Exception as e:
                        # Lidar com a exceção
                        erro = ft.Text(f"Deu o erro: {e}")

                linha_vazia = ft.Text("\n", size=5)
                pagina.add(linha_vazia)

                btn_ok = ft.ElevatedButton("OK", on_click=ok, width=95, scale=1.3)
                btn_voltar1 = ft.ElevatedButton("Voltar", on_click=voltar, width=95, scale=1.3)

                col_btn3 = [btn_ok, espaco1, btn_voltar1]

                row_btn2 = ft.Row(spacing=20, controls=col_btn3, alignment="center")
                
                pagina.add(row_btn2)

            except Exception as e:
                # Lidar com a exceção
                erro = ft.Text(f"Deu o erro: {e}")

        def renavam(evento):
            try:
                pagina.clean()

                renavam = ft.TextField(label="Digite o renavam")

                pagina.add(renavam)

                # Defina uma variável para controlar se o formulário foi preenchido ou não
                form_preenchido = False

                mensagemNEncontrado = ft.Text("Não encontrado", size=20)

                def ok(evento):
                    try:
                        # Conectando ao banco de dados
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="root",
                            database="inovacao"
                        )
                        cursor = conn.cursor()

                        # Verificar se o valor existe no banco de dados
                        cursor.execute("SELECT * FROM entrada WHERE renavam = %s", (renavam.value,))
                        resultado = cursor.fetchone()

                        if resultado:
                            pagina.clean()

                            data_entrada = ft.Text(f"Data de Entrada: {resultado[0]}", size=20)
                            comprado = ft.Text(f"Comprado: {resultado[1]}", size=20)
                            rua = ft.Text(f"Rua: {resultado[2]}", size=20)
                            numero = ft.Text(f"Número: {resultado[3]}", size=20)
                            bairro = ft.Text(f"Bairro: {resultado[4]}", size=20)
                            cidade = ft.Text(f"Cidade: {resultado[5]}", size=20)
                            telefone = ft.Text(f"Telefone: {resultado[6]}", size=20)
                            #renavam = ft.Text(f"Renavam: {resultado[7]}", size=20)
                            placa = ft.Text(f"Placa: {resultado[8]}", size=20)
                            marca = ft.Text(f"Marca: {resultado[9]}", size=20)
                            modelo = ft.Text(f"Modelo: {resultado[10]}", size=20)
                            ano = ft.Text(f"Ano: {resultado[11]}", size=20)
                            cor = ft.Text(f"Cor: {resultado[12]}", size=20)
                            obsc = ft.Text(f"OBS: {resultado[13]}", size=20)

                            col10 = [data_entrada, comprado, telefone]
                            col11 = [rua, numero, bairro, cidade]
                            col12 = [placa, marca, modelo, ano, cor]

                            row10 = ft.Row(spacing=20, controls=col10, alignment="center")
                            row11 = ft.Row(spacing=20, controls=col11, alignment="center")
                            row12 = ft.Row(spacing=20, controls=col12, alignment="center")

                            #pagina.add(placa)

                            pagina.add(row10)
                            pagina.add(row11)
                            pagina.add(row12)
                            pagina.add(obsc)

                            data_atual = dt.datetime.now()
                            data_formatada = data_atual.strftime("%d/%m/%Y")

                            dt_saida = ft.TextField(data_formatada)
                            vendido = ft.TextField(label="Vendido ao Sr.")
                            rua_saida_widget = ft.TextField(label="Rua")
                            numero_saida_widget = ft.TextField(label="Nº", width=100)
                            bairro_saida_widget = ft.TextField(label="Bairro")
                            cidade_saida_widget = ft.TextField(label="Cidade")
                            telefone_saida_widget = ft.TextField(label="Telefone")
                            obs_saida_widget = ft.TextField(label="OBS", width=600)

                            col20 = [dt_saida, vendido, telefone_saida_widget]
                            col21 = [rua_saida_widget, numero_saida_widget, bairro_saida_widget, cidade_saida_widget]
                            col22 = [obs_saida_widget]

                            row20 = ft.Row(spacing=20, controls=col20, alignment="center")
                            row21 = ft.Row(spacing=20, controls=col21, alignment="center")
                            row22 = ft.Row(spacing=20, controls=col22, alignment="center")

                            linha_vazia = ft.Text("\n", size=5)
                            pagina.add(linha_vazia)

                            pagina.add(row20)
                            pagina.add(row21)
                            pagina.add(row22)
                                    
                            pagina.update()

                            resp_widget = ft.Text("Adicionado com sucesso", size=20)
                                    
                            def salvar_placa(evento):
                                campos_vazios = []

                                if dt_saida.value == "":
                                    campos_vazios.append("Data de Entrada")
                                if vendido.value == "":
                                    campos_vazios.append("Marca")
                                if rua_saida_widget.value == "":
                                    campos_vazios.append("Modelo")
                                if numero_saida_widget.value == "":
                                    campos_vazios.append("Ano")
                                if bairro_saida_widget.value == "":
                                    campos_vazios.append("Renavam")
                                if cidade_saida_widget.value == "":
                                    campos_vazios.append("Placa")
                                if telefone_saida_widget.value == "":
                                    campos_vazios.append("Cor")
                                
                                mensagemFaltou = None

                                if campos_vazios:
                                    mensagemFaltou = ft.Text("Faltou preencher os seguintes campos: {}".format(", ".join(campos_vazios)), text_align="center", size=20)
                                    pagina.add(mensagemFaltou)

                                else:

                                    # Conectando ao banco de dados
                                    conn = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="root",
                                        database="inovacao"
                                    )
                                    cursor = conn.cursor()

                                    data_entrada = resultado[0]
                                    comprado = resultado[1]
                                    rua = resultado[2]
                                    numero = resultado[3]
                                    bairro = resultado[4]
                                    cidade = resultado[5]
                                    telefone = resultado[6]
                                    renavam = resultado[7]
                                    placa = resultado[8]
                                    marca = resultado[9]
                                    modelo = resultado[10]
                                    ano = resultado[11]
                                    cor = resultado[12]
                                    obsc = resultado[13]

                                    if obs_saida_widget.value != "":
                                        cursor.execute("insert into saida(DATA_SAIDA,VENDIDO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM_ENTRADA, PLACA_ENTRADA,MARCA_ENTRADA,MODELO_ENTRADA,ANO_ENTRADA,COR_ENTRADA,OBSV) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_saida.value, vendido.value, rua_saida_widget.value, numero_saida_widget.value, bairro_saida_widget.value, cidade_saida_widget.value, telefone_saida_widget.value, int(renavam), placa, marca, modelo, ano, cor, obs_saida_widget.value))

                                    else:
                                        cursor.execute("insert into saida(DATA_SAIDA,VENDIDO,RUA,NUMERO,BAIRRO,CIDADE,TELEFONE,RENAVAM_ENTRADA, PLACA_ENTRADA,MARCA_ENTRADA,MODELO_ENTRADA,ANO_ENTRADA,COR_ENTRADA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dt_saida.value, vendido.value, rua_saida_widget.value, numero_saida_widget.value, bairro_saida_widget.value, cidade_saida_widget.value, telefone_saida_widget.value, int(renavam), placa, marca, modelo, ano, cor))

                                    conn.commit()
                                    conn.close()

                                    vendido.value = ""
                                    rua_saida_widget.value = ""
                                    numero_saida_widget.value = ""
                                    bairro_saida_widget.value = ""
                                    cidade_saida_widget.value = ""
                                    telefone_saida_widget.value = ""
                                    obs_saida_widget.value = ""

                                    pagina.add(resp_widget)
                                
                            linha_vazia = ft.Text("\n", size=5)
                            pagina.add(linha_vazia)

                            btn_salvar = ft.ElevatedButton("Salvar", on_click=salvar_placa, width=110, scale=1.3)
                            espaco = ft.Text("")
                            btn_voltar = ft.ElevatedButton("Voltar", on_click=voltar, width=110, scale=1.3)

                            col_btn = [btn_salvar, espaco, espaco2, btn_voltar]

                            row_btn = ft.Row(spacing=20, controls=col_btn, alignment="center")

                            pagina.add(row_btn)

                            # Fechando a conexão
                            conn.close()
                                    
                        else:
                            pagina.add(mensagemNEncontrado)
                            
                    except Exception as e:
                        # Lidar com a exceção
                        erro = ft.Text(f"Deu o erro: {e}")

                linha_vazia = ft.Text("\n", size=5)
                pagina.add(linha_vazia)

                btn_ok = ft.ElevatedButton("OK", on_click=ok, width=95, scale=1.3)
                btn_voltar1 = ft.ElevatedButton("Voltar", on_click=voltar, width=95, scale=1.3)

                col_btn3 = [btn_ok, espaco1, btn_voltar1]

                row_btn2 = ft.Row(spacing=20, controls=col_btn3, alignment="center")
                    
                pagina.add(row_btn2)

            except Exception as e:
                # Lidar com a exceção
                erro = ft.Text(f"Deu o erro: {e}")

        def voltar(evento):
            # Limpar a página completamente
            pagina.clean()

            # Adicionar widgets padrão de volta à página
            pagina.add(texto)
            pagina.add(btn_pesquisar)
            pagina.add(btn_entrada)
            pagina.add(btn_saida)

            pagina.update()

        btn_placa = ft.ElevatedButton("Placa", on_click=placa, width=110, scale=1.3)
        espaco1 = ft.Text("")
        btn_renavam = ft.ElevatedButton("Renavam", on_click=renavam, width=110, scale=1.3)
        espaco2 = ft.Text("")
        btn_voltar2 = ft.ElevatedButton("Voltar", on_click=voltar, width=110, scale=1.3)

        col_btn2 = [btn_placa, espaco1, btn_renavam, espaco2, btn_voltar2]

        row_btn2 = ft.Row(spacing=20, controls=col_btn2, alignment="center")

        linha_vazia = ft.Text("\n", size=5)
        pagina.add(linha_vazia)
        pagina.add(row_btn2)

        pagina.update()


    def pesquisar(evento):
        pagina.clean()

        resp_widget = ft.Text("Não encontrado.", size=20)

        def placa(evento):
            try:
                pagina.clean()

                placa = ft.TextField(label="Digite a placa")

                pagina.add(placa)
                
                def ok(evento):
                    # Conectando ao banco de dados
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="inovacao"
                    )
                    cursor = conn.cursor()

                    # Verificar se o valor existe no banco de dados
                    cursor.execute("SELECT * FROM entrada, saida WHERE placa = %s and PLACA_ENTRADA = %s", (placa.value,placa.value))
                    resultado = cursor.fetchone()

                    if resultado:
                        pagina.clean()
                        
                        data_entrada = ft.Text(f"Data de Entrada: {resultado[0]}", size=20)
                        comprado = ft.Text(f"Comprado Sr.: {resultado[1]}", size=20)
                        rua = ft.Text(f"Rua: {resultado[2]}", size=20)
                        numero = ft.Text(f"Número: {resultado[3]}", size=20)
                        bairro = ft.Text(f"Bairro: {resultado[4]}", size=20)
                        cidade = ft.Text(f"Cidade: {resultado[5]}", size=20)
                        telefone = ft.Text(f"Telefone: {resultado[6]}", size=20)
                        renavam = ft.Text(f"Renavam: {resultado[7]}", size=20)
                        #placa = ft.Text(f"Placa: {resultado[8]}", size=20)
                        marca = ft.Text(f"Marca: {resultado[9]}", size=20)
                        modelo = ft.Text(f"Modelo: {resultado[10]}", size=20)
                        ano = ft.Text(f"Ano: {resultado[11]}", size=20)
                        cor = ft.Text(f"Cor: {resultado[12]}", size=20)
                        obsc = ft.Text(f"OBS: {resultado[13]}", size=20)

                        dt_saida = ft.Text(f"Data de saída: {resultado[14]}", size=20)
                        vendido = ft.Text(f"Vendido Sr.: {resultado[15]}", size=20)
                        rua_vendido = ft.Text(f"Rua: {resultado[16]}", size=20)
                        numero_vendido = ft.Text(f"Número: {resultado[17]}", size=20)
                        bairro_vendido = ft.Text(f"Bairro: {resultado[18]}", size=20)
                        cidade_vendido = ft.Text(f"Cidade: {resultado[19]}", size=20)
                        tel_vendido = ft.Text(f"Telefone: {resultado[20]}", size=20)
                        obsv = ft.Text(f"OBS: {resultado[27]}", size=20)
                        
                        col10 = [data_entrada, comprado, telefone]
                        col11 = [rua, numero, bairro, cidade]
                        col12 = [renavam, marca, modelo, ano, cor]
                        col15 = [obsc]
                        col13 = [dt_saida, vendido, tel_vendido]
                        col14 = [rua_vendido, numero_vendido, bairro_vendido, cidade_vendido]
                        col16 = [obsv]
                        
                        row10 = ft.Row(spacing=20, controls=col10, alignment="center")
                        row11 = ft.Row(spacing=20, controls=col11, alignment="center")
                        row12 = ft.Row(spacing=20, controls=col12, alignment="center")
                        row13 = ft.Row(spacing=20, controls=col13, alignment="center")
                        row14 = ft.Row(spacing=20, controls=col14, alignment="center")
                        row15 = ft.Row(spacing=20, controls=col15, alignment="center")
                        row16 = ft.Row(spacing=20, controls=col16, alignment="center")

                        pagina.add(row10)
                        pagina.add(row11)
                        pagina.add(row12)
                        pagina.add(row15)
                        pagina.add(row13)
                        pagina.add(row14)
                        pagina.add(row16)

                        pagina.add(espaco1)
                        pagina.add(btn_voltar)
                                    
                        pagina.update()
                                    
                    else:
                        pagina.add(resp_widget)

                    # Fechando a conexão
                    conn.close()

            except Exception as e:
                # Lidar com a exceção
                erro = ft.Text(f"Deu o erro: {e}")

            linha_vazia = ft.Text("\n", size=5)
            pagina.add(linha_vazia)

            btn_ok = ft.ElevatedButton("OK", on_click=ok, width=110, scale=1.3)

            col2 = [btn_ok, espaco1, btn_voltar]

            row2 = ft.Row(spacing=20, controls=col2, alignment="center")

            pagina.add(row2)

            pagina.update()
                
        def renavam(evento):
            try:
                pagina.clean()

                renavam = ft.TextField(label="Digite o renavam")

                pagina.add(renavam)

                def ok_renavam(evento):
                    # Conectando ao banco de dados
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="root",
                        database="inovacao"
                    )
                    cursor = conn.cursor()

                    # Verificar se o valor existe no banco de dados
                    cursor.execute("SELECT * FROM entrada, saida WHERE renavam = %s and RENAVAM_ENTRADA = %s", (renavam.value,renavam.value))
                    resultado = cursor.fetchone()

                    if resultado:
                        pagina.clean()

                        data_entrada = ft.Text(f"Data de Entrada: {resultado[0]}", size=20)
                        comprado = ft.Text(f"Comprado: {resultado[1]}", size=20)
                        rua = ft.Text(f"Rua: {resultado[2]}", size=20)
                        numero = ft.Text(f"Número: {resultado[3]}", size=20)
                        bairro = ft.Text(f"Bairro: {resultado[4]}", size=20)
                        cidade = ft.Text(f"Cidade: {resultado[5]}", size=20)
                        telefone = ft.Text(f"Telefone: {resultado[6]}", size=20)
                        #renavam = ft.Text(f"Renavam: {resultado[7]}", size=20)
                        placa = ft.Text(f"Placa: {resultado[8]}", size=20)
                        marca = ft.Text(f"Marca: {resultado[9]}", size=20)
                        modelo = ft.Text(f"Modelo: {resultado[10]}", size=20)
                        ano = ft.Text(f"Ano: {resultado[11]}", size=20)
                        cor = ft.Text(f"Cor: {resultado[12]}", size=20)
                        obsc = ft.Text(f"OBS: {resultado[13]}", size=20)

                        dt_saida = ft.Text(f"Data de saída: {resultado[14]}", size=20)
                        vendido = ft.Text(f"Vendido Sr.: {resultado[15]}", size=20)
                        rua_vendido = ft.Text(f"Rua: {resultado[16]}", size=20)
                        numero_vendido = ft.Text(f"Número: {resultado[17]}", size=20)
                        bairro_vendido = ft.Text(f"Bairro: {resultado[18]}", size=20)
                        cidade_vendido = ft.Text(f"Cidade: {resultado[19]}", size=20)
                        tel_vendido = ft.Text(f"Telefone: {resultado[20]}", size=20)
                        obsv = ft.Text(f"OBS: {resultado[27]}", size=20)

                        col10 = [data_entrada, comprado, telefone]
                        col11 = [rua, numero, bairro, cidade]
                        col12 = [placa, marca, modelo, ano, cor]
                        col15 = [obsc]
                        col13 = [dt_saida, vendido, tel_vendido]
                        col14 = [rua_vendido, numero_vendido, bairro_vendido, cidade_vendido]
                        col16 = [obsv]

                        row10 = ft.Row(spacing=20, controls=col10, alignment="center")
                        row11 = ft.Row(spacing=20, controls=col11, alignment="center")
                        row12 = ft.Row(spacing=20, controls=col12, alignment="center")
                        row13 = ft.Row(spacing=20, controls=col13, alignment="center")
                        row14 = ft.Row(spacing=20, controls=col14, alignment="center")
                        row15 = ft.Row(spacing=20, controls=col15, alignment="center")
                        row16 = ft.Row(spacing=20, controls=col16, alignment="center")

                        pagina.add(row10)
                        pagina.add(row11)
                        pagina.add(row12)
                        pagina.add(row15)
                        pagina.add(row13)
                        pagina.add(row14)
                        pagina.add(row16)

                        pagina.add(espaco1)
                        pagina.add(btn_voltar)
                                    
                        pagina.update()
                                    
                    else:
                        pagina.add(resp_widget)

                    # Fechando a conexão
                    conn.close()
                
            except Exception as e:
                # Lidar com a exceção
                erro = ft.Text(f"Deu o erro: {e}")

            linha_vazia = ft.Text("\n", size=5)
            pagina.add(linha_vazia)

            btn_ok = ft.ElevatedButton("OK", on_click=ok_renavam, width=110, scale=1.3)

            col3 = [btn_ok, espaco1, btn_voltar]

            row3 = ft.Row(spacing=20, controls=col3, alignment="center")

            pagina.add(row3)

        def voltar(evento):
            # Limpar a página completamente
            pagina.clean()

            # Adicionar widgets padrão de volta à página
            pagina.add(texto)
            pagina.add(btn_pesquisar)
            pagina.add(btn_entrada)
            pagina.add(btn_saida)

        linha_vazia = ft.Text("\n", size=5)
        pagina.add(linha_vazia)

        btn_placa = ft.ElevatedButton("Placa", on_click=placa, width=110, scale=1.3)
        espaco1 = ft.Text("")
        btn_renavam = ft.ElevatedButton("Renavam", on_click=renavam, width=110, scale=1.3)
        espaco2 = ft.Text("")
        btn_voltar = ft.ElevatedButton("Voltar", on_click=voltar, width=110, scale=1.3)

        col = [btn_placa, espaco1, btn_renavam, espaco2, btn_voltar]

        row = ft.Row(spacing=20, controls=col, alignment="center")

        perg = ft.Text("Placa ou renavam ?", size=20)

        pagina.add(perg)

        pagina.add(row)
        
        pagina.update()


    btn_pesquisar = ft.ElevatedButton("Pesquisar", on_click=pesquisar, width=200, scale=1.3)
    btn_entrada = ft.ElevatedButton("Entrada", on_click=Entrada, width=200, scale=1.3)
    btn_saida = ft.ElevatedButton("Saída", on_click=Saida, width=200, scale=1.3)
    
    pagina.add(texto)

    # Botão de mostrar todos os carros
    pagina.add(btn_pesquisar)

    # Botão de adicionar um carro
    pagina.add(btn_entrada)

    # Botão de excluir um carro
    pagina.add(btn_saida)

    pagina.update()

ft.app(target=main)