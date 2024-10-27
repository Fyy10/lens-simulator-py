<!-- TOC -->
* [lens-simulator](#lens-simulator)
  * [Usage](#usage)
  * [Scene](#scene)
  * [Results](#results)
<!-- TOC -->

# lens-simulator

Simulate lens behavior through path tracing

## Usage

Set lens properties in `utils/Config.py` and run `main(filename)` from `main.py`.

The output image will be in the `img` folder.

## Scene

![scene](scene.png)

## Results

f/2 aperture focused at 100mm with variable focal length:

![f2_100](img/combined/f2_100.png)

50mm lens focused at 100mm with variable aperture:

![50mm_100](img/combined/50mm_100.png)

50mm f/1.8 with variable focal distance:

![50mm_f1.8](img/combined/50mm_f1.8.png)

equivalent focal length (sensor size changes):

$$
f=\frac{1}{\frac{\ell'}{\ell}\cdot\frac{1}{f'} + \frac{1}{u}\left(1-\frac{\ell'}{\ell}\right)}
$$

![exp_dof](img/exp_dof/exp_dof.png)
