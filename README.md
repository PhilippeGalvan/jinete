
# jinete

<img align="right" width="15%" src="https://raw.githubusercontent.com/garciparedes/jinete/master/res/images/jinete.svg?sanitize=true" alt="jinete">

[![PyPI](https://img.shields.io/pypi/v/jinete.svg)](https://pypi.org/project/jinete)
[![Read the Docs](https://img.shields.io/readthedocs/jinete.svg)](https://jinete.readthedocs.io/)
[![Travis (.org) branch](https://img.shields.io/travis/garciparedes/jinete/master.svg)](https://travis-ci.org/garciparedes/jinete/branches)
[![Codecov](https://img.shields.io/codecov/c/github/garciparedes/jinete.svg)](https://codecov.io/gh/garciparedes/jinete)
[![GitHub](https://img.shields.io/github/license/garciparedes/jinete.svg)](https://github.com/garciparedes/jinete/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/garciparedes/jinete.svg)](https://github.com/garciparedes/jinete)

## Description 

High Performance solving suite for the Pickup and Delivery Problem and its related extensions. 

*IMPORTANT*: This project is still under its early stage of development. So it's not recommended yet to use on real world projects. 

This library has been inspired (and created) by a Final Degree Project, which you can read at: https://github.com/garciparedes/tfg-pickup-and-delivery


## Getting Started

### Prerequisites
* `python>=3.7`

### Installation
```bash
pip install jinete
```

Here is a simple example about how to run `jinete` to solve a HashCode 2018 Online Qualification instance. 
```python
import jinete as jit

file_path = './res/datasets/hashcode/a_example.in'

solver = jit.Solver(
    loader=jit.FileLoader,
    loader_kwargs={
        'file_path': file_path,
        'formatter_cls': jit.HashCodeLoaderFormatter
    },
    algorithm=jit.InsertionAlgorithm,
)
result = solver.solve()
# ...

```

## Documentation
You can find the documentation at: https://jinete.readthedocs.io


## Development

First of all, you need to create a `virtualenv`:

```bash
python -m venv venv
source venv/bin/activate
```

Then install the library and all its extra dependencies (with the `all` option):

```bash
pip intall -e .[all]
```

To run code style checks you can simply type:
```bash
flake8
```

To perform the tests with coverage you can need to type:

```bash
coverage run -m unittest discover tests
```

## Repository Contents

* [`examples`](https://github.com/garciparedes/jinete/tree/master/examples/): Basic examples to start using the library.
* [`jinete`](https://github.com/garciparedes/jinete/tree/master/jinete/): The source code of the library.
  * [`algorithms`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/): [TODO]
    * [`exacts`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/exacts): [TODO]
    * [`heuristics`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/heuristics): [TODO]
    * [`metaheuristics`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/metaheuristics): [TODO]
    * [`utils`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/utils): [TODO]
      * [`crossers`](https://github.com/garciparedes/jinete/tree/master/jinete/algorithms/utils/crossers): [TODO]
  * [`dispatchers`](https://github.com/garciparedes/jinete/tree/master/jinete/dispatchers/): [TODO]
  * [`loaders`](https://github.com/garciparedes/jinete/tree/master/jinete/loaders/): [TODO]
    * [`formatters`](https://github.com/garciparedes/jinete/tree/master/jinete/loaders/formatters/): [TODO]
  * [`models`](https://github.com/garciparedes/jinete/tree/master/jinete/models/): [TODO]
  * [`storers`](https://github.com/garciparedes/jinete/tree/master/jinete/storers/): [TODO]
    * [`formatters`](https://github.com/garciparedes/jinete/tree/master/jinete/storers/formatters/): [TODO]
* [`setup.py`](https://github.com/garciparedes/jinete/tree/master/setup.py): The builder of this library.
* [`tests`](https://github.com/garciparedes/jinete/tree/master/tests/): The library tests.

## LICENSE
This project is licensed under [MIT](LICENSE) license.
