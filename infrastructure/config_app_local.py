SECRET_KEY = 'chave secreta'
CACHE_TYPE = 'simple'
SWAGGER = {
    'title': 'Catálogo de Receitas Gourmet',
    'uiversion': 3,
    'version': '0.0.1',
    'openapi': '3.0.2',
    'components': {
        'securitySchemes': {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
                'description': 'Insira o token JWT no formato **Bearer &lt;seu_token&gt;**'
            }
        },
        'security': [{'BearerAuth': []}]
    }
}

SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = 'chave_secreta_token'
