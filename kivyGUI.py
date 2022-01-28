from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import pickle
import webbrowser as wb


def generar_nombres():
    nombres = [
        'Marcos', 'Ignacio', 'Alfonso', 'Jordi', 'Ricardo', 'Salvador',
        'Hugo', 'Emilio', 'Guillermo', 'Gabriel', 'Marcos', 'Julio',
        'Julián', 'Gonzalo', 'José Miguel', 'Tomás', 'Agustín', 'Martín',
        'José Ramón', 'Nicolás', 'Félix', 'Joan', 'Ismael', 'Cristian',
        'Samuel', 'Héctor', 'Juan Francisco', 'José', 'Mariano', 'Lucas',
        'José Carlos', 'Domingo', 'Sebastián', 'Alfredo', 'Álex', 'César',
        'Felipe', 'Víctor', 'Rodrigo', 'Gregorio', 'Alberto', 'Kaworu',
        'Sonia', 'Sandra', 'Marina', 'Susana', 'Natalia', 'Yolanda',
        'Margarita', 'Claudia', 'Eva', 'Carla', 'Esther', 'Phoebe',
        'Sofía', 'Noelia', 'Verónica', 'Carolina', 'Miriam', 'Inés',
        'Belén', 'Daniela', 'Martina', 'Mai', 'Thais']

    apellidos = [
        'González', 'Rodríguez', 'Fernández', 'Díaz', 'Pérez', 'Gómez',
        'Lucero', 'Sosa', 'Quiroga', 'Martínez', 'López', 'Romero',
        'Sánchez', 'Ruiz', 'Benítez', 'Silva', 'Flores', 'García',
        'Muñoz', 'Rojas', 'Soto', 'Contreras', 'Sepúlveda', 'Morales',
        'Fuentes', 'Hernández', 'Torres', 'Araya', 'Flores', 'Espinoza',
        'Valenzuela', 'Castillo', 'Tapia', 'Reyes', 'Gutiérrez', 'Castro',
        'Pizarro', 'Álvarez', 'Carrasco', 'Cortés', 'Herrera', 'Núñez',
        'Jara', 'Vergara', 'Rivera', 'Figueroa', 'Riquelme', 'Miranda',
        'Bravo', 'Vera', 'Molina', 'Vega', 'Campos', 'Sandoval',
        'Orellana', 'Cárdenas', 'Olivares', 'Alarcón', 'Gallardo',
        'Ortiz', 'Garrido', 'Salazar', 'Guzmán', 'Saavedra', 'Navarro',
        'Aguilera', 'Parra', 'Romero', 'Aravena', 'Vargas', 'Cáceres',
        'Yáñez', 'Leiva', 'Escobar', 'Valdés', 'Vidal', 'Salinas',
        'Zúñiga', 'Peña', 'Godoy', 'Lagos', 'Maldonado', 'Bustos',
        'Medina', 'Palma', 'Pino', 'Moreno', 'Sanhueza', 'Carvajal',
        'Navarrete', 'Sáez', 'Alvarado', 'Donoso', 'Poblete', 'Bustamante',
        'Toro', 'Ortega', 'Venegas', 'Guerrero', 'Mendoza', 'Farías',
        'San Martín']
    lista_nombres = []

    for i in range(9):
        lista_nombres.append(
            random.choice(nombres) +
            ' ' + random.choice(apellidos)
            )
    return lista_nombres


try:
    open('horarios.pickle', 'xb')
    load_data = open('horarios.pickle', 'rb')
    print('horarios.pickle no existe. Creando horarios.pickle')

except:
    load_data = open('horarios.pickle', 'rb')
    print('horarios.pickle existe. load_data = horarios.pickle')

try:
    previousinfo = pickle.load(load_data)
    sectores = previousinfo

except:
    sectores = {}
    archivo2 = open("sectores.txt", "r", encoding="utf-8")
    for linea in archivo2:
        ll = linea.split(", ")
        sectores[ll[0]] = [
            [ll[1], [generar_nombres()[0], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                }], [
                generar_nombres()[1], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                }], [
                generar_nombres()[2], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                }]],
            [ll[2], [
                generar_nombres()[3], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                }], [
                generar_nombres()[4], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                    }], [
                generar_nombres()[5], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                    }]],
            [ll[3][:-1], [
                generar_nombres()[6], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                    }], [
                generar_nombres()[7], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                    }], [
                generar_nombres()[8], {
                    "09:00": True, "10:00": True, "11:00": True,
                    "12:00": True, "13:00": True, "14:00": True,
                    "15:00": True, "16:00": True, "17:00": True,
                    "18:00": True, "19:00": True, "20:00": True
                    }]]]
    archivo2.close()

archivo_r = open("datos.txt", "r", encoding="utf-8")
usuarios = {}
for linea in archivo_r:
    if linea != "":
        datos = linea.split(", ")
        datos[3] = datos[3][:-1]
        usuarios[datos[1]] = [datos[0], datos[2], datos[3]]
archivo_r.close()

# links de informacion
link1 = "https://www.who.int/es/news-room/questions-and-answers/item/coronavirus-disease-covid-19-pregnancy-and-childbirth"
link2 = "https://www.mayoclinic.org/es-es/should-pregnant-women-be-vaccinated-for-covid-19/vid-20511503"
link3 = "https://www.unicef.org/es/coronavirus/consejos-para-embarazo-durante-pandemia-coronavirus-covid19"


# Función para crear un numero aleatorio


def espera():
    numero = random.randint(1, 10)
    return numero


variable1 = espera()


# Creando las ventanas


class Win1(Screen):
    def verificar(self):
        self.data_n = self.ids.nombre.text
        self.data_r = self.ids.rut.text

        if self.data_r in usuarios:
            self.manager.current = "win2"
        else:
            self.ids.rut.hint_text = "Rut incorrecto"
            self.ids.val_reg.text = 'Registrese'
            self.ids.rut.text = ""


class WinLogin(Screen):
    def registrarse(self):
        self.data_n = self.ids.nombrer.text
        self.data_r = self.ids.rutr.text
        self.data_g = self.ids.gmailr.text
        self.data_f = self.ids.fonasa
        archivo_w = open("datos.txt", "a+", encoding="utf-8")
        if self.data_f.text == "Si":
            if self.data_n and self.data_r and self.data_g != "":
                if "-" in self.data_r and len(self.data_r) == 10:
                    if "@" in self.data_g and self.data_g.count("@") == 1:
                        if self.data_r in usuarios:
                            self.ids.rutr.text = ""
                            self.ids.rutr.hint_text = "Este rut ya \
                                                        esta registrado"
                        else:
                            self.datos = {
                                "nombre": self.data_n,
                                "rut": self.data_r,
                                "correo": self.data_g
                                }
                            archivo_w.write(self.data_n + ", " +
                                            self.data_r + ", " +
                                            self.data_g + ", " +
                                            "Tiene fonasa" + "\n")
                            usuarios[self.data_r] = [
                                self.data_n,
                                self.data_g,
                                "Tiene Fonasa"
                                ]
                            self.manager.current = "win1"
                    else:
                        self.ids.gmailr.text = ""
                        self.ids.gmailr.hint_text = (
                            "Correo invalido asegurese" +
                            "que este bien escrito"
                            )
                else:
                    self.ids.rutr.text = ""
                    self.ids.rutr.hint_text = (
                        "Rut invalido " +
                        "escribalo sin" +
                        "puntos y con guión"
                        )
        elif self.data_f.text == "No":
            if self.data_n and self.data_r and self.data_g != "":
                if "-" in self.data_r and len(self.data_r) == 10:
                    if "@" in self.data_g and self.data_g.count("@") == 1:
                        if self.data_r in usuarios:
                            self.ids.rutr.text = ""
                            self.ids.rutr.hint_text = (
                                "Este rut ya" +
                                " esta registrado"
                                )
                        else:
                            self.datos = {
                                "nombre": self.data_n,
                                "rut": self.data_r,
                                "correo": self.data_g
                                }
                            archivo_w.write(
                                self.data_n + ", " +
                                self.data_r + ", " +
                                self.data_g + ", " +
                                "Tiene fonasa" + "\n"
                                )
                            usuarios[self.data_r] = [
                                self.data_n,
                                self.data_g,
                                "Tiene Fonasa"
                                ]
                            self.manager.current = "win1"
                    else:
                        self.ids.gmailr.text = ""
                        self.ids.gmailr.hint_text = (
                            "Correo invalido asegurese" +
                            "que este bien escrito"
                            )
                else:
                    self.ids.rutr.text = ""
                    self.ids.rutr.hint_text = (
                        "Rut invalido " +
                        "escribalo sin puntos y con guión"
                        )
        elif self.data_f.text == "¿Esta en fonasa?":
            self.data_f.text = "Seleccione una opción"
        archivo_w.close()


class Win2(Screen):
    lugares = ["Santiago Centro", "Maipú", "La Florida", "Cerro Navia",
               "San Bernardo", "Quinta Normal", "Providencia",
               "Ñuñoa", "La Pintana", "La Cisterna", "El Bosque",
               "Quilicura", "San Miguel", "La Granja"]

    def cargar_direcciones(self):
        self.data_s = self.ids.spinner1.text
        self.ids.spinner2.values = ["1.- " + sectores[self.data_s][0][0],
                                    "2.- " + sectores[self.data_s][1][0],
                                    "3.- " + sectores[self.data_s][2][0]
                                    ]

    def boton_habilitar(self, dt):
        self.boton_v3 = self.manager.get_screen("win3").ids.sgte_v3
        self.boton_v3.disabled = False

    def habilitar(self):
        self.data_d = self.ids.spinner2.text
        if self.data_s != "Sector" and self.data_d != "Direcciones":
            self.manager.current = "win2_1"
            Clock.schedule_once(self.boton_habilitar, variable1)


class Win2_1(Screen):
    horas = ["09:00", "10:00", "11:00",
             "12:00", "13:00", "14:00",
             "15:00", "16:00", "17:00",
             "18:00", "19:00", "20:00"]

    def cargar_especialistas(self):
        self.data_s = self.manager.get_screen("win2").data_s
        self.data_d = self.manager.get_screen("win2").data_d
        if "1.- " in self.data_d:
            self.direccion = sectores[self.data_s][0][0]
            self.especialista = 0
            self.ids.spinner4.values = [
                "1.- " + sectores[self.data_s][0][1][0],
                "2.- " + sectores[self.data_s][0][2][0],
                "3.- " + sectores[self.data_s][0][3][0]
                ]
        elif "2.- " in self.data_d:
            self.direccion = sectores[self.data_s][1][0]
            self.especialista = 1
            self.ids.spinner4.values = [
                "1.- " + sectores[self.data_s][1][1][0],
                "2.- " + sectores[self.data_s][1][2][0],
                "3.- " + sectores[self.data_s][1][3][0]
                ]
        elif "3.- " in self.data_d:
            self.direccion = sectores[self.data_s][2][0]
            self.especialista = 2
            self.ids.spinner4.values = [
                "1.- " + sectores[self.data_s][2][1][0],
                "2.- " + sectores[self.data_s][2][2][0],
                "3.- " + sectores[self.data_s][2][3][0]
                ]

    def cambiar_pag(self, dt):
        self.manager.current = "win3"

    def verificar_hora(self):
        self.data_s = self.manager.get_screen("win2").data_s
        self.data_e = self.ids.spinner4.text
        self.data_h = self.ids.spinner3.text
        if "1.- " in self.data_e:
            if sectores[self.data_s][self.especialista][1][
                        1][self.data_h]:
                self.ids.confirmacion.text = "Hora disponible"
                Clock.schedule_once(self.cambiar_pag, 2)
            elif not sectores[self.data_s][self.especialista][
                                1][1][self.data_h]:
                    self.ids.confirmacion.text = "Hora no disponible"
        elif "2.- " in self.data_e:
            if sectores[self.data_s][self.especialista][
                        2][1][self.data_h]:
                self.ids.confirmacion.text = "Hora disponible"
                Clock.schedule_once(self.cambiar_pag, 2)
            elif not sectores[self.data_s][self.especialista][
                                2][1][self.data_h]:
                self.ids.confirmacion.text = "Hora no disponible"
        elif "3.- " in self.data_e:
            if sectores[self.data_s][self.especialista][3][1][self.data_h]:
                self.ids.confirmacion.text = "Hora disponible"
                Clock.schedule_once(self.cambiar_pag, 2)
            elif not sectores[self.data_s][self.especialista][
                                3][1][self.data_h]:
                self.ids.confirmacion.text = "Hora no disponible"


class Win3(Screen):
    def cambiar_texto(self):
        self.data_n = self.manager.get_screen("win1").data_n
        self.data_s = self.manager.get_screen("win2").data_s
        self.direccion = self.manager.get_screen("win2_1").direccion
        self.hora = self.manager.get_screen("win2_1").ids.spinner3.text
        self.medico = self.manager.get_screen("win2_1").ids.spinner4.text
        self.data_l = self.manager.get_screen("win4").ids.lugar

        self.data_l.text = (
            f"Srta {self.data_n} su hora esta disponible" +
            f" en: \n{self.direccion} a las " +
            f"{self.hora} con {self.medico[4:]}"
            )

    def abrir_link1(self):
        wb.open(link1)

    def abrir_link2(self):
        wb.open(link2)

    def abrir_link3(self):
        wb.open(link3)


class Win4(Screen):
    def ocupar_hora(self):
        self.data_s = self.manager.get_screen("win2").data_s
        self.data_e = self.manager.get_screen("win2_1").data_e
        self.data_h = self.manager.get_screen("win2_1").data_h
        self.especialista = self.manager.get_screen("win2_1").especialista

        if "1.- " in self.data_e:
            if sectores[self.data_s][self.especialista][1][1][self.data_h]:
                sectores[self.data_s][self.especialista][
                            1][1][self.data_h] = False
        elif "2.- " in self.data_e:
            if sectores[self.data_s][self.especialista][2][1][self.data_h]:
                sectores[self.data_s][self.especialista][
                            2][1][self.data_h] = False
        elif "3.- " in self.data_e:
            if sectores[self.data_s][self.especialista][3][1][self.data_h]:
                sectores[self.data_s][self.especialista][
                            3][1][self.data_h] = False


class Win5(Screen):
    def opinion(self):
        self.text_opinion = self.ids.write_r.text
        archive = open("reseñas.txt", "a+", encoding="utf-8")
        info_opinion = {"opinion": self.text_opinion}
        self.data_s = self.manager.get_screen("win2").data_s
        if info_opinion["opinion"] != "":
            archive.write(f"Una Usuaria de {self.data_s} comentó: \n" +
                            info_opinion["opinion"] + "\n\n")
            archive.close()
        self.ids.write_r.text = ''


class Win6(Screen):
    
    

    def load_review(self):
        review = open("reseñas.txt", "r", encoding="utf-8")
        self.ids.view_r.text = review.read()
        review.close()


class WinManager(ScreenManager):
    # para cerrar con el boton salir en comentarios

    def save_info(self):
        newsave = open('horarios.pickle', 'wb')
        pickle.dump(sectores, newsave)
        newsave.close()


# Permite hacer andar la app


class MainApp(App):
    title = "Pou"
    icon = "pou.png"

    def build(self):
        return WinManager()


if __name__ == '__main__':
    MainApp().run()
    # para cerrar con el boton x
    newsave = open('horarios.pickle', 'wb')
    pickle.dump(sectores, newsave)
    newsave.close()
