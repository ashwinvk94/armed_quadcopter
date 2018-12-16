# Armed Quacopter

This repository contains the files to simulate a quadcopter with a 3 degree of freedom robot attatched to its bottom.

### Prerequisites

* Install [V-REP](http://www.coppeliarobotics.com/downloads.html)

## Running the Pick and Place demonstration
Open the V-REP simulation environment and open the pick_place_cylinder.ttt files provided in the "scenes" folder.
Open a terminal in the local repository directory and run the python file using the command,
```
python pick_place.py
```
![sim_pic_1](https://user-images.githubusercontent.com/35679537/50048636-81dc2880-009f-11e9-806a-3445c7e62ad7.png)
Open the pick_place_cuboid.ttt file in order to view the simulation for the pick and place of a cuboid object. To run the simulation, run the same python file mentioned above.

## Running the Inverse Kinematics demonstration
In this demo, the user can vary the position and orientation of the object and the quadcopter and the arm will automatically orient so as to grasp the object. In this demo, the object has been made massless and non-respondable for a better demonstration.

Open the V-REP simulation environment and open the ik.ttt files provided in the "scenes" folder.
Open a terminal in the local repository directory and run the python file using the command,
```
python ik.py
```
![inverse_kinematics](https://user-images.githubusercontent.com/35679537/50048639-9cae9d00-009f-11e9-9659-71a9fb2c9cb7.png)
The quadcopter should move to the grasping position. Now you can vary the position and orientation of the cylindrical object by using V-REP's built-in [objectMovement UI](http://www.coppeliarobotics.com/helpFiles/en/objectMovement.htm)  The quadcopter should move so as to grasp the object in the updated position and orientation.

Demonstration videos can be found at:
(https://www.youtube.com/watch?v=TAcblA4842w)
(https://www.youtube.com/watch?v=bQ_WQfneV_g)
(https://www.youtube.com/watch?v=F-4HzJd8PGQ&t=1s)

## Built With

* [V-REP](http://www.dropwizard.io/1.0.2/docs/) - The V-REP Simulation Framework
* [Python](https://www.python.org/) - The python programming language

## Authors

* **Ashwin Varghese Kuruttukulam** 

## License

This project is licensed under the MIT License
