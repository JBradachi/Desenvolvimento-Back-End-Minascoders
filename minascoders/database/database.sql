-- Garante que a comunicação entre o banco de dados e o backend se dará na
-- codificação correta. Não remova essa linha sob hipótese alguma!
SET CHARACTER_SET_CLIENT = utf8mb4;
SET CHARACTER_SET_CONNECTION = utf8mb4;
SET CHARACTER_SET_RESULTS = utf8mb4;
SET COLLATION_CONNECTION = utf8mb4_general_ci;

-- Cria o banco de dados se ele não existir
CREATE DATABASE IF NOT EXISTS mysqlsite;

-- Usa o banco de dados mysqlsite
USE mysqlsite;

-- Criação das tabelas

-- Tabela de notícias
CREATE TABLE IF NOT EXISTS noticia (
    id INTEGER NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    data_publicacao DATE NOT NULL,
    resumo TEXT,
    autor VARCHAR(100),
    imagem TEXT,  -- Campo para URL da imagem
    PRIMARY KEY (id),
    UNIQUE (titulo, data_publicacao) -- Evita duplicatas
);

-- Tabela de patrocinadores
CREATE TABLE IF NOT EXISTS patrocinador (
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    nivel INTEGER,
    link_site VARCHAR(255),
    logo TEXT,  -- Campo para URL da logo
    PRIMARY KEY (id),
    UNIQUE (nome) -- Evita duplicatas
);

-- Tabela de participantes
CREATE TABLE IF NOT EXISTS participante (
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    link_github VARCHAR(255),
    imagem TEXT,  -- Campo para URL da imagem
    PRIMARY KEY (id),
    UNIQUE (nome) -- Evita duplicatas
);

-- Inserir notícias (evitando duplicatas)
INSERT IGNORE INTO noticia (titulo, data_publicacao, resumo, autor, imagem) VALUES
('MinasCoders no Pódio da Maratona Sydle Levty de Programação da SECOM', '2024-12-14', 'Equipe do MinasCoders conquistou lugar no pódio da maratona, destacando-se em desafios de programação.', 'João Silva', 'https://example.com/imagem3.jpg'),
('Subgrupos do MinasCoders no SIPEEC', '2024-12-11', 'Os subgrupos do MinasCoders apresentaram seus projetos inovadores no SIPEEC, destacando suas contribuições tecnológicas.', 'Maria Oliveira', 'https://example.com/imagem3.jpg'),
('MinasCoders Pesquisa no SIPEEC', '2024-12-10', 'O MinasCoders apresentou suas pesquisas mais recentes no SIPEEC, focando em inovações tecnológicas e científicas.', 'Carlos Souza', 'https://example.com/imagem3.jpg'),
('Equipes Selecionadas para a Semana Imersiva da Campus Mobile', '2024-12-09', 'Equipes do MinasCoders foram selecionadas para a Semana Imersiva da Campus Mobile, um evento de intensivo em desenvolvimento mobile.', 'João Silva', 'https://example.com/imagem4.jpg'),
('MinasCoders na Maratona de Programação da SECOM Jr.', '2024-12-08', 'MinasCoders brilhou na Maratona da SECOM Jr., destacando-se em resolução de problemas e desafios técnicos.', 'Maria Oliveira', 'https://example.com/imagem5.jpg'),
('MinasCoders na Mostra de Profissões', '2024-12-07', 'MinasCoders participou da Mostra de Profissões, apresentando seus projetos e incentivando jovens talentos na área de tecnologia.', 'Carlos Souza', 'https://example.com/imagem6.jpg'),
('Equipes Selecionadas para a Semana Imersiva da Campus Mobile', '2024-12-06', 'Novas equipes do MinasCoders foram escolhidas para a Semana Imersiva da Campus Mobile, focada em aprimorar habilidades em programação móvel.', 'João Silva', 'https://example.com/imagem7.jpg');

-- Inserir patrocinadores (evitando duplicatas)
INSERT IGNORE INTO patrocinador (nome, nivel, link_site, logo) VALUES
('Afterverse', '5', 'https://afterverse.com/pt', 'https://afterverse.com/_nuxt/img/logo.8c0d728.svg'),
('Acasistemas', '4', 'https://acasistemas.com.br/', 'https://acasistemas.com.br/assets/images/aca-site-logo-320x119.png'),
('Vetta SMS Group', '4', 'https://vetta.com.br/pt', 'https://www.vetta.digital/assets/img/logo/vetta.svg'),
('DTI', '4', 'https://www.dtidigital.com.br/', 'https://sindinfor.org.br/wp-content/uploads/2021/02/case-dti-1280x640-1.jpg'),
('Cinnecta', '3', 'https://www.matera.com/br/cinnecta-agora-e-matera-insights/', 'https://kptl.com.br/wp-content/uploads/2020/04/cinnecta-1.png'),
('CIANDT', '3', 'https://ciandt.com/br//', 'https://dmwnh9nwzeoaa.cloudfront.net/2020-12/devops-ciandt-thumb.png'),
('FAPEMIG', '3', 'https://fapemig.br/pt/', 'https://www2.ufjf.br/inovacaogv/wp-content/uploads/sites/69/2022/07/fapemig-e1661178865786.jpeg'),
('FemaleTechLeaders', '3', 'https://femaletechleaders.com.br./', 'https://femaletechleadersmagazine.com/wp-content/uploads/2021/04/female-tech-leaders-logo-1.png'),
('Meninas Digitais', '3', 'https://meninas.sbc.org.br/', 'https://horizontes.sbc.org.br/wp-content/uploads/2024/06/meninas_digitaisSmall.png'),
('NESPeD', '3', 'https://nesped.caf.ufv.br/', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbPUaWfak5_WG1C6wdDryiUnnEMTlPNw-XYg&s');

-- Inserir participantes (evitando duplicatas)
INSERT IGNORE INTO participante (nome, email, link_github, imagem) VALUES
('Rafaella Ferreira', 'rafaella.pinheiro@ufv.br', 'https://github.com/Rafafps', 'https://ufvvirtuallabs-oficial.web.app/static/media/rafaela.870ff8cca9ec5f06edc8.jpeg'),
('Ingred Almeida', 'ingred.almeida@ufv.br', 'https://github.com/ingredalmeida1', '/static/images/ingred_perfil.jpeg'),
('João Bradachi', 'joao.bradachi@ufv.br', 'https://github.com/JBradachi', '/static/images/bradas_perfil.jpeg'),
('Pâmela Diniz', 'pamela.diniz@ufv.br', 'https://github.com/pamyd05', '/static/images/pamela_perfil.png');