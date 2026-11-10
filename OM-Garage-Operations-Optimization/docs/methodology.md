# Methodology

## Process groups
A — Car parking, complementary check, paint inspection and discussion.  
B — Below wash, engine wash and above wash.  
C — Sanding, compounding polish, post-correction wash and IPA.  
D — Ceramic coating, lamp-dry time and additional coatings.  
E — Interior cleaning, leather/plastic coating and inspection.

## Workstation mapping
- Wet Bay: one station; the modelled wet-process time is fixed at 110 minutes.
- Dry Bay: up to two parallel slots.
- Extra Bay: one slot.

## Staffing logic
The model calculates active Dry Bay slots as the minimum of the number of cars, two physical Dry Bay slots and total workers. Workers per active slot are the whole-number allocation, capped at two workers per slot. This prevents a zero-worker division when there are fewer workers than potential slots.

## Performance measures
System cycle time is the maximum of the station cycle times. Flow time is the sum of process times plus a simplified queue-wait allowance. Shift throughput is calculated as the floor of 720 minutes divided by cycle time.

These are deterministic, simplified calculations. They are not a discrete-event simulation or an optimized staff roster.
