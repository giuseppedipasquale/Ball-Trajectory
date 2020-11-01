# Ball-Trajectory
This project, as the name clearly states, is the study of a ball trajectory. In particular, a basketball trajectory! <br/>
The idea behind this project is to have a fun and not-too-complex physics problem that can be explored using technology. <br/>
The endgoal is to engage with students, kids, nephews or whoever is enthusiast about STEM (in my case it was my younger cousins), and introduce them to the wonders of physics, engineering and technology in a practical and results-oriented approach. <br/>
The project consists in the following phases:
1. *Experimental phase*: consists in preparing the experimental setup, measuring the properties of the ball, performing the experiments (ball drop, throw, bounce) and recording with a camera.
1. *Processing with Blender*: consists in processing the camera recordings from the previous phase (tracking of the ball) and exporting the *x,y* coordinates into the OUTPUT.csv file. This is performed using the Python script export_trajectory.py inside the Blender environemnt.
1. *Simulation with Python*: consists in performing simulations of the ball trajectory, solving the ordinary differential equation system associated. The simulation is performed using the solve_trajectory.py script.
1. *Comparison and conclusions*: consists in comparing the trajectory obtained from the experiments and the simulations and drawing the relevant conclusions.


