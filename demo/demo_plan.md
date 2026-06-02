# SafeOption AI Demo Plan

## Objective

The goal of the first MVP demo is to demonstrate that SafeOption AI can help beginner retail investors understand option risk before trading.

This demo focuses on educational guidance rather than automated trading.

---

# Demo Scope

## Module 1 — Sell Put Risk Calculator

### User Inputs

* Stock Symbol
* Current Stock Price
* Strike Price
* Premium Received
* Expiry Date

---

### System Outputs

* Break-even Price
* Maximum Risk
* Estimated Annualized Return
* Assignment Risk Warning
* Dividend Risk Warning
* Educational Notes

---

# Example Output

## Example

Stock:
IBM

Current Price:
210

Sell Put Strike:
200

Premium:
2.50

Days to Expiry:
7

---

## SafeOption AI Output

Break-even:
197.50

Maximum Risk:
High if stock falls below strike.

Annualized Return:
Approximate short-term premium yield displayed.

Assignment Risk:
Moderate.

Dividend Risk:
Low.

Educational Warning:
Selling puts can result in stock assignment. Users should only sell puts on stocks they are willing to own.

---

# MVP Technical Direction

Initial prototype:

* Streamlit Web Demo

Future versions:

* Web App
* Mobile App
* AI Educational Assistant
* Multilingual Interactive Platform

---

# Current Languages

* English
* Chinese

---

# Future Expansion

* Español
* 日本語
* 한국어
* हिन्दी

---

# Important Principle

SafeOption AI is an educational and risk-awareness platform.

The system does NOT:

* execute trades
* provide guaranteed returns
* manage user funds
* provide financial advice

---

# Current Development Stage

Early MVP Design

Target:
Proof of Usefulness Hackathon Submission
