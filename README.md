# Lottery Simulator

A demo simulation project for lottery organization.

`weeklyRevenue` is the revenue gained by the number of tickets that played multiplied by 3.0.
Because of 1 ticket is 3.0 liras.

`dropBox` is the share of the lottery organization gained by %45 of the `weeklyRevenue`
Thus if the `weeklyRevenue` is 1,658,307 liras, 746,238.15 will be saved to dropBox of the lottery organization.
Remained part of `weeklyRevenue` which is %55 of the `weeklyRevenue` will be paid to winners according to share rates described below.

Value of the `dropBox` will be cumulative, because of that revenue of the every week will accumulate on dropBox.
!If no person can know 2,3,4,5 out of 6 lucky numbers. Their share from the prize will be added to dropBox.
!If no person can know 6 out of 6 lucky numbers. Their share from the prize will be added to `broughtForward` variable to forward that prize for the future weeks. `broughtForward` will be cumulative as well.

!If at the end of the year(12 months/48 weeks) no person can know 6 out of 6 lucky numbers prize in the broughtForward will be added to dropBox as well.
