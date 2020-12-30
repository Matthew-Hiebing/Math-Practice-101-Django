# Math Game Practice App :woman_teacher:
This project was created to help 3rd graders practice their math skills at one of my local elementary schools.  Typically, students have a hard time switching between operators (multiplication, division, addition, and subtraction).  The goal of the project was to get them accustomed to rapid math problem changes and practice their skills for the state's STAR tests.

Currently, the back-end and front-end is handled by Django (Python, CSS, HTML, JS) but another project is being built to handle the front-end using React.  The repo for this project is called, "Python-Math-Game-Front-End".

Some improvements that I may implement at a later date:\
1.) Difficulty Selection - Increasee or decrease the random integers that are used in the math problems.\
2.) Operator Selection - Allow users to select what type of math problems they want to see.\
3.) Problem Batch Mode - Give the users pre-made batches of problems instead of one at a time.\
4.) Improved Stats Analysis - Give the teacher a better overview of the students performance using graphs/charts.\

Click [here](https://math-game-practice.herokuapp.com/) to visit the in-production site hosted on Heroku.

## Installation
```bash
pip install django # You will need Django for the web development part of this project
pip install -r requirements.txt # Run this command to install all the necessary packages
```

## Usage

```python
import random
from random import choice

random.randint(0,12) # Returns a random number between 0 and 12
random.choice([func1,func2,func3]) # Returns a random element from a non-empty sequence item from a list, set, tuple, or dictionary

```
## Creators
Matthew Hiebing: [Matthew-Hiebing](https://github.com/Matthew-Hiebing)\
Guillermo Vargas: [gavargas22](https://github.com/gavargas22)

## Questions?
Send me a message on GitHub ([Matthew-Hiebing](https://github.com/Matthew-Hiebing) or E-mail me at: Matthew.Hiebing@gmail.com.

## License
Copyright 2020

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
