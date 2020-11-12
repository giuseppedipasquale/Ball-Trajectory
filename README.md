# trajectoryanalyst
This project, as the name clearly states, is the study of a ball trajectory. In particular, a basketball trajectory! <br/>
The idea behind this project is to have a fun and not-too-complex physics problem that can be explored using technology. <br/>
The end goal is to engage with students, kids, nephews or STEM enthusiasts in general (in my case it was my younger cousins), and introduce them to the wonders of physics, engineering and technology in a practical and results-oriented approach. <br/>
The project is divided in phases. Each phase can be used to showcase/teach a different theoretical and practical concept. The in-depth level of the concepts can be tailored to the target education and knowledge. </br>
1. *Experimental Phase*: consists in preparing the experimental setup, measuring the properties of the ball, performing the experiments (ball drop, throw, bounce) and recording with a camera. In this phase it is important to emphasize the practical issues, and show, in conjuncion with the following phases, how they affect the end result. From the very first phase it is possible to pose challenges that may go from the basic "How to measure the diameter of the ball with good precision?" to how to make sure the measurements are as accurate as possible and the conversion from "video" to S.I. units is reliable (for more advanced).
1. *Data processing*: consists in processing the camera recordings from the previous phase (tracking of the ball) with Blender and exporting the *x,y* coordinates into the *OUTPUT.csv* file. This is performed using the Python script *export_trajectory.py* inside the Blender environemnt. Below a gif showing the video of my cousins (Chiara and Davide, right to left) playing with the ball, being tracked using the tracking tool of Blender.
![](ball_traj.gif)
1. *Simulation with Python*: consists in performing simulations of the ball trajectory, solving the ordinary differential equation system associated. The simulation is performed using the *solve_trajectory.py* script.
The simulation phase can be presented as a magic tool that predicts the future for the youngest, or can be explained much more in depth to the eldest, showing a practical example of equation of motion numerical integration, more or less complex models for gravity and drag, etc. </br>
1. *Comparison and conclusions*: consists in comparing the trajectory obtained from the experiments and the simulations and drawing the relevant conclusions.
When it comes down to comparing simulation and experiments I believe is fun to show how the assumptions affect the simulation.
For example, if one considers only gravity in the simulation, the two trajectories are a bit different.
![pic1_2](https://user-images.githubusercontent.com/63881945/97815155-7773a980-1c8c-11eb-8bee-ab94691746bc.PNG)
But if the drag is also taken into account, the result is much closer.
![pic1_1](https://user-images.githubusercontent.com/63881945/97815133-527f3680-1c8c-11eb-8a4d-51b8b8831806.PNG)
<a/>

Another example is the pendulum. In the figure below it is possible to appreciate a plot of the measured angle with respect to the vertical against the simulation results.
![pendulum1](https://user-images.githubusercontent.com/63881945/98943353-a2ad9280-24ef-11eb-93f2-9a8d761e0ccf.PNG)


One thing that is very important, in my opinion, is to ask always before, what they expect is going to happen and make them do the work, get their hands dirty, get the wrong path and learn from it.
Have fun!



