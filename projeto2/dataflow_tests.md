# Dataflow testing
X -> covered

-   `frame, ignore`
    du path:

    1. 1-2 -> any complete path  X

-   `multivars`
    du paths:
    isinstance(ast.AnnAssign) True
    1. 1-2-3-7-8-12-13-14-16  -> (unfeasible) se passa no 8 tem que passar no 15
    2. 1-2-3-7-8-12-13-14-17 (complete/unfeasible)        
    3. 1-2-3-7-8-12-13-15-14-17 (complete) X         
    4. 1-2-3-7-8-12-13-15-14-16 -> 1-2-3-7-8-12-13-15-14-16-18 X

    isinstance(ast.AnnAssign) False
        len(node.targets <=1)
    5. 1-2-3-7-9-10-12-13-14-17 (complete)
    6. 1-2-3-7-9-10-12-13-14-16 -> 1-2-3-7-9-10-12-13-14-16-19 X
    7. 1-2-3-7-9-10-12-13-15-14-17 (complete) X
    8. 1-2-3-7-9-10-12-13-15-14-16 -> 1-2-3-7-9-10-12-13-15-14-16-18 X

        len(node.targets > 1)
    9. 1-2-3-7-9-11-10-12-13-14-17 (complete) X
    10. 1-2-3-7-9-11-10-12-13-14-16 -> 1-2-3-7-9-11-10-12-13-14-16-19 X
    11. 1-2-3-7-9-11-10-12-13-15-14-17 (complete) X
    12. 1-2-3-7-9-11-10-12-13-15-14-16 -> 1-2-3-7-9-11-10-12-13-15-14-16-18
    

-   `raise_exc`
    du paths:

    1. 1-2          X
    2. 1-2-4-5      (complete)  NOT
    3. 1-2-4-6      (complete)  NOT
    4. 1-2-3-20-21   (complete)  NOT
    5. 1-2-3-20-22   (complete) NOT

-   `node`
    du paths:
    1. 2-3                      X
    2. 2-4                      NOT
    3. 3-20                     NOT
    4. 3-7                      X
    5. 3-7-9                    X
    6. 3-7-9-10                 X
    7. 3-7-9-11                 X
    8. 3-7-8 (p. use and c.use) X
    9. 3-7-9-10-12              X
    10. 3-7-9-11-10-12          X
    11. 3-7-8-12                X

-   `target`
    du paths:
    1. 8-12     X
    2. 10-12    X

-   `names`
    du paths:           X
    1. 12-13-14         X
    2. 12-13-15         X
    3. 12-13-14-17      X
    4. 12-13-14-16-18   X
    5. 12-13-14-16-19   X

    6. 15-14-17         X
    7. 15-14-16-18      X
    8. 15-14-16-19      (unfeasible)
