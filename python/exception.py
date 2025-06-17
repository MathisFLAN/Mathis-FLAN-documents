from conducteur import Conducteur
from route import Route

R1=Route("A64",80)
R2=Route("B65",100)
R3=Route("H69",130)

C1=Conducteur("Paul", 110, 12)
C2=Conducteur("Jeanne", 80, 12)
C3=Conducteur("Kurt", 160, 12)

try :
    C1.rouler(R2)
except Exception as e:
    print("Attention à vous !", e)

try :
    C2.rouler(R1)
except Exception as e:
    print("Attention à vous !", e)

try :
    C3.rouler(R3)
except Exception as e:
    print("Attention à vous !", e)