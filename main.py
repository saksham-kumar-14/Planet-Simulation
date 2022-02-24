import pygame , sys , math

pygame.init()
WIDTH,HEIGHT=900,700
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet Simulation")


G = 6.67 / (10**(11)) 	
SUN_MASS = 2 * (10**30) 

P1_DIS = 69 * (10**6)
P2_DIS = 105 * (10**6)
P3_DIS = 148  * (10**6)
P4_DIS = 220 * (10**6)

class Body():
	def __init__(self, distance_from_sun , actual_distance_from_sun , radius , color):
		global G , SUN_MASS

		self.distance_from_sun = distance_from_sun
		self.radius = radius
		self.color = color

		self.pos = [ WIDTH//2 , HEIGHT//2 ]
		self.omega = 0
		if distance_from_sun!=0:
			self.pos = [ WIDTH//2 + distance_from_sun , HEIGHT//2 ] 
			vel = math.sqrt((G*SUN_MASS)/(actual_distance_from_sun))
			self.omega = vel/actual_distance_from_sun

		self.current_angle = 0 

		self.positions = [  ]


	def draw(self):
		pygame.draw.circle(SCREEN, self.color, self.pos, self.radius)

		for i in range(len(self.positions)):
			if i != 0:
				pygame.draw.line(SCREEN, self.color, self.positions[i-1], self.positions[i], 2)

	def move(self):
		if self.current_angle < 370:
			self.positions.append([ math.floor(self.pos[0]) , math.floor(self.pos[1]) ])

		self.current_angle += self.omega*100

		self.pos[0] = (WIDTH//2) + ((self.distance_from_sun)*math.cos(self.current_angle/57.3))
		self.pos[1] = (HEIGHT//2) + ((self.distance_from_sun)*math.sin(self.current_angle/57.3))


def main():
	sun = Body( 0, 0, 50, (255,0,0) )
	p1 = Body( 90, P1_DIS, 9, (200,200,200) )
	p2 = Body( 125, P2_DIS, 12, (255,160,0) )
	p3 = Body( 190, P3_DIS, 15, (0,150,255) )
	p4 = Body( 275, P4_DIS, 12, (255,80,0) )

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

		SCREEN.fill((0,0,0))
		sun.draw()
		p1.draw()
		p2.draw()
		p3.draw()
		p4.draw()

		p1.move()
		p2.move()
		p3.move()
		p4.move()

		pygame.time.Clock().tick(80)
		pygame.display.update()






# main execution
if __name__ == '__main__':

	main()