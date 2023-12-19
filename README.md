# Secret Santa
### Execution
#### Environment
python 3.11
#### To Test
pytest
#### To run
python3 secretsanta.py
or
python3 -m secretsanta


### Target
1. read from input json to class participant
2. random match output should have no duplication nor left out
3. send out email
4. support invalid match


### Input format
```Json
{
  "participants": [
    {
      "name":"name",
      "email": "email@email.com",
      "address": "address"
    }
  ],
  "invalid_match": [
    ["awwwww", "bobbingbobb"],
  ]
}
```