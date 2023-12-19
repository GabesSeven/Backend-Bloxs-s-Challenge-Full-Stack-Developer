"""
blocklist.py

Este arquivo contém apenas a lista de bloqueio dos tokens JWT. Será importado por
app e o recurso de logout para que os tokens possam ser adicionados à lista de bloqueio quando o
usuário efetua logout.
"""

BLOCKLIST = set()
