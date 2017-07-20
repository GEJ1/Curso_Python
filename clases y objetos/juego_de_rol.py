# coding=utf-8

'''
OPCION 1:

1) Modelar una clase personaje, que posea las siguientes características:
	- Tiene nombre.
	- Posee nivel, todos los personajes inician en nivel 1.
	- Cada nivel requiere 10*nivel puntos de experiencia.
	- Posee atributos fuerza, agilidad e inteligencia que van de 1 a 100.
	- Sus atributos comienzan en 1 y cada nivel aumenta en 1.
	- Puede caminar a 0.5 metros por segundo.
	- Puede correr a 0.8 metros por segundo más 0.01 m/s por cada punto de agilidad que posea.
	- Posee vida, que va de 0 a 100.
	- Se requiere observar la vida del personaje de la siguiente manera:
	     Si la vida es 0, el personaje está muerto.
	     De 1 a 10 está mal herido, estado crítico.
	     De 11 a 30 está mal herido.
	     De 31 a 60 está herido.
	     De 61 a 99 está levemente herido.

	- Puede recibir daño (en newtons): 1 newton equivale a 1 de vida.
	- Puede golpear, generando daño (en newtons): 0.5 * fuerza

2) Modelar un Guerrero, que también es un personaje.
	- Puede golpear con 1 newton de fuerza multiplicado por la cantidad de puntos de fuerza que posea.
	- Puede defenderse de recibir daño si posee un escudo de la siguiente manera: 1 newton * fuerza.

3) Modelar un Mago, que también es un personaje.
	- Puede golpear con 1 newton de fuerza multiplicado por la cantidad de puntos de inteligencia que posea.
	- Puede defenderse de recibir daño si posee un escudo magico: 1 newton * fuerza.

4) Persona en el mundo, es un personaje:
	- Es un laburante, pero puede ser despedido.
	- No tiene obra social, pero puede adquirirla.
	- Cobra en negro, a menos que no tenga trabajo.
	- Le cae la afip.

6) Modelar Mundo:
	- En el mundo no existen 2 personajes con el mismo nombre.
	- El mundo inicia con 4 personajes a elección (de usuario o no)
	- El mundo recibe instrucciones del juego que pueden ser:
		- Se pueden agregar personajes.
		- Se pueden eliminar personajes.
		- Entrenar personaje: Recibe un personaje y lo hace entrenar en el gimnasio, el mismo recibe 10 puntos de experiencia.
		- Pelear : Dado dos personajes los hace combatir hasta que uno gane ("mate" al otro).
		Una vez que el combate termina  imprime por pantalla el resultado del combate y estado actual de los mismos.
		Automáticamente luego del combate el "dios programador" del mundo hace que los personajes se curen al 100%.
		-Carrera olímpica: los personajes compiten en una carrera en simultaneo, no existen los empates y alguien siempre gana la carrera.
		Se deberá representar un podio con los participantes.
		- Imprime una lista de laburantes.
		- Se le puede mandar agentes de la afip a los personajes (a todos a la vez)


#Practicando con el ejemplo de 'Python para todos'

class Coche:

	def __init__(self, gasolina):
		self.gasolina = gasolina
		print 'Tenemos', gasolina, 'litros'
		
	def arrancar(self):
		if self.gasolina > 0:
			self.gasolina = self.gasolina - 1
			print 'Arranca'
		else:
			print 'No arranca'
			
	
	def conducir(self):
		if self.gasolina >0:
			self.gasolina = self.gasolina - 1
			print 'Quedan', self.gasolina, 'litros'
		else:
			print 'No se mueve'
			
mi_coche = Coche(3)

#
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.conducir()
mi_coche.arrancar()
'''
	
class Personaje:
	
	def __init__(self,nombre,nivel=1,fuerza= 1,agilidad= 1,inteligencia= 1,puntos_exp= 0,vida=100,distancia=0): 
		self.nombre = nombre
		
		self.puntos_exp = puntos_exp
		
		self.nivel = nivel
		
		self.fuerza = fuerza 
		self.agilidad = agilidad 
		self.inteligencia = inteligencia
		self.vida = vida
		
		self.distancia = distancia
	
	def nombre_personaje(self): #Hereda de self
		print 'Mi nombre es' , self.nombre
		
		
	def nivel_personaje(self):
		if self.puntos_exp > 10:
			self.nivel = int((self.nivel*self.puntos_exp)/10)
			self.fuerza = self.nivel
			self.agilidad = self.nivel 
			self.inteligencia = self.nivel
			
			print 'Tu personaje tiene nivel', self.nivel +1
		else:
			print 'Tu personaje tiene nivel', self.nivel 
			
	def atributos_personaje(self):
		if self.nivel > 1:
			self.fuerza = 1*self.nivel
			self.agilidad = 1*self.nivel 
			self.inteligencia = 1*self.nivel
			print 'Fuerza: ', self.fuerza ,'/', 'Agilidad: ', self.agilidad ,'/', 'Inteligencia: ' , self.inteligencia
		else:
			print 'Fuerza: ', self.fuerza ,'/', 'Agilidad: ', self.agilidad ,'/', 'Inteligencia: ' , self.inteligencia
	
	def vida_personaje(self):
		
		if self.vida == 100:
			print self.vida,':  Tu personaje tiene vida completa'
			
		elif 60 < self.vida < 100:
			print self.vida,': Tu personaje está levemente herido'
			
		elif 30< self.vida <61:
			print self.vida,': Tu personaje está herido'
			
		elif 10< self.vida <31:
			print self.vida,': Tu personaje está mal herido'
			
		elif 0< self.vida <11:
			print self.vida,': Tu personaje está en estado crítico'
			
		else:
			print self.vida,': Tu personaje ha muerto'
			
	def caminar(self):
		
		self.distancia = self.distancia + 0.5 
		print 'Caminaste 0.5 metros'
		print 'Te encontras a' , self.distancia, 'metros de tu punto de partida'
		
		
	def correr(self):
		
		self.distancia = self.distancia + 0.8 + (0.01*self.agilidad)
		print 'Caminaste', self.distancia, 'metros'
		print 'Te encontras a' , self.distancia, 'metros de tu punto de partida'
		
	def golpear(self):
		danio = 0.5*self.fuerza
		
		print 'Ejerciste' , danio, 'Newtons de danio'
		
		
	def recibir_danio(self):
		self.vida = self.vida - 1
		print 'Recibiste' , 1- self.distancia, 'Newtons de danio'
		print 'Tu vida ahora es ', self.vida
		
			
class Guerrero(Personaje): #Hereda de Personaje
	def __init__()
		
			
			
mi_personaje = Personaje('Ricardo')


mi_personaje.golpear()



		
				
	
	
	
	
	
	
