from marshmallow import Schema, fields

# Esquemas personalizados para cada modelo
class ContaSchema(Schema):
    class Meta:
        fields = (
            'id_conta', 'id_pessoa', 'saldo', 'limite_saque_diario',
            'flag_ativo', 'tipo_conta', 'data_criacao'
        )

class TransacaoSchema(Schema):
    class Meta:
        fields = ('id_transacao', 'id_conta', 'valor', 'data_transacao')

class PessoaSchema(Schema):
    class Meta:
        fields = (
            'id_pessoa', 'nome', 'sobrenome', 'cpf', 'data_nascimento',
            'email', 'date_joined', 'is_deleted'
        )
