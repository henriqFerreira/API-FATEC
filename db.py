import sqlite3
import json

class db:
    def create_db(self):
        conn = sqlite3.connect("data.sqlite")

        with open("schema.sql") as f:
            conn.executescript(f.read())
    
    def insert_vagas(self, arquivo):
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()

        with open(arquivo, mode='r', encoding='utf-8') as f:
            content = json.load(f)
        for data in content:
            if "beneficios" in data and "descEmpresa" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_cidade, vaga_estado, vaga_descricao, vaga_beneficios, vaga_descricao_empresa) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['cidade'], data['estado'], data['descricao'], data['beneficios'], data['descEmpresa']))
                conn.commit()
            elif "beneficios" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_cidade, vaga_estado, vaga_descricao, vaga_beneficios) VALUES (?,?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['cidade'], data['estado'], data['descricao'], data['beneficios']))
                conn.commit()
            elif "descEmpresa" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_cidade, vaga_estado, vaga_descricao, vaga_descricao_empresa) VALUES (?,?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['cidade'], data['estado'], data['descricao'], data['descEmpresa']))
                conn.commit()
            else:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_cidade, vaga_estado, vaga_descricao) VALUES (?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['cidade'], data['estado'], data['descricao']))
                conn.commit()
    
    def insert_cursos(self, arquivo):
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()

        with open(arquivo, mode='r', encoding='utf-8') as f:
            content = json.load(f)
        for data in content:
            cur.execute("INSERT INTO cursos (curso_categoria, curso_titulo, curso_tipo, curso_formato, curso_duracao, curso_conclusao) VALUES (?,?,?,?,?,?)", (data['categoriaCurso'], data['tituloCurso'], data['tipoCurso'], data['formatoCurso'], data['duracaoCurso'], data['conclusaoCurso']))
            conn.commit()

    def get_data_grafico(self):
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()


        stmt = cur.execute("SELECT COUNT(*) FROM vagas").fetchone()
        totalVagas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1").fetchone()
        vagasTi = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=0").fetchone()
        vagasGerais = stmt[0]


        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='ti'").fetchone()
        vagasTI = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='banco-de-dados'").fetchone()
        vagasBanco_de_dados = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='redes'").fetchone()
        vagasRedes = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='software'").fetchone()
        vagasSoftware = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='hardware'").fetchone()
        vagasHardware = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='back-end'").fetchone()
        vagasBack_end = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='front-end'").fetchone()
        vagasFront_end = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='seguran??a-da-informa????o'").fetchone()
        vagasSeguran??a_da_informa????o = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='engenheiro-de-dados'").fetchone()
        vagasEngenheiro_de_dados = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='cientista-de-dados'").fetchone()
        vagasCientista_de_dados = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='programa????o'").fetchone()
        vagasPrograma????o = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='desenvolvedor'").fetchone()
        vagasDesenvolvedor = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='business-inteligence'").fetchone()
        vagasBusiness_inteligence = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='cloud-computing'").fetchone()
        vagasCloud_computing = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='intelig??ncia-artificial'").fetchone()
        vagasIntelig??ncia_artificial = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='python'").fetchone()
        vagasPython = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='php'").fetchone()
        vagasPhp = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='javaScript'").fetchone()
        vagasJavaScript = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='fullstack'").fetchone()
        vagasFullstack = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='java'").fetchone()
        vagasJava = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='web-designer'").fetchone()
        vagasWeb_designer = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='s??nior'").fetchone()
        vagasS??nior = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='pleno'").fetchone()
        vagasPleno = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='dba'").fetchone()
        vagasDba = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='sistemas'").fetchone()
        vagasSistemas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='SQL'").fetchone()
        vagasSQL = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='server'").fetchone()
        vagasServer = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='inform??tica'").fetchone()
        vagasInform??tica = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1 AND vaga_categoria='tecnologia'").fetchone()
        vagasTecnologia = stmt[0]


        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Coopera????o%'").fetchone()
        cursos_cooperacao = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Empreendedorismo%'").fetchone()
        cursos_empreendedorismo = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Finan??as%'").fetchone()
        cursos_financas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Inova????o%'").fetchone()
        cursos_inovacao = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Leis%'").fetchone()
        cursos_leis = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Mercado e Vendas%'").fetchone()
        cursos_mercado_e_vendas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Organiza????o%'").fetchone()
        cursos_organizacao = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE'%Pessoas%'").fetchone()
        cursos_pessoas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM cursos WHERE curso_categoria LIKE '%Planejamento%'").fetchone()
        cursos_planejamento = stmt[0]
        

        data = {
            "totalVagas": totalVagas,
            "vagasTi": vagasTi,
            "vagasGerais": vagasGerais,


            "vagasTI": vagasTI,
            "vagasBanco_de_dados": vagasBanco_de_dados,
            "vagasRedes": vagasRedes,
            "vagasSoftware": vagasSoftware,
            "vagasHardware": vagasHardware,
            "vagasBack_end": vagasBack_end,
            "vagasFront_end": vagasFront_end,
            "vagasSeguran??a_da_informa????o": vagasSeguran??a_da_informa????o,
            "vagasEngenheiro_de_dados": vagasEngenheiro_de_dados,
            "vagasCientista_de_dados": vagasCientista_de_dados,
            "vagasPrograma????o": vagasPrograma????o,
            "vagasDesenvolvedor": vagasDesenvolvedor,
            "vagasBusiness_inteligence": vagasBusiness_inteligence,
            "vagasCloud_computing": vagasCloud_computing,
            "vagasIntelig??ncia_artificial": vagasIntelig??ncia_artificial,
            "vagasPython": vagasPython,
            "vagasPhp": vagasPhp,
            "vagasJavaScript": vagasJavaScript,
            "vagasFullstack": vagasFullstack,
            "vagasJava": vagasJava,
            "vagasWeb_designer": vagasWeb_designer,
            "vagasS??nior": vagasS??nior,
            "vagasPleno": vagasPleno,
            "vagasDba": vagasDba,
            "vagasSistemas": vagasSistemas,
            "vagasSQL": vagasSQL,
            "vagasServer": vagasServer,
            "vagasInform??tica": vagasInform??tica,
            "vagasTecnologia": vagasTecnologia,


            "cursos_cooperacao": cursos_cooperacao,
            "cursos_empreendedorismo": cursos_empreendedorismo,
            "cursos_financas": cursos_financas,
            "cursos_inovacao": cursos_inovacao,
            "cursos_leis": cursos_leis,
            "cursos_mercado_e_vendas": cursos_mercado_e_vendas,
            "cursos_organizacao": cursos_organizacao,
            "cursos_pessoas": cursos_pessoas,
            "cursos_planejamento": cursos_planejamento

        }

        return data


