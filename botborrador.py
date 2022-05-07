import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bs4 import BeautifulSoup
import requests
import webbrowser

token = "..."


def inicio(bot, update):
    try:
        username = update.message.from_user.username
        message = "Hola, conoce los /comandos " + username
        update.message.reply_text(message)
    except Exception as error:
        print("Error 001 {}".format(error.args[0]))


def echo(bot, update):
    try:
        text = update.message.text
        update.message.reply_text(text)
    except Exception as error:
        print("Error 004 {}".format(error.args[0]))


def ayuda(bot, update):
    try:
        message = "Puedes enviar texto o imágenes, o ver los /comandos"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 005 {}".format(error.args[0]))


def error(bot, update, error):
    try:
        print(error)
    except Exception as e:
        print("Error 006 {}".format(e.args[0]))


def comandos(bot, update):
    try:
        message = "Los comandos, a la fecha, son: \n \n /cesados - archivos excel de campañas anteriores, por empresa \n \n /drive - acceso al drive de google, por empresa\n \n /firma - descargar mi firma personal para agregar a documentos en formato pdf \n \n /hortifrut - enlaces de trabajo \n \n /personal - acceso a enlaces personales \n \n /pltc - precio del litecoin \n \n /semanas - nos nuestra el calendario semanal del 2022 \n \n /wkp - wikipedia en español\n \n /youtube - enlace a youtube"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 007 {}".format(error.args[0]))


def ltc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/litecoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text
    return format_result
def pltc(bot, update):
    try:
        message = f'El precio actual del litecoin es de {ltc_scraping()}'
        update.message.reply_text(message)
    except Exception as e:
        print("Error 008 {}".format(e.args[0]))


def bcr_scraping():
    url = requests.get('https://www.bcrp.gob.pe')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('Mínimo')
    format_result = result.string
    return format_result
def tcc(bot, update):
    try:
        message = f'El tipo de cambio actual es de {bcr_scraping()}'
        update.message.reply_text(message)
    except Exception as e:
        print("Error 009 {}".format(e.args[0]))


def getImage(bot, update):
    try:
        message = "Recibiendo imagen"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id

        filename = os.path.join("descargas/", "{}.jpg".format(id))
        file.download(filename)

        message = "Imagen guardada"
        update.message.reply_text(message)

    except Exception as e:
        print("Error 010 {}".format(e.args[0]))

def wkp(bot, update):
    try:
        message = "Abrir wikipedia en https://es.wikipedia.org/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 011 {}".format(error.args[0]))


def hortifrut(bot, update):
    try:
        message = "------------------------------------------------- \n Páginas de trabajo en HF Perú: \n \n /acs - asignación de correlativos de Semillero, registro \n https://docs.google.com/spreadsheets/d/1Q3aXycc0_J9o7jgIi-y5Mu7wicJZS-PGBEem6Nb_TzQ/edit?pli=1#gid=714979526/ \n \n /bc - berry connect \n http://berryconnect.com/ \n \n" \
                  "/pa - Perú activos, registro (drive)\nhttps://docs.google.com/spreadsheets/d/1d_fbDybgwjY4tLqRhsCkX-NcPrplw6V8l1ufhcWNAxI/edit?pli=1#gid=537944161 \n \n /pc - Perú cesados, registro (drive) https://docs.google.com/spreadsheets/d/1iszsaE4NgniBP-gghQ2V2a4iXP3f-oPLTFnL80FM20c/edit#gid=416158579\n \n /rec - recepción de documentos, registro (drive) https://docs.google.com/spreadsheets/d/10u8Vf9sEFsnJxlOuu0PPATJfO22jFA08EhyTAGAadHQ/edit#gid=0 \n \n " \
                  "/req - requerimientos, registro (drive) https://docs.google.com/spreadsheets/d/1EpiS3v4-b02iR6OJsq5VysEJBKvJMz4Q0K6RdMQfWIQ/edit#gid=0 \n \n /rhsys - rhsys XD \n http://hortifrut.rhsys.pe/ \n \n /tct - Tal cesados, registro https://docs.google.com/spreadsheets/d/1Swh9BgcDjBJXEVV0SXwqBzY_b9a8CWUGfYK88IlMGag/edit#gid=853588120 \n \n /ti - acceso a Easy \n IT https://easyit-hortifrut.refined.site/ \n \n ------------------------------------------------- \n Fotochecks: \n \n /f41416408 - fotocheck de Jorge https://photos.google.com/photo/AF1QipMlZPYkYqwqqjfaLgVTV3dkX4iPgwCMg1SvGrom \n \n /f76794134 - fotocheck de Marlit https://photos.google.com/photo/AF1QipO-7iRroEZqGpjL6hbnpMALuGhop1APbjOJEf1n \n \n ------------------------------------------------- \n Correo institucional: \n /outlook - https://outlook.office365.com/mail \n \n ------------------------------------------------- \n Canales de comunicación: \n \n Canal de denuncias: \n 080018172 \n \n Hortifrut en línea (trámites, consultas): \n 080071199 \n \n Whatsapp: \n 992890000 \n"

        update.message.reply_text(message)
    except Exception as error:
        print("Error 012 {}".format(error.args[0]))

def scrap_req():
        paginay = webbrowser.open('https://docs.google.com/spreadsheets/d/1EpiS3v4-b02iR6OJsq5VysEJBKvJMz4Q0K6RdMQfWIQ/edit#gid=0')
        return (paginay)
def req(bot, update):
    try:
        message = {scrap_req()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 013 {}".format(e.args[0]))

def scrap_pc():
        paginay = webbrowser.open(
            'https://docs.google.com/spreadsheets/d/1iszsaE4NgniBP-gghQ2V2a4iXP3f-oPLTFnL80FM20c/edit#gid=416158579')
        return (paginay)
def pc(bot, update):
    try:
        message = {scrap_pc()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 014 {}".format(e.args[0]))

def scrap_rec():
        paginay = webbrowser.open(
            'https://docs.google.com/spreadsheets/d/10u8Vf9sEFsnJxlOuu0PPATJfO22jFA08EhyTAGAadHQ/edit#gid=0')
        return (paginay)
def rec(bot, update):
    try:
        message = {scrap_rec()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 015 {}".format(e.args[0]))

def scrap_tct():
        paginay = webbrowser.open(
            'https://docs.google.com/spreadsheets/d/1Swh9BgcDjBJXEVV0SXwqBzY_b9a8CWUGfYK88IlMGag/edit#gid=966380499')
        return (paginay)
def tct(bot, update):
    try:
        message = {scrap_tct()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 016 {}".format(e.args[0]))

def scrap_acs():
        paginay = webbrowser.open(
            'https://docs.google.com/spreadsheets/d/1Q3aXycc0_J9o7jgIi-y5Mu7wicJZS-PGBEem6Nb_TzQ/edit?pli=1#gid=714979526')
        return (paginay)
def acs(bot, update):
    try:
        message = {scrap_acs()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 017 {}".format(e.args[0]))

def scrap_rhsys():
        paginay = webbrowser.open(
            'http://hortifrut.rhsys.pe/')
        return (paginay)
def rhsys(bot, update):
    try:
        message = {scrap_rhsys()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 018 {}".format(e.args[0]))

def scrap_ti():
        paginay = webbrowser.open(
            'https://easyit-hortifrut.refined.site/portal/2')
        return (paginay)
def ti(bot, update):
    try:
        message = {scrap_ti()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 019 {}".format(e.args[0]))

def scrap_pa():
        paginay = webbrowser.open(
            'https://docs.google.com/spreadsheets/d/1d_fbDybgwjY4tLqRhsCkX-NcPrplw6V8l1ufhcWNAxI/edit?pli=1#gid=537944161')
        return (paginay)
def pa(bot, update):
    try:
        message = {scrap_pa()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 020 {}".format(e.args[0]))

def scrap_bc():
        paginay = webbrowser.open(
            'https://hfch-adfs.hortifrut.com/adfs/ls?SAMLRequest=fZLbTsMwDIZfJfJ9egjtGNE6NJgmJnGYWOGCG5SmKY3UJiNOGbw9XXcQXMCt%2Fdu%2F%2FdmTy8%2B2IR%2FKobYmgziIgCgjbanNWwZP%2BYKO4XI6QdE2bMNnna%2FNo3rvFHrSFxrk%2B0wGnTPcCtTIjWgVci%2F5enZ3y1kQ8Y2z3krbAJn3hdoIP5jV3m%2BQh2FdyZqKssKgts7rynU%2BkLYNd6GwQSAL66QavDOoRIMKyHKewWsxYiJKypKmxZmiyXgkaSFiRtOL6iKWhRgXieiliJ1aGvTC%2BAxYxBiNEspGeZTwlPH0PDhj6QuQ1WHKK2322%2F%2B3UrEXIb%2FJ8xVdPaxzIM9Hir0ADsz44O5%2Bwvq%2FsUBUbscHpkc%2B2%2B02wE5KhVgJ6a3DAc8JFk7Cn16na933zZfzlW20%2FCKzprHba6eEVxl416kBayv83%2BPEQTxEdEmrQco7gxsldaVVCeH0YPv7Labf&RelayState=%2Flogin&SigAlg=http%3A%2F%2Fwww.w3.org%2F2000%2F09%2Fxmldsig%23rsa-sha1&Signature=aJpQAkZJK28PaSJqM9AFJATn87IHpTMYoy1vwnbpcuw3AgM%2FFhV26L9sLpzmeRzD7gSm5YVlaIvTQAss0BJjD%2FXRb%2BsaCeBSd9iUQH7tU1954wEBJ7oJ53VXkj8Vd1SkQiP%2BqBF8OMhMnCSjZd4sO%2FmBvFZZD0bD%2BltszgE6Wpg%3D')
        return (paginay)
def bc(bot, update):
    try:
        message = {scrap_bc()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 021 {}".format(e.args[0]))

def scrap_f41416408():
        paginay = webbrowser.open(
            'https://photos.google.com/photo/AF1QipMlZPYkYqwqqjfaLgVTV3dkX4iPgwCMg1SvGrom')
        return (paginay)
def f41416408(bot, update):
    try:
        message = {scrap_f41416408()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 022 {}".format(e.args[0]))

def outlook(bot, update):
    try:
        message = "Abrir outlook en https://outlook.office365.com/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 023 {}".format(error.args[0]))

def cesados(bot, update):
    try:
        message = "------------------------------------------------- \n Inv. Berries 2019 - 2020: https://docs.google.com/spreadsheets/d/1IQxOaq3bC-FlYT-zBFxufsqgvxNIC2arCc5v7VY_jYk/edit#gid=0 \n \n Inv. Berries 2020 - 2021: https://docs.google.com/spreadsheets/d/1L9wY2mnZZLv3Upbiv30FygaJxgDK1L-3aQ_l7bNh7jk/edit#gid=0 \n \n Inv. Berries 166 LBS antiguas https://docs.google.com/spreadsheets/d/1vVb34fP3CjnWiO8izjkZXVeJzCooFyhqYO1IiRsH1Ck/edit#gid=0\n \n" \
                  "Inv. Perú DESCANSOS TEMPORALES (3067):\nhttps://docs.google.com/spreadsheets/d/1Tga-fROaKMO3ifGJVHx-CDTEE_Qy-8oefXDu5dgKvYg/edit#gid=0 \n \n Inv. Perú cesados 2020 -2021 https://docs.google.com/spreadsheets/d/1FYvOGkgEetuaDv862CytmtuIql5p2itIbnOHnq6baqA/edit#gid=0 \n \n Inv. Perú cesados - 2019 - 2020: https://docs.google.com/spreadsheets/d/1k2H4OIirPFm6HRHmJQkuszORJFdp_p44AdCrs8tk0BY/edit#gid=0 \n \n Inv. Tal cesados - 2020 - 2021: https://docs.google.com/spreadsheets/d/1r_9Lt638uwamSeZO7V3_nsXCuZscVFTVwKFNkxDLImk/edit#gid=0 \n \n Inv. Tal cesados - 2019 - 2020: https://docs.google.com/spreadsheets/d/14NBVANd3nyVkljuJHvG9CFwp2ys8Y0nhYzSLt9COi74/edit#gid=0 \n \n Inv. Tal de DESCANSOS TEMPORALES: https://docs.google.com/spreadsheets/d/1zSEQIioyEg-qMOJbxc8bKdhaZA8g0nWT4uBzidUWJSc/edit#gid=0 \n \n Inv. Tal de LBS (1539): https://docs.google.com/spreadsheets/d/1d4kqB5W2-h0RippCjGg65FDgRgBOhdzCSnfsw-0wUck/edit#gid=0 \n \n Inv. Tal de LLAMAMIENTO DE LABORES (375): https://docs.google.com/spreadsheets/d/1z5pG04fyV7VzZz2yA-wrxltC5Y_meBc9ZZSxkr_JzJ4/edit#gid=0 \n \n" \
                  "Inv. Perú LBS del 2018 -2019 (1142) https://docs.google.com/spreadsheets/d/12VzlNyEyLFjmgrXRXMVjxk8tzB5C3eaia9rI0v1CHgw/edit#gid=0 \n \n            \n"

        update.message.reply_text(message)
    except Exception as error:
        print("Error 024 {}".format(error.args[0]))

def scrap_f76794134():
        paginay = webbrowser.open(
            'https://photos.google.com/photo/AF1QipO-7iRroEZqGpjL6hbnpMALuGhop1APbjOJEf1n')
        return (paginay)
def f76794134(bot, update):
    try:
        message = {scrap_f76794134()}
        update.message.reply_text(message)
    except Exception as e:
        print("Error 025 {}".format(e.args[0]))

def youtube(bot, update):
    try:
        message = "Acceder en https://www.youtube.com/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 026 {}".format(error.args[0]))

def semanas(bot, update):
    try:
        message = "Ver las semanas del 2022 en https://www.calendario-365.es/calendario-2022.html"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 027 {}".format(error.args[0]))

def firma(bot, update):
    try:
        message = "Descargar el tamaño de firma adecuado, de https://drive.google.com/drive/folders/1KXC2FmFl9EsTCDwDaevaZsCBmUxLbFDQ, y luego insertar al pdf correspondiente a través de ilovepdf \n ------------------------------------------------- \n \n /firma1 - tamaño 267x176 https://drive.google.com/file/d/15kwNn09uOsHLE80IjaTPcPCXRj_nzIjm/view \n \n /firma2 - tamaño 201x132 https://drive.google.com/file/d/1ZsrKpwZuGpgnWqeZLkAprmtdrN0mfbFa/view \n \n /firma3 - tamaño 134x88 https://drive.google.com/file/d/1P2TEzOinlhPyg04i7WJZic_NZfwrjMWu/view \n \n /firma4 - tamaño 67x44 https://drive.google.com/file/d/1uXK-Lsh5YisIrrBR3ox75aX1G0FQtPBy/view?usp=sharing \n \n ------------------------------------------------- \n Una vez elegida y descargada la foto se trabaja con el ilovepdf a través del siguiente enlace: \n \n https://www.ilovepdf.com/es/insertar_imagen_texto_pdf#watermark-options,image "
        update.message.reply_text(message)
    except Exception as error:
        print("Error 028 {}".format(error.args[0]))

def firma1(bot, update):
    try:
        message = "En el dispositivo, abrir en el Drive en https://drive.google.com/file/d/15kwNn09uOsHLE80IjaTPcPCXRj_nzIjm/view/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 029 {}".format(error.args[0]))

def firma2(bot, update):
    try:
        message = "En el dispositivo, abrir en el Drive en https://drive.google.com/file/d/1ZsrKpwZuGpgnWqeZLkAprmtdrN0mfbFa/view"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 030 {}".format(error.args[0]))

def firma3(bot, update):
    try:
        message = "En el dispositivo, abrir en el Drive en /firma3 - tamaño 134x88 https://drive.google.com/file/d/1P2TEzOinlhPyg04i7WJZic_NZfwrjMWu/view"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 031 {}".format(error.args[0]))

def firma4(bot, update):
    try:
        message = "En el dispositivo, abrir en el Drive en https://drive.google.com/file/d/1uXK-Lsh5YisIrrBR3ox75aX1G0FQtPBy/view?usp=sharing"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 032 {}".format(error.args[0]))

def drive(bot, update):
    try:
        message = "abrir el drive en https://drive.google.com/drive/my-drive"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 033 {}".format(error.args[0]))

def personal(bot, update):
    try:
        message = "------------------------------------------------- \n Estas son las páginas y cuestiones personales que por ahora estoy considerando: \n \n /amazon - enlace a Amazon Prime \n \n /cencosud - para pagar la tarjeta de Flor \n \n /computrabajo - enlace a computrabajo \n \n /fixture - para ver la programación de partidos de hoy día, de mañana y pasado mañana \n \n /futbol - fechas de pago de clases de José \n \n /internet - fechas de pago del internet de Orbex \n \n /linkedin - enlace a linkedin \n \n /netflix - enlace a netflix \n \n /pagos - mis fechas y montos de pago \n \n /tallas y medidas de ropa"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 034 {}".format(error.args[0]))

def amazon(bot, update):
    try:
        message = "Abrir Amazon Prime en https://www.primevideo.com/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 035 {}".format(error.args[0]))

def cencosud(bot, update):
    try:
        message = "Recordar que siempre se debe pagar por el Continental. El número de la tarjeta de Flor es: \n\n 5292060014836803"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 036 {}".format(error.args[0]))

def computrabajo(bot, update):
    try:
        message = "Abrir computrabajo en https://www.computrabajo.com.pe/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 037 {}".format(error.args[0]))


def futbol(bot, update):
    try:
        message = "El pago de la mensualidad es de S/.80, los 25 de cada mes, empezando desde el 25/4/22 pagándose por mes adelantado. Adicionalmente, se paga S/.2 al día por uso de cancha donde se practica. \n \n La historia es así: \n \n 1er mes: pago el 25.4.22 por clases de fútbol del 25.4.22 al 24.5.22. \n \n 2do mes: pago el 25.5.22 por clases de fútbol del 25.5.22 al 24.6.22. \n \n ------------------------------------------------- \n Formas de pago: \n \n BCP \n cuenta: \n 57099257618073 \n CCI: \n 00257019925761807308 \n \n Yape \n A su mismo número personal \n 968681094"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 038 {}".format(error.args[0]))

def internet(bot, update):
    try:
        message = "El pago de la mensualidad es de S/.50, los 25 de cada mes, empezando desde el 25/5/22 pagando al consumirse el mes, esto es, después de consumir un mes de servicio. \n \n La historia es así: \n \n 1er mes: pago el 25.5.22 por servicio de internet del 21.4.22 (fecha de instalación) al 25.5.22. \n \n 2do mes: pago el 25.6.22 por servicio de internet del 26.5.22 al 25.6.22. \n \n ------------------------------------------------- \n Formas de pago: \n \n Interbank \n número de cuenta a nombre de Medina Orbezo Helard Miguel:\n 8983179129720 \n CCI: 00389801317912972046 \n  \n \n BCP \n cuenta: \n 57038612681061 \n CCI: \n 00257013861268106105 \n \n Yape (el número de Mike): \n 964562729"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 039 {}".format(error.args[0]))


def linkedin(bot, update):
    try:
        message = "Abrir linkedin en https://www.linkedin.com/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 040 {}".format(error.args[0]))

def netflix(bot, update):
    try:
        message = "Abrir netflix en https://www.netflix.com/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 041 {}".format(error.args[0]))

def pagos(bot, update):
    try:
        message = "Mis obligaciones mensuales, en orden cronológico, son las siguientes: \n \n Día 5: \n amazon, S/.17 -  descuento automático. \n Se puede visualizar directamente este concepto con el comando \n /amzpago \n \n Día 15: \n cuarto, S/. 150 \n Se puede visualizar de manera individual con el comando /cuarto \n \n Día 20: \n pensión de José, S/.250 - el 20 es el máximo día para pagar. \n Se puede visualizar de manera individual con el comando /pension \n \n Día 23: \n celular, S/.280 - el 23 es el último día de pago. \n Se puede visualizar individualmente con el comando \n /celpago \n \n Día 25: \n fútbol, S/.80 \n ver detalle en /futbol \n \n Día 25: \n internet \n ver detalle en /internet \n \n Día 29 o 30: \n netflix, S/.35 - descuento automático. \n Se puede visualizar directamente este concepto con el comando \n /ntfpago"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 042 {}".format(error.args[0]))

def pension(bot, update):
    try:
        message = "Todos los 20 de cada mes, como máximo, se paga la pensión de alimentos. \n Pago S/.250 al mes por este concepto."
        update.message.reply_text(message)
    except Exception as error:
        print("Error 043 {}".format(error.args[0]))

def cuarto(bot, update):
    try:
        message = "Todos los 15 de cada mes. \n Pago S/.150 por este concepto. "
        update.message.reply_text(message)
    except Exception as error:
        print("Error 044 {}".format(error.args[0]))

def amzpago(bot, update):
    try:
        message = "Todos los 5 de cada mes. \n Me descuentan automáticamente 17 soles. "
        update.message.reply_text(message)
    except Exception as error:
        print("Error 045 {}".format(error.args[0]))

def celpago(bot, update):
    try:
        message = "El último día de pago es el 23 de cada mes. \n Pago actualmente S/.280 (S/.200 por el celular, y S/.80 por la línea que tengo)."
        update.message.reply_text(message)
    except Exception as error:
        print("Error 046 {}".format(error.args[0]))

def ntfpago(bot, update):
    try:
        message = "Todos los 29 o 30 de cada mes. \n Me descuentan automáticamente 35 soles. "
        update.message.reply_text(message)
    except Exception as error:
        print("Error 047 {}".format(error.args[0]))

def tallas(bot, update):
    try:
        message = "Mis tallas, y/o las medidas de mi ropa, son las siguientes: \n \n CAMISA \n Talla S, incluso en esta talla algunas tendrían que achicarse un poco más, básicamente de la parte de abajo. \n Pero la talla XS es muy pequeña, no comprar nunca XD.  \n \n PANTALÓN \n Cintura: xxx cms \n Basta: xxx cms \n \n SHORT \n Cintura: xxx cms \n Basta: xxx cms"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 048 {}".format(error.args[0]))

def fixture(bot, update):
    try:
        message = "Ver la programación de partidos en (actualizar al ir a la página): \n https://www.lapelotona.com/partidos-de-futbol-para-hoy-en-vivo/"
        update.message.reply_text(message)
    except Exception as error:
        print("Error 049 {}".format(error.args[0]))

def main():
    try:
        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("inicio", inicio))

        dp.add_handler(CommandHandler("fixture", fixture))

        dp.add_handler(CommandHandler("tallas", tallas))

        dp.add_handler(CommandHandler("ntfpago", ntfpago))

        dp.add_handler(CommandHandler("pension", pension))

        dp.add_handler(CommandHandler("celpago", celpago))

        dp.add_handler(CommandHandler("amzpago", amzpago))

        dp.add_handler(CommandHandler("cuarto", cuarto))

        dp.add_handler(CommandHandler("pagos", pagos))

        dp.add_handler(CommandHandler("linkedin", linkedin))

        dp.add_handler(CommandHandler("netflix", netflix))

        dp.add_handler(CommandHandler("ayuda", ayuda))

        dp.add_handler(CommandHandler("internet", internet))

        dp.add_handler(CommandHandler("personal", personal))

        dp.add_handler(CommandHandler("futbol", futbol))

        dp.add_handler(CommandHandler("computrabajo", computrabajo))

        dp.add_handler(CommandHandler("cencosud", cencosud))

        dp.add_handler(CommandHandler("pltc", pltc))

        dp.add_handler(CommandHandler("amazon", amazon))

        dp.add_handler(CommandHandler("tcc", tcc))

        dp.add_handler(CommandHandler("drive", drive))

        dp.add_handler(CommandHandler("firma", firma))

        dp.add_handler(CommandHandler("firma1", firma1))

        dp.add_handler(CommandHandler("firma2", firma2))

        dp.add_handler(CommandHandler("firma3", firma3))

        dp.add_handler(CommandHandler("firma4", firma4))

        dp.add_handler(CommandHandler("wkp", wkp))

        dp.add_handler(CommandHandler("youtube", youtube))

        dp.add_handler(CommandHandler("hortifrut", hortifrut))

        dp.add_handler(CommandHandler("req", req))

        dp.add_handler(CommandHandler("pc", pc))

        dp.add_handler(CommandHandler("rec", rec))

        dp.add_handler(CommandHandler("tct", tct))

        dp.add_handler(CommandHandler("acs", acs))

        dp.add_handler(CommandHandler("rhsys", rhsys))

        dp.add_handler(CommandHandler("semanas", semanas))

        dp.add_handler(CommandHandler("ti", ti))

        dp.add_handler(CommandHandler("pa", pa))

        dp.add_handler(CommandHandler("bc", bc))

        dp.add_handler(CommandHandler("f41416408", f41416408))

        dp.add_handler(CommandHandler("f76794134", f76794134))

        dp.add_handler(CommandHandler("outlook", outlook))

        dp.add_handler(CommandHandler("comandos", comandos))

        dp.add_handler(CommandHandler("cesados", cesados))

        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()
        print("Bot listo")
    except Exception as e:
        print("Error 003 {}".format(e.args[0]))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Error 002 {}".format(e.args[0]))