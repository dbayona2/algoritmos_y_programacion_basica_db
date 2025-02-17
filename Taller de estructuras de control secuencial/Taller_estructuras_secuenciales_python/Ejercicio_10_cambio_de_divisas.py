#Entrada_chelines
chelines=int(input("Increse la cantidad de chelines: "))
#Caja_Negra_Chelines
cambiochelinesapesetas=(956.871/100)
chelinesapesetas=(cambiochelinesapesetas*chelines)
#Salida_chelines
print(chelines, "Chelines ", "equivalen a", chelinesapesetas, "pesetas ")
#entradas de Dracmas Griegos a Francos Franceses
Dracmas= int(input("Ingrese la cantidad de Dracmas Griegos: "))
#Caja_negra_de_Dracmas_Griegos_a_Francos_Franceses
CambioDracmaaPesetas = (88.607/100)
CambioPesetasaFrancoF = (1/20.11)
DracmasaFrancoF = (((Dracmas*CambioDracmaaPesetas))*CambioPesetasaFrancoF)
#Salida_de_Dracmas_Griegos_a_Francos_Franceses
print(Dracmas, " Dracmas Griegos", " equivalen a ", DracmasaFrancoF, "francos franceses ")
#Entradas_de_Pesetas_a_Dolar_EUU_y_Liras_Italianas
pesetas=int(input("Ingrese la cantidad de Pesetas: "))
#Caja_negra_Pesetas_a_Dolar_EEUU_y_Lira_Italiana
CambioDolaraPeseta = (1/122.499)
CambioLiraIaPeseta = (100/9.289)
PesetaaDolar = (pesetas*CambioDolaraPeseta)
PesetaaLiraI = (pesetas*CambioLiraIaPeseta)
#Salida_de_Peseta_a_Dolar_EUU_y_Lira_Italiana
print(pesetas, " Pesetas", " equivalen a ", PesetaaDolar, " dolares EEUU y ", PesetaaLiraI, " libras italianas. ")