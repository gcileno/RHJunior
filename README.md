# Projeto de desenvolvimento de uma plataforma integrada de gestão de pessoas para Empresas Juniors

<details>
    <summary>Visão Geral</summary>

    Plataforma integrada para gestão de pessoas focada em Empresas Juniores: cadastro de membros, projetos, avaliações, relatórios e emissão de certificados.
</details>

<details>
    <summary>Funcionalidades</summary>

    - Cadastro e autenticação de membros  
    - Gestão de projetos e equipes  
    - Controle de presença e avaliações  
    - Relatórios e exportação de dados
    - Emissão de Relatórios
    - Emissão de Certificados
    - Autenticidade de Certificados emitidos
</details>

<details>
    <summary>Arquitetura</summary>
    Monolítica (estado atual)
    - Aplicação monolítica: frontend, backend e lógica de domínio numa única base/deploy.
    - Atualmente funcionando parcialmente com um banco local SQLite (arquivo .db) — usado para desenvolvimento e testes.
</details>


<details>
    <summary>Instalação</summary>

    1. Clonar o repositório
        ```
        git clone <URL_DO_REPOSITORIO>
        cd <NOME_DO_REPOSITORIO>
        ```
    2. Criar e ativar um ambiente virtual
        ```
        python -m venv .venv
        # Windows
        .venv\Scripts\activate
        # macOS / Linux
        source .venv/bin/activate
        ```
    3. Instalar dependências a partir do requirements.txt
        ```
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
    4. Configurar variáveis de ambiente
        - Copiar `.env.example` para `.env` e ajustar SECRET_KEY e credenciais necessárias.
    5. Inicializar o banco e executar (quando aplicável)
        ```
        python manage.py migrate
        python manage.py createsuperuser  # opcional
        python manage.py runserver
        ```
</details>


<details>
    <summary>Como contribuir</summary>

    Abra uma issue para discutir mudanças e envie pull requests seguindo o guia de contribuição.
</details>


