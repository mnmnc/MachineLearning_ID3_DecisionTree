MachineLearning_ID3_DecisionTree
================================

Decision Tree creation with ID3 algorithm implemented in Python3. 

## OUTPUT:
```python
                [DBG] No root detected. Searching for first one.
                [DBG] New root found: AURA
                Calculation for: AURA = Sunny
                        Calculation for: WILG = High
                                        Decision:   PLAY = 0
                        Calculation for: WILG = Normal
                                        Decision:   PLAY = 1
                Calculation for: AURA = Cloudy
                                Decision:   PLAY = 1
                Calculation for: AURA = Raining
                        Calculation for: WIND = Low
                                        Decision:   PLAY = 1
                        Calculation for: WIND = High
                                        Decision:   PLAY = 0

```

## OUTPUT IN DEBUG MODE:
```python
                [DBG] No root detected. Searching for first one.
                [DBG] Counted 5 0 values for PLAY attribute.
                [DBG] Counted 9 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9402859586706309
                [DBG] Calculating for AURA  for value 0
                [DBG] Calculating for AURA  for value 1
                [DBG] Calculating for AURA  for value 2
                [DBG] Gain for attribute AURA is 0.2467498197744391
                [DBG] Counted 5 0 values for PLAY attribute.
                [DBG] Counted 9 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9402859586706309
                [DBG] Calculating for WIND  for value 1
                [DBG] Calculating for WIND  for value 0
                [DBG] Gain for attribute WIND is 0.04812703040826932
                [DBG] Counted 5 0 values for PLAY attribute.
                [DBG] Counted 9 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9402859586706309
                [DBG] Calculating for TEMP  for value 0
                [DBG] Calculating for TEMP  for value 1
                [DBG] Calculating for TEMP  for value 2
                [DBG] Gain for attribute TEMP is 0.029222565658954647
                [DBG] Counted 5 0 values for PLAY attribute.
                [DBG] Counted 9 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9402859586706309
                [DBG] Calculating for WILG  for value 0
                [DBG] Calculating for WILG  for value 1
                [DBG] Gain for attribute WILG is 0.15183550136234142
                [DBG] Highest gain given by attribute: AURA
                [DBG] New root found: AURA
                [DBG] Getting unique values for  AURA
                Calculation for: AURA = Sunny
[       {'PLAY': 0, 'TEMP': 0, 'WILG': 0, 'WIND': 1},
        {'PLAY': 0, 'TEMP': 0, 'WILG': 0, 'WIND': 0},
        {'PLAY': 0, 'TEMP': 1, 'WILG': 0, 'WIND': 1},
        {'PLAY': 1, 'TEMP': 2, 'WILG': 1, 'WIND': 1},
        {'PLAY': 1, 'TEMP': 1, 'WILG': 1, 'WIND': 0}]
                [DBG] Counted 3 0 values for PLAY attribute.
                [DBG] Counted 2 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for WIND  for value 1
                [DBG] Calculating for WIND  for value 0
                [DBG] Gain for attribute WIND is 0.01997309402197489
                [DBG] Counted 3 0 values for PLAY attribute.
                [DBG] Counted 2 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for TEMP  for value 0
                [DBG] Calculating for TEMP  for value 1
                [DBG] Calculating for TEMP  for value 2
                [DBG] Gain for attribute TEMP is 0.5709505944546686
                [DBG] Counted 3 0 values for PLAY attribute.
                [DBG] Counted 2 1 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for WILG  for value 0
                [DBG] Calculating for WILG  for value 1
                [DBG] Gain for attribute WILG is 0.9709505944546686
                [DBG] Highest gain given by attribute: WILG
        Found new root: WILG
                [DBG] Getting unique values for  WILG
                        Calculation for: WILG = High
[       {'PLAY': 0, 'TEMP': 0, 'WIND': 1},
        {'PLAY': 0, 'TEMP': 0, 'WIND': 0},
        {'PLAY': 0, 'TEMP': 1, 'WIND': 1}]
                                        Decision:   PLAY = 0
                        Calculation for: WILG = Normal
[{'PLAY': 1, 'TEMP': 2, 'WIND': 1}, {'PLAY': 1, 'TEMP': 1, 'WIND': 0}]
                                        Decision:   PLAY = 1
                Calculation for: AURA = Cloudy
[       {'PLAY': 1, 'TEMP': 0, 'WILG': 0, 'WIND': 1},
        {'PLAY': 1, 'TEMP': 2, 'WILG': 1, 'WIND': 0},
        {'PLAY': 1, 'TEMP': 1, 'WILG': 0, 'WIND': 0},
        {'PLAY': 1, 'TEMP': 0, 'WILG': 1, 'WIND': 1}]
                                Decision:   PLAY = 1
                Calculation for: AURA = Raining
[       {'PLAY': 1, 'TEMP': 1, 'WILG': 0, 'WIND': 1},
        {'PLAY': 1, 'TEMP': 2, 'WILG': 1, 'WIND': 1},
        {'PLAY': 0, 'TEMP': 2, 'WILG': 1, 'WIND': 0},
        {'PLAY': 1, 'TEMP': 1, 'WILG': 1, 'WIND': 1},
        {'PLAY': 0, 'TEMP': 1, 'WILG': 0, 'WIND': 0}]
                [DBG] Counted 3 1 values for PLAY attribute.
                [DBG] Counted 2 0 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for WIND  for value 1
                [DBG] Calculating for WIND  for value 0
                [DBG] Gain for attribute WIND is 0.9709505944546686
                [DBG] Counted 3 1 values for PLAY attribute.
                [DBG] Counted 2 0 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for TEMP  for value 1
                [DBG] Calculating for TEMP  for value 2
                [DBG] Gain for attribute TEMP is 0.01997309402197489
                [DBG] Counted 3 1 values for PLAY attribute.
                [DBG] Counted 2 0 values for PLAY attribute.
                [DBG] Full data entropy: 0.9709505944546686
                [DBG] Calculating for WILG  for value 0
                [DBG] Calculating for WILG  for value 1
                [DBG] Gain for attribute WILG is 0.01997309402197489
                [DBG] Highest gain given by attribute: WIND
        Found new root: WIND
                [DBG] Getting unique values for  WIND
                        Calculation for: WIND = Low
[       {'PLAY': 1, 'TEMP': 1, 'WILG': 0},
        {'PLAY': 1, 'TEMP': 2, 'WILG': 1},
        {'PLAY': 1, 'TEMP': 1, 'WILG': 1}]
                                        Decision:   PLAY = 1
                        Calculation for: WIND = High
[{'PLAY': 0, 'TEMP': 2, 'WILG': 1}, {'PLAY': 0, 'TEMP': 1, 'WILG': 0}]
                                        Decision:   PLAY = 0

```
