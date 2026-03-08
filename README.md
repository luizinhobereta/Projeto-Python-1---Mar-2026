# 📌 Pinterest Clone — Flask Web Application

Uma aplicação web desenvolvida em **Python com Flask**, inspirada na dinâmica da plataforma **Pinterest**, onde usuários podem publicar e visualizar imagens em um feed visual.

O objetivo deste projeto é demonstrar **estruturação profissional de aplicações Flask**, integração com banco de dados e implementação de funcionalidades comuns em redes sociais baseadas em conteúdo visual.

Este projeto foi desenvolvido como **projeto de estudo e demonstração técnica de habilidades em desenvolvimento backend e web architecture.**

---

# 🚀 Funcionalidades

* 👤 Cadastro de usuários
* 🔐 Autenticação (login/logout)
* 🖼 Upload de imagens
* 🧾 Página de perfil com fotos do usuário
* 📌 Feed com publicações
* 🔗 Relacionamento entre usuários e posts
* 💾 Persistência de dados com SQLAlchemy

---

# 🧠 Tecnologias Utilizadas

| Tecnologia  | Função                   |
| ----------- | ------------------------ |
| Python      | Linguagem principal      |
| Flask       | Framework web            |
| SQLAlchemy  | ORM para banco de dados  |
| Flask-Login | Gerenciamento de sessões |
| Flask-WTF   | Formulários e validação  |
| SQLite      | Banco de dados           |
| HTML + CSS  | Interface                |
| Bootstrap   | Layout responsivo        |
| Jinja2      | Templates dinâmicos      |

---

# 🏗 Estrutura do Projeto

Projeto organizado em **arquitetura modular**, separando responsabilidades.

```
ProjetoClonePinterest
│
├── sistema
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   │
│   ├── templates
│   │   ├── homepage.html
│   │   ├── perfil.html
│   │   └── login.html
│
├── static
│   ├── css
│   ├── fotos_posts
│   └── imagens
│
├── main.py
└── requirements.txt
```

Essa organização permite **escalabilidade e manutenção do código**.

---

# 💻 Como executar o projeto

## Clonar o repositório

```
git clone https://github.com/seuusuario/seurepositorio.git
```

## Entrar na pasta

```
cd ProjetoClonePinterest
```

## Criar ambiente virtual

```
python -m venv .venv
```

## Ativar ambiente

Windows

```
.venv\Scripts\activate
```

Linux / Mac

```
source .venv/bin/activate
```

## Instalar dependências

```
pip install -r requirements.txt
```

## Executar aplicação

```
python main.py
```

Servidor disponível em:

```
http://127.0.0.1:5000
```

---

# 📚 Objetivo do Projeto

Este projeto foi criado para exercitar conceitos importantes de **desenvolvimento web com Python**, incluindo:

* Arquitetura de aplicações Flask
* Modelagem de banco de dados
* Upload e gerenciamento de arquivos
* Autenticação de usuários
* Organização de projetos escaláveis

---

# 👨‍💻 Autor

**Luis Bereta**

Desenvolvedor de software com experiência em:

* Python
* PHP
* MySQL
* Automação de processos
* Desenvolvimento de sistemas administrativos
* Integração de APIs
* Sistemas para gestão pública

Também atuo no desenvolvimento de soluções digitais para **prefeituras, câmaras municipais e empresas**, criando sistemas que automatizam processos e melhoram a gestão da informação.

---

# 📬 Contato

GitHub
https://github.com/luizinhobereta
22 988140628
luizinhobereta@gmail.com

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma **estrela no repositório**.
