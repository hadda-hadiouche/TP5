
from xml.dom.minidom import parse
import xml.dom.minidom


class model:
    def __init__(self):
        self.numAdmis = 0
        self.numDettes = 0
        self.numAjour = 0
        self.listEtudiant = []
        self.listMoyenne = []

    def getEudiantsInfo(self):
        DOMTree = xml.dom.minidom.parse("D:/tpMTI/tp5/trv/Etudiants.xml")
        Etudiants = DOMTree.documentElement
        EtudiantList = Etudiants.getElementsByTagName("Etudiant")
        for Etudiant in EtudiantList:
            etudiantTab = []

            nom = Etudiant.getElementsByTagName('nom')[0]
            etudiantTab.append(nom.childNodes[0].data)
            prenom = Etudiant.getElementsByTagName('prenom')[0]
            etudiantTab.append(prenom.childNodes[0].data)
            matricule = Etudiant.getElementsByTagName('matricule')[0]
            etudiantTab.append(matricule.childNodes[0].data)
            moyenneS1 = Etudiant.getElementsByTagName('moyenneS1')[0]
            etudiantTab.append(moyenneS1.childNodes[0].data)
            moyenneS2 = Etudiant.getElementsByTagName('moyenneS2')[0]
            etudiantTab.append(moyenneS2.childNodes[0].data)
            moy = (float(moyenneS1.childNodes[0].data) + float(moyenneS2.childNodes[0].data)) / 2
            self.listMoyenne.append(moy)
            etudiantTab.append(moy)
            credit = Etudiant.getElementsByTagName('credit')[0]
            cred = credit.childNodes[0].data
            etudiantTab.append(cred)
            if moy >= 10:
                self.numAdmis = self.numAdmis + 1
                etudiantTab.append("Admis")
            elif float(cred) >= 40:
                self.numDettes = self.numDettes + 1
                etudiantTab.append("Admis avec dettes")
            else:
                self.numAjour = self.numAjour + 1
                etudiantTab.append("Ajournee")

            self.listEtudiant.append(etudiantTab)

        return self.listEtudiant

    def getStatistiques(self):
        return (
        max(self.listMoyenne), min(self.listMoyenne), self.numAdmis, self.numDettes, self.numAjour, self.listMoyenne.__len__())


class view:
    def __init__(self, ):
        pass

    def showEtudiantInfo(self, etudiants):
        for etududian in etudiants:
            print(etududian[0], "\t**", etududian[1], "\t**", etududian[2], "\t**", etududian[3], "\t**", etududian[4],
                  "\t**", etududian[5], "\t**", etududian[6], "\t**", etududian[7])
            print("***************************************************************************************")

    def showStatistiques(self, meilMoy, mauvMoy, numAdmis, numDettes, numAjour, listMoyLen):
        print("\n\n** La meilleure moyenne est :  " + str(meilMoy))
        print("** mauvaise moyenne est :  " + str(mauvMoy))
        print("** Le nombre des etudiants Admis :  " + str(numAdmis))
        print("** Le nombre des etudiants Admis avec dettes :  " + str(numDettes))
        print("** Le nombre des etudiants  ajournee :  " + str(numAjour))


class controleur:
    def __init__(self):
        """ constructeur du controleur """
        # initialiser le model de donnees
        self.data_model = model()
        self.affichage = view()

    def show(self):
        EtudList = self.data_model.getEudiantsInfo()
        self.affichage.showEtudiantInfo(EtudList)

        meilMoy, mauvaMoy, numAdmis, numDettes, numAjour, listMoyLen = self.data_model.getStatistiques()
        self.affichage.showStatistiques(meilMoy, mauvaMoy, numAdmis, numDettes, numAjour, listMoyLen)


if __name__ == '__main__':
    contro = controleur()
    contro.show()
