
### **Case Técnico API**
Objetivo:
- Desenvolver uma API RESTful que permita o registro e a consulta de atividades fisicas realizadas por funcionários
  
---

### **Instruções**

Utilize o comando abaixo para instalar as dependências:

```
python -m pip install flask_sqlalchemy flask
```

Para executar a API utilize o comando:
```
python app.py
```

---
### **Rotas**
- GET /atividades - Retorna todas as atividades
- GET /atividades/{funcional} - Retorna todas as atividades de um funcionário
- POST /atividades - Cadastra uma atividade

#### Exemplo requisição JSON da rota POST /atividades:
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
