# Ball-Trajectory
This project, as the name clearly states, is the study of a ball trajectory. In particular, a basketball trajectory! <br/>
The idea behind this project is to have a fun and not-too-complex physics problem that can be explored using technology. <br/>
The end goal is to engage with students, kids, nephews or STEM enthusiasts in general (in my case it was my younger cousins), and introduce them to the wonders of physics, engineering and technology in a practical and results-oriented approach. <br/>
The project is composed by the following phases:
1. *Experimental*: consists in preparing the experimental setup, measuring the properties of the ball, performing the experiments (ball drop, throw, bounce) and recording with a camera.
1. *Processing with Blender*: consists in processing the camera recordings from the previous phase (tracking of the ball) and exporting the *x,y* coordinates into the *OUTPUT.csv* file. This is performed using the Python script *export_trajectory.py* inside the Blender environemnt.
1. *Simulation with Python*: consists in performing simulations of the ball trajectory, solving the ordinary differential equation system associated. The simulation is performed using the *solve_trajectory.py* script.
1. *Comparison and conclusions*: consists in comparing the trajectory obtained from the experiments and the simulations and drawing the relevant conclusions.
<a/>
Each phase can be used to showcase/teach a different theoretical and practical concept. The in-depth level of the concepts can be tailored to the target education and knowledge. </br>
For example, the simulation phase can be presented as a magic tool that predicts the future for the youngest, or can be explained much more in depth to more advanced students, showing a practical example of equation of motion numerical integration, more or less complex models for gravity and drag. </br>

![pic1_0](https://user-images.githubusercontent.com/63881945/97815162-835f6b80-1c8c-11eb-99d7-018cd3a13ae0.PNG)
![pic1_1](https://user-images.githubusercontent.com/63881945/97815133-527f3680-1c8c-11eb-8a4d-51b8b8831806.PNG)
![pic1_2](https://user-images.githubusercontent.com/63881945/97815155-7773a980-1c8c-11eb-8bee-ab94691746bc.PNG)
