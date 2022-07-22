from importlib.resources import path
import sys
import time
import os
from time import sleep

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)

    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    printProgressBar(0)

    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()

def progressBar1(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)

    def printProgressBar1 (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    printProgressBar1(0)

    for i, item1 in enumerate(iterable):
        yield item1
        printProgressBar1(i + 1)
    print()

final = 0

while final == 0:
    local = input ('---- TRANSFERENCIA ENTRE MAQUINAS ----\n1.PRINCIPAL PARA LOCAL\n2.TRANSFERENCIA VIA REDE(APENAS MIDIAS E MYSQL)\n3.Sair\n')
    verifica_pasta = os.path.exists('C:\Pulsar\script_pulsar')
    if verifica_pasta == False:
        print("Nao foi possivel encontrar a pasta script_pulsar!\nCrie a pasta para que o script funcione corretamente")
        print("Finalizando!")
        sleep(4)
        exit()
    if local == '2':
      hp = input('HOSTNAME PRINCIPAL: ')
      hr = input('HOSTNAME RESERVA: ')
      print('\n--------------------------------------------------------\n')

      p_com = input('ORIGEM CAMINHO COMERCIAL\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho: ')
      r_com = input('\nDESTINO CAMINHO COMERCIAL\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho:  ')
      comercial = ('xcopy "' + p_com +'\\"*.* "' + r_com + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')
      
      p_jorn = input('ORIGEM CAMINHO JORNAL\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho: ')
      r_jorn = input('\nDESTINO CAMINHO JORNAL\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho:  ')
      jornal = ('\nxcopy "' + p_jorn +'\\"*.* "' + r_jorn + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_musica = input('ORIGEM CAMINHO MUSICA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\MUSICA\nDigite o caminho: ')
      r_musica = input('\nDESTINO CAMINHO MUSICA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\MUSICA\nDigite o caminho:  ')
      musica = ('\nxcopy "' + p_musica +'\\"*.* "' + r_musica + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_vinheta = input('ORIGEM CAMINHO VINHETA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\VINHETA\nDigite o caminho: ')
      r_vinheta = input('\nDESTINO CAMINHO VINHETA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\VINHETA\nDigite o caminho:  ')
      vinheta = ('\nxcopy "' + p_vinheta +'\\"*.* "' + r_vinheta + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_horacerta = input('ORIGEM CAMINHO HORA CERTA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\HORA_CERTA\nDigite o caminho: ')
      r_horacerta = input('\nDESTINO CAMINHO HORA CERTA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\HORA_CERTA\nDigite o caminho:  ')
      horacerta = ('\nxcopy "' + p_horacerta +'\\"*.* "' + r_horacerta + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_infor = input('ORIGEM CAMINHO INFORMATIVO\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\INFORMATIVO\nDigite o caminho: ')
      r_infor = input('\nDESTINO CAMINHO INFORMATIVO\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\INFORMATIVO\nDigite o caminho:  ')
      informativo = ('\nxcopy "' + p_infor +'\\"*.* "' + r_infor + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_grav = input('ORIGEM CAMINHO GRAVADOS\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\GRAVADOS\nDigite o caminho: ')
      r_grav = input('\nDESTINO CAMINHO GRAVADOS\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\GRAVADOS\nDigite o caminho:  ')
      gravados = ('\nxcopy "' + p_grav +'\\"*.* "' + r_grav + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      print('echo --- GERANDO TRANSFERENCIA MYSQL ---\n')
      bd = ('\nnet stop mysql\nxcopy \\\\' + hp + '\mysql\data\\*.* C:\mysql\data\\ /s /y /c /k /d\nnet start mysql\n')

      sleep(2)
      
      items1 = list(range(0, 25))

      for item1 in progressBar1(items1, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

      print('\necho --- CONCLUIDO! ---\n')
      print('--------------------------------------------------------\n')

      finalizar = input('Finalizar programa ?\n1. Finalizar\n2. Reiniciar\n')
      if finalizar == '1':
        final = 1
        sys.stdout = open("C:\Pulsar\script_pulsar\BACKUP_PULSAR.bat", "w")
        print(comercial,
        jornal,
        musica,
        vinheta,
        horacerta,
        informativo,
        gravados,
        bd)
      if finalizar == '2':
        print('Aguarde!\n')
        sleep(2)
        continue


    if local == '1':
      hp = input('HOSTNAME PRINCIPAL: ')
      hr = input('HOSTNAME RESERVA: ')

      print('\n--------------------------------------------------------\n')
      p_com = input('ORIGEM CAMINHO COMERCIAL\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho: ')
      r_com = input('\nDESTINO CAMINHO COMERCIAL\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho:  ')
      comercial = ('xcopy "' + p_com +'\\"*.* "' + r_com + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')
      
      p_jorn = input('ORIGEM CAMINHO JORNAL\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho: ')
      r_jorn = input('\nDESTINO CAMINHO JORNAL\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho:  ')
      jornal = ('\nxcopy "' + p_jorn +'\\"*.* "' + r_jorn + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_musica = input('ORIGEM CAMINHO MUSICA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\MUSICA\nDigite o caminho: ')
      r_musica = input('\nDESTINO CAMINHO MUSICA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\MUSICA\nDigite o caminho:  ')
      musica = ('\nxcopy "' + p_musica +'\\"*.* "' + r_musica + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_vinheta = input('ORIGEM CAMINHO VINHETA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\VINHETA\nDigite o caminho: ')
      r_vinheta = input('\nDESTINO CAMINHO VINHETA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\VINHETA\nDigite o caminho:  ')
      vinheta = ('\nxcopy "' + p_vinheta +'\\"*.* "' + r_vinheta + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_horacerta = input('ORIGEM CAMINHO HORA CERTA\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\HORA_CERTA\nDigite o caminho: ')
      r_horacerta = input('\nDESTINO CAMINHO HORA CERTA\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\HORA_CERTA\nDigite o caminho:  ')
      horacerta = ('\nxcopy "' + p_horacerta +'\\"*.* "' + r_horacerta + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_infor = input('ORIGEM CAMINHO INFORMATIVO\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\INFORMATIVO\nDigite o caminho: ')
      r_infor = input('\nDESTINO CAMINHO INFORMATIVO\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\INFORMATIVO\nDigite o caminho:  ')
      informativo = ('\nxcopy "' + p_infor +'\\"*.* "' + r_infor + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      p_grav = input('ORIGEM CAMINHO GRAVADOS\nExemplo: \\\\MAQUINAPRINCIPAL\\AUDIOS_PULSAR\\GRAVADOS\nDigite o caminho: ')
      r_grav = input('\nDESTINO CAMINHO GRAVADOS\nExemplo: D:\\PULSAR\\AUDIOS_PULSAR\\GRAVADOS\nDigite o caminho:  ')
      gravados = ('\nxcopy "' + p_grav +'\\"*.* "' + r_grav + '\\" /s /y /c /k /d \n')
      print('\n--------------------------------------------------------\n')

      print('echo --- GERANDO TRANSFERENCIA MYSQL ---\n')
      bd = ('\nnet stop mysql\nxcopy \\\\' + hp + '\mysql\data\\*.* C:\mysql\data\\ /s /y /c /k /d\nnet start mysql\n')

      sleep(2)
      
      items1 = list(range(0, 25))

      for item1 in progressBar1(items1, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

      print('\necho --- CONCLUIDO! ---\n')
      print('--------------------------------------------------------\n')

      print('\necho --- GERANDO ARQUIVO DE BACKUP SQL ---\n')
      pasw = input('SENHA DO BANCO DE DADOS PADRÃO ?\n1.PADRÃO\n2.OUTRA\n')
      if pasw == "1":
        print('--------------------------------------------------------\n')
        instancia_sql = input ("---------------INFORME A INSTANCIA DO SQL---------------\nExemplo: 0001\nDigite aqui: ")
        cod_station = input ("\n---------------INFORME O COD_STATION---------------\nExemplo: 1\nDigite aqui: ")
        bkp_pasta = input ("\nINFORME O NOME DA PASTA ONDE SERA GERADO O BACKUP\nOBSERVACAO: APENAS O NOME DA PASTA E COM A MESMA NOMENCLATURA NAS DUAS MAQUINAS (PRINCIPAL E RESERVA)\nDigite aqui: ")
        print('\n--------------------------------------------------------\n')
        sql_arqv = ('\nsqlcmd -S ' + hp + '\PULSARSQL -U sa -P pulsar -Q "BACKUP DATABASE [Pulsar Multimedia ('+instancia_sql+')] TO DISK='+ '\'' +'C:\Pulsar\\' + bkp_pasta + '\BASE_PADRAO.bak' + '\''  + 'WITH INIT"')
        print('\necho --- GERANDO COMANDO DE BACKUP SQL PADRAO ---\n')
        sql2_arqv = ('\nsqlcmd -S '+ hp +'\PULSARSQL -U sa -P pulsar -Q "BACKUP DATABASE [Pulsar Multimedia ('+instancia_sql+')] TO DISK='+ '\'' + 'C:\Pulsar\\' + bkp_pasta + '\BASE_PADRAO_%date:~-4,4%_%date:~-7,2%_%date:~-10,2%_%time:~0,2%_%time:~3,2%.bak'+'\'' + '"')
        
        print('echo --- GERANDO COMANDO PARA COPIAR BACKUP SQL VIA REDE ---\n')
        sql_copy = ('\nxcopy "\\\\'+ hp +'\Pulsar\\' + bkp_pasta + '\\"*.* "C:\Pulsar\\' + bkp_pasta + '\\" /s /y /c /k /d\n')
        sql_dell = ('\ndel \\\\'+ hp +'\Pulsar\\' + bkp_pasta + '\ /Q\n')
        forfile = ('\nforfiles /p "C:\Pulsar\\' + bkp_pasta + '" /s /m . /c "cmd /c DEL @path" /d -3')

        print('echo --- GERANDO COMANDO PARA RESTAURAR SQL SERVER  ---\n')
        restore = ('\nsqlcmd -S '+ hr +'\PULSARSQL -i  C:\Pulsar\script_pulsar\Restore-pulsar.sql -o  C:\Pulsar\script_pulsar\log\logSAIDA.txt')
        
        items = list(range(0, 25))

        for item in progressBar(items, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

        print('\necho --- CONCLUIDO! ---\n')
        print('--------------------------------------------------------\n')

        print('echo --- GERANDO ARQUIVO PARA RESTAURAR SQL ---\n')
        print('Qual a versão SQL que está sendo utilizada ?\n')
        versao_sql = input ('Versão SQL utilizada: 14 - 12\nDigite a versão do SQL: ')
        print("----------------------------------LOGIN (TRAFFIC)----------------------------------")
        login_sql = input ("\nLOGIN DO USUÁRIO PADRAO (SUPORTE): ")
        senha_sql = input ("\nSENHA DO USUÁRIO PADRAO (1 AO 6): ")
        print('\n---------------------------------------------------------------------------------\n')
        r2_vinheta = input ("Informe o endereço via rede das vinhetas (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\VINHETAS\nDigite o caminho: ")
        r2_jorn = input ("\nInforme o endereço via rede do jornal (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho: ")
        r2_com = input ("\nInforme o endereço via rede dos comerciais (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho: ")
        print('\n--------------------------------------------------------\n')
        linha_1 = ('USE master\n')
        linha_2 = ('\nALTER DATABASE [Pulsar Multimedia ('+instancia_sql+')] SET SINGLE_USER WITH ROLLBACK IMMEDIATE\n')
        linha_3 = ('\nRESTORE DATABASE [Pulsar Multimedia ('+instancia_sql+')]\n')
        linha_4 = ('\nFROM DISK = N\'C:\Pulsar\\'+bkp_pasta+'\\BASE_PADRAO.bak\' \n')
        linha_5 = ('\nWITH  FILE = 1,\n')
        linha_6 = ('\nMOVE N\'Pulsar Multimedia ('+instancia_sql+')\' TO N\'C:\Program Files\Microsoft SQL Server\MSSQL'+versao_sql+'.PULSARSQL\MSSQL\DATA\Pulsar Multimedia ('+instancia_sql+').mdf\',\n')
        linha_7 = ('\nMOVE N\'Pulsar Multimedia ('+instancia_sql+')_log\' TO N\'C:\Program Files\Microsoft SQL Server\MSSQL'+versao_sql+'.PULSARSQL\MSSQL\DATA\Pulsar Multimedia ('+instancia_sql+')_log.LDF\',\n')
        linha_8 = ('\nNOUNLOAD, RECOVERY, CONTINUE_AFTER_ERROR, REPLACE, STATS = 5;\n')
        linha_9 = ('\nALTER DATABASE [Pulsar Multimedia ('+instancia_sql+')]SET MULTI_USER\n')
        linha_10 = ('\nuse [Pulsar Multimedia ('+instancia_sql+')]  EXEC sp_change_users_login \'report\';\n')
        linha_11 = ('\nuse [Pulsar Multimedia ('+instancia_sql+')]  EXEC sp_change_users_login '+'\'Auto_fix'+'\', \''+login_sql+'\', NULL, \''+senha_sql+'\'; \n')
        linha_12 = ('\nUPDATE TOP(1) commercial_stations SET ')
        linha_13 = ('\nDirectory_7=\''+r2_vinheta+'\\\',\n')
        linha_14 = ('\nDirectory_8=\''+r2_jorn+'\\\',\n')
        linha_15 = ('\nDirectory_14=\''+r2_com+'\\\',\n')
        linha_16 = ('\nEnable_Use_Setup_Traffic = 1 WHERE Cod_Station = \''+ cod_station + '\';')
        
        items = list(range(0, 25))

        for item in progressBar(items, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

        print('\necho --- CONCLUIDO! ---\n')
        print('--------------------------------------------------------\n')

        finalizar = input('Finalizar programa ?\n1. Finalizar\n2. Reiniciar\n')
        if finalizar == '1':
            verifica_pasta = os.path.exists('C:\Pulsar\script_pulsar')
            if verifica_pasta == True:
                sys.stdout = open("C:\Pulsar\script_pulsar\BACKUP_PULSAR.bat", "w")
                print(comercial,
                jornal,
                musica,
                vinheta,
                horacerta,
                informativo,
                gravados,
                bd,
                sql_arqv,
                sql2_arqv,
                sql_copy,
                sql_dell,
                forfile,
                restore)
    
                sys.stdout = open("C:\Pulsar\script_pulsar\RESTORE-PULSAR.sql", "w")
                print(linha_1, linha_2, linha_3,linha_4, linha_5, linha_6, linha_7, linha_8, linha_9, linha_10, linha_11, linha_12, linha_13, linha_14, linha_15, linha_16)
                final = 1
        if finalizar == '2':
            print('Aguarde!')
            sleep(2)
            continue

      if pasw == "2":
        print('--------------------------------------------------------\n')
        snh = input('DIGITE A SENHA: ')
        instancia_sql = input ("\n---------------INFORME A INSTANCIA DO SQL---------------\nExemplo: 0001\nDigite aqui: ")
        cod_station = input ("\n---------------INFORME O COD_STATION---------------\nExemplo: 1\nDigite aqui: ")
        bkp_pasta = input ("\nINFORME O NOME DA PASTA ONDE SERA GERADO O BACKUP\nOBSERVACAO: APENAS O NOME DA PASTA E COM A MESMA NOMENCLATURA NAS DUAS MAQUINAS (PRINCIPAL E RESERVA)\nDigite aqui: ")
        sql_arqv = ('\nsqlcmd -S ' + hp + '\PULSARSQL -U sa -P '+ snh +' -Q "BACKUP DATABASE [Pulsar Multimedia ('+instancia_sql+')] TO DISK='+ '\'' +'C:\Pulsar\\' + bkp_pasta + '\BASE_PADRAO.bak'+ '\'' +' WITH INIT"')
        print('\necho --- GERANDO ARQUIVO DE BKP SQL COMUM ---\n')
        sql2_arqv = ('\nsqlcmd -S '+ hp +'\PULSARSQL -U sa -P '+ snh + ' -Q "BACKUP DATABASE [Pulsar Multimedia ('+instancia_sql+')] TO DISK='+ '\'' + 'C:\Pulsar\\' + bkp_pasta + '\BASE_PADRAO_%date:~-4,4%_%date:~-7,2%_%date:~-10,2%_%time:~0,2%_%time:~3,2%.bak'+'\'' + '"')

        print('echo --- COPIANDO BKP SQL VIA REDE ---\n')
        sql_copy = ('\nxcopy "\\\\'+ hp +'\Pulsar\\' + bkp_pasta + '\\"*.* "C:\Pulsar\\' + bkp_pasta + '\\" /s /y /c /k /d\n')
        sql_dell = ('\ndel \\\\'+ hp +'\Pulsar\\' + bkp_pasta + '\ /Q\n')
        forfile = ('\nforfiles /p "C:\Pulsar\\' + bkp_pasta + '" /s /m . /c "cmd /c DEL @path" /d -3')

        print('echo --- RESTAURANDO O BANCO SQL SERVER  ---\n')
        restore = ('\nsqlcmd -S '+ hr +'\PULSARSQL -i  C:\Pulsar\script_pulsar\Restore-pulsar.sql -o  C:\Pulsar\script_pulsar\log\logSAIDA.txt')

        sleep(1)

        items = list(range(0, 25))

        for item in progressBar(items, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

        print('\necho --- CONCLUIDO! ---\n')
        print('--------------------------------------------------------\n')

        print('echo --- GERANDO ARQUIVO PARA RESTAURAR SQL ---\n')
        print('Qual a versão SQL que está sendo utilizada ?\n')
        versao_sql = input ('Versão SQL utilizada: 14 - 12\nDigite a versão do SQL: ')
        print("----------------------------------LOGIN (TRAFFIC)----------------------------------")
        login_sql = input ("\nLOGIN DO USUÁRIO PADRAO (SUPORTE): ")
        senha_sql = input ("\nSENHA DO USUÁRIO PADRAO (1 AO 6): ")
        print('\n---------------------------------------------------------------------------------\n')
        r2_vinheta = input ("Informe o endereço via rede das vinhetas (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\VINHETAS\nDigite o caminho: ")
        r2_jorn = input ("\nInforme o endereço via rede do jornal (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\JORNAL\nDigite o caminho: ")
        r2_com = input ("\nInforme o endereço via rede dos comerciais (Maquina reserva)\nExemplo: \\\\"+ hr + "\PULSAR\\AUDIOS_PULSAR\\COMERCIAL\nDigite o caminho: ")
        print('\n--------------------------------------------------------\n')
        linha_1 = ('USE master\n')
        linha_2 = ('\nALTER DATABASE [Pulsar Multimedia ('+instancia_sql+')] SET SINGLE_USER WITH ROLLBACK IMMEDIATE\n')
        linha_3 = ('\nRESTORE DATABASE [Pulsar Multimedia ('+instancia_sql+')]\n')
        linha_4 = ('\nFROM DISK = N\'C:\Pulsar\\'+bkp_pasta+'\\BASE_PADRAO.bak\' \n')
        linha_5 = ('\nWITH  FILE = 1,\n')
        linha_6 = ('\nMOVE N\'Pulsar Multimedia ('+instancia_sql+')\' TO N\'C:\Program Files\Microsoft SQL Server\MSSQL'+versao_sql+'.PULSARSQL\MSSQL\DATA\Pulsar Multimedia ('+instancia_sql+').mdf\',\n')
        linha_7 = ('\nMOVE N\'Pulsar Multimedia ('+instancia_sql+')_log\' TO N\'C:\Program Files\Microsoft SQL Server\MSSQL'+versao_sql+'.PULSARSQL\MSSQL\DATA\Pulsar Multimedia ('+instancia_sql+')_log.LDF\',\n')
        linha_8 = ('\nNOUNLOAD, RECOVERY, CONTINUE_AFTER_ERROR, REPLACE, STATS = 5;\n')
        linha_9 = ('\nALTER DATABASE [Pulsar Multimedia ('+instancia_sql+')]SET MULTI_USER\n')
        linha_10 = ('\nuse [Pulsar Multimedia ('+instancia_sql+')]  EXEC sp_change_users_login \'report\';\n')
        linha_11 = ('\nuse [Pulsar Multimedia ('+instancia_sql+')]  EXEC sp_change_users_login '+'\'Auto_fix'+'\', \''+login_sql+'\', NULL, \''+senha_sql+'\'; \n')
        linha_12 = ('\nUPDATE TOP(1) commercial_stations SET\n')
        linha_13 = ('\nDirectory_7=\''+r2_vinheta+'\\\',\n')
        linha_14 = ('\nDirectory_8=\''+r2_jorn+'\\\',\n')
        linha_15 = ('\nDirectory_14=\''+r2_com+'\\\',\n')
        linha_16 = ('\nEnable_Use_Setup_Traffic = 1 WHERE Cod_Station = \''+ cod_station + '\';')

        sleep(2)
        
        items = list(range(0, 25))

        for item in progressBar(items, prefix = 'Progresso:', suffix = 'Completo', length = 30):
          time.sleep(0.1)

        print('\necho --- CONCLUIDO! ---\n')
        print('--------------------------------------------------------\n')
        
        finalizar = input('Finalizar programa ?\n1. Finalizar\n2. Reiniciar\n')
        if finalizar == '1':
            verifica_pasta = os.path.exists('C:\Pulsar\script_pulsar')
            if verifica_pasta == True:
                sys.stdout = open("C:\Pulsar\script_pulsar\BACKUP_PULSAR.bat", "w")
                print(comercial,
                jornal,
                musica,
                vinheta,
                horacerta,
                informativo,
                gravados,
                bd,
                sql_arqv,
                sql2_arqv,
                sql_copy,
                sql_dell,
                forfile,
                restore)
    
                sys.stdout = open("C:\Pulsar\script_pulsar\RESTORE-PULSAR.sql", "w")
                print(linha_1, linha_2, linha_3,linha_4, linha_5, linha_6, linha_7, linha_8, linha_9, linha_10, linha_11, linha_12, linha_13, linha_14, linha_15, linha_16)
                final = 1
        if finalizar == '2':
            print('Aguarde!')
            sleep(2)
            continue

    if local == '3':
      print('Finalizando!')
      sleep(1)
      exit()
    verifica_pastaLog = os.path.exists('C:\Pulsar\script_pulsar\log')
    if verifica_pastaLog == False:
        directory = "log"
  
  
        parent_dir = "C:\Pulsar\script_pulsar\\"

        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        sys.stdout.close()
    if verifica_pastaLog == True:
        sleep(1)
        exit()
