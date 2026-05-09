# Functional Core, Imperative Shell

Push decisions to the center. Push side effects to the edge.

## Structure

- **Functional core**: pure functions. Input in, output out. No IO. No state mutation. No clock. No randomness.
- **Imperative shell**: reads from the world (DB, API, clock, user input), calls the core, writes results back.

The shell is thin. The core is thick. All interesting logic lives in the core.

## Properties of the core

- Given same input, always same output.
- No exception thrown for business decisions. Return result types instead.
- Fully testable without mocks, databases, or network.

## Properties of the shell

- Performs IO.
- Passes real data to the core.
- Writes core output to the world.
- Handles infrastructure errors.

## Decision rules

- Business rule that transforms data → core.
- Database read or write → shell.
- Sending email or publishing event → shell.
- Decision based on current time → pass the time as parameter into the core.
- Random value needed → generate in shell, pass into core.
- If a function cannot be tested without mocking → it has IO that belongs in the shell.

## Smells

- business logic inside a function that also calls the database
- core function that calls `datetime.now()` or `random.uuid()` internally
- unit test that requires mocks to test a business rule
- shell so thick it contains decisions that belong in the core
- result of pure computation buried inside a try/except that catches infrastructure errors
