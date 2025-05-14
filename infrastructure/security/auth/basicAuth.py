from flask_httpauth import HTTPBasicAuth

class BasicAuthentication:
    """
    Classe que gerencia a autenticação HTTP Basic usando Flask-HTTPAuth.

    Attributes:
        auth (HTTPBasicAuth): Instância de autenticação HTTP.
        users (dict): Dicionário contendo nomes de usuários e suas senhas em texto plano (não recomendado para produção).

    Methods:
        verify_password(username, password):
            Método estático responsável por validar a autenticação de um usuário.
            Verifica se o nome de usuário está registrado e se a senha corresponde.
    """
    
    auth = HTTPBasicAuth()
    
    users = {
        "user1": "password1",
        "user2": "password2"
    }

    @staticmethod
    @auth.verify_password
    def verify_password(username, password):
        """
        Verifica se o nome de usuário e a senha fornecidos são válidos.

        Args:
            username (str): Nome de usuário enviado na requisição HTTP Basic.
            password (str): Senha associada ao nome de usuário.

        Returns:
            str or None: Retorna o nome de usuário se a autenticação for bem-sucedida, caso contrário, retorna None.
        """
        if username in BasicAuthentication.users and BasicAuthentication.users[username] == password:
            return username
