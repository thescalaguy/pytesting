# Property-based testing  

Property-based testing is a technique for testing software where we specify certain properties that the code under test should satisfy. 
A test harness then checks the code by running it against a broad range of generated inputs.   

For example, we can have a function `f(x: int)` which should work for all positive integers. A property-based test would test this function by generating 
positive integers, negative integers, very large or very small integers, and so on. The function should behave as expected for all these inputs.  

This repository contains examples for property testing Python code using [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).  

## Running the code  

Install Poetry  

```shell
pip install poetry
```  

Install the packages  

```shell
poetry install
```  

Bring up the Docker containers

```shell
docker-compose up -d
```  

Run the tests  

```shell
PYTHONPATH=. pytest .
```