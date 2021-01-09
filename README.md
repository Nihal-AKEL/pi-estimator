# pi-estimator
Estimation de pi par pyspark et numpy.<br />
Comparaison des performances: <br />
| n=100.000 | Spark | Numpy |
| :---: | :---: | :---: |
| Temps d'execution en s | 11,30 | 0,11 |
| Valeurs de pi | 3,1442 | 3,14068 |
| Ecart % Math.pi en val abs| 0,08%| 0,02% |<br />

Pour n = 1.000.000 : <br />
| n=1.000.000 | Spark | Numpy |
| :---: | :---: | :---: |
| Temps d'execution en s | 11,15 | 1,09 |
| Valeurs de pi | 3,14032 | 3,14117 |
| Ecart % Math.pi en val abs| -0,04%| -0,01% |<br />

On remarque que l'estimation de pi est plus précise.

