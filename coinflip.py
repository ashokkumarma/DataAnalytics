import random
for flips_per_run in (10, 100,1000,10000,100000,1000000):
  expected=int(flips_per_run/2)
  print("Runs of " + str(flips_per_run) + "s flip - expect " + str(expected) + " tails:")
  for try_count in (10, 100,1000,10000,100000,1000000):
    tail_count_in_flips = []
    for tries in range(1,try_count+1):
      head_count = 0
      tail_count=0
      for flip_count in range(1,flips_per_run+1):
        random_num = random.randint(1,1000)
        if (random_num % 2)==0:
          #print("\tflip_count:" +str(flip_count) + " random_num :" + str(random_num))
          head_count = head_count + 1;
          #print("head_count :" + str(head_count))
        else:
          #print("\tflip_count:" +str(flip_count) + " random_num :" + str(random_num))          
          tail_count = tail_count + 1;
      #append tail_count at end of try
      tail_count_in_flips.append(tail_count)
    print("\tOn " + str(tries) + " tries, reached:" + str(max(tail_count_in_flips)))
    max_tail_count_in_flips = max(tail_count_in_flips);
  #print("max_tail_count_in_flips :" + str(max_tail_count_in_flips) + " expected :" + str(expected))
  percent_error= ((max_tail_count_in_flips-expected)/expected)*100
  print("\tPercentage Error: " + str(int(percent_error)) + "%")
