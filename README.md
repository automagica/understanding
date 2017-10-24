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
Set environment variable `UNDERSTANDING_API_KEY` to for example your Wit.ai key. As an alternative, you can provide the `api_key` keyword argument for the `Understanding` object.

Initialize the `Understanding` object, providing the service name (`wit` currently only supported).
```
understand = Understanding('<service>')
```

Messages can then be parsed through:
```
understand.parse('I would like to order two beers and one coke')
```
This will result in a dictionary containing the parsed message for intents and entities.