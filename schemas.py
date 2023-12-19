from marshmallow import Schema, fields

class TransacaoSchema(Schema):
    id_transacao = fields.Int(dump_only=True)
    id_conta = fields.String(required=True)
    valor = fields.Float()
    data_transacao = fields.Date()

class ContaSchema(Schema):
    id_conta = fields.String(dump_only=True)
    id_pessoa = fields.Int(required=True)
    saldo = fields.Decimal(as_string=True)
    limite_saque_diario = fields.Decimal(as_string=True)
    flag_ativo = fields.Boolean()
    tipo_conta = fields.Int()
    data_criacao = fields.Date()
    transacoes = fields.Nested(TransacaoSchema, many=True, dump_only=True)

class PessoaSchema(Schema):
    id_pessoa = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)
    nome = fields.Str()
    sobrenome = fields.Str()
    cpf = fields.Str()
    data_nascimento = fields.Date()
    date_joined = fields.DateTime(dump_only=True)
    is_deleted = fields.Boolean(dump_only=True)
    contas = fields.Nested(ContaSchema, many=True, dump_only=True)