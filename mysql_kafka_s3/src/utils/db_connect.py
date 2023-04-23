import os
from log_handler import logger


def get_mysql_connection_properties() -> dict:
    params = find_params(['MYSQL_USER_NAME', 'MYSQL_HOST', 'MYSQL_PASSWORD', 'MYSQL_PORT', 'MYSQL_DB_NAME'])
    host = params['MYSQL_HOST']
    port = params['MYSQL_PORT']
    db_name = params['MYSQL_DB_NAME']

    connection_properties = {
        'user': params['MYSQL_USER_NAME'],
        'password': params['MYSQL_PASSWORD'],
        'url': f"jdbc:mysql://{host}:{port}/{db_name}",
        'driver': "com.mysql.cj.jdbc.Driver"
    }

    return connection_properties


def find_params(params: list) -> dict:
    params_values = {}
    try:
        for param in params:
            params_values[param] = os.getenv(param)
        return params_values
    except Exception as ex:
        logger.error(f"Not able to find {param} in environment variables due to {ex}!!!!!")
        raise ex
