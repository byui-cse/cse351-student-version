#  Week 09 Team Teaching: Party Room

## Overview

You will be implementing a hotel room where guests can throw a party and where the cleaning staff will clean.

## Assignment

The project file is `team.py` in the `lesson_09/team` folder in GitHub.  Refer to this file for instructions.

### Description of the problem

In a hotel, there are a number of guests and cleaning staff.  There is a conference room where guests can enter to have a party.

**Rules of using the room**

1. The guests and cleaning staff will be processes in your assignment.
2. If someone from the cleaning staff is in the room cleaning, no guest can enter the room.  Only one person from the cleaning staff can be in the room at a time.  If guests are in the room, the cleaning staff will wait until the room is empty before entering.
3. If the room is empty or other guests are in the room, guests can enter the room.  You can have multiple guests in the room at the same time.
4. The first guest to enter the empty room, will turn on the lights.
5. The last guest to leave the room, will turn off the lights.  (This is not the first guest in most cases)
6. Guests can enter and leave the room at anytime as long as the room is empty or contains other guests. It is not uncommon for guests to enter the room, leave and then enter the room again while the party is happening.
7. Assign each cleaner and guest an unique number/ID.
8. Use constants CLEANING_STAFF and HOTEL_GUESTS to know how many processes to create.
9. Remember, multiple guests must be able to be in the room at the same time.
10. Run your program for 1 minute.  While your program is running, keep track of the number of times the room of cleaned and the number of parties held.  A party starts with the lighting being turned on and ends when the lights are turned off.
11. Make sure your assignment matches the format/text of the sample output below.
12. You are not allowed to use lists or queues to control access to the room. You can use a list to keep track of the processes that you create.  The solution requires 2 locks.
13. Do not use try...except statements

### Sample output of the assignment

From the sample output below.  This is only the last part of the output of the running program.  Notice that guests sometimes enter-leave and then enter-leave again during the same party.

```
                     :
                     :
Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner: 2
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Turning on the lights for the party vvvvvvvvvvvvvv
Guest: 1, count = 1
Guest: 3, count = 2
Guest: 4, count = 3
Guest: 5, count = 4
Guest: 2, count = 4
Guest: 4, count = 4
Guest: 1, count = 5
Turning off the lights  ^^^^^^^^^^^^^^^^^^^^^^^^^^
Starting to clean the room >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cleaner: 2
Finish cleaning the room <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Turning on the lights for the party vvvvvvvvvvvvvv
Guest: 1, count = 1
Guest: 4, count = 2
Guest: 5, count = 3
Guest: 2, count = 4
Guest: 3, count = 3
Guest: 5, count = 2
Guest: 1, count = 3
Guest: 3, count = 2
Guest: 3, count = 2
Guest: 4, count = 2
Guest: 1, count = 3
Guest: 2, count = 4
Room was cleaned 35 times, there were 23 parties
```
