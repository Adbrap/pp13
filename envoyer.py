def envoie_ticker():
    # Informations de connexion FTP
    ftp_host = 'ftp.cluster030.hosting.ovh.net'
    ftp_user = 'abtrado'
    ftp_password = '4a9dFrYgfrSB'

    # Connexion au serveur FTP
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_password)

    # Envoi du fichier "mots.txt" vers le serveur FTP
    with open('mots.txt', 'rb') as file:
        ftp.storbinary('STOR mots.txt', file)

    # Fermeture de la connexion FTP
    ftp.quit()

# Exemple d'utilisation de la fonction
envoie_ticker()
