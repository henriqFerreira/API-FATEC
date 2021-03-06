CREATE TABLE IF NOT EXISTS usuarios (
	user_id INTEGER PRIMARY KEY,
	user_name varchar(50) not NULL,
	user_senha varchar(64) NOT NULL,
	user_email varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS vagas (
	vaga_id INTEGER PRIMARY KEY,
	vaga_categoria VARCHAR(30) NOT NULL,
	vaga_focada BOOLEAN NOT NULL CHECK (vaga_focada IN (0, 1)),
	vaga_titulo VARCHAR(40) NOT NULL,
	vaga_nivel VARCHAR(20) NOT NULL,
	vaga_empresa VARCHAR(50) NOT NULL,
	vaga_salario VARCHAR(15) NOT NULL,
	vaga_cidade VARCHAR(30),
	vaga_estado VARCHAR(30),
	vaga_descricao TEXT NOT NULL,
	vaga_beneficios VARCHAR(200),
	vaga_descricao_empresa TEXT
);

CREATE TABLE IF NOT EXISTS inscricoes (
	inscri_ID INTEGER PRIMARY KEY,
	inscri_userid INTEGER NOT NULL,
	inscri_vagaid INTEGER NOT NULL,
	FOREIGN KEY (inscri_userid) REFERENCES usuarios (user_id),
	FOREIGN KEY (inscri_vagaid) REFERENCES vagas (vaga_id)
);

CREATE TABLE IF NOT EXISTS cursos (
	curso_ID INTEGER PRIMARY KEY,
	curso_categoria VARCHAR(30) NOT NULL,
	curso_titulo VARCHAR(40) NOT NULL,
	curso_tipo VARCHAR(10) NOT NULL,
	curso_formato VARCHAR(10) NOT NULL,
	curso_duracao VARCHAR(30),
	curso_conclusao VARCHAR(30)
);