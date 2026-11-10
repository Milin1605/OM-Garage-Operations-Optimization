# OM Garage — Operations Optimization Simulator

An interactive, browser-based simulation of an automotive detailing and ceramic-coating garage. The project explores how staffing, parallel workstations, process times and coating packages affect cycle time, flow time and indicative financial contribution.

## Live demo
Enable GitHub Pages after publishing this repository. The URL will be:
`https://YOUR-GITHUB-USERNAME.github.io/OM-Garage-Operations-Optimization/`

## Run locally
No installation or build step is required. Download or clone the repository and open `index.html` in a modern browser.

## What the simulator includes
- Controls for simultaneous car arrivals, permanent workers, temporary workers and coating layers.
- Cycle-time and bottleneck view for Wet Bay, Dry Bay and Extra Bay.
- Illustrative floor-plan view of parking and workstations.
- 12-hour shift and throughput view.
- Process-step breakdown.
- Scenario table covering 1–5 cars, 1–6 permanent workers and 0–6 temporary workers.

## Model structure
The process is grouped into five stages:
- A: Car parking, complementary check, paint inspection and discussion.
- B: Below wash, engine wash and above wash.
- C: Sanding, compounding polish, post-correction wash and IPA.
- D: Ceramic coating, lamp-dry time and additional coatings.
- E: Interior cleaning, leather/plastic coating and inspection.

The model treats Wet Bay time as fixed at 110 minutes. Variable work is assigned a simplified workers-per-active-slot value. Dry Bay has at most two parallel slots; Extra Bay is represented as one slot.

## Core calculations
- System cycle time (CT) = maximum of Wet Bay, Dry Bay and Extra Bay station cycle times.
- Flow time (FT) = sum of the modelled process times plus the modelled queue-wait allowance.
- Cars per 12-hour shift = floor(720 / system CT).
- Cars per day = two identical 12-hour shifts.
- Labour cost per shift = permanent workers × ₹66.66/hour × 12 + temporary workers × ₹322/hour × 12.
- Indicative surplus per car = revenue × (1 − 15% model allowance) − estimated labour cost per car.

## Important assumptions and limitations
This is an educational simulation, not a production scheduling system or a validated financial model.
- The 15% revenue allowance is an illustrative assumption, not a verified expense ratio.
- Rent, utilities, materials, taxes, maintenance, marketing, equipment depreciation, downtime and other overheads are not fully modelled.
- The queue-wait allowance is simplified and does not simulate individual arrival times or a real queue.
- The 2 × 12-hour shift plan assumes continuous operation and does not model breaks, handovers, absenteeism or demand variation.
- Worker allocation is simplified; the model does not solve a detailed labour-assignment or multi-skill scheduling problem.
- The same simplified workforce-per-slot measure is applied to variable tasks across stations. Real operations may require dedicated teams and explicit travel/transfer times.
- Process times, wages, revenues and capacity assumptions should be validated with actual garage data before making business decisions.

## Suggested future improvements
1. Validate process times and wage assumptions using real operational observations.
2. Model worker assignment by station and skill, including non-overlapping resource constraints.
3. Add stochastic arrivals, service-time variation, breaks and equipment downtime.
4. Add material, utility, rent and other operating costs.
5. Compare scenarios using a formal optimization model and sensitivity analysis.
6. Add data export and scenario comparison.

## Technology
HTML, CSS, JavaScript, Canvas and SVG. No backend or external JavaScript dependency is required.

## Project status
Educational prototype — calculations and assumptions require real-world validation before operational use.
