from buyer import Buyer
from sellers import *
from interaction import Interaction

# user interaction
value = 10
range_min = 11
range_max = 15
imp_incr = 0.2
imp_init = 0

rounds = 4
i = 0
total_profit = 0
while i < rounds:
  maxprice = int(random.uniform(range_min, range_max+1)) #+1 to include the upper bound
  buyer = Buyer(maxprice, imp_init, imp_incr)
  seller = UserInputSeller(value)

  interaction = Interaction(buyer, seller, verbose=True)
  profit = interaction.run_interaction()
  total_profit += profit
  i+= 1
print(f"Total_profit is ${total_profit} over {rounds} rounds for an average return of ${round(total_profit/rounds,2)}")