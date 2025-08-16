## Prepcode

```
FUNCTION even_or_odd(number: integer) RETURNS string
    GET the number as an integer parameter
    CHECK if the number is divisible by 2
        IF the number is divisible by 2 no remainder
            RETURN "Even"
        ELSE the number has a remainder when divided by 2
            RETURN "Odd"
        END IF
END FUNCTION
```
