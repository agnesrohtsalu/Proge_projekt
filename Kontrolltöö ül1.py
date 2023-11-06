sisend= input("Sisesta faili nimi: ")
pealkiri= input("Sisesta loetud raamatu pealkiri: ")
nüüd_loetud= int(input("Mitu lehekülge lugesid? "))

raamatute_arv=0
loetud_raamatud= 0
#pealkirjad= []
fail= open("raamatud.txt", encoding= "utf-8")
while True:
    rida1= fail.readline()
    rida2= fail.readline()
    rida3= fail.readline()
    if rida1 == "":
        break
    raamat= rida1.strip()
    lehtede_arv= int(rida2.strip())
    loetud= int(rida3.strip())
    raamatute_arv+= 1
    #pealkirjad.append(raamat)
    
    if lehtede_arv == loetud:
            loetud_raamatud+= 1
    if pealkiri == raamat:
        if (lehtede_arv - (loetud + nüüd_loetud))== 0:
            tulem= 1
            loetud_raamatud+= 1
            #print(f"Tubli lugesid raamatu lõpuni! Veel on vaja lugeda {raamatute_arv - loetud_raamatud} raamat(ut).")
        if (lehtede_arv - (loetud + nüüd_loetud))!= 0:
            tulem= 0
            lugeda_jäänud= (lehtede_arv - (loetud + nüüd_loetud))
            #print(f"Raamatust on jäänud lugeda {lehtede_arv - (loetud + nüüd_loetud)} lk. Veel on vaja lugeda {raamatute_arv - loetud_raamatud} raamat(ut).")
    
fail.close()

if tulem ==1:
    print(f"Tubli lugesid raamatu lõpuni! Veel on vaja lugeda {raamatute_arv - loetud_raamatud} raamat(ut).")
if tulem == 0:
    print(f"Raamatust on jäänud lugeda {lugeda_jäänud} lk. Veel on vaja lugeda {raamatute_arv - loetud_raamatud} raamat(ut).")

tulemus= open("loetud.txt", "w", encoding="utf-8")
tulemus.write(f"Loetud raamatute arv: {loetud_raamatud}")
tulemus.close()
print("test")