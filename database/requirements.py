try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySql Connector não está instalado.')
else:
    print('MySql Connector está instalado e pronto para uso.')
