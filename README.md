# Understanding
Understanding module for chat bots.

## Requirements
Python 3+

## Installation
```
git clone <this repo url>
cd understanding
pip install .
```

## Example usage
Initialize the `Understanding` object, providing the service name (`wit` currently only supported) and API key.
```
understand = Understanding('<service>','<api-key>')
```

Messages can then be parsed through:
```
understand.parse('I would like to order two beers and one coke')
```
This will result in a dictionary containing the parsed message for intents and entities.