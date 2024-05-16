immutable_var = 2, True , "bezzy" #если у списка нет квадратных скобок то это неизменяемый кортеж
print ( immutable_var) #он занимает меньше памяти. и кроме как обьяснить это тем, что так устроен
#(immutable_var[0] = 88 #пайтон), я не могу, если нет квадратных скобок то это не изменяется
mutable_list = [2, False, 'babadok']
print(mutable_list)
mutable_list[0] = ("killing")
mutable_list[1] = 219
mutable_list[2] = True
print(mutable_list)