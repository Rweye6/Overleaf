import os.path

DOSSIERS = os.listdir("/home/rweye/Nextcloud/Documents/Overleaf/2GT/")
fichiers = []
dossier = ""
mot=".tex"
for j in range(len(DOSSIERS)):
     os.chdir("/home/rweye/Nextcloud/Documents/Overleaf/2GT/"+DOSSIERS[j])
     dossier = os.listdir("/home/rweye/Nextcloud/Documents/Overleaf/2GT/"+DOSSIERS[j])
     for i in range(len(dossier)):
          if dossier[i].find(mot) > 0 :
               fichiers.append(dossier[i])
               print(dossier[i])
               #if os.path.exists(file):
               #     os.remove(file)
               #fichier = open(fichiers[i],"x")
               #fichier.write(container)
               #fichier.close()
               ###Compilation ###
               instructions = "pdflatex "+dossier[i]
               os.system(instructions)
               #readpdf = "START "+dossier[i][:-4]+".pdf"
               #os.system(readpdf)
     print(len(fichiers))
     fichiers = []