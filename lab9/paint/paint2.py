import pygame , random
from collections import deque
pygame.init()

running = True


class player_brush ( pygame.sprite.Sprite ):

    def __init__(self):
        super().__init__()
        self.color_mode = random.choice([ "blue" , "red" , "green" , "white"])
        self.radius = 40
        self.points = deque(maxlen=2)
        self.types = [ "square" , "rtrianlge" , "circle" , "etriangle", "rhombus" ]
        self.type = random.choice( self.types )
        self.stop = False 

    def draw( self, screen  ):


        if len(self.points) < 2 :
            return
        
        if self.color_mode == "blue":
            gradient_color = ( 0 , 0 , 255 )
        elif self.color_mode == "red":
            gradient_color = ( 255 , 0 , 0 )
        elif self.color_mode == "green": 
            gradient_color = (0 , 255 , 0 )
        elif self.color_mode == "white" :
            gradient_color = ( 255 , 255 , 255 )

        end = self.points[1]
        start = self.points[0]

        delta_x = ( start[0]-end[0] )
        delta_y = ( start[1]-end[1] )

        iterations = max( abs( delta_x) , abs( delta_y ) , 1 )

        r = self.radius 
        hr = int (r/2) 


        for i in range( iterations ):
            progress = i/iterations
            aprogress = 1 - progress

            x = int ( aprogress * start[0] + progress*end[0] )
            y = int ( aprogress * start[1] + progress*end[1] )


            if self.type == "circle" : 
                pygame.draw.circle( screen , gradient_color, ( x , y ), r )

            if self.type == "square" : 
                pygame.draw.rect( screen , gradient_color , ( x, y, r , r ) )

            if self.type == "rtrianlge" : 
                pygame.draw.polygon( screen, gradient_color , [ (x, y) , (x + r , y ) , (x, y - r )] )

            if self.type ==  "etriangle" : 
                pygame.draw.polygon( screen , gradient_color , [ ( x, y ) , ( x + r , y  ) , ( x + hr , y - r) ]  )

            if self.type == "rhombus" : 
                pygame.draw.polygon( screen , gradient_color , [ (x , y) , ( x + hr , y - hr ) , ( x + r , y ) , ( x + hr , y + hr )])

            






screen = pygame.display.set_mode(( 600 , 600 ))
screen.fill(( 255, 255, 255 ))

clock = pygame.time.Clock()

brush = player_brush()

index = random.randint( 0 , 4 )

def drawtext ( screen , text , size , xy , color ):

    font = pygame.font.SysFont ( "Comic Sans" , size )
    temp = font.render( text , True , color )
    screen.blit( temp , xy )





while running :


    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False 

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r  :
                brush.color_mode = "red"
                
            if event.key == pygame.K_g  :
                brush.color_mode = "green"
                
            if event.key == pygame.K_b :
                brush.color_mode = "blue"

            if event.key == pygame.K_e :
                brush.color_mode = "white"
            
            if event.key == pygame.K_a :
                
                pygame.draw.rect( screen , (255 , 255 , 255) , ( 0 , 7 , 84 , 22 ) )
                index -= 1
                if index == -1 :
                    index = 4 
                

            
            if event.key == pygame.K_d :
                
                pygame.draw.rect( screen , (255 , 255 , 255) , ( 0 , 7 , 84 , 22 ) )
                
                
                index +=1 
                if index == 5 :
                    index = 0
                
            if event.key == pygame.K_SPACE :
                brush.stop = not brush.stop

            
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 : brush.radius = max( 1 , brush.radius - 1 ) 
            elif event.button == 3 : brush.radius = min ( 150 , brush.radius + 1 )

        if event.type == pygame.MOUSEMOTION:

            position = event.pos
            brush.points.append( position )

            

    
    brush.type = brush.types[index]

    drawtext( screen , brush.type , 20  , (0,0) , ( 255 , 165 , 0 ) )  
    
    if not brush.stop:
        brush.draw ( screen )


    
    









    pygame.display.update()
    clock.tick(60)


pygame.quit()    