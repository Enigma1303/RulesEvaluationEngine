# Rules Evaluation Engine

A Rule evaluation engine built in Python that evaluates dynamic business rules against entity data.

This project simulates how real backend systems make approval / rejection decisions based on configurable rules rather than hardcoded logic.

---

## Features

- Rules loaded dynamically from JSON (no hardcoding)
- Entity data loaded from JSON
- Operator mapping (no large if/else chains)
- Graceful handling of malformed rules
- Structured decision output (APPROVED / REJECTED)
- Proper logging with file persistence
- Clean separation of responsibilities

---

## How it Works

1. **RulesParserAndValidation**
   - Loads rules from `rules.json`
   - Validates structure and operators
   - Skips malformed rules gracefully

2. **RulesEvaluator**
   - Loads entity data from `entity.json`
   - Evaluates each rule independently
   - Collects failed rules without crashing

3. **Result Generation**
   - APPROVED → if all rules pass
   - REJECTED → if one or more rules fail