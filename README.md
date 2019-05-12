# UrbanInsights
## at Hacktival 2019

## What is UrbanInsights?
UrbanInsight is an approach to analyze current apartment and housing situations in urban areas. Today, most cities are fighting against rising rental costs, lack of apartments and the generel increase of the cost of living. This is especially a burden for low-income families, who might be dependant on public transportation or other infrastructure that only a city can offer.
We use open data to search for inefficient, small buildings that only accommodate a small ammount of people and suggest city planners, politicians and everyone else who wants to improve the housing situation a map that shows potential spots for denser buildings.

## How does it work?
We use open LIDAR datasets and OpenStreetmap data in python to look for small, inefficient houses. Then we analyze their volume, estimate the ammount of persons living there and flag potential houses for replacement. The estimation of persons and the maximum height of buildings is configurable by users of this tool.

## Challenges we ran into
Having never worked with big data analyzation and LIDAR data processing before, we had to spend a considerable ammount of time reading into these topics to accomplish the current state of this project. 

## Installation
First of all, clone the project into your desired directory:  
`git clone https://github.com/Skypr/Hacktival2019`  

We use Python 3.6+ and pip3 for the project and it's dependencies, so make sure you are up to the newest version:  
`python3 --version`  
`pip3 --version`  

The project was written in jupyter for easier understanding:  
`pip3 install jupyter`  

To start jupyter, type `jupyter notebook` in your command line switch to the cloned archive and open `Mit OpenStreetMap.ipynb`
