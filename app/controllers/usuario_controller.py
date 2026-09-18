from app.models.usuario import carregar_usuarios


class UsuarioController:
    def __init__(self):
        self._usuarios = carregar_usuarios()

    def login(self, nome, senha):
        usuario = self._buscar_por_nome(nome)
        if usuario is None or not usuario.verificar_senha(senha):
            return None
        return self._para_dicionario(usuario)

    def _buscar_por_nome(self, nome):
        for usuario in self._usuarios:
            if usuario.mostrar_nome() == nome:
                return usuario
        return None

    def _para_dicionario(self, usuario):
        return {
            'id': usuario.mostrar_id(),
            'nome': usuario.mostrar_nome(),
            'perfil': usuario.mostrar_perfil(),
            'permissoes': usuario.permissoes(),
        }
