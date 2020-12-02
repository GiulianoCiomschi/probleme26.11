s1=str(input("Dati numele,prenumele:"))
s2=s1.split()
if((s2[0]==s2[0].title())and(s2[1]==s2[1].title())):
    print("Nume,prenume introdus corect")
else:
    print("Nume,prenume introdus incorect")