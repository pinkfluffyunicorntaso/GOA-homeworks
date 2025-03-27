#data conversion არის ერთი მონაცემთ ტიპის სხვა ტიპზე რო გადაიყვან მაგ int(3.0)
# implicitly არის ტიპის გარდაქმნა რომელიც ავტომატურად ხდება პითონის მიერ
# Explicitly არის მომხმარებელი მიერ გარდაქმნა რო ხდება მაგ float(), int() ან str()

1 = int("1") #int ში გადაყავს str
2 = int(1.0) #int ში გადაყავს float
3 = float(1) #float ში გადაყავს int
4 = float("1") #float ში გადაყავს str
5 = str(1) #str ში გადაყავს int
6 = str(1.0) #str ში გადაყავს float
