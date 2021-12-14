kredyt = 12000
oprocentowanie = 3
ratakredytu = 200

print("Kwota kredytu = 12000")
print ("Oprocentowanie kredytu = 3%")
print("rata kredytu spłacana co miesiąc = 200")

styczen19 = (int(1)+(float(1.5928245)+int(oprocentowanie))/int(1200))*int(kredyt)-int(ratakredytu)
print("W styczniu 2019 twoja pozostała kwota kredytu to",(round(styczen19,2)), "i jest to",round((kredyt - styczen19),2),
      "mniej niż w poprzednim miesiącu")
luty19 = (int(1)+(float(-0.4535091012)+int(oprocentowanie))/int(1200))*float(styczen19)-int(ratakredytu)
print(luty19)
marzec19 = (int(1)+(float(2.3246717171)+int(oprocentowanie))/int(1200))*float(luty19)-int(ratakredytu)
print(marzec19)
kwiecien19 = (int(1)+(float(1.2612544072)+int(oprocentowanie))/int(1200))*float(marzec19)-int(ratakredytu)
print(kwiecien19)
maj19 = (int(1)+(float(1.78252628571251)+int(oprocentowanie))/int(1200))*float(kwiecien19)-int(ratakredytu)
czerwiec19 = (int(1)+(float(2.3293845415
)+int(oprocentowanie))/int(1200))*float(maj19)-int(ratakredytu)
lipiec19 = (int(1)+(float(1.5022298422)+int(oprocentowanie))/int(1200))*float(czerwiec19)-int(ratakredytu)
sierpien19 = (int(1)+(float(1.7825262857)+int(oprocentowanie))/int(1200))*float(lipiec19)-int(ratakredytu)
wrzesien19 = (int(1)+(float(2.3288489941)+int(oprocentowanie))/int(1200))*float(sierpien19)-int(ratakredytu)
pazdziernik19 = (int(1)+(float(0.6169213482)+int(oprocentowanie))/int(1200))*float(wrzesien19)-int(ratakredytu)
listopad19 = (int(1)+(float(2.3522958864)+int(oprocentowanie))/int(1200))*float(pazdziernik19)-int(ratakredytu)
grudzien19 = (int(1)+(float(0.3377795452)+int(oprocentowanie))/int(1200))*float(listopad19)-int(ratakredytu)
styczen20 = (int(1)+(float(1.5770352473)+int(oprocentowanie))/int(1200))*float(grudzien19)-int(ratakredytu)
luty20 = (int(1)+(float(-0.2927814426)+int(oprocentowanie))/int(1200))*float(styczen20)-int(ratakredytu)
marzec20 = (int(1)+(float(2.4861965902)+int(oprocentowanie))/int(1200))*float(luty20)-int(ratakredytu)
kwiecien20 = (int(1)+(float(0.2671103178)+int(oprocentowanie))/int(1200))*float(marzec20)-int(ratakredytu)
maj20 = (int(1)+(float(1.4179526723)+int(oprocentowanie))/int(1200))*float(kwiecien20)-int(ratakredytu)
czerwiec20 = (int(1)+(float(1.0542432673)+int(oprocentowanie))/int(1200))*float(maj20)-int(ratakredytu)
lipiec20 = (int(1)+(float(1.4805201045)+int(oprocentowanie))/int(1200))*float(czerwiec20)-int(ratakredytu)
sierpien20 = (int(1)+(float(1.5770352473)+int(oprocentowanie))/int(1200))*float(lipiec20)-int(ratakredytu)
wrzesien20 = (int(1)+(float(-0.0774206903)+int(oprocentowanie))/int(1200))*float(sierpien20)-int(ratakredytu)
pazdziernik20 = (int(1)+(float(1.165733987)+int(oprocentowanie))/int(1200))*float(wrzesien20)-int(ratakredytu)
listopad20 = (int(1)+(float(-0.4041867176)+int(oprocentowanie))/int(1200))*float(pazdziernik20)-int(ratakredytu)
grudzien20 = (int(1)+(float(1.4997085208)+int(oprocentowanie))/int(1200))*float(listopad20)-int(ratakredytu)