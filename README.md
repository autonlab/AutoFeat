[![Typing SVG](https://readme-typing-svg.demolab.com?font=Georgia&size=26&duration=4000&pause=400&color=F70000&vCenter=true&multiline=true&width=750&height=100&lines=AutoFeat;A+High+Performance+Library+for+Time-Series+Featurization)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.9.6-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.24.4-lightblue)
[![License](https://img.shields.io/badge/License-Apache_2.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)

# ⏳ AutoFeat ⌛

A high performance library for time series featurization. 

## What? 🙋

`AutoFeat` is a high-performant domain agnostic package for time series featurization. Despite the domain agnostic focus of the package, we recognize the benefit of domain knowledge and have included a few domain specific featurizers for popular domains like healthcare. With time series data, as with any data, it is often helpful to perform preprocessing before extracting information from it such as exploring the frequency domain as well as the time domain. We have provided a number of preprocessors that can transform the distribution or space to a form more amenable to certain featurizations. The package is lightweight, fast and easy to use. We hope you enjoy it! 🎉

## Why? 🤔

To prevent others from reinventing the wheel, we have compiled a featurization library for dealing with time-series data. We have also included a number of preprocessors to transform the data into a form more amenable to certain featurizations. Finally, our goal was to make this package without too many dependencies and overhead.

AutoFeat provides a number of advantages over other packages:
- **Simple**: The package must be easy to use and require as little user input as possible.
- **Interpretable**: The software abstractions must be intuitive, easy to understand and easy to debug.
- **Fast**: The tool must be fast enough to be used in large scale production environments.
- **Flexible**: The package must be modular and allow for easy extensibility to leverage community contributions.

## Assumptions 🧐

**Note**: We have made a few assumptions to start out with but we are working on making the package more flexible and robust. If you have any suggestions, please open an issue or PR! 🙂

> - The input data is a **1D** time series in the form of a **numpy array**.
> - If there are missing values, they must be represented by `np.nan` to be detected, otherwise, gaps in the time series are **not** detected.

## Installation 📦

```bash
pip install autofeat
```

*Installing inside a python virtual environment or a conda environment is recommended.*

## Features 🧠

We provide a variety of features ranging from domain agnostic to domain specific (e.g. healthcare) featurizers, as well as a number of preprocessors to transform the data into a form more amenable to certain featurizations. This list is constantly growing so please check back often! Feel free to contribute your own featurizers and open a PR! 🎉

## Contributing 🤝

We'd love to hear from you! If you've found anything missing, feel free to open an issue or PR! 🙂

## Authors 👨‍💻

[Dhruv Srikanth](https://dhruvsrikanth.github.io)

[Auton Lab](https://autonlab.org)

## License 📝

[![License](https://img.shields.io/badge/License-Apache_2.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)

For more details, check out the license [here](https://github.com/autonlab/AutoFeat/blob/main/LICENSE).


If you enjoy using `AutoFeat`, please consider starring the [repository](https://github.com/autonlab/AutoFeat) ⭐️.
