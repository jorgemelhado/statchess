# Projeto Statchess — Plano Completo

## 1. Visão Geral
O projeto Statchess tem como objetivo criar uma aplicação capaz de consultar dados da API do Lichess, processá-los, armazená-los e disponibilizá-los por meio de uma API própria, evoluindo futuramente para um frontend visual.

---

## 2. Tecnologias Recomendadas

### Backend
| Tecnologia | Motivo |
|-----------|--------|
| Python | Simples, rápido para prototipar, excelente para APIs |
| FastAPI | Framework moderno, rápido, com tipagem e documentação automática |
| Requests | Biblioteca simples para fazer requisições HTTP |
| Uvicorn | Servidor ASGI rápido para rodar FastAPI |

### Infraestrutura
| Componente | Escolha recomendada | Motivo |
|-----------|----------------------|--------|
| IDE | VS Code | Extensões excelentes para Python |
| Versionamento | Git + GitHub | Fluxo profissional |
| Deploy | Render / Railway | Fácil, gratuito para protótipos |
| Banco de dados | PostgreSQL | Robusto e padrão do mercado |

---

## 3. Estrutura do Projeto
statchess/
│
├── .venv/                # ambiente virtual
├── src/
│   ├── main.py           # script principal
│   ├── lichess_client.py # módulo de integração com Lichess
│   └── api/              # (Fase 2) FastAPI
├── tests/                # (Fase 3) testes automatizados
├── requirements.txt
├── README.md
└── LICENSE

---

## 4. Fases do Projeto

### Fase 0 — Preparação
- Instalar Python  
- Instalar VS Code  
- Criar diretório do projeto  
- Inicializar Git  
- Criar .gitignore  
- Criar ambiente virtual .venv  
- Criar estrutura inicial  

---

### Fase 1 — Script que consulta a API do Lichess
Objetivo: Criar um script simples que faz uma requisição HTTP real.

Entregáveis:
- lichess_client.py  
- main.py  
- Dependência requests instalada  
- Projeto funcionando localmente  

Passos:
1. Criar módulo que consulta API  
2. Tratar erros de requisição  
3. Imprimir partidas no terminal  
4. Commitar e enviar ao GitHub  

---

### Fase 2 — Criar API própria com FastAPI
Objetivo: Transformar o script em uma API REST.

Endpoints previstos:
| Endpoint | Função |
|----------|--------|
| GET /games/{username} | Retorna partidas do usuário |
| GET /stats/{username} | Retorna estatísticas básicas |
| GET /health | Verifica se a API está no ar |

Entregáveis:
- Estrutura FastAPI  
- Documentação automática (Swagger)  
- Servidor local rodando com Uvicorn  

---

### Fase 3 — Persistência e Banco de Dados
Objetivo: Armazenar partidas para consultas futuras.

Tarefas:
- Criar banco PostgreSQL  
- Criar tabelas  
- Criar camada de acesso a dados  
- Criar endpoints que leem do banco  

---

### Fase 4 — Deploy
Objetivo: Colocar a API no ar.

Plataformas recomendadas:
- Render  
- Railway  
- Fly.io  

Entregáveis:
- API pública  
- Logs  
- Monitoramento básico  

---

### Fase 5 — Frontend
Objetivo: Criar interface visual para consultar estatísticas.

Tecnologias sugeridas:
- React  
- TailwindCSS  
- Vite  

---

## 5. Roadmap Geral
| Fase | Objetivo | Status |
|------|----------|--------|
| Fase 0 | Preparação | ✔️ Concluída |
| Fase 1 | Script HTTP | Em andamento |
| Fase 2 | API FastAPI | Próxima |
| Fase 3 | Banco de dados | Futuro |
| Fase 4 | Deploy | Futuro |
| Fase 5 | Frontend | Futuro |

---

## 6. Explicação das Tecnologias

### Python
Simples, poderoso e com enorme ecossistema de bibliotecas.

### FastAPI
- Rápido  
- Tipado  
- Documentação automática  
- Ideal para APIs modernas  

### Requests
Facilita requisições HTTP sem complicação.

### Git + GitHub
Fluxo profissional, histórico, branches, colaboração.

---

## 7. Conclusão
Este documento resume todo o plano do projeto Statchess, desde a preparação até o frontend final. Ele serve como guia para você avançar com clareza e segurança.
