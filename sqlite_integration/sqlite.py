import sqlalchemy
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    Session
)
from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    select
)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)

    account = relationship(
        "Conta", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Conta (nome: {self.nome}, cpf: {self.cpf}, endereco: {self.endereco})"

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    client = relationship("Cliente", back_populates="account")

    def __repr__(self):
        return f"Conta (tipo: {self.tipo}, numero: {self.numero}, saldo: {self.saldo})"

# DB Connection
engine = sqlalchemy.create_engine("sqlite://")

# Create classes as datatables
Base.metadata.create_all(engine)

inspector_engine = sqlalchemy.inspect(engine)

print(inspector_engine.get_table_names())

with Session(engine) as session:
    gus = Cliente(
        nome = "Gustavo",
        cpf = "990887400",
        endereco = "Rua dos bobos no. 0",
        account = [Conta(tipo="corrente", agencia="0001", numero=1234, saldo=100)]
    )

    mike = Cliente(
        nome = "Michael",
        cpf = "008768912",
        endereco = "Rua dos bobos no. 100",
        account = [Conta(tipo="poupanca", agencia="0001", numero=3344, saldo=500)]
    )

    #Persist data on DB
    session.add_all([gus, mike])
    session.commit()

    stmt = select(Cliente).where(Cliente.nome.in_(["Gustavo", "Michael"]))
    for client in session.scalars(stmt):
        print(client)

