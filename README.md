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

Open the pick_place_cuboid.ttt file in order to view the simulation for the pick and place of a cuboid object. To run the simulation, run the same python file mentioned above.

## Running the Inverse Kinematics demonstration
In this demo, the user can vary the position and orientation of the object and the quadcopter and the arm will automatically orient so as to grasp the object. In this demo, the object has been made massless and non-respondable for a better demonstration.

Open the V-REP simulation environment and open the ik.ttt files provided in the "scenes" folder.
Open a terminal in the local repository directory and run the python file using the command,
```
python ik.py
```

The quadcopter should move to the grasping position. Now you can vary the position and orientation of the cylindrical object by using V-REP's built-in [objectMovement UI](http://www.coppeliarobotics.com/helpFiles/en/objectMovement.htm)  The quadcopter should move so as to grasp the object in the updated position and orientation.


## Built With

* [V-REP](http://www.dropwizard.io/1.0.2/docs/) - The V-REP Simulation Framework
* [Python](https://www.python.org/) - The python programming language

## Authors

* **Ashwin Varghese Kuruttukulam** 

## License

This project is licensed under the MIT License
