from marshmallow import Schema, fields

class TransacaoSchema(Schema):
    id_conta = fields.String(load_only=True)
    valor = fields.Float()
    
    id_transacao = fields.String(dump_only=True)
    data_transacao = fields.Date(dump_only=True)

class ContaSchema(Schema):
    id_pessoa = fields.String(load_only=True)
    saldo = fields.Decimal(as_string=True)
    limite_saque_diario = fields.Decimal(as_string=True)
    tipo_conta = fields.Int()
    
    id_conta = fields.String(dump_only=True)
    flag_ativo = fields.Boolean(dump_only=True)
    data_criacao = fields.Date(dump_only=True)
    
class PessoaSchema(Schema):
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)
    nome = fields.Str()
    sobrenome = fields.Str()
    cpf = fields.Str()
    data_nascimento = fields.Date()
    
    id_pessoa = fields.String(dump_only=True)
    data_criacao = fields.DateTime(dump_only=True)
    usuario_ativo = fields.Boolean(dump_only=True)
    
class LoginSchema(Schema):
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)