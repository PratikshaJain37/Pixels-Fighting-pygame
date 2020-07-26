# Pixels Fighting (Pygame)

Which colour will win? It's random!

A zero player game, inspired by the "viral" http://pixelsfighting.com/ and loosely based on <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's Game Of Life</a>, made using Pygame.

<screenshot here>
<hr>

## Prerequisites

You will need to install Pygame to run this. It is recommended that you run the project on a virtual environment, and that you build pygame, rather than installing it with pip (for optimal CPU usage).
Refer to [this](http://www.pygame.org/wiki/CompileUbuntu#Python%203.x%20into%20vihref=rtual%20environment) guide.


## Getting Started

Once you have pygame and the virtual environment setup, clone this repository.
```
$ git clone https://github.com/PratikshaJain37/pixels-fighting-pygame
```
After making sure you are in the directory which contains the code, run the 'main' script using python3
```
$ cd pixels-fighting-pygame
$ python3 main.py
```
A pygame window should appear, with the simulated Pixels Fighting game starting.


## Testing and Tweaking the code

You are welcome to tweak and test the code for a variety of inputs. 

* SIZE determines the size of the individual 'Boxes' which contain colour. 
* INT determines the number of pixels that will be 'fighting'. (Technically, it is determined by INT_SQ)
    You can adjust SIZE and INT for more clarity. However, having a high INT will result in more CPU consumption.
* The FPS can be adjusted using the time.sleep() function at the end of the main loop. It is currently set to update every 0.1 seconds.
* Feel free to adjust the colours :P


<hr>

## Contributing

If you have some suggestions, feel free to raise an Issue and submit a pull request!



## License

This project is licensed under the MIT License.
