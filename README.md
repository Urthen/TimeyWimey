#Timey Wimey

The only programming language that looks good in a bow tie. The basic concept is that while execution continues linearly, updates to variables can be propagated both forwards and backwards in time.

## Concepts

### statement
An individual line of code is a statement. Statements may be nested to form code blocks. For example, while/when/if blocks, as well as time locks, both nest statements inside themselves.

A statement can be unexecuted, executing, waiting, or exhausted.

Unexecuted statements are statements within an execution which are not parsed as waiting, but have not yet been reached by execution.
Waiting means this statement was parsed but a conditional is not yet met, so it has not actually done anything.
Executing means this is the current statement being processed in a given execution (see below). Due to nesting execution/propagation, more than one statment can be marked as executing at a time, but one statement cannot be executed again while it is still marked as executing.
Exhausted statments were executed successfully and will not be executed again.

Statements consist of precisely one operator. Each operator is a node. Operators can have operands, each of which is a node. Nodes can be constants, variables, or another operator.
Some operators have a nested execution (WHILE/WHEN/IF/LOCK) - these operators themselves cannot be an operand of another operator.

### execution
An execution is simply a list of statements. Statements are executed in the order they are in the file. However, statements which cannot be evaluated (due to variable not defined) are stored as unexecuted. WHILE and WHEN blocks also are stored, though they can be executed immediately if their conditional is true.

Execution of a statement consists of the actual statement execution (including storing of unexecutable statements or while/when blocks), then if a change was made, propogation of that change.

Execution ends once the last statement has been read and (if possible) executed, even if there are statements left unexecuted. These merely represent unused code branches.

### propogation
When any change to variable state is made (define or set a variable, delete a variable), that change immediately propogates outwards (alternating up and down a statement at a time) and causes re-evaluation of waiting statements or while/when conditionals which references that variable. This allows variables to be used towards the top of a file, but defined at the bottom. This wave of execution is simply referred to as propogation.

Propogation nests, so a propogation which triggers another change starts the new propogation immediately, then (normally) resumes the previous propogation. If the second change is to the same variable that is currently propogating, it stops the first propogation before starting the new one.

Once propogation of a change is completed, execution continues.

Execution can also nest within propogation (see next section). Execution differs from propogation in that propogation expands in both directions and will only evaluate unexecuted statements, or re-evaluate while/when conditions. Execution only expands downwards, and executes each statement in line.

### while/when/if statements
WHILE and WHEN both begin execution when a propogation is recieved setting the condition from false to true. That propogation is paused until their code block execution is complete.
IF begins execution whenever propogation is recieved and the condition is true - even if it was already true, unlike WHILE/WHEN.

All execute their code blocks to completion even if the code block changes the condition to false.

Statements within a WHILE/WHEN/IF code block do not recieve propogation from outside the block, but do send out propogation immediately. The code block does not act like a time lock.

In a WHILE block, if the condition is still true at the end of the code block, it will return execution to the top of the code block.
WHEN and IF blocks always end execution at the end of the code block.
WHEN blocks will not execute again until the condition transitions to false, then true again. IF statements will execute again on any change to their variables, so long as the conditional is still true.

WHEN statements are waiting when false, executing after set to true, then exhasted after the code block.
IF and WHILE statements are always waiting unless they are executing.

### paradox

A paradox (effectively, infinite loop) can occur when one WHEN/WHILE statement causes a propogation that triggers another WHEN/WHILE statement, which propogates back and triggers the first.
To resolve this, a WHEN/WHILE statement will not be re-evaluated for execution stealing until after the code block executes.

For example:


    when = x 3
        x = 5

    when = x 5
        x = 3

    x = 3


would set X to 3, trigger the first WHEN, which sets x to 5, triggering the second WHEN, which sets x to 3. The first WHEN will not be re-evaluated until execution of the code block has finished, which is after the x = 5 statement was executed and x = 3 statement has propogated back. Therefore, the first WHEN does not realize it was ever false.

### time lock
A time lock is a block that "freezes" exterior propogation when executed, and allows the interior to execute and propogate to completion before returning execution to the outer time context.
Once a lock has been exited, any changed variables propogate outside the lock (in normal up/down order from the top and bottom of the lock) in the order of which they were changed.
A variable that has been changed multiple times only propogates the latest result.
A variable that was created and undefined in the same block does not propogate any changes.
Time locks may be nested.


## Operators


    //			Comment - line is ignored

    (any type)
    = x y		Sets x to y, returns new value of y
    == x y		Returns equality of x and y
    ? x			Returns true if x is set.
    print x		Prints x immediately when executed

    (number only)
    (in place and return result)
    ++ x
    += x y
    -- x
    -= x y
    (return value)
    / x y
    + x y
    - x y
    > x y
    >= x y
    < x y
    <= x y


    (string only)
    +$ x .. y	Concatenate x, y, etc

    (boolean only)
    & x .. y	AND of x .. y
    | x .. y	OR of x .. y
    ! x			NOT x
