
### **Case Técnico API**
Objetivo:
- Desenvolver uma API RESTful que permita o registro e a consulta de atividades fisicas realizadas por funcionários

---
### **Rotas**
- GET /atividades - Retorna todas as atividades
- GET /atividades/{funcional} - Retorna todas as atividades de um funcionário
- POST /atividades - Cadastra uma atividade

---

### **Instruções**

Utilize o comando abaixo no terminal para instalar as dependências:

```
python -m pip install flask_sqlalchemy flask pytest
```

Para executar a API utilize o comando:
```
flask run
```

Para testar a API utilize o comando:
```
pytest testes_unitarios.py
```
---

### **Corpo da requisição**

Header (Chave API obrigatória em todas as rotas):
```
  {
    "x-api-key": "case_tecnico"
  }
```

#### Exemplo de uma requisição JSON para rota POST /atividades:

Header:
```
  {
    "x-api-key": "case_tecnico"
  }
```

Payload:

```
  {
    "funcional": "123456",
    "dataHora": "2025-09-24T07:30:00",
    "codigoAtividade": "RUN",
    "descricaoAtividade": "Corrida de 5km"
  }
```

---

### **Detalhes**

- **Python 3.9+**
- **Flask** → Framework
- **Flask-SQLAlchemy** → ORM para banco de dados
- **SQLite** → Banco de dados
- **Gerenciamento de Erros** → Gerenciador global de erros
- **Pytest** -> Testes unitários
- **API key** -> Validação chave API
- **Logs** -> Registro de logs
