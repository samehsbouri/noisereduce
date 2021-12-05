# noisereduce
![Noisereduce](https://github.com/timsainb/noisereduce/raw/master/assets/noisereduce.png)

## 1 - Contexte et définition du projet :
Parfois nous recevons un message vocal avec beaucoup de bruits de fond qui peuvent être ennuyeux et nous ne pouvons pas entendre les choses clairement.


## 2- Objectif :
La réduction du bruit sert à supprimer les bruits de fond indésirables et à rendre le son aussi clair que possible. 

### 3-Fonctionnement: 
Ce projet s'appuie sur une méthode appelée "spectral gating" qui est une forme de Noise Gate. Il fonctionne en calculant un spectrogramme d'un signal (et éventuellement un signal de bruit) et en estimant un seuil de bruit (ou gate) pour chaque bande de fréquence de ce signal/bruit. Ce seuil est utilisé pour calculer un masque, qui élimine le bruit en dessous du seuil variable en fréquence.


### [Noisereduce](https://pypi.org/project/noisereduce/) (lien de la bibliothèque)

  
#### |Sameh Sbouri|sameh.sbouri@istic.ucar.tn|2-LIRS
