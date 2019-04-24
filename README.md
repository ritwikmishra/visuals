# visuals
Helpful for visualising data (though not easy to interpret by human eyes)

## images
![figure 1](Figure_1.png)
![figure 2](Figure_2.png)
![figure 3](Figure_3.png)

## legends.txt

```
Test conducted on: 2019-04-24 13:10:19:989372
X-axis = 'att1' attribute
Y-axis = 'att2' attribute
Z-axis = 'att3' attribute
There will be 3 diagrams containing all the boundary values of 'att4' attribute generated automatically
Size of the points depends on 'att5' attribute automatically
	If att5.value() < 16.0	then	Point size = 20
	If att5.value() < 23.0	then	Point size = 40
	If att5.value() < 30.0	then	Point size = 60
Color of the points depends on 'att6' attribute automatically
	If att6.value() < 4.0	then	Point color = blue
	If att6.value() < 7.0	then	Point color = green
	If att6.value() < 10.0	then	Point color = red
Color of the point edge depends on 'att7' attribute automatically
	If att7.value() < 31.0	then	color of the point edge = #4d5384
	If att7.value() < 42.0	then	color of the point edge = #4d8453
	If att7.value() < 60.0	then	color of the point edge = #844d4d
Marker of the point depends on 'att8' attribute generated automatically
	If att8.value() < 0.84	then	marker of the point = o
	If att8.value() < 1.19	then	marker of the point = v
	If att8.value() < 1.5	then	marker of the point = s
	Refer to https://matplotlib.org/api/markers_api.html#module-matplotlib.markers to see markers and their respective symbols
Opacity of the point depends on 'att9' attribute. All the values are scaled between 0 (transparent) to 1 (opaque) by dividing all by the MAX value
Width of the point edge depends on 'att10' attribute. All the values are scaled between 0.7 to 1.5
	Refer to the source code to see the formula.

		Images generated successfully!
===================================================================
```

## dataset description
```
              att1         att2         att3         att4         att5         att6         att7         att8         att9        att10        att11        att12
count  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000  1500.000000
mean    750.500000     0.509585    49.733051     5.068733    19.844000     5.590667    36.616000     1.008573    47.698667     5.037200     2.528073    19.047807
std     433.157015     0.289919    29.207101     2.884874     6.129223     2.802680    10.644376     0.289443    13.073197     2.809066     0.879024     9.094775
min       1.000000     0.000000     0.016000     0.000000    10.000000     1.000000    13.000000     0.500000    25.000000     0.000000     1.000000     1.590000
max    1500.000000     1.000000    99.939000    10.000000    30.000000    10.000000    60.000000     1.500000    70.000000    10.000000     3.990000    48.000000
```