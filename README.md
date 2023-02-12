# Sundash
 
 This project is to visualize data from the Royal Observatory of Belgium's SILSO (Sunspot Index and Long-term Solar Observations) database and to show the latest image of sun from NASA website. 
With combination of these two interactive graphs and the latest sun image, it allows the user to understand the historical and trending solar activities better.


The first visualization, called “Interactive Sunspot Graphing,” allows the user to choose year range and smoothness to be graphed. The default value is the monthly line plot, but the user could make a second line that is more smooth than the first monthly line plot. The number indicated in the slider is how much month you want to average through. For example, if you choose 7 like in the image, it generates the averaged data of every 7 months, which makes the red line more smooth.

<img width="1440" alt="Screen Shot 2023-02-10 at 3 31 59" src="https://user-images.githubusercontent.com/119906364/218288549-c8c95e99-9aa2-4f9f-9c2e-29522ccb7475.png">


Next, I built the interactive “Variability of Sunspot Cycle” graph. It allows the user to choose variability on the slider, and transforms the dataset into fractional years based on the input. It has an intention to experiment on how many years exactly need to peak the solar activity again, in general. It sets to be 11 years as a default because the span between peaks is approximately 11 years on average based on my try and error, which you could see in the nice curve of the graph below.

<img width="1440" alt="Screen Shot 2023-02-10 at 3 32 14" src="https://user-images.githubusercontent.com/119906364/218288551-c4d02a30-b40e-43b9-8601-6a788a2c0df6.png">


Lastly, the “Real-time NASA Solar Image” shows the latest image of the sun according to NASA website published information. It also allows the user to choose their preferred filtering of sun image from the dropdown menu. Because it is using a direct jpg link from NASA website, the image changes when NASA decides to change the image. It helps the user to understand more on solar activity in a combination with above two graphings.

<img width="1440" alt="Screen Shot 2023-02-10 at 3 33 06" src="https://user-images.githubusercontent.com/119906364/218288552-2546a016-0dc0-42b7-a4a8-425b3d4e52b9.png">

