import operator

# Mapping of operators strings to their functions so we can use them as strings only and not need a lot of if else statements
#all the time and if a new operator is added we just need to add it here
OPERATOR_MAP = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}
