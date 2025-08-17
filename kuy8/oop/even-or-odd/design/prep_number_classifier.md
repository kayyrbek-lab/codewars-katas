## Prepcode

```
CLASS NumberClassifier
    METHOD __init__(number: int)
        VALIDATE that number is an integer
        STORE number as instance attribute


    METHOD classify()   RETURNS str
        CHECK if the stored number is divisible by 2
            IF divisible with no remainder
                RETURN "Even"
            ELSE
                RETURN "Odd"
            END IF
END CLASS
```
