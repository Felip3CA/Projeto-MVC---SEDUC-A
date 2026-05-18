from app.database import Session, engine, Base
from app.models.usuario import Usuario
from app.auth import hash_senha

Usuarios = [
    {   
        "nome": "Admin",
        "email": "admin@teste.com",
        "senha": "admin123",
        "role": "admin"
    },
    {
        "nome": "Professor",
        "email": "professor@admin.com",
        "senha": "professor123",
        "role": "professor"
    },
]

def criar_usuario():
    db = Session()

    try:
        for usuario in Usuarios:
            # Verificar se o usuário já existe
            existente = db.query(Usuario).filter_by(email=usuario["email"]).first()

            if existente:
                print(f"Já existe esse email: {usuario['email']} no banco")
                continue
            else:
                novo_usuario = Usuario(
                    nome=usuario["nome"],
                    email=usuario["email"],
                    senha_hash=hash_senha(usuario["senha"]),
                    role=usuario["role"]
                )
                db.add(novo_usuario)
            db.commit()
            print(f"Usuários cadastrados com sucesso!")
    except Exception as erro:
        db.rollback()
        print(erro)
    finally:
        db.close()


#Chamar a função para criar os usuarios
criar_usuario()

#Com base nisso, preciso criar mais rotas para editar - desativar - criar usuarios



