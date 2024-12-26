from loguru import logger

logger.add("execution.log", format="{time} - {level} - {message}", level="INFO" )

def log_execution(func):
    """"
    Decorato para logar inicio, os parametros e o fim da execução de uma funcao
    """
    def wrapper(*args, **kwargs):
        logger.info(f'Executando {func.__name__} com args = {args} kwargs = {kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'{func.__name__} retornou {result}')
            return result
        except Exception as e:
            logger.error(f'Erro na execuçao de {func.__name__}: {e}')
    return wrapper


def multiplica_result_args(func):
    """
    Multiplica o resultado da soma pelos argumentos
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            result *= arg
        return result
    return wrapper
