from gasp import *

begin_graphics()



Line((300,210),(290,190))
Line((290,190),(310,190))
Circle((300,200),40)
Circle((285,210),5)
Circle((315,210),5)
Arc((300, 200), 30, 225, 315)



update_when('key_pressed')  
end_graphics()
drawstick(200,200)




    