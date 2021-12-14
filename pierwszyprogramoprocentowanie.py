kredyt = 12000
oprocentowanie = 3
ratakredytu = 200

print("Kwota kredytu = 12000")
print ("Oprocentowanie kredytu = 3%")
print("rata kredytu spłacana co miesiąc = 200")

styczen19 = (int(1)+(float(1.5928245)+int(oprocentowanie))/int(1200))*int(kredyt)-int(ratakredytu)
print("W | styczniu 2019 | twoja pozostała kwota kredytu to|",(round(styczen19,2)), "| i jest to | ",round((kredyt - styczen19),2),
      " | mniej niż w poprzednim miesiącu")
luty19 = (int(1)+(float(-0.4535091012)+int(oprocentowanie))/int(1200))*float(styczen19)-int(ratakredytu)
print("W lutym 2019 twoja pozostała kwota kredytu to",(round(luty19,2)), "i jest to",round((styczen19 - luty19),2),
      "mniej niż w poprzednim miesiącu")
marzec19 = (int(1)+(float(2.3246717171)+int(oprocentowanie))/int(1200))*float(luty19)-int(ratakredytu)
print("W marcu 2019 twoja pozostała kwota kredytu to",(round(marzec19,2)), "i jest to",round((luty19 - marzec19),2),
      "mniej niż w poprzednim miesiącu")
kwiecien19 = (int(1)+(float(1.2612544072)+int(oprocentowanie))/int(1200))*float(marzec19)-int(ratakredytu)
print("W kwietniu 2019 twoja pozostała kwota kredytu to",(round(kwiecien19,2)), "i jest to",round((marzec19 - kwiecien19),2),
      "mniej niż w poprzednim miesiącu")
maj19 = (int(1)+(float(1.78252628571251)+int(oprocentowanie))/int(1200))*float(kwiecien19)-int(ratakredytu)
print("W maju 2019 twoja pozostała kwota kredytu to",(round(maj19,2)), "i jest to",round((maj19 - kwiecien19),2),
      "mniej niż w poprzednim miesiącu")
czerwiec19 = (int(1)+(float(2.3293845415)+int(oprocentowanie))/int(1200))*float(maj19)-int(ratakredytu)
print("W czerwcu 2019 twoja pozostała kwota kredytu to",(round(czerwiec19,2)), "i jest to",round((czerwiec19 - maj19),2),
      "mniej niż w poprzednim miesiącu")
lipiec19 = (int(1)+(float(1.5022298422)+int(oprocentowanie))/int(1200))*float(czerwiec19)-int(ratakredytu)
print("W lipcu 2019 twoja pozostała kwota kredytu to",(round(lipiec19,2)), "i jest to",round((lipiec19 - czerwiec19),2),
      "mniej niż w poprzednim miesiącu")
sierpien19 = (int(1)+(float(1.7825262857)+int(oprocentowanie))/int(1200))*float(lipiec19)-int(ratakredytu)
print("W sierpniu 2019 twoja pozostała kwota kredytu to",(round(sierpien19,2)), "i jest to",round((sierpien19 - lipiec19),2),
      "mniej niż w poprzednim miesiącu")
wrzesien19 = (int(1)+(float(2.3288489941)+int(oprocentowanie))/int(1200))*float(sierpien19)-int(ratakredytu)
print("We wrześniu 2019 twoja pozostała kwota kredytu to",(round(wrzesien19,2)), "i jest to",round((wrzesien19 - sierpien19),2),
      "mniej niż w poprzednim miesiącu")
pazdziernik19 = (int(1)+(float(0.6169213482)+int(oprocentowanie))/int(1200))*float(wrzesien19)-int(ratakredytu)
print("W październiku 2019 twoja pozostała kwota kredytu to",(round(pazdziernik19,2)), "i jest to",round((pazdziernik19 - wrzesien19),2),
      "mniej niż w poprzednim miesiącu")
listopad19 = (int(1)+(float(2.3522958864)+int(oprocentowanie))/int(1200))*float(pazdziernik19)-int(ratakredytu)
print("W listopadzie 2019 twoja pozostała kwota kredytu to",(round(listopad19,2)), "i jest to",round((listopad19 - pazdziernik19),2),
      "mniej niż w poprzednim miesiącu")
grudzien19 = (int(1)+(float(0.3377795452)+int(oprocentowanie))/int(1200))*float(listopad19)-int(ratakredytu)
print("W grudniu 2019 twoja pozostała kwota kredytu to",(round(grudzien19,2)), "i jest to",round((grudzien19 - listopad19),2),
      "mniej niż w poprzednim miesiącu")
styczen20 = (int(1)+(float(1.5770352473)+int(oprocentowanie))/int(1200))*float(grudzien19)-int(ratakredytu)
print("W styczniu 2020 twoja pozostała kwota kredytu to",(round(styczen20,2)), "i jest to",round((styczen20 - grudzien19),2),
      "mniej niż w poprzednim miesiącu")
luty20 = (int(1)+(float(-0.2927814426)+int(oprocentowanie))/int(1200))*float(styczen20)-int(ratakredytu)
print("W lutym 2020 twoja pozostała kwota kredytu to",(round(luty20,2)), "i jest to",round((luty20 - styczen20),2),
      "mniej niż w poprzednim miesiącu")
marzec20 = (int(1)+(float(2.4861965902)+int(oprocentowanie))/int(1200))*float(luty20)-int(ratakredytu)
print("W marcu 2020 twoja pozostała kwota kredytu to",(round(marzec20,2)), "i jest to",round((marzec20 - luty20),2),
      "mniej niż w poprzednim miesiącu")
kwiecien20 = (int(1)+(float(0.2671103178)+int(oprocentowanie))/int(1200))*float(marzec20)-int(ratakredytu)
print("W kwietniu 2020 twoja pozostała kwota kredytu to",(round(kwiecien20,2)), "i jest to",round((kwiecien20 - marzec20),2),
      "mniej niż w poprzednim miesiącu")
maj20 = (int(1)+(float(1.4179526723)+int(oprocentowanie))/int(1200))*float(kwiecien20)-int(ratakredytu)
print("W maju 2020 twoja pozostała kwota kredytu to",(round(maj20,2)), "i jest to",round((maj20 - kwiecien20),2),
      "mniej niż w poprzednim miesiącu")
czerwiec20 = (int(1)+(float(1.0542432673)+int(oprocentowanie))/int(1200))*float(maj20)-int(ratakredytu)
print("W czerwcu 2020 twoja pozostała kwota kredytu to",(round(czerwiec20,2)), "i jest to",round((czerwiec20 - maj20),2),
      "mniej niż w poprzednim miesiącu")
lipiec20 = (int(1)+(float(1.4805201045)+int(oprocentowanie))/int(1200))*float(czerwiec20)-int(ratakredytu)
print("W lipcu 2020 twoja pozostała kwota kredytu to",(round(lipiec20,2)), "i jest to",round((lipiec20 - czerwoec20),2),
      "mniej niż w poprzednim miesiącu")
sierpien20 = (int(1)+(float(1.5770352473)+int(oprocentowanie))/int(1200))*float(lipiec20)-int(ratakredytu)
print("W sierpniu 2020 twoja pozostała kwota kredytu to",(round(sierpien20,2)), "i jest to",round((sierpien20 - lipiec20),2),
      "mniej niż w poprzednim miesiącu")
wrzesien20 = (int(1)+(float(-0.0774206903)+int(oprocentowanie))/int(1200))*float(sierpien20)-int(ratakredytu)
print("We wrześniu 2020 twoja pozostała kwota kredytu to",(round(wrzesien20,2)), "i jest to",round((wrzesien20 - sierpien20),2),
      "mniej niż w poprzednim miesiącu")
pazdziernik20 = (int(1)+(float(1.165733987)+int(oprocentowanie))/int(1200))*float(wrzesien20)-int(ratakredytu)
print("W październiku 2020 twoja pozostała kwota kredytu to",(round(pazdziernik20,2)), "i jest to",round((pazdziernik20 - wrzesien20),2),
      "mniej niż w poprzednim miesiącu")
listopad20 = (int(1)+(float(-0.4041867176)+int(oprocentowanie))/int(1200))*float(pazdziernik20)-int(ratakredytu)
print("W listopadzie 2020 twoja pozostała kwota kredytu to",(round(listopad20,2)), "i jest to",round((listopad20 - pazdziernik20),2),
      "mniej niż w poprzednim miesiącu")
grudzien20 = (int(1)+(float(1.4997085208)+int(oprocentowanie))/int(1200))*float(listopad20)-int(ratakredytu)
print("W grudniu 2020 twoja pozostała kwota kredytu to",(round(grudzien20,2)), "i jest to",round((grudzien20 - listopad20),2),
      "mniej niż w poprzednim miesiącu")