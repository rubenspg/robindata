# Robindata

Robindata is a simple command line tool written in Python to interact with [Robinhood](https://robinhood.com) app.

There are some useful commands like:
1) Export all your transactions to a CSV file;
2) Show the performance of your portfolio or trades (per a given period of time);


## Usage

### How to Install

#### Requirements

- Python 3.6+
- Pip

1) Clone this repository

```sh
$ git clone ...
```

2) Enter in the source code directory and install right from the source (or via pip from PyPI):

```sh
$ python setup.py install
```

## Commands

### Export transactions

The following command will connect to Robinhood and export all your transactions to a CSV file and store it in your local directory.

```sh
$ robindata export-transactions
```

### Resources
The interaction with Robinhood API is made by this [Robinhood library](https://github.com/robinhood-unofficial/pyrh).

## Contribution
Feel free to fork and make Pull Requests to this repo adding more functionalities.
