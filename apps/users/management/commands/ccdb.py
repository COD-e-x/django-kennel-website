import logging

import pyodbc
from django.core.management import BaseCommand
from kennel.settings import USER, PASSWORD, HOST, PAD_DATABASE, DRIVER, DATABASE

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        connection_string = f"""DRIVER={DRIVER};
                                SERVER={HOST};
                                UID={USER};
                                PWD={PASSWORD};
                                DATABASE={PAD_DATABASE}"""
        try:
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True
            cursor = conn.cursor()
            # noinspection SqlNoDataSourceInspection
            cursor.execute(rf"CREATE DATABASE {DATABASE}")
            logging.info(f"База данных {DATABASE} успешно создана.")
        except pyodbc.ProgrammingError as e:
            logger.error(f"Ошибка программирования SQL: {e}")
        except pyodbc.InterfaceError as e:
            logger.error(f"Ошибка интерфейса: {e}")
        except Exception as e:
            logger.error(f"Другая ошибка: {e}")
        else:
            logger.info(f"База дынных {DATABASE} успешно создана.")
